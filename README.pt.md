<p align="right">
  <a href="README.md">🇺🇸 English</a>
</p>

<h1 align="center">🗒️ CLInote</h1>

📋 **Sobre**

O **CLInote** é um gerenciador de notas minimalista, focado em alta produtividade para quem vive no terminal. Desenvolvido para ser rápido, portátil e sem distrações, permitindo que você crie, liste e edite suas notas diretamente pelo seu editor favorito.

---

🚀 **Funcionalidades**

* **Terminal-First:** Otimizado para um fluxo de trabalho CLI ágil.
* **Inteligente:** Detecção automática do melhor editor disponível (Vim > Nano > Notepad).
* **Portátil:** Funciona nativamente em Windows, Linux e macOS.
* **Leve:** Sem dependências desnecessárias.

---

📦 **Instalação**

```bash
pip install CLInote
```

---

🛠️ **Como usar**

Após a instalação, o comando `gr` estará disponível globalmente:

| Ação | Comando | Descrição |
| :--- | :--- | :--- |
| **Criar nota** | `gr add <nome>` | Cria uma nova nota e abre o editor. |
| **Listar tudo** | `gr list` | Exibe todas as suas notas salvas. |
| **Abrir nota** | `gr <nome>` | Abre uma nota existente para edição. |
| **Deletar nota** | `gr delete <id>` | Remove uma nota permanentemente. |

---

💻 **Configurando editores CLI (Recomendado)**

Para a experiência completa no terminal, instale o Vim ou Nano:

* **Linux:**
    * Ubuntu/Debian: `sudo apt update && sudo apt install vim nano`
    * Fedora: `sudo dnf install vim nano`
* **macOS:** `brew install vim nano`
* **Windows:** `winget install vim.vim nano.nano`

---

💡 **Filosofia do Projeto**

O **CLInote** acredita que a produtividade vem da simplicidade. O sistema buscará automaticamente o editor mais eficiente no seu ambiente. Caso nenhum editor CLI seja encontrado, o sistema utiliza o editor padrão do seu sistema operacional (Notepad).

---

💡 **Dicas de Edição**

```
O CLInote utiliza o editor do sistema. Aqui estão os comandos essenciais:

Vim:
  Entrar no modo de inserção/editar: Pressione i.
  Salvar e sair: ESC, digite :x e dê Enter.
  Copiar texto: Segure SHIFT enquanto seleciona com o mouse, depois use Ctrl + C.

Nano:
  Salvar: Ctrl + O e Enter.
  Sair: Ctrl + X.
  Copiar: Selecione com o mouse e use Ctrl + Shift + C (ou apenas Enter em alguns terminais).
```

---

🗂️ **Arquitetura de Dados**

Os dados são armazenados localmente de forma persistente:
* **Windows:** `%APPDATA%\CLInote\`
* **Linux/macOS:** `~/.config/CLInote/`

---

🛠 **Tecnologias**

* **Python 3:** Linguagem principal do projeto.
* **JSON:** Armazenamento leve e estruturado dos metadados.
* **Subprocess:** Integração segura com editores de sistema.
* **Shutil:** Detecção inteligente de dependências no PATH.

---

📄 **Licença**

MIT © Geovani Rodrigues 2026
