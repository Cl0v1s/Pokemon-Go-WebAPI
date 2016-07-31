from bottle import *
import os
import re
import logging
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from base64 import *
from subprocess import Popen, PIPE

from pgoapi import pgoapi
from pgoapi import utilities as util

#=============VARIABLES=============================================

# Definition des variables globales
Debug = True

#=============METHODES=============================================

#Affiche l'erreur
def showError(data, message):
    data["state"] = "NO"
    data["message"] = message
    return data


#Retourne les informations de l'utilisateur precise
@route("/api", method=['GET', 'POST'])
def api():
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
    #Creation du dictionnaire de donnees
    data = {"state" : "OK", "message" : ""};
    if Debug == False:
        #Determination des arguments (decryptage)
        params = request.query.get("params")
        if params == None: #Si c'est pas en get, on recupere en POST
            params = request.forms.get("params")

        #chargement de la clef privee
        keydata = None
        with open(os.path.dirname(os.path.realpath(__file__))+'/id_rsa') as privatefile:
            keydata = privatefile.read()
        rsakey = RSA.importKey(keydata)
        rsakey = PKCS1_v1_5.new(rsakey)

        #decryptage des parametres 
        params = base64.urlsafe_b64decode(params)

        params = rsakey.decrypt(params, 'TkC8VkBfFYHjuVl6ym7sBHdvTgaX')
        if params == "TkC8VkBfFYHjuVl6ym7sBHdvTgaX": #Si c'est le defaut alors c'est qu'il y a erreur
            return showError(data, "You are using an outdated version, please regenerate your card at https://chaipokoi.github.io/Pokemon-Go-WebAPI/.")

        params = params.split("&")
        userparam = params[0]
        #Suppression du premier arguments
        params.remove(userparam)
        #Join de toutes les arguments restants en mot de passe (contourner probleme si mdp contient un &)
        passwordparam = "".join(params)
    else:
        userparam = request.query.get("user")
        passwordparam = request.query.get("password")

    #verification des parametres
    if userparam == None or passwordparam == None:
        return showError(data, "You must specify a username and a password")


    #Systeme d'authentification
    auth_method = 'ptc'
    if "@gmail.com" in userparam:
        auth_method = 'google'

    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(module)10s] [%(levelname)5s] %(message)s')
    # log level for http request class
    logging.getLogger("requests").setLevel(logging.WARNING)
    # log level for main pgoapi class
    logging.getLogger("pgoapi").setLevel(logging.INFO)
    # log level for internal pgoapi class
    logging.getLogger("rpc_api").setLevel(logging.INFO)

    #Lancement de l'api
    api = pgoapi.PGoApi()

    #Parametrage de la position 
    position = util.get_pos_by_name("New York")
    api.set_position(*position)

    #Login
    if not api.login(auth_method, userparam, passwordparam, app_simulation = True):
        return showError(data, "Wrong username/password or server error")

    #Lancement des requetes
    asks = request.query.get("requests")
    if "," in asks:
        asks = asks.split(",")
        req = api.create_request()
        for ask in asks:
            try:
                getattr(req, ask)()
            except:
                return showError(data, "Api call '"+ask+"' doesnt exist.")
        data["results"] = req.call()
    else: 
        try:
            data["results"] = getattr(api, asks)()
        except:
            return showError(data, "Api call '"+asks+"' doesnt exist.")

    return data


#Retourne la clef publique 
@route("/pubkey")
def getpubkey():
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
    #Chargement de la cle privee
    with open(os.path.dirname(os.path.realpath(__file__))+'/id_rsa.pub') as privatefile:
        keydata = privatefile.read()
    #Conversion de X.509 vers PKCS1
    pkcs = keydata.replace("-----BEGIN PUBLIC KEY-----", "")
    pkcs = pkcs[33:len(pkcs)]
    pkcs = "-----BEGIN RSA PUBLIC KEY-----\n" + pkcs;
    pkcs = pkcs.replace("-----END PUBLIC KEY-----", "-----END RSA PUBLIC KEY-----")

    return {"pubkey" : keydata}


if Debug == False: 
    application = default_app()
else:
    run(host='localhost', port=8080)