document.addEventListener('DOMContentLoaded', ()=>{
    var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
    const base = 'http://127.0.0.1:8000/'
    document.querySelector('#login').onclick  = ()=>{
        const request = new XMLHttpRequest();

        const name = document.querySelector('#name').value; 
        const pass = document.querySelector('#pass').value;
        
        request.open('POST', base);
        
        request.onload = ()=>{
            const data = JSON.parse(request.responseText);
            if(data.success)
                window.location.replace(base+'main/');
            else
                document.querySelector('#message_login').innerHTML = 'Invalid Username/Password';
            
        }
        request.setRequestHeader("X-CSRFToken", csrftoken);
        const data = new FormData();
        data.append('username', name);
        data.append('pass', pass);
        request.send(data);
        return false;
    }



    document.querySelector('#register').onclick  = ()=>{
        const request = new XMLHttpRequest();
    
        const name   = document.querySelector('#regname').value; 
        const pass   = document.querySelector('#regpass').value;
        const repass = document.querySelector('#reregpass').value;
        var message = ''
        if(/^[a-zA-Z0-9- ]*$/.test(name) == false)
            message = 'Username should be alphanumeric';
        else if(pass!=repass)
            message = 'Passwords don\'t match';
        else if(pass.length<6)
            message = 'Too short password'
        
        if(message!=''){
            document.querySelector('.message_register').innerHTML = message;
            return false;
        }

        request.open('POST', base+'check/');
        request.onload = ()=>{
            const data = JSON.parse(request.responseText);
            if(data.success)
                window.location.replace(base+'register/')
            else
                message = 'Username allredy exist';
            document.querySelector('.message_register').innerHTML = message;
        }
        
        request.setRequestHeader("X-CSRFToken", csrftoken);
        const data = new FormData();
        data.append('name', name);
        data.append('pass', pass);
        request.send(data);
        return false;
    }

});