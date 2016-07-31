
/**
 * Raccourcis pour getElementById
 */
function node(id)
{
    return document.getElementById(id);
}

/**
 * Présente une nouvelle information dans le noeud spécifié
 */
function showInfo(nod, name, value)
{
    var html = "<div>\
                    <h2>"+name+"</h2>\
                    <span>"+value+"</span>\
                </div>";
    nod.innerHTML += html;
}

/**
 * Affiche une erreur dans le noeud spécifié
 */
function showError(nod, value)
{
    var html = "<div>\
                    <span>"+value+"</span>\
                </div>";
    nod.innerHTML += html;
}

/* 
 * Examine la requete pour en extraire les paramètres
 */
function parseQuery()
{
    var regex = new RegExp("params=(.*)");
    var res = regex.exec(window.location.href);
    return res[1]
}

/**
 * Examine le résultat d'une requete ajax
 */
function parseResponse(result)
{
    var data = JSON.parse(result);
    //gestion des erreurs
    if(data.state != "OK")
    {
        showError(node("errors"), data.message);
        return;
    }
    //Affichage des statistiques du joueur
    var player = data["results"]["responses"]["GET_PLAYER"]["player_data"];
    console.log(player);
    showInfo(node("stat"), "Username", player["username"]);
    var since = new Date(player["creation_timestamp_ms"]);//affichage de la date de debut de jeu
    since = since.getMonth() + "/" + since.getDate() + "/"+since.getFullYear();
    showInfo(node("stat"), "Play since", since);
    var currencies = player["currencies"]; //affichage des monnaies
    for(var i = 0; i != currencies.length; i++)
    {
        var currency = currencies[i];
        var amount = 0;
        if(currency["amount"] != undefined)
            amount = currency["amount"];
        showInfo(node("stat"), currency["name"], amount);
    }
    var player = data["results"]["responses"]["GET_INVENTORY"]["inventory_delta"]["inventory_items"]; //recherche des stats du joueur dans son inventaire
    for(var i = 0; i != player.length; i++)
    {
        var item = player[i]["inventory_item_data"];
        if(item["player_stats"] != undefined)
        {
            player = item["player_stats"];
            break;
        }
    }
    showInfo(node("stat"), "Level", player["level"]);
    showInfo(node("stat"), "Experience", player["experience"] + "/" + player["next_level_xp"]);
    showInfo(node("stat"), "Capture rate", player["pokemons_captured"] + "/" + player["pokemons_encountered"]);
    showInfo(node("stat"), "Pokedex", player["unique_pokedex_entries"]);

    //Affichage des pokemons du joueur
    var team = new Array();
    var teamData = data["results"]["responses"]["GET_INVENTORY"]["inventory_delta"]["inventory_items"]; //récupération des pokemons
    for(var i = 0; i != player.length; i++)
    {
        var item = teamData[i]["inventory_item_data"];
        if(item["pokemon_data"] != undefined)
        {
            //récupération du sprite
            
            team.push(item["pokemon_data"])
        }
    }
    team.sort(function(a,b) //tri du plus récent au plus vieux
    {
        if(a["creation_time_ms"] < b["creation_time_ms"])
            return 1;
        else if(b["creation_time_ms"] < a["creation_time_ms"])
            return -1;
        else return 0;
    });
    //Suppression des pokémons trop vieux
    team.splice(6,team.length);


    team.forEach(function(entry) {
     showInfo(node("team"), "", "<img src='"+entry.sprite+"'>");   
    });

    
    
}

/* 
 * Démarre une requete AJAX à l'adresse spécifiée
 */
function startRequest(url)
{
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (xhttp.readyState == 4 && xhttp.status == 200) {
            parseResponse(xhttp.responseText);
        }
        else if(xhttp.readyState == 4)
        {
            showError(node("errors"), "There is something wrong with the PokemonGo servers :'(");
        }
    };
    console.log("Processing "+url);
    xhttp.open("GET", url, true);
    xhttp.send();
}



window.onload = function()
{
    var params = parseQuery();
    startRequest("https://localhost:8080/api?params="+params+"&requests=get_player,get_inventory");
}

