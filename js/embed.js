
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
    var player = data["player"];
    showInfo(node("stat"), "Username", player["username"]);
    var since = new Date(player["since"]);
    since = since.getMonth() + "/" + since.getDate() + "/"+since.getFullYear();
    showInfo(node("stat"), "Play since", since);
    showInfo(node("stat"), "Pokecoin", player["pokecoin"]);
    showInfo(node("stat"), "Stardust", player["stardust"]);
    showInfo(node("stat"), "Level", player["level"]);
    showInfo(node("stat"), "Experience", player["xp"] + "/" + player["next_xp"]);
    showInfo(node("stat"), "Capture rate", player["captured"] + "/" + player["encountered"]);
    showInfo(node("stat"), "Pokedex", player["pokedex"]);

    //Affichage des pokemons du joueur
    var team = player["team"];
    team.sort(function(a,b) //tri du plus récent au plus vieux
    {
        if(a.capture_date < b.capture_date)
            return 1;
        else if(b.capture_date < a.capture_date)
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
            showError(node("errors"), "Network or server error, please check your credentials and try again later.");
        }
    };
    console.log("Processing "+url);
    xhttp.open("GET", url, true);
    xhttp.send();
}



window.onload = function()
{
    var params = parseQuery();
    startRequest("https://pokemon-chaipokoi.rhcloud.com/api?params="+params);
}

