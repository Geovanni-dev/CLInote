<p align="right">
  <a href="README.pt.md">🇧🇷 Ler em Português</a>
</p>

<h1 align="center">🗒️ CLInote</h1>

📋 **About**

**CLInote** is a minimalist note manager focused on high productivity for terminal users. Built to be fast, portable, and distraction-free, it lets you create, list, and edit your notes directly from your favorite editor.

---

🚀 **Features**

* **Terminal-First:** Optimized for an agile CLI workflow.
* **Smart:** Automatic detection of the best available editor (Vim > Nano > Notepad).
* **Portable:** Works natively on Windows, Linux, and macOS.
* **Lightweight:** No unnecessary dependencies.

---

📦 **Installation**

```bash
pip install CLInote
```

---

🛠️ **Usage**

After installation, the `gr` command will be available globally:

| Action | Command | Description |
| :--- | :--- | :--- |
| **Create note** | `gr add <name>` | Creates a new note and opens the editor. |
| **List all** | `gr list` | Displays all your saved notes. |
| **Open note** | `gr <name>` | Opens an existing note for editing. |
| **Delete note** | `gr delete <id>` | Permanently removes a note. |

---

💻 **Setting up CLI editors (Recommended)**

For the full terminal experience, install Vim or Nano:

* **Linux:**
    * Ubuntu/Debian: `sudo apt update && sudo apt install vim nano`
    * Fedora: `sudo dnf install vim nano`
* **macOS:** `brew install vim nano`
* **Windows:** `winget install vim.vim nano.nano`

---

💡 **Project Philosophy**

**CLInote** believes that productivity comes from simplicity. The system automatically looks for the most efficient editor in your environment. If no CLI editor is found, the system falls back to your operating system's default editor (Notepad).

---

💡 **Editing Tips**

```
CLInote uses your system editor. Here are the essential commands:

Vim:
  Enter insert/edit mode: Press i.
  Save and quit: ESC, type :x and press Enter.
  Copy text: Hold SHIFT while selecting with the mouse, then use Ctrl + C.

Nano:
  Save: Ctrl + O and Enter.
  Quit: Ctrl + X.
  Copy: Select with the mouse and use Ctrl + Shift + C (or just Enter on some terminals).
```

---

🗂️ **Data Architecture**

Data is stored locally and persistently:
* **Windows:** `%APPDATA%\CLInote\`
* **Linux/macOS:** `~/.config/CLInote/`

---

🛠 **Technologies**

* **Python 3:** Main project language.
* **JSON:** Lightweight, structured metadata storage.
* **Subprocess:** Safe integration with system editors.
* **Shutil:** Smart dependency detection on PATH.

---

📄 **License**

MIT © Geovani Rodrigues 2026