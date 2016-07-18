# Pokémon Go WebAPI

## Description 

Ce projet vise à fournir une interface web au projet de [Tejado](https://github.com/tejado/pokemongo-api-demo), permettant de consulter des informations relatives 
au jeu en réalité augmentée Pokémon GO. 

A terme, le service proposera des 'cartes' à distribuer sous forme d'image et d'iframe web pour exposer son avancée en jeu. 

## Usage 

Exécuter le script api.py lancera un serveur web écoutant sur localhost:8080.  
L'accès à l'API se fait via http://localhost:8080/api .  
Il est nécessaire de transmettre les identifiants de l'utilisateur à l'API. Ceci peut se réaliser via les méthodes GET ou POST (via un formulaire par exemple).  

Le paramètre attendu par la page se nomme 'params'. Il doit s'agir d'une chaine de caractère (username&password) encodée en base64 cryptée à l'aide de RSA via la clé publique fournie dans le répetoire 'example'.
Vous trouverez dans ce même répertoire la procédure à suivre pour interroger l'API. 

(A noter que le jeu de clé fournit dans le repo n'est pas celui utilisé en production)

## Démonstration 

Vous pouvez tester l'API ici: http://pokemon-chaipokoi.rhcloud.com/api?user=username&password=password  (OUTDATED, pas sécurisé)

A noter qu'aucune information relative à vos identifiants n'est enregistrée. 

## Example 

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
