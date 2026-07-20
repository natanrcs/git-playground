// Seleciona apenas o botão pelo ID
const botao = document.getElementById("theme-toggle");

// Adiciona o evento de clique
botao.addEventListener("click", () => {
   // O 'toggle' adiciona 'dark-mode' se não existir, ou remove se já existir
   document.body.classList.toggle("dark-mode");
});
