function validateform() {
    var name = document.myform.name.value;
    var password = document.myform.password.value;
    var re_password=document.myform.re_password.value;
    var x = document.myform.email.value;
    var atposition = x.indexOf("@");
    var dotposition = x.lastIndexOf(".");

    if (name == null || name == "") {
        alert("Name can't be blank");
        return false;
    } else if (password.length < 6) {
        alert("Password must be at least 6 characters long.");
        return false;
    }
    else if(re_password.length<6){
        alert("conform password must be at least 6 characters long.");
        return false;
    }
    
    

    if (atposition < 1 || dotposition < atposition + 2 || dotposition + 2 >= x.length) {
        alert("Please enter a valid e-mail address \n atpostion:" + atposition + "\n dotposition:" + dotposition);
        return false;
    }

    if(password==re_password){
        return true;
    }
    else{
        alert("Both Password should be same");
        return false;
    }
}  
function myfunction(){
    var x=document.myform.password.value;
    if(x.type=="password"){
        x.type="text";

    }else{
        x.type="password";
    }
}


   
