from .configurer import configuration
from .console import console
import json
from .utility import write_sequence_file

def show(args):

	write_sequence_file(configuration['path'])

	try: 
		f = open (configuration['path'], "r")
		default = json.load(f)
	except Exception as e:
		console.print(e, style='bad')
		console.print ("There is no sequence file I can find at the configured path.", style='bad')
		return

	sequence = default
	idz = args.id
	
	if (len(idz) == 0):
		one_element_seq = {'seq':[]}
		for entry in sequence:
			one_element_seq.get('seq').append({'id':entry})
		show_sequence(one_element_seq)
		return
	else:
		id = idz[0]
	found = False
	last_found_id = None
	if (id in sequence):
		last_found_id = id
		sequence = sequence[id]
		found = True
	for id_idx in range(1,len(idz)):
		id = idz[id_idx]

		for entry in sequence['seq']:
			if ("id" in entry and id == entry["id"]) or ("name" in entry and id == entry["name"]):
				last_found_id = id
				if ("id" in entry):
					sequence = entry
				else:
					one_element_seq = {'seq':[entry]}
					sequence = one_element_seq
				found = True
				break
			else:
				found = False

	if not found:
		console.print ("Last found id: ", last_found_id)
		return
	show_sequence(sequence)

def show_sequence(sequence):
	seq = sequence.get('seq')
	if seq is None or len(seq) == 0:
		console.print("There are no sequences.", style='good') 
	try:
		for entry in seq:
			if ("name" in entry):
				console.print("[accent]name[/accent]   : " + "[good]" + entry["name"] + "[/good]")
				console.print("[accent]command[/accent]: " + "[good]" + entry["command"] + "[/good]")
			elif ("id" in entry):
				console.print("[accent]subseq[/accent]: " + "[important]" + entry["id"] + "[/important]" + 
					(" / [important]" + entry["title"] + "[/important]" if "title" in entry else "")) 
	except Exception as e:
		console.log("An error occurred while looking at the entry", style='bad')
		console.print(e, style="bad")