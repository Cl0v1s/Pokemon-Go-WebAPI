from bottle import *
import os
import re
import rsa
import base64
from subprocess import Popen, PIPE

#=============VARIABLES=============================================

# Definition des variables globales
Errors = ["[-] RPC server offline", "[-] Wrong username/password" ]
Success = "[+] Login successful"
Separator = "\n"
    #Verification de la plateform d'execution
if os.name == 'nt':
    Separator = "\r\n"

#Chargement de la cle privee
with open(os.path.dirname(os.path.realpath(__file__))+'/id_rsa') as privatefile:
    keydata = privatefile.read()
Privkey = rsa.PrivateKey.load_pkcs1(keydata)

#=============METHODES=============================================

#Fonction de recherche par regex augmentee
def search(pattern, string):
    m = re.search(pattern, string)
    if m != None: 
        return m.group(1)
    else: 
        return "N/A"

#Retourne les informations de l'utilisateur precise
@route("/api", method=['GET', 'POST'])
def api():
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
    #Creation du dictionnaire de donnees
    data = {"state" : "OK", "message" : "", "output" : ""};
    #Determination des arguments (decryptage)
    params = request.query.get("params")
    if params == None: #Si c'est pas en get, on recupere en POST
        params = request.forms.get("params")
    params = params + "=="
    params = base64.urlsafe_b64decode(params)

    params = rsa.decrypt(params, Privkey)
    params = params.split("&")
    userparam = params[0]
    #Suppression du premier arguments
    params.remove(userparam)
    #Join de toutes les arguments restants en mot de passe (contourner probleme si mdp contient un &)
    passwordparam = "".join(params)
    
    #verification des parametres
    if userparam == None or passwordparam == None:
        data["state"] = "NO"
        data["message"] = "You must specify a username and a password"
        return data

    #Systeme d'authentification
    if "@gmail.com" in userparam:
        auth = '-agoogle'
    else: 
        auth = '-aptc'
    #Nom utilisateur
    user = '-u'+userparam+'';
    #Mot de passe 
    password = '-p'+passwordparam+''
    #Emplacement
    location = '-l "New York, Washington Square"'
    #Lancement du client api
    process = Popen(["python", os.path.dirname(os.path.realpath(__file__)) + "/engine/main.py", auth, user, password, location], stdout=PIPE)
    #lecture du resultat
    output = process.communicate()[0].split(Separator);
    #Gestion des erreurs
    for entry in output: 
        if entry in Errors:
            data["state"] = "NO"
            data["output"] = "<br>".join(output);
            data["message"] = entry
            return data #Arret des operation et signalement de l'erreur 
        #Login reussit
        if Success in entry:
            data["message"] = "It's OK"
            #Ajout de la sortie console 
            data["output"] = "<br>".join(output);
            #Remplissage des donnees
            data["username"] = search("Username: (.*?)<br>", data["output"])
            data["since"] = search("You are playing Pokemon Go since: (.*?)<br>", data["output"])
            data["pokestorage"] = search("Poke Storage: (.*?)<br>", data["output"])
            data["itemstorage"] = search("Item Storage: (.*?)<br>", data["output"])
            data["pokecoin"] = search("POKECOIN: (.*?)<br>", data["output"])
            data["stardust"] = search("STARDUST: (.*?)<br>", data["output"])
            return data;

#Retourne la clef publique 
@route("/pubkey")
def getpubkey():
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
    #Chargement de la cle privee
    with open(os.path.dirname(os.path.realpath(__file__))+'/id_rsa.pub') as privatefile:
        keydata = privatefile.read()
    return {"pubkey" : keydata}


application = default_app()

#run(host='localhost', port=8080)