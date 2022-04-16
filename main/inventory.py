"""lists the sequences and available commands."""
import json
from .configurer import configuration
from .console import console
from .utility import write_sequence_file

def show(args):
    """finds and prints the requested sequence"""
    write_sequence_file(configuration['path'])

    try:
        with open (configuration['path'], "r", encoding="utf-8") as file:
            default = json.load(file)
    except Exception as exception:
        console.print(exception, style='bad')
        console.print ("There is no sequence file I can find at the configured path.", style='bad')
        return

    sequence = default
    idz = args.id

    if len(idz) == 0:
        one_element_seq = {'seq':[]}
        for entry in sequence:
            one_element_seq.get('seq').append({'id':entry})
        show_sequence(one_element_seq)
        return
        
    sequence_id = idz[0]

    found = False
    last_found_id = None

    if sequence_id in sequence:
        last_found_id = sequence_id
        sequence = sequence[sequence_id]
        found = True
    for id_idx in range(1,len(idz)):
        sequence_id = idz[id_idx]

        for entry in sequence['seq']:
            found = False
            is_subseq = "id" in entry and sequence_id == entry["id"]
            is_command = "name" in entry and sequence_id == entry["name"]
            if is_subseq or is_command:
                last_found_id = sequence_id
                if "id" in entry:
                    sequence = entry
                else:
                    one_element_seq = {'seq':[entry]}
                    sequence = one_element_seq
                found = True
                break

    if not found:
        console.print ("Last found id: ", last_found_id)
        return
    show_sequence(sequence)

def show_sequence(sequence):
    """prints the sequence"""
    seq = sequence.get('seq')
    if seq is None or len(seq) == 0:
        console.print("There are no sequences.", style='good')
    try:
        for entry in seq:
            if "name" in entry:
                console.print("[accent]name[/accent]   : "
                    + "[good]" + entry["name"] + "[/good]")
                console.print("[accent]command[/accent]: " + "[good]"
                    + entry["command"] + "[/good]")
            elif "id" in entry:
                console.print("[accent]subseq[/accent]: "
                    + "[important]" + entry["id"] + "[/important]" +
                    (" / [important]" + entry["title"]
                    + "[/important]" if "title" in entry else ""))
    except Exception as exception:
        console.log("An error occurred while looking at the entry", style='bad')
        console.print(exception, style="bad")
