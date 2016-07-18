import rsa

(pubkey, privkey) = rsa.newkeys(512)

with open('id_rsa', "w") as privatefile:
    privatefile.write(privkey.save_pkcs1());
with open('id_rsa.pub', "w") as privatefile:
    privatefile.write(pubkey.save_pkcs1());
with open('example/id_rsa.pub', "w") as privatefile:
    privatefile.write(pubkey.save_pkcs1());