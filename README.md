# Pokémon Go WebAPI

## Description 

Ce projet vise à fournir une interface web au projet de [Tejado](https://github.com/tejado/pokemongo-api-demo), permettant de consulter des informations relatives 
au jeu en réalité augmentée Pokémon GO. 

A terme, le service proposera des 'cartes' à distribuer sous forme d'image et d'iframe web pour exposer son avancée en jeu. 

## Usage 

## Hébergement de l'API

### Générer un jeu de clés

Pour être en mesure de communiquer avec l'API, les informations de connexion doivent être cryptées via RSA.  
Pour l'utiliser, générez tout d'abord un jeu de clés en exécutant le script genkeys.py.

### Lancer l'API

La seconde étape est de lancer l'API. Pour se faire, exécutez le script api.py. Celui-ci va lancer un serveur HTTP.

## Communiquer avec l'API

### Récupérer la clef publique 

Pour communiquer avec l'API, les informations de connexion doivent être cryptées via RSA.  
Pour se faire, vous devez donc récupérer la clef publique accessible à http://le-server/pubkey

### Se connecter à l'API

Les données de l'API sont accessible à http://le-server/api. 

Celle-ci attends un paramètre (via GET ou POST) nommé 'params'.  
Il doit présenter les informations de connexion mise en forme tel que 'username&password'.
Ces informations doivent être envoyé au serveur cryptée avec RSA grâce à la clef publique précedemment récupérée, et encodées en base64 urlsafe. 

Si tout se passe bien, l'API renverra les informations relatives au joueur spécifié. 

## Démonstration 

Vous pouvez tester l'API ici: http://pokemon-chaipokoi.rhcloud.com/api?user=username&password=password  (OUTDATED, pas sécurisé)

A noter qu'aucune information relative à vos identifiants n'est enregistrée. 

Un exemple de script client est présent dans "example/main.py". 

## Exemple 

Url : http://localhost:8080/api?user=chaipokoi&password=12345  (OUTDATED, pas sécurisé)

<pre>
{
   "username":"chaipokoi",
   "itemstorage":"350",
   "pokestorage":"250",
   "since":"2016-07-17 10:50:42",
   "pokecoin":"0",
   "state":"OK",
   "stardust":"0",
   "output":"[!] Your given location: Washington Square, Greenwich, NY 12834, USA<br>[!] lat/long/alt: 43.0909305 -73.4989367 0.0<br>[!] PTC login for: chaipokoi<br>[+] RPC Session Token: TGT-3975819-HVp6bJxuMpT1D ...<br>[+] Received API endpoint: https://pgorelease.nianticlabs.com/plfe/62/rpc<br>[+] Login successful<br>[+] Username: chaipokoi<br>[+] You are playing Pokemon Go since: 2016-07-17 10:50:42<br>[+] Poke Storage: 250<br>[+] Item Storage: 350<br>[+] POKECOIN: 0<br>[+] STARDUST: 0<br>",
   "message":"It's OK"
}
</pre>

## Prérequis

- [Bottlepy](http://bottlepy.org)
- Les élements requis par le projet de [Tejado](https://github.com/tejado).  

## Crédits 

Thanks a lot to [Mila432](https://github.com/Mila432/Pokemon_Go_API) and [Tejado](https://github.com/tejado) for the engine behind the webApi  
Thanks a lot to [elliottcarlson](https://github.com/elliottcarlson) for the Google Auth PR  
