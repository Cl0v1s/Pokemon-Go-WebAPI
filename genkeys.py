import rsa
import os

(pubkey, privkey) = rsa.newkeys(512)

with open(os.path.dirname(os.path.realpath(__file__))+'/id_rsa', "w") as privatefile:
    privatefile.write(privkey.save_pkcs1());
with open(os.path.dirname(os.path.realpath(__file__))+'/id_rsa.pub', "w") as privatefile:
    privatefile.write(pubkey.save_pkcs1());
with open(os.path.dirname(os.path.realpath(__file__))+'/example/id_rsa.pub', "w") as privatefile:
    privatefile.write(pubkey.save_pkcs1());