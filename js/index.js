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
            //showError(node("errors"), "Network or server error, please check your credentials and try again later.");
        }
    };
    xhttp.open("GET", "http://localhost:8080/pubkey", true);
    xhttp.send();
}

function processEnd(key)
{
    key = JSON.parse(key);
    var e = key.e;
    var n = key.n;

    var username = node("username").value;
    var password = node("password").value;
    var credentials = username+"&"+password;
    
    var encrypter = new RSAKey;
    console.log(e);
    console.log(n);
    encrypter.setPublic(n,e);
    var cypher = encrypter.encrypt(credentials);
    console.log(cypher);

}

window.onload = function()
{
    node("process").addEventListener("click", processStart);
}