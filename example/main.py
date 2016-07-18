import rsa
import base64
import urllib2

#lecture de la clé publique 
with open('id_rsa.pub') as privatefile:
    keydata = privatefile.read()
pubkey = rsa.PublicKey.load_pkcs1(keydata)

#Détermination des paramètres à encrypter
params = "username&password" #username&password

#Encryptage des paramètres
params = rsa.encrypt(params, pubkey)
params = base64.b64encode(params)

#Assemblage de l'URL
url = "http://localhost:8080/api?params="+params

content = urllib2.urlopen(url).read()
print content
