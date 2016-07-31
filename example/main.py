import rsa
import base64
import urllib2

#lecture de la cle publique 
with open('id_rsa.pub') as privatefile:
    keydata = privatefile.read()
#Conversion de X.509 vers PKCS1
keydata = keydata.replace("-----BEGIN PUBLIC KEY-----", "")
keydata = keydata[33:len(keydata)]
keydata = "-----BEGIN RSA PUBLIC KEY-----\n" + keydata;
keydata = keydata.replace("-----END PUBLIC KEY-----", "-----END RSA PUBLIC KEY-----")

pubkey = rsa.PublicKey.load_pkcs1(keydata)

#Determination des parametres a encrypter
params = "username&password" #username&password

#Encryptage des parametres
params = rsa.encrypt(params, pubkey)

params = base64.urlsafe_b64encode(params)


print "Encoded: "+params

#Assemblage de l'URL
url = "http://localhost:8080/api?params="+params+"&requests=get_player,get_inventory"

content = urllib2.urlopen(url).read()
print content

