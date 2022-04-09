import ssl
import os
from .utility import get_boolean
from .utility import get_int
from .utility import get_sequence_file_path
from configparser import ConfigParser
from pathlib import Path
from .console import console

props = Path(os.path.dirname(__file__)) / "raumd.conf"
keys = {}
separator = "="

configurer = ConfigParser()

configurer.read(props)

configuration = {}
configuration["url"] = configurer['working']["url"]
configuration["path"] = get_sequence_file_path(configurer['working']["path"])
configuration["_global_failearly"] = get_boolean(configurer['working']["failearly"])
configuration["_global_verbose"] = get_boolean(configurer['working']["verbose"])
configuration["timeout"] = get_int(configurer['working']["timeout"])
configuration["localssl"] = get_boolean(configurer['working']["localssl"])

if configuration["localssl"]:
	configuration["context"] = ssl._create_unverified_context()
else:
	configuration["context"] = None

def configure(args):
	
	if args.reset:

		url = 'https://airlocks.xyz'
		path = 'sequence.json'
		timeout = ''
		failearly = 'Yes'
		localssl = 'Yes'
		verbose = 'Yes'
				
		if not configurer.has_section('working'):
			configurer.add_section('working')

		configurer.set("working", "url", url)
		configurer.set("working", "path", path)
		configurer.set("working", "timeout", timeout)
		configurer.set("working", "failearly", failearly)
		configurer.set("working", "localssl", localssl)

	elif args.show:

		console.print("[accent]url[/accent]      :", configurer['working']["url"])
		console.print("[accent]path[/accent]     :", configurer['working']["path"])
		console.print("[accent]timeout[/accent]  :", configurer['working']["timeout"])
		console.print("[accent]localssl[/accent] :", configurer['working']['localssl'])
		console.print("[accent]verbose[/accent]  :", configurer['working']["verbose"])
		console.print("[accent]failearly[/accent]:", configurer['working']["failearly"])

	else:
		if args.url is not None:
			console.print('Setting url to: ', args.url[0])
			configurer.set("working", "url", args.url[0])
		
		if args.path is not None:
			console.print('Setting path to: ', args.path[0])
			configurer.set("working", "path", args.path[0])
		
		if args.timeout is not None:
			console.print('Setting timeout to: ', args.timeout[0])
			configurer.set("working", "timeout", str(args.timeout[0]))

		if args.failearly is not None:
			console.print('Setting failearly to: ', args.failearly[0])
			configurer.set("working", "failearly", args.failearly[0])

		if args.localssl is not None:
			console.print('Setting localssl to: ', args.localssl[0])
			configurer.set("working", "localssl", args.localssl[0])

		if args.verbose is not None:
			console.print('Setting verbose to: ', args.verbose[0])
			configurer.set("working", "verbose", args.verbose[0])

	if not args.show:
		try:
			with open(props, 'w') as configfile:
				configurer.write(configfile)
		except Exception as e: 
			console.print('An exception occurred while trying to write to the configure file.', style='bad')
			console.print(e, style='bad')