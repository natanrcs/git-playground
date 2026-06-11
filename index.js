const inputName = document.getElementById("inputName").value;
const inputEmail = document.getElementById("inputEmail").value;
const messageContent = document.getElementById("messageContent").value;
const button = document.getElementById("button");
databaseTempory = []

function functiongetDados(databaseTempory,inputName,inputEmail,messageContent){
    allDados = {"names": inputName,"emails": inputEmail,"messages":messageContent};
    if(allDados.names === "" | allDados.emails === "" | allDados.messageContent === ""){
        alert("Preencha os campos abaixos!");
    };
    databaseTempory.append(allDados);
    console.log("Dados salvos no database.");
};
button.addEventListener("click",functiongetDados);