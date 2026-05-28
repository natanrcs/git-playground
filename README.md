# 🚀 Git Playground: Aprendendo na Prática

Este repositório é o meu "parque de diversões" particular para dominar o Git e o terminal do macOS. O objetivo principal aqui é testar comandos, errar sem medo, criar e excluir arquivos, e fixar o fluxo de trabalho de desenvolvimento.

Afinal, a prática leva à perfeição e eu decidi focar no **"arroz com feijão"** bem feito!

---

## 🛠️ Tecnologias e Ferramentas
*   **Git** (Controle de versão)
*   **Terminal macOS** (Zsh/Bash)
*   **GitHub** (Repositório remoto)

## 🎯 Objetivos deste Repositório
- [x] Entender o fluxo local para o remoto (`add`, `commit`, `push`).
- [x] Praticar a criação e alternância de branches.
- [x] Testar a remoção de arquivos e pastas via terminal.
- [ ] Dominar a resolução de conflitos e merges.

## 📜 Comandos que estou dominando
git init = iniciar o git no repositorio
git add = adiciona os arquivos
git commit -m = mensagem da alteraçao
git branch = mostra qual branch voce tá
git merge = mescla sua alteracao na main
git log = mostra historicos de commits
git diff = mostra a diferença no que foi alterado
git restore = volta para ultima versao do projeto
git switch -c nome-da-branch = cria e entra branch
git pull = atualiza o repo local com base no github
git rebase = pega oque foi alterado e cria uma nova linha do tempo linear

### Branches
```bash
# Criar e entrar em uma nova branch
git switch -c nome-da-branch
```

### Gerenciamento de Arquivos
```bash
# Apagar arquivo local e do Git ao mesmo tempo
git rm nome-do-arquivo.txt

# Apagar uma pasta inteira
git rm -r nome-da-pasta
```

### Sincronização
```bash
# Mesclar alterações na branch principal
git switch main
git merge nome-da-branch
```

---

> 💡 *Conforme eu for evoluindo, este README e os arquivos do projeto serão atualizados. O foco é meter o loco nos commits até o fluxo entrar na mente!*
