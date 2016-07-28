/**
 * Raccourcis pour getElementById
 */
function node(id)
{
    return document.getElementById(id);
}

/**
 * Convertit chaine b64 en urlsafe b64
 */
function Base64EncodeUrl(str){
    return str.replace(/\+/g, '-').replace(/\//g, '_').replace(/\=+$/, '');
}

/**
 * Affiche une erreur
 */
function showError(message)
{
    node("generator").innerHTML = "\
    <font color='#D5889D'>Error:</font> "+message;
}

/**
 * Affiche le code d'intégration de la carte
 */
function showCode(token)
{
    node("generator").innerHTML = "\
    Here is your card integration code, paste it in a forum, a web page or any place that supports iframes.<br>\
    <textarea style='width: 100%;'>\
        <iframe scrolling='no' src='https://chaipokoi.github.io/Pokemon-Go-WebAPI/embed.html?params="+token+"' style='width: 100%; height: 325px; overflow: hidden; border:none;' scrolling='NO'></iframe>\
    </textarea>";

    node("sample").src = "https://chaipokoi.github.io/Pokemon-Go-WebAPI/embed.html?params="+token;

}

/**
 * Lance le test de fonctionnement du token
 */
function retrieveStart(token)
{
//récupération de la clef 
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (xhttp.readyState == 4 && xhttp.status == 200) {
            retrieveEnd(token, xhttp.responseText);
        }
        else if(xhttp.readyState == 4)
        {
            //showError(node("errors"), "Network or server error, please check your credentials and try again later.");
        }
    };
    xhttp.open("GET", "https://pokemon-chaipokoi.rhcloud.com/api?params="+token, true);
    xhttp.send();
}

/**
 * Handle de fonctionnement du token
 */
function retrieveEnd(token, result)
{
    result = JSON.parse(result);
    if(result.state == "OK") //si le système fonctionne bien, on affiche le code 
    {
        showCode(token);
    }
    else 
        showError(result.message);
}

/**
 * Obtient le data token et produit le code de carte  
 */
function encryptionStart()
{
    //récupération de la clef 
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (xhttp.readyState == 4 && xhttp.status == 200) {
            encryptionEnd(xhttp.responseText);
        }
        else if(xhttp.readyState == 4)
        {
            //showError(node("errors"), "Network or server error, please check your credentials and try again later.");
        }
    };
    xhttp.open("GET", "https://pokemon-chaipokoi.rhcloud.com/pubkey", true);
    xhttp.send();
}

/**
 * Une fois la clef publique récupérée, on encrypte les données et on les envoie
 */
function encryptionEnd(key)
{
    key = JSON.parse(key);
    key = key.pubkey;

    var username = node("username").value;
    var password = node("password").value;
    var credentials = username+"&"+password;
    
    var encrypt = new JSEncrypt();
    encrypt.setPublicKey(key);
    var token = encrypt.encrypt(credentials);
    token = Base64EncodeUrl(token) + "==";
    console.log(token)
    retrieveStart(token);

}

window.onload = function()
{
    node("process").addEventListener("click", encryptionStart);
}