<<<<<<< HEAD
const button = document.getElementById("theme-toggle");
button.addEventListener("click", ()=>{
   document.body.classList.toggle("dark-mode");
});
=======
// Seleciona apenas o botão pelo ID
const botao = document.getElementById("theme-toggle");

// Adiciona o evento de clique
botao.addEventListener("click", () => {
   // O 'toggle' adiciona 'dark-mode' se não existir, ou remove se já existir
   document.body.classList.toggle("dark-mode");
});
>>>>>>> 1a2cf675d852f67bf8072f9f106aa7e16a7d965c
