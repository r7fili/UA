from PIL import Image, ImageDraw, ImageFont
import io
import os
import sqlite3 as sql
from platform import architecture
import cherrypy
import base64
from Crypto.Cipher import AES
import requests 
from cryptography.fernet import Fernet
import json
import hashlib

SESSION_KEY = 'very secret and unguessable'

baseDir = os.path.dirname(os.path.abspath(__file__))

# config = {
#     "/": {          "tools.staticdir.root": baseDir },

#     "/html": {      "tools.staticdir.on": True,
#                     "tools.staticdir.dir": "html" },
#     "/js": {        "tools.staticdir.on": True,
#                     "tools.staticdir.dir": "js" },
#     "/css": {       "tools.staticdir.on": True,
#                     "tools.staticdir.dir": "css" },
#     "/images": {    "tools.staticdir.on": True,
#                     "tools.staticdir.dir": "images" },
# }

class Root(object):
    
    @cherrypy.expose
    def index(self):
        return open("index.html")


#socket port
cherrypy.config.update({'server.socket_port': 10014,})

cherrypy.quickstart(Root(), "/")