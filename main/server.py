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
from runner import run_server


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
    run_server(args, sequence)
    f = open(sequence, "r")
    data = f.read()
    console.print(data)
    try:
        dictdata = json.loads(data)
        jsondata = json.dumps(dictdata)
    except Exception as e:
        logger.info("An error occurred when assuming this is a json file.")
        dictdata = {}
        dictdata['error'] = 'The response was not a json file'
        jsondata = json.dumps(dictdata)
        request.setResponseCode(400)
        
    request.write(jsondata.encode('utf-8'))
    request.finish()

@app.route('/get/<sequence>/', methods=['GET', 'OPTIONS'])
def pg_get(request, sequence):
    set_no_cache_headers(request)
    logger.info("Am I here?.")
    console.print("Am I here?.", style='good')

    return sequence

def start_server(args):
    try:
        app.run("0.0.0.0", 7474)
    except Exception as e:
        logger.info("Oops app run problem!")
        logger.error(e)




