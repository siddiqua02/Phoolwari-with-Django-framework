function validate(e){
   //   console.log(e);
    let name = document.getElementById("name").value
    // alert(name)

    let gender = document.getElementsByName("gender")
    let mobile = document.getElementById("mobile").value
    let email = document.getElementById("email").value
    let address = document.getElementById("address").value
    let password = document.getElementById("password").value
    let password2 = document.getElementById("password2").value
    let term = document.getElementById("term").checked

    let name_error = document.getElementById("name_error")
    let gender_error = document.getElementById("gender_error")
    let mobile_error = document.getElementById("mobile_error")
    let email_error = document.getElementById("email_error")
    let address_error = document.getElementById("address_error")
    let password_error = document.getElementById("password_error")
    let password2_error = document.getElementById("password2_error")
    let term_error = document.getElementById("term_error")
    
    let error = false

    if(name==""){
        name_error.innerHTML="name is required"
        error=true

    }
    else{
        name_error.innerHTML=""
    }
    //gender
    if(!gender[0].checked && !gender[1].checked){
        gender_error.innerHTML="Gender is required field"
        error = true
    }
    else{
        gender_error.innerHTML=""
    }
    //mobile
    let mobile_pattern=/[6-9][0-9]{9}/
    if(!mobile.match(mobile_pattern)){
        mobile_error.innerHTML="Please enter valid mobile number"
        error = true
    }
    else{
        mobile_error.innerHTML=""
    }
    let email_pattern = /\b[\w\._]{4,}@\w{3,7}\.\w{2,}/
    if(!email.match(email_pattern)){
        email_error.innerHTML="Please enter valid email"
        error = true
    }
    else{
        email_error.innerHTML=""
    }
    if(address===""){
        address_error.innerHTML="Address is required"
        error=true

    }
    else{
        address_error.innerHTML=""
    }

    if(country===""){
        country_error.innerHTML="Country is Required"
    }
    else{
        country_error.innerHTML=""
    }
    //password
    let pass_pattern = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,16}/
    if(!password.match(pass_pattern)){
        password_error.innerHTML="Please enter a strong password "
        error=true
    }
    else{
        password_error.innerHTML=""
    }
    if(password!==password2){
        password2_error.innerHTML="Password and confirm password not same"
        error=true
    }
    else{
        password2_error.innerHTML=""
    }
    if(!term){
        term_error.innerHTML="Please agree to terms and conditions"
        error=true
    }
    else{
        term_error.innerHTML=""
    }

    if(error){
        document.getElementById("form").classList.add("was-validated")
        e.preventDefault()
    }

}