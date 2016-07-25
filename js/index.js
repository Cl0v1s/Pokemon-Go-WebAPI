/**
 * Raccourcis pour getElementById
 */
function node(id)
{
    return document.getElementById(id);
}

/**
 * Obtient le data token et produit le code de carte  
 */
function processStart()
{
    //récupération de la clef 
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (xhttp.readyState == 4 && xhttp.status == 200) {
            processEnd(xhttp.responseText);
        }
        else if(xhttp.readyState == 4)
        {
            showError(node("errors"), "Network or server error, please check your credentials and try again later.");
        }
    };
    xhttp.open("GET", "https://pokemon-chaipokoi.rhcloud.com/pubkey", true);
    xhttp.send();
}

function processEnd(key)
{
    key = JSON.parse(key).pubkey;
    //key = key.replace(/\n/g, "");
    var username = node("username").value;
    var password = node("password").value;
    var credentials = username+"&"+password;
    


}

window.onload = function()
{
    node("process").addEventListener("click", processStart);
}