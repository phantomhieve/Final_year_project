document.addEventListener('DOMContentLoaded', () => {
    
    var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
    const base = window.location.origin;
    const login = findGetParameter('login');

    /*
        emulate form submission on 'Enter'
    */
    document.querySelector('body').addEventListener('keydown', event=>{
        if (event.keyCode == 13) 
            document.querySelector('#login').click();
    });

    /*
        Function to update the user data.
    */
    document.querySelector('#edit_profile').onclick = () => {
        const request = new XMLHttpRequest();
        
        const fname   = document.querySelector('#fname').value;
        const lname   = document.querySelector('#lname').value;
        const email   = document.querySelector('#email').value;
        const country = document.querySelector('#country').value;
        var date    = new Date(document.querySelector('#dob').value);
        const pic     = document.querySelector('#pic');
        const dob     = fixDate(date); 
        
        request.open('POST', base+'/profile/');

        request.onload = ()=>{
            const data = JSON.parse(request.responseText);
            message = 'Sucessfully updated data'
            if(! data.success)
                message = 'Fill all the fields'
            if(login){
                window.location.replace(base+'/main/');
            }
            M.toast({html: message, classes: 'rounded'})
        };
        
        request.setRequestHeader("X-CSRFToken", csrftoken);
        const data = new FormData();
        data.append('name', fname+' '+lname)
        data.append('image', pic.files[0]);
        data.append('email', email);
        data.append('country', country);
        data.append('dob', dob);
        request.send(data);
        return false;

    }
    /*
        Function to display image before upload.
    */
    document.getElementById("pic").onchange = function () {
        var reader = new FileReader();
        reader.onload = function (e) {
            document.getElementById("profile").src = e.target.result;
        };
        reader.readAsDataURL(this.files[0]);
    };
    /*
        Function to fix date
    */
   function fixDate(date){
        var day=date.getDate(), month=date.getMonth()+1, year=date.getFullYear();
        if(month<10) month = '0'+month;
        if(day<10) day = '0'+day;
        return year+"-"+month+"-"+day
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