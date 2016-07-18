from bottle import *
import os
from subprocess import Popen, PIPE


Errors = ["[-] RPC server offline", "[-] Wrong username/password" ]
Success = "[+] Login successful"

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
    output = process.communicate()[0].split("\r\n");
    #Gestion des erreurs
    for entry in output: 
        if entry in Errors:
            data["state"] = "NO"
            data["message"] = entry
            return data #Arret des operation et signalement de l'erreur 
        #Login reussit
        if Success in entry:
            data["message"] = "It's OK"
            #Remplissage des donnees
            #data["username"] = output[6].split(": ")[1]
            #data["since"] = output[7].split(": ")[1]
            #data["pokestorage"] = output[8].split(": ")[1]
            #data["itemstorage"] = output[9].split(": ")[1]
            #data["pokecoin"] = output[10].split(": ")[1]
            #data["stardust"] = output[11].split(": ")[1]


    #Ajout de la sortie console 
    data["output"] = "<br>".join(output);

    return data;

application = default_app()

#run(host='localhost', port=8080)