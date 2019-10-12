function openNav() {
  document.getElementById("open").style.display = "none"; 
  document.getElementById("close").style.display = "block";                   
document.getElementById("mySidenav").style.width = "250px";
}

function closeNav() {
  document.getElementById("close").style.display = "none";  
  document.getElementById("open").style.display = "block"; 

document.getElementById("mySidenav").style.width = "0";
}