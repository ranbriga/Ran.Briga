function openForm() {
  var a = document.getElementById("myForm").style.display;
  if ( a != "block" ){
    document.getElementById("myForm").style.display = "block";
  }
}

function closeForm() {
    var b = document.getElementById("myForm").style.display;
  if ( b != "none" ){
    document.getElementById("myForm").style.display = "none";
  }
}
