document.addEventListener('DOMContentLoaded', ()=>{
    /*
        Initial load of data
    */
    const base = window.location.origin;
    var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val(); 
    const animeId = findGetParameter('animeId');

    loadPage();
    function loadPage(){
        const request = new XMLHttpRequest();
        request.open('GET', base+'/anime/?animeId='+animeId)
        request.onload = ()=>{
            const data = JSON.parse(request.responseText);
            putData(data);
            
        }
        request.setRequestHeader("X-CSRFToken", csrftoken);
        request.send();
    }

    /*
        Function to put data on the page
    */
    function putData(data){
        const anime = data.anime[0];
        document.querySelector("#title").innerHTML = anime.name;
        document.querySelector("#title2").innerHTML = anime.name;
        document.querySelector("#info").innerHTML = anime.info.substr(0,1000);
        document.querySelector("#anime_image").src = anime.image;
        document.querySelector("#release_date").innerHTML = anime.release_date;
        document.querySelector("#average_rating").innerHTML = anime.average_rating;
        document.querySelector("#contributor").innerHTML = data.contributor;
        putGenre(data.genre);
        putSeason(anime.episodes);
    }

    /*
        Function to put genre data
    */
    function putGenre(data){
        var table = document.querySelector("#genre");
        for(var i=0; i< data.length;i++){
            var row = table.insertRow(0);
            var cell1 = row.insertCell(0);
            cell1.innerHTML = data[i].name;
        }
    }
    
    /*
        Function to put Season data
    */
    function putSeason(data){
        var episodes = data.split(',');
        var table = document.querySelector("#seasons");
        for(var i=episodes.length; i>0;i--){
            var row = table.insertRow(0);
            var cell1 = row.insertCell(0);
            cell1.innerHTML = "Season "+ (i)+ " - "+episodes[i-1];
        }
        
    }

    /*
        Funcion to retrive get param
    */
    function findGetParameter(parameterName) {
        var result = null,
            tmp = [];
        location.search
            .substr(1)
            .split("&")
            .forEach(function (item) {
            tmp = item.split("=");
            if (tmp[0] === parameterName) result = decodeURIComponent(tmp[1]);
            });
        return result;
    }
});