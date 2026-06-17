<h1 align="center">🗒️ CLInote</h1>

📋 **Sobre**

O **CLInote** é um gerenciador de notas minimalista, focado em alta produtividade para quem vive no terminal. Desenvolvido para ser rápido, portátil e sem distrações, permitindo que você crie, liste e edite suas notas diretamente pelo seu editor favorito.

🚀 **Funcionalidades**

* **Terminal-First:** Otimizado para um fluxo de trabalho CLI ágil.
* **Inteligente:** Detecção automática do melhor editor disponível (Vim > Nano > Notepad).
* **Portátil:** Funciona nativamente em Windows, Linux e macOS.
* **Leve:** Sem dependências desnecessárias.

📦 **Instalação**

```bash
pip install CLInote
```

🛠️ **Como usar**

Após a instalação, o comando `nc` estará disponível globalmente:

| Ação | Comando | Descrição |
| :--- | :--- | :--- |
| **Criar nota** | `nc add <nome>` | Cria uma nova nota e abre o editor. |
| **Listar tudo** | `nc list` | Exibe todas as suas notas salvas. |
| **Abrir nota** | `nc <nome>` | Abre uma nota existente para edição. |
| **Deletar nota** | `nc delete <id>` | Remove uma nota permanentemente. |

💻 **Configurando editores CLI (Recomendado)**

Para a experiência completa no terminal, instale o Vim ou Nano:

* **Linux:**
    * Ubuntu/Debian: `sudo apt update && sudo apt install vim nano`
    * Fedora: `sudo dnf install vim nano`
* **macOS:** `brew install vim nano`
* **Windows:** `winget install vim.vim nano.nano`

💡 **Filosofia do Projeto**

O **CLInote** acredita que a produtividade vem da simplicidade. O sistema buscará automaticamente o editor mais eficiente no seu ambiente. Caso nenhum editor CLI seja encontrado, o sistema utiliza o editor padrão do seu sistema operacional (Notepad).

💡 **Dicas de Edição**
```` bash
O CLInote utiliza o editor do sistema. Aqui estão os comandos essenciais:

Vim:
Entrar no modo de inserção/editar: Pressione i.

Salvar e sair: ESC, digite :x e dê Enter.

Copiar texto: Segure SHIFT enquanto seleciona com o mouse, depois use Ctrl + C.

------

Nano:
Salvar: Ctrl + O e Enter.

Sair: Ctrl + X.

Copiar: Selecione com o mouse e use Ctrl + Shift + C (ou apenas Enter em alguns terminais).
````

🗂️ **Arquitetura de Dados**

Os dados são armazenados localmente de forma persistente:
* **Windows:** `%APPDATA%\CLInote\`
* **Linux/macOS:** `~/.config/CLInote/`

🛠 **Tecnologias**

* **Python 3:** Linguagem principal do projeto.
* **JSON:** Armazenamento leve e estruturado dos metadados.
* **Subprocess:** Integração segura com editores de sistema.
* **Shutil:** Detecção inteligente de dependências no PATH.

<h1 align="center">ENGLISH</h1>

📋 **About**

**CLInote** is a minimalist note manager focused on high productivity for terminal users. Built to be fast, portable, and distraction-free, it lets you create, list, and edit your notes directly from your favorite editor.

🚀 **Features**

* **Terminal-First:** Optimized for an agile CLI workflow.
* **Smart:** Automatic detection of the best available editor (Vim > Nano > Notepad).
* **Portable:** Works natively on Windows, Linux, and macOS.
* **Lightweight:** No unnecessary dependencies.

📦 **Installation**

```bash
pip install CLInote
```

🛠️ **Usage**

After installation, the `nc` command will be available globally:

| Action | Command | Description |
| :--- | :--- | :--- |
| **Create note** | `nc add <name>` | Creates a new note and opens the editor. |
| **List all** | `nc list` | Displays all your saved notes. |
| **Open note** | `nc <name>` | Opens an existing note for editing. |
| **Delete note** | `nc delete <id>` | Permanently removes a note. |

💻 **Setting up CLI editors (Recommended)**

For the full terminal experience, install Vim or Nano:

* **Linux:**
    * Ubuntu/Debian: `sudo apt update && sudo apt install vim nano`
    * Fedora: `sudo dnf install vim nano`
* **macOS:** `brew install vim nano`
* **Windows:** `winget install vim.vim nano.nano`

💡 **Project Philosophy**

**CLInote** believes that productivity comes from simplicity. The system automatically looks for the most efficient editor in your environment. If no CLI editor is found, the system falls back to your operating system's default editor (Notepad).

💡 **Editing Tips**

```bash
CLInote uses your system editor. Here are the essential commands:

Vim:
Enter insert/edit mode: Press i.

Save and quit: ESC, type :x and press Enter.

Copy text: Hold SHIFT while selecting with the mouse, then use Ctrl + C.

------

Nano:
Save: Ctrl + O and Enter.

Quit: Ctrl + X.

Copy: Select with the mouse and use Ctrl + Shift + C (or just Enter on some terminals).
```

🗂️ **Data Architecture**

Data is stored locally and persistently:
* **Windows:** `%APPDATA%\CLInote\`
* **Linux/macOS:** `~/.config/CLInote/`

🛠 **Technologies**

* **Python 3:** Main project language.
* **JSON:** Lightweight, structured metadata storage.
* **Subprocess:** Safe integration with system editors.
* **Shutil:** Smart dependency detection on PATH.

📄 **License**

MIT © Geovani Rodrigues 2026

