import http.server
import socketserver
import urllib
from pathlib import PurePosixPath
import json
import urllib.request

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

@app.route('/execute/<sequence>/', methods=['POST'])
def pg_create(request, sequence):
    set_no_cache_headers(request)

    logger.info("execute/sequence/" + sequence)
    content = json.loads(request.content.read())
    logger.info(content)

    # args = dict(id= [sequence], failearly= False, verbose= False)
    args = {}
    args['id']=[sequence]
    args['failearly']=False
    args['verbose']=False
    args['params']=[]
    logger.info(args)
    run_server(args)
    f = open("out.json", "r")
    data = f.read()
    return data

def start_server(args):
    try:
        app.run("0.0.0.0", 7474)
    except Exception as e:
        logger.info("Oops app run problem!")
        logger.error(e)




