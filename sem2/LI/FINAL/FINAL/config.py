import os
import sqlite3


def db_connection(db_path): 
    if (os.path.exists(db_path)):
        conn = sqlite3.connect(db_path)
        return conn
    else: 
        print("Erro! Ligação à Base de Dados falhada")
    

def path_definer (path):
    if (os.path.exists(path)):
        return path
    else: 
        print("ERRO! Caminho inválido")


#PARA SABER O NOVO ID
def count_ids(tablename):
    conn = db_connection('database.db')
    cur = conn.cursor()
    query = f"SELECT COUNT(*) FROM {tablename}"
    cur.execute (query)
    tmp = cur.fetchone()
    conn.close()
    return tmp[0] + 1


def select_query(query):
    conn = db_connection('database.db')
    cur = conn.cursor()
    
    cur.execute(query)
    data =  cur.fetchall()
    conn.close()
    return data
    

def execute_query(query):
    conn = db_connection('database.db')
    cur = conn.cursor()
    
    cur.execute(query)
    conn.commit()
    conn.close()










CYPHER_KEY = b'Kw>\x94\xe7\\\x82\x13\xaa@0\xea\xb6\xe3\xc8a'                #Key para cifrar as imagens privadas
IMG_PATH = path_definer('../data/img/')                                     #Caminho para a pasta das imagens inseridas na aplicação
WEB_PATH = path_definer('../web/')                                          #Caminho para a pasta dos ficheiros HTML
API_PATH = os.path.abspath(os.getcwd())                                     #Caminho para a pasta da API
CHERRYPY_WEB_PATH = API_PATH + '/' + WEB_PATH                               #Caminho para o CherryPy fazer os caminhos


SERVER_CONFIG = {                                                           #Variável com a configuração do Servidor
        
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': API_PATH
        },
        '/css': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': CHERRYPY_WEB_PATH + '/css'
        },
        '/js': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': CHERRYPY_WEB_PATH + '/js'
        },
        '/img': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': CHERRYPY_WEB_PATH + '/img'
        },
        '/vendors': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': CHERRYPY_WEB_PATH + '/vendors'
        },
        '/dataimg': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': IMG_PATH
        }
    }