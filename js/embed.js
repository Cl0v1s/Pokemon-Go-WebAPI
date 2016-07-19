
/* 
 * Examine la requete pour en extraire les paramètres
 */
function parseQuery()
{
    var regex = new RegExp("params=(.*)");
    var res = regex.exec(window.location.href);
    return res
}


window.onload = function()
{
    var params = parseQuery();
    document.write(params)
}

