let databaseTempory = [];
const button = document.getElementById("button");

function functiongetDados(){
    const inputName = document.getElementById("inputName").value;
    const inputEmail = document.getElementById("inputEmail").value;
    const messages = document.getElementById("messageContent").value;

    const allDados = {"names":inputName,"emails":inputEmail,"messages":messages};
    if(allDados.names === "" || allDados.emails === "" || allDados.messages === ""){
        alert("Preencha os campos!");
        return;
    }
    databaseTempory.pop(allDados)
    console.log("Salvos com sucesso no database temporario",databaseTempory);
};
button.addEventListener("click",functiongetDados);

function Calopsita() {
    let message = "calopsita master";
    for(let i = 0; i < 10; i++){
        console.log(message);
    }
};