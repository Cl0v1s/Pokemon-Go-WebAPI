from bottle import *
import os
import re
from subprocess import Popen, PIPE


Errors = ["[-] RPC server offline", "[-] Wrong username/password" ]
Success = "[+] Login successful"

Separator = "\n"
#Verification de la plateform d'execution
if os.name == 'nt':
    Separator = "\r\n"

def search(pattern, string):
    m = re.search(pattern, string)
    if m != None: 
        return m.group(1)
    else: 
        return "N/A"

@route("/api", method=['GET', 'POST'])
def api():

    #Creation du dictionnaire de donnees
    data = {"state" : "OK", "message" : "", "output" : ""};
    #Determination des arguments
    userparam = request.query.get("user")
    passwordparam = request.query.get("password")
    if userparam == None or passwordparam == None:
        userparam = request.forms.get("user")
        passwordparam = request.forms.get("password")
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

application = default_app()

#run(host='localhost', port=8080)