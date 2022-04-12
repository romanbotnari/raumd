"""imports commands into the sequence file."""
import json
import urllib.request as urllib2

from .configurer import configuration
from .console import console
from .utility import write_sequence_file

def download(args):
    """downloads sequence."""
    write_sequence_file(configuration['path'])

    with open (configuration['path'], "r", encoding="utf-8") as file:
        default = json.load(file)

        status, sequence = download_sequence(args.id)

        if status == "ok":
            with open (configuration['path'], "w", encoding="utf-8") as sequence_file:
                new_sequence_name = args.id[len(args.id) -1]
                if args.rename is not None:
                    new_sequence_name = args.rename[0]
                default[new_sequence_name] = sequence
                json.dump(default, sequence_file)
                console.print("Import succeded.", style="good")
        else:
            console.print('Couldn\'t find the sequence:', style='bad')
            console.print(sequence)

def download_sequence(sequence):
    """downloads sequence."""
    try:
        body = {"sub_seq": []}
        if len(sequence) > 1:
            for entry in sequence[1:len(sequence)]:
                body.get('sub_seq').append(entry)
        jsondata = json.dumps(body)
        jsondataasbytes = jsondata.encode('utf-8')
        req = urllib2.Request(configuration['url'] + "/api/download/" + sequence[0])

        req.add_header('Content-Length', len(jsondataasbytes))
        req.add_header('Content-Type', 'application/json')

        with urllib2.urlopen(req, jsondataasbytes, context=configuration['context']) as response:
            text = response.read()
            stud_obj = json.loads(text)
            return "ok", stud_obj

    except Exception as exception:
        console.print("Oops download failed!", style="bad")
        console.print(exception, style="bad")
        return "nok", None
