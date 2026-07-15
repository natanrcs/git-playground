# 🚀 Git Playground: Aprendendo na Prática

Eeste repo é um playground pessoal onde vou colocar em pratica o uso de versionamento com git.
Aqui posso errar a vontade e entender como o versionamento funciona na prática e pegar o fluxo do dia a dia usando comandos essenciais do git.

Comandos essenciais do dia-a-dia:
git status - mostra o estado atual do repositório: arquivos modificados, adicionados (staged) ou não rastreados

git branch - lista as branches existentes no repositório (a atual aparece marcada com *)

git branch -b nova-branch - obs: a flag correta é "git checkout -b nova-branch" ou "git switch -c nova-branch"; cria e já move para uma nova branch chamada "nova-branch"

git rebase - reaplica os commits de uma branch em cima de outra, reescrevendo o histórico para deixá-lo linear

git merge - une o histórico de outra branch com a branch atual, criando um commit de merge (quando necessário)

git commit -m "nova mensagem" - grava as alterações que estão na staging area como um novo commit, com a mensagem indicada

git init - inicializa um novo repositório Git na pasta atual

git log - exibe o histórico de commits (autor, data, hash e mensagem)

git diff - mostra as diferenças entre arquivos modificados e o último commit (ou entre outras referências, dependendo dos parâmetros)

git restore - desfaz alterações em arquivos, revertendo-os para o estado do último commit (ou remove do stage, com --staged)

git add . - adiciona todos os arquivos modificados/novos da pasta atual à staging area, preparando-os para o commit

git rm nome-do-arquivo - remove um arquivo do repositório (e do diretório de trabalho) e já marca a remoção para o próximo commit

git rm -r nome-da-pasta - remove uma pasta inteira (recursivamente) do repositório e do diretório de trabalho, marcando para o próximo commit