const buttonTheme = document.getElementById("theme-toggle");
buttonTheme.addEventListener("click",()=>{
   document.body.classList.toggle("dark-mode");
   console.log("tema alterado com sucesso!")
});
