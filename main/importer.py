from .console import console
import urllib.request as urllib2
from .configurer import configuration
import json
from .utility import write_sequence_file

def download(args):

	write_sequence_file(configuration['path'])

	f = open (configuration['path'], "r")
	default = json.load(f)

	status, sequence = download_sequence(args.id)

	if status == "ok":
		f1 = open (configuration['path'], "w")
		to = args.id[len(args.id) -1]
		if(args.rename is not None):
			to = args.rename[0]
		default[to] = sequence
		json.dump(default, f1)
		console.print("Import succeded.", style="good")
	else:
		console.print('Couldn\'t find the sequence:', style='bad')
		console.print(sequence)
	
def download_sequence(sequence):
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

        response = urllib2.urlopen(req, jsondataasbytes, context=configuration['context'])

        text = response.read()
        stud_obj = json.loads(text)
        return "ok", stud_obj
    except Exception as e:
        console.print("Oops download failed!", style="bad")
        console.print(e, style="bad")
        return "nok", None