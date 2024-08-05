function validate(e){
    //console.dir(e);
    let first_name=document.getElementById("first_name").value
    let last_name=document.getElementById("last_name").value
    let email=document.getElementById("email").value
    let username=document.getElementById("username").value
    let password=document.getElementById("password").value
    let password2=document.getElementById("password2").value
    // alert(name)
    let first_name_error=document.getElementById("first_name_error")
    let last_name_error=document.getElementById("last_name_error")
    let email_error=document.getElementById("email_error")
    let username_error=document.getElementById("username_error")
    //let password_error=document.getElementById("password_error")
    let password2_error=document.getElementById("password2_error")




    let error=false;
    if( first_name==""){
        first_name_error.innerHTML="First name is Required"
        error=true;
    }
    else
        first_name_error.innerHTML=""

    if(last_name==""){
        last_name_error.innerHTML="Last name is Required"
        error=true;
    }
    else
        last_name_error.innerHTML=""

    if(username==""){
        username_error.innerHTML=" User name is Required"
        error=true;
    }
    else
        username_error.innerHTML=""
    
    

    //email
    let email_pattern=/\b[\w\._]{4,}@\w{3,7}\.\w{2,}/
    if(email==""){
        email_error.innerHTML="Email is required"
        error=true
    }
    else if(!email.match(email_pattern)){
        email_error.innerHTML="please enter a valid email"
        error=true
    }
    else
        email_error.innerHTML=""

    //password 
    // let password_pattern = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$/
    // if(!password.match(password_pattern)){
    //     password_error.innerHTML="please enter a valid password"
    //     error=true
    // }
    // else
    //     password_error.innerHTML=""
    
    if(password!=password2 || password2==""){
        password2_error.innerHTML="password does not match"
        error=true
    }
    else
        password2.error.innerHTML="";
    
    //

    if(error){
        document.getElementById("form").classList.add("was-validated")
        e.preventDefault()
    }
    
}
       
1
// function validate(e){
//     password=document.getElementById('password').value
//     password2=document.getElementById('password2').value
//     cnf_password=document.getElementById('cnf_password')    
//     if (password != password2 || password2==""){
//         cnf_password.innerHTML="password does not match"
//         document.getElementById("form").classList.add("was-validated")
//         e.preventDefault()
        
//     }
    
// }
    
    
