document.addEventListener('DOMContentLoaded', ()=>{
    /* 
        Initial load of data
    */
    var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
    const request = new XMLHttpRequest();
    const base = window.location.origin;

    request.open('GET', base+'/animes/?page=1');
    request.onload = ()=>{
        const data = JSON.parse(request.responseText);
        putData(data);
    }
    
    /*
        Function to call data from pagination
    */


    /*
        Function to put data in the cards
    */
    function putData(data){
        size = data.length
        for(var i=1; i<size+1; i++){
            var anime = data[i-1];
            document.querySelector("#image_"+i).src = anime.image;
            document.querySelector("#title_"+i).innerHTML = anime.name;
            document.querySelector("#data_"+i).innerHTML = anime.info.substring(0,200)+"....";
        }
        for(var i=size+1; i<10;i++){
            document.querySelector("#card_"+i).style.display = "none";
        }
    }
    request.setRequestHeader("X-CSRFToken", csrftoken);
    request.send();
    return false;
});