function loadDoc(url, cFunction) {
    var xhttp = new XMLHttpRequest();//Creating a new XMLHttpRequest object to handle AJAX
    xhttp.onreadystatechange = function() {//Event handler for when the AJAX call state changes
        if (this.readyState == 4 && this.status == 200) {//Check if AJAX call was successful
            cFunction(this);//Calling the callback function to handle the AJAX response
        }
    };
    xhttp.open("GET", url, true);//Configuring the AJAX request
    xhttp.send();//Sending the AJAX request
}
function myFn1(xhttp) {
    document.getElementById("menu").innerHTML = xhttp.responseText;//Updating the HTML of the menu element with the AJAX response
}

function myFn2(xhttp) {
    document.getElementById("cafe").innerHTML = xhttp.responseText;//Updating the HTML of the cafe element with the AJAX response
}