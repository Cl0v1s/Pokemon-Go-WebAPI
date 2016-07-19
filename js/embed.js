
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
    document.write(result);  
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
    startRequest("http://pokemon-chaipokoi.rhcloud.com/api?params="+params);
}

