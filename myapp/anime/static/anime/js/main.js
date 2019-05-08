document.addEventListener('DOMContentLoaded', ()=>{
    /* 
        Initial load of data
    */
    const base = window.location.origin;
    var total_pages = 1 , current_page = 1;
    var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
    loadPage();
    
    
    function loadPage(){
        const request = new XMLHttpRequest();
        request.open('GET', base+'/page/')
        request.onload = ()=>{
            const data = JSON.parse(request.responseText);
            total_pages = data.pages;
            changePage(current_page);
        }
        request.setRequestHeader("X-CSRFToken", csrftoken);
        request.send();
    }

    /*
        Function to change page
    */
   function changePage(page){
        const request = new XMLHttpRequest();
        request.open('GET', base+'/animes/?page='+page);
        request.onload = ()=>{
            const data = JSON.parse(request.responseText);
            putData(data);
        }
        request.setRequestHeader("X-CSRFToken", csrftoken);
        request.send(null);
   }
    
    
    /*
        Pagination previous page
    */
   document.querySelector('#btn_prev').onclick = (event)=>{
        event.preventDefault();
        if (current_page > 1) {
            current_page--;
            document.querySelector('#page').innerHTML = current_page;
            changePage(current_page);
        }
        else{
            M.toast({html:"You are on first page", classes: 'rounded'})
        }
    }

    /*
        Pagination next page
    */
    document.querySelector('#btn_next').onclick = (event)=>{
        event.preventDefault();
        if (current_page < total_pages) {
            current_page++;
            document.querySelector('#page').innerHTML = current_page;
            changePage(current_page);
        }
        else{
            M.toast({html:"You are on last page", classes: 'rounded'})
        }
    }
    
    /*
        Function to put data in the cards
    */
    function putData(data){
        size = data.length
        for(var i=1; i<10;i++){
            document.querySelector("#card_"+i).style.display = "block";
        }
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
    return false;
});