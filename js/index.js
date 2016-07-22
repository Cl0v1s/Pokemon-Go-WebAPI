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

    key = "-----BEGIN PUBLIC KEY-----\
AAAAB3NzaC1yc2EAAAADAQABAAABAQDOUwbPkzLjcfyffjdOiOMygM/HEii2tQ3LAH425gFhVY7Z/TvvTKaUwvmwMPyKfIgZOwT8z9TiZOM8wABT8Niq/yje3F42AtYy0iQxKg7eVMgZh6QrFHAeOP8rfmWuhw0M0W0HmpyEhCeGpF9HnRzF9WozJOFQYatRoiNzh0V5nwBIcNdO010wHzlbrfAl0wEx4UdhZaW+18kbkNlcZKO0VHU9bRXUQ+aDRxX1gK/stWF1/XOhfIHa24ME+R1VNRqS+ku9TymPn4CDlzK7OfcFXt5yYBKc1th89FlO2w9LFx4ApogzDya1kpfqIQ50oVHQjGbKf7o5NXazJ8KUgzKp\
-----END PUBLIC KEY-----";
    

    console.log(key);

    key = RSA.getPublicKey(key);
    console.log(key);
    var token = RSA.encrypt(credentials, key);
    console.log(token);
}

window.onload = function()
{
    node("process").addEventListener("click", processStart);
}