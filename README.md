# Pokemon Go WebAPI

## Description 

This project aims to provide a JSON API allowing to retrieve data from the Pokemon Go servers reachable by any system connected to the Internet.   

In the future, the service will propose a "card" system to show your ingame progression to your friends. 

Please note that your login informations are encrypted, not saved and will not be used by anyone expect yourself. 

## How to use

### Use the API

The API is already reachable at https://pokemon-chaipokoi.rhcloud.com/api  
In order to work, the API expects an access token created with the user's credentials. To protect your data, the credentials must be encrypted with RSA and encoded in urlsafe base64.

#### The process

* Get the API public key at https://pokemon-chaipokoi.rhcloud.com/pubkey
* Format the credentials in the following format: username&password
* Encrypt the credentials with RSA and the given public key
* Encode the encrypted credentials in urlsafe base64
* Access the API at https://pokemon-chaipokoi.rhcloud.com/api?params=your_access_token
* Get your data !

(A code sample is present in the example directory)

### Host the api

You can host the API by yourself.  
You just have to follow theese simple steps.

#### The process

* Send the code on your server
* Start the genkeys.py script to create new private/public rsa keys
* Start the api.py script to start the api server 
* You can now access your own version of the API !

## Requirements

- [Bottlepy](http://bottlepy.org)
- [Python-rsa](https://pypi.python.org/pypi/rsa)
- Python 2.7
- requests
- protobuf (>=3)
- gpsoauth

## Crédits 

[Mila432](https://github.com/Mila432) for the login secrets
[elliottcarlson](https://github.com/elliottcarlson) for the Google Auth PR
[Tjado](https://github.com/tejado) for the pgoapi
[AeonLucid](https://github.com/AeonLucid) for improved protos
[AHAAAAAAA](https://github.com/AHAAAAAAA) for parts of the s2sphere stuff
