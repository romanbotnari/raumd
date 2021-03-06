"""runs sequences of commands."""
import subprocess
import json
from threading import Timer

from .console import console
from .configurer import configuration

SEPARATOR = "="

def find_sequence(idz, sequence):
    """find the sequence from sequence.json file."""
    sequence_id = idz[0]
    found = False

    if sequence_id in sequence:
        sequence = sequence[sequence_id]
        if len(idz) == 1:
            found = True
    else:
        console.print("Couldn't find the sequence", style='bad')
        return found, None
    for id_idx in range(1,len(idz)):
        sequence_id = idz[id_idx]

        for entry in sequence['seq']:
            found = False
            is_subseq = "id" in entry and sequence_id == entry["id"]
            is_command = "name" in entry and sequence_id == entry["name"]
            if is_subseq or is_command:
                if "id" in entry:
                    sequence = entry
                else:
                    one_element_seq = {'seq':[entry]}
                    sequence = one_element_seq
                found = True
                break
    return found, sequence

def run(args):
    """run the sequence from sequence.json file."""
    try:
        file = open (configuration['path'], "r", encoding="utf-8")
        default = json.load(file)
    except:
        console.print ("There is no sequence file I can find at the configured path.", style='bad')
        return

    sequence = default

    found, run_this_sequence = find_sequence(args.id, sequence)

    if not found:
        console.print ("I have nothing to run")
        return

    options = {'dryrun': False, 'failearly': args.failearly, 'verbose': args.verbose}

    with console.status("[blue]Running sequences...[/blue]\n"):
        try:
            run_sequence(run_this_sequence, args.params, options)
        except Exception as exception:
            console.print("An error occurred while running the sequences", style="bad")
            console.print(exception, style="bad")

def dryrun(args):
    """dryrun the sequence from sequence.json file."""
    try:
        file = open (configuration['path'], "r", encoding="utf-8")
        default = json.load(file)
    except Exception as exception:
        console.print ("There is no sequence file I can find at the configured path.", style='bad')
        console.print(exception, style="bad")
        return

    sequence = default
    found, run_this_sequence = find_sequence(args.id, sequence)

    if not found:
        console.print ("I have nothing to run", style="bad")
        return

    options = {'dryrun': True, 'failearly': True}

    try:
        run_sequence(run_this_sequence, args.params, options)
    except Exception as exception:
        console.print("An error occurred while running the sequences", style="bad")
        console.print(exception, style="bad")

def run_sequence(sub_seq, params, options):
    """start every process defined in the sequence."""
    if 'seq' not in sub_seq.keys() or sub_seq['seq'] is None:
        console.print ('Nothing to run', style='bad')
        return
    for entry in sub_seq['seq']:
        if "name" in entry.keys():
            console.print ('[accent]name[/accent]   :', entry["name"])
            comm = entry["command"]
            if params is not None and len(params) > 0:
                for parameter in params:
                    if SEPARATOR in parameter:
                        name, value = parameter.split(SEPARATOR, 1)
                        comm = comm.replace(name, value)

            console.print ('[accent]command[/accent]:', entry["command"])
            if not options['dryrun']:
                errcode = 0
                try:
                    with subprocess.Popen(comm, shell=True, stdout=subprocess.PIPE, bufsize=1, universal_newlines=True) as process:
                        timer = Timer(configuration['timeout'], stop_process,[process])
                        timer.start()
                        for line in process.stdout:
                            if options["verbose"] or configuration["_global_verbose"]:
                                console.print(line, end='', markup=False)
                finally:
                    timer.cancel()

                errcode = process.returncode
                if errcode != 0:
                    console.print("An error occurred while running the command!", style="bad")
                    if options["failearly"] or configuration["_global_failearly"]:
                        console.print('Fail early policy on, stopping execution.', style="bad")
                        return
                else:
                    console.print("Sequence completed!", style="good")

        elif "id" in entry.keys():
            run_sequence(entry, params, options)
        else:
            console.print ("Bad sequence definition??")

def stop_process(process):
    """stop the process if the timeout was exceeded."""
    console.print('Timeout expired, stopping process', style='bad')
    process.terminate()
    