# 🗒️ notesCLI

📋 **Sobre**

O **notesCLI** é um gerenciador de notas minimalista, focado em alta produtividade para quem vive no terminal. Desenvolvido para ser rápido, portátil e sem distrações, permitindo que você crie, liste e edite suas notas diretamente pelo seu editor favorito.

🚀 **Funcionalidades**

* **Terminal-First:** Otimizado para um fluxo de trabalho CLI ágil.
* **Inteligente:** Detecção automática do melhor editor disponível (Vim > Nano > Notepad).
* **Portátil:** Funciona nativamente em Windows, Linux e macOS.
* **Leve:** Sem dependências desnecessárias.

📦 **Instalação**

```bash
pip install notesCLI
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

O **notesCLI** acredita que a produtividade vem da simplicidade. O sistema buscará automaticamente o editor mais eficiente no seu ambiente. Caso nenhum editor CLI seja encontrado, o sistema utiliza o editor padrão do seu sistema operacional (Notepad).

🗂️ **Arquitetura de Dados**

Os dados são armazenados localmente de forma persistente:
* **Windows:** `%APPDATA%\notesCLI\`
* **Linux/macOS:** `~/.config/notesCLI/`

🛠 **Tecnologias**

* **Python 3:** Linguagem principal do projeto.
* **JSON:** Armazenamento leve e estruturado dos metadados.
* **Subprocess:** Integração segura com editores de sistema.
* **Shutil:** Detecção inteligente de dependências no PATH.

📄 **Licença**

MIT © Geovani Rodrigues 2026