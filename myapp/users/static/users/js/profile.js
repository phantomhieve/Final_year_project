document.addEventListener('DOMContentLoaded', () => {
    
    var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
    const base = window.location.origin;


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
        const dob     = document.querySelector('#dob').value;
        const pic     = document.querySelector('#pic');
        
        request.open('POST', base+'/profile/');

        request.onload = ()=>{
            const data = JSON.parse(request.responseText);
            message = 'Sucessfully updated data'
            if(! data.success)
                message = 'Try again ERROR occoured'
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
        Function to change user password.
    document.querySelector('#change_pass').onclick = () => {
    }
    */
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
});