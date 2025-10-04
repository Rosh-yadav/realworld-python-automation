
# Day 01: Project Folder Automation 📂

In this project, we automate the creation of a **standard project folder structure** using Python.  
Instead of manually creating folders and files, this script sets everything up for you in seconds.  

---

## 🔑 What You’ll Learn
This script introduces several **core Python concepts** that are commonly used in automation:

1. **Functions (`def`)** → To group related logic into reusable blocks.  
2. **Error Handling (`try-except`)** → To prevent program crashes when folders already exist or unexpected issues occur.  
3. **f-Strings** → To print clear and dynamic messages (e.g., show folder paths).  
4. **Command-Line Arguments (`argparse`)** → To make the script flexible instead of hardcoding values.  
5. **The `main()` Function** → Organizes program flow in a professional way.  
6. **`if __name__ == '__main__'`** → Ensures the script only runs when executed directly.  
7. **Creating Files (`open()`)** → Automatically generates a `README.md` in your new project folder.  

---

## 🚀 How to Run
Run the script with:
```bash
python folder_structure.py "C:\Users\YourName\Projects" MyNewApp
````

* `"C:\Users\YourName\Projects"` → Base path where the project will be created.
* `MyNewApp` → Project folder name.

The script will create this structure:

```
MyNewApp/
│
├── src/
├── assets/
├── tests/
├── docs/
└── README.md
```

---

## 🛠️ Modules Used

* **`os`** → To interact with the operating system (create folders, join paths).
* **`argparse`** → To handle command-line inputs cleanly.

These two modules make the script powerful and flexible for real-world use cases.

---

## 📖 More Learning

For a detailed breakdown of each concept used in this script, see [explanation_notes.md](explanation_notes.md).



