from bottle import *
from subprocess import Popen, PIPE


@route("/api")
def api():
    #Création du dictionnaire de données
    data = {};
    #Détermination des arguments
    #Système d'authentification
    auth = '-agoogle'
    #Nom utilisateur
    user = '-u "gmail_account_username@gmail.com"';
    #Mot de passe 
    password = '-p "password"'
    #Emplacement
    location = '-l "New York, Washington Square"'
    #Lancement du client api
    process = Popen(["python", "engine/main.py", auth, user, password, location], stdout=PIPE)
    #lecture du resultat
    output = process.communicate()[0].split("\r\n");
    return output[0];

run(host='localhost', port=8080)