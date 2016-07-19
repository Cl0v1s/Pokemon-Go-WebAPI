
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
        node("errors").innerHTML = "<ul><li>"+data.message+"</li></ul>"; //affichage de l'erreur
        return;
    }
    //Affichage des statistiques
    showInfo(node("stat"), "Username", data["username"]);
    showInfo(node("stat"), "Play since", data["since"]);
    showInfo(node("stat"), "Pokecoin", data["pokecoin"]);
    showInfo(node("stat"), "Stardust", data["stardust"]);
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

