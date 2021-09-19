function myFunction() {
    var x = document.getElementById("com-replay");
    var b = document.getElementById("formButton")
    
    if (x.style.display === "none") {
      x.style.display = "block";
      b.style.display = "none"
    } else {
      x.style.display = "none";
      b.style.display = "block"
    }
  } 