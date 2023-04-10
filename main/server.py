import http.server
import socketserver
import urllib
from pathlib import PurePosixPath
import json
import urllib.request
from console import console
import os
import time, threading, socket
from socketserver import ThreadingMixIn
import logging
from logging.handlers import TimedRotatingFileHandler
from klein import run, route, Klein, resource
from runner import run_server, find_sequence
from importer import download_server
from configurer import configuration


log_name = "server.log"

log_format = "%(threadName)s %(asctime)s - %(levelname)s - %(message)s"

log_level = 10

handler = TimedRotatingFileHandler(log_name, when="midnight", interval=1)
handler.setLevel(log_level)
formatter = logging.Formatter(log_format)
handler.setFormatter(formatter)

# add a suffix which you want
handler.suffix = "%Y%m%d"

logger = logging.getLogger('simple')
logger.setLevel(log_level)

logger.addHandler(handler)

logger.info ('Starting server...')

app = Klein()

def set_no_cache_headers(request):
    request.setHeader('Cache-Control', "no-cache, no-store, must-revalidate")
    request.setHeader('Access-Control-Allow-Origin', '*')
    request.setHeader('Access-Control-Allow-Methods', '*')
    request.setHeader('Access-Control-Allow-Headers', '*')
    request.setHeader('Pragma', 'no-cache')
    request.setHeader('Expires', '0')

@app.route('/execute/<sequence>/', methods=['GET', 'OPTIONS'])
def pg_execute(request, sequence):
    set_no_cache_headers(request)
    logger.info("Am I here?.")
    console.print("Am I here?.", style='good')

    logger.info("execute/sequence/" + sequence)
    args = {}
    args['id']=[sequence]
    args['failearly']=True
    args['verbose']=False
    args['params']=[]
    logger.info(args)
    result = run_server(args, sequence)
    try:
        jsondata = json.dumps(result)
    except Exception as e:
        logger.info("An error occurred when assuming this is a json file.")
        dictdata = {}
        dictdata['error'] = 'The response was not a json file'
        jsondata = json.dumps(dictdata)
        request.setResponseCode(400)
        
    console.print(jsondata)
    request.write(jsondata.encode('utf-8'))
    request.finish()

    return

@app.route('/sequence/save/', methods=['POST', 'OPTIONS'])
def pg_save(request):
    set_no_cache_headers(request)
    console.print(request.method.decode())
    console.print(request.method.decode() == 'OPTIONS')

    if request.method.decode() == 'OPTIONS':
        request.setResponseCode(200)
        request.finish()
        console.print("stopping exec")
        return
    logger.info("Am I here?.")
    console.print("Am I here?.", style='good')
    console.print(request)
    content = json.loads(request.content.read())
    console.print("request.args {}", content)
    console.print(content['id'])

    logger.info("sequence/save/")
    args = {}
    args['id']=[content['id']]
    args['failearly']=True
    args['verbose']=False
    args['rename']=None
    args['params']=[]
    logger.info(args)
    try:
        download_server(args, content)
        jsondata = json.dumps(content)
        request.setResponseCode(200)
    except Exception as e:
        logger.info("An error occurred when assuming this is a json file.")
        console.log(e)
        dictdata = {}
        dictdata['error'] = 'The response was not a json file'
        jsondata = json.dumps(dictdata)
        request.setResponseCode(400)
        
    console.print(jsondata)
    request.write(jsondata.encode('utf-8'))
    request.finish()

    return

@app.route('/get/<sequence>/', methods=['GET', 'OPTIONS'])
def pg_get(request, sequence):
    set_no_cache_headers(request)
    logger.info("Am I here?.")
    console.print("Am I here?.", style='good')

    try:
        file = open (configuration['path'], "r", encoding="utf-8")
        default = json.load(file)
    except:
        console.print ("There is no sequence file I can find at the configured path.", style='bad')
        return

    found, run_this_sequence = find_sequence([sequence], default)

    console.print(run_this_sequence)

    if not found:
        console.print ("I haven't found the sequence")
        run_this_sequence = {"result": "Not found"}
        return
    
    try:
        jsondata = json.dumps(run_this_sequence)
    except Exception as e:
        logger.info("An error occurred when assuming this is a json file.")
        dictdata = {}
        dictdata['error'] = 'The response was not a json file'
        jsondata = json.dumps(dictdata)
        request.setResponseCode(400)
        
    console.print(jsondata)
    request.write(jsondata.encode('utf-8'))
    request.finish()

    return

@app.route('/sequence/all/', methods=['GET', 'OPTIONS'])
def pg_get_all(request):
    set_no_cache_headers(request)
    logger.info("Am I here?.")
    console.print("Am I here?.", style='good')

    try:
        file = open (configuration['path'], "r", encoding="utf-8")
        dictdata = json.load(file)
        jsonobj = json.dumps(dictdata)
    except Exception as e:
        logger.info("An error occurred when assuming this is a json file.")
        dictdata = {}
        dictdata['error'] = 'The response was not a json file'
        jsonobj = json.dumps(dictdata)
        request.setResponseCode(400)
        
    console.print(jsonobj)
    request.write(jsonobj.encode('utf-8'))
    request.finish()

    return

def start_server(args):
    try:
        app.run("0.0.0.0", 7474)
    except Exception as e:
        logger.info("Oops app run problem!")
        logger.error(e)




