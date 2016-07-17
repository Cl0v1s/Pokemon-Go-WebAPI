from bottle import *
import os
from subprocess import Popen, PIPE


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
    #Erreur du serveur/Mauvais mot de passe
    if (len(output) >= 4 or len(output) >= 5) and (output[4] == "[-] Wrong username/password" or output[5] == "[-] Wrong username/password"):
        data["state"] = "NO"
        data["message"] = "Servers down (Auth) or wrong username/password"
    #RPC Server offline 
    if(len(output) >=6) and output[6] == "[-] RPC server offline":
        data["state"] = "NO"
        data["message"] = "Servers down (RPC)"
    #Login reussit
    if(len(output) >= 5) and output[5] == "[+] Login successful":
        data["message"] = "It's OK"
        #Remplissage des donnees
        data["username"] = output[6].split(": ")[1]
        data["since"] = output[7].split(": ")[1]
        data["pokestorage"] = output[8].split(": ")[1]
        data["itemstorage"] = output[9].split(": ")[1]
        data["pokecoin"] = output[10].split(": ")[1]
        data["stardust"] = output[11].split(": ")[1]


    #Ajout de la sortie console 
    data["output"] = "<br>".join(output);

    return data;

application = default_app()

#run(host='localhost', port=8080)