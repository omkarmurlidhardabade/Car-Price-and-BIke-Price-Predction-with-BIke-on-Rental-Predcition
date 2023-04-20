function myFunction() {
    var x = document.getElementById("myInput");
    if (x.type === "password") {
      x.type = "text";
    } else {
      x.type = "password";
    }
  }

  function reset(){
    document.getElementById("myInput").value.reset();
    document.getElementById("uname").value.reset();
}