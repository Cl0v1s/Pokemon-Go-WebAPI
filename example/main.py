import rsa
import base64
import urllib2

#lecture de la cle publique 
with open('id_rsa.pub') as privatefile:
    keydata = privatefile.read()
pubkey = rsa.PublicKey.load_pkcs1(keydata)

#Determination des parametres a encrypter
params = "chaipokoi&0662240307" #username&password

#Encryptage des parametres
params = rsa.encrypt(params, pubkey)

params = base64.urlsafe_b64encode(params)

params = params.replace("=", "")


#Assemblage de l'URL
url = "http://localhost:8080/api?params="+params

content = urllib2.urlopen(url).read()
print content
