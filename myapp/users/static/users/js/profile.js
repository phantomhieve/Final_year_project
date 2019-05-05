document.addEventListener('DOMContentLoaded', () => {
    var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
    const base = window.location.origin;
    document.querySelector('#edit_profile').onclick = () => {
        const request = new XMLHttpRequest();
        
        const fname   = document.querySelector('#fname').value;
        const lname   = document.querySelector('#lname').value;
        const email   = document.querySelector('#email').value;
        const country = document.querySelector('#country').value;
        const dob     = document.querySelector('#dob').value;
        var pic;
        
        var input = document.querySelector("#pic");
        var fReader = new FileReader();
        fReader.readAsDataURL(input.files[0]);
        fReader.onloadend = function(event){
            var img = document.getElementById("yourImgTag");
            pic = event.target.result;
            

        }





        request.open('POST', base+'/profile/');
        
        request.onload = ()=>{
            const data = JSON.parse(request.responseText);
            message = 'Sucessfully updated data'
            if(! data.success)
                message = 'Try again ERROR occoured'
            alert(message);
        }
        
        request.setRequestHeader("X-CSRFToken", csrftoken);
        const data = new FormData();
        data.append('name', fname+' '+lname)
        data.append('image', pic);
        data.append('email', email);
        data.append('country', country);
        data.append('dob', dob);
        request.send(data);
        return false;

    }
    document.querySelector('#change_pass').onclick = () => {

    }
});