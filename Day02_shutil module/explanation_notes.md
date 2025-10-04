
````markdown
# 🐍 Python `shutil` Module – Notes

## 📌 What is `shutil`?
- `shutil` stands for **“shell utilities”**.  
- It is part of Python’s **standard library** (no installation needed).  
- It provides **high-level file and folder operations** like copy, move, delete, and archiving.  
- Think of it as an upgrade to the `os` module for handling files/folders.

---

## 📂 Commonly Used Functions

### 1. Copy a File
```python
import shutil
shutil.copy("file.txt", "backup/file.txt")   # copy file only
shutil.copy2("file.txt", "backup/file.txt")  # copy file + metadata (timestamps, permissions)
````

---

### 2. Copy an Entire Folder

```python
shutil.copytree("project_folder", "project_backup")
```

✅ Recursively copies everything inside `project_folder` into `project_backup`.

---

### 3. Move (Cut-Paste) Files or Folders

```python
shutil.move("file.txt", "archive/file.txt")
```

✅ Moves the file to a new location.

---

### 4. Delete a Folder

```python
shutil.rmtree("old_folder")
```

⚠️ Permanently deletes the entire folder and its contents.

---

### 5. Create Archives (Zip/Tar)

```python
shutil.make_archive("project_backup", 'zip', "project_folder")
```

✅ Creates a `project_backup.zip` file containing everything in `project_folder`.

---

### 6. Extract Archives

```python
shutil.unpack_archive("project_backup.zip", "extracted_folder")
```

✅ Extracts contents of the `.zip` into `extracted_folder`.

---

---

## 🔑 Difference Between `os` and `shutil`

* **`os` module** → Low-level tasks (check if file exists, list files, rename).
* **`shutil` module** → High-level tasks (copy, move, delete, archive folders).

---

✅ Use `shutil` whenever you need **file/folder automation** in your projects!

```

### ⚡ Common `shutil` Functions

* `shutil.copy()` → Copy files
* `shutil.copytree()` → Copy entire folders
* `shutil.move()` → Move (cut–paste) files/folders
* `shutil.rmtree()` → Delete folders
* `shutil.make_archive()` → Create zip/tar backups
* `shutil.unpack_archive()` → Extract archives

## 3 — Mistakes you made earlier (and why they were a problem)

1. **Indentation error** — you had:

   ```python
   for filename in os.listdir(...):
       file_path = ...
   if os.path.isfile(file_path):
       ...
   ```

   The `if` was **outside** the for loop due to wrong indentation, so only the last file was checked. Python uses indentation to define blocks — keep the `if` indented under the `for`. Use a linter or `python -m py_compile` to catch this (see below).

2. **Vendor folders created in `source`** — you used:

   ```python
   vendor_folder = os.path.join(source_folder, vendor)
   ```

   That puts `Apple/` inside the `export/` folder. You probably want `sorted/Apple/`. Fix: use `destination_folder`.


3. **`__pycache__` confusion** — Python auto-creates this when it compiles `.py` to `.pyc` (see next section). It’s normal; ignore in git.

---

## 4 — What is `__pycache__` and `.pyc` files? (detailed)

* When Python runs a `.py` file, it first compiles it to **bytecode** so execution is faster next time.
* The compiled bytecode is saved as a `.pyc` file inside `__pycache__/`.
* Example filename: `file_sorter.cpython-311.pyc` (the `cpython-311` part depends on your Python version).
* This caching speeds up startup because Python can reuse the `.pyc` if the `.py` hasn't changed.
* You should **not** commit `__pycache__/` or `.pyc` files into git — add them to `.gitignore`.

---

## 5 — How to run & test (step-by-step)

1. Place the script `file_sorter.py` in a folder, and in the same folder create `export/`.
2. Add test files to `export/`:

   * `apple_invoice1.pdf`
   * `intel_report1.csv`
   * `note_dell_01.txt`
   * `random_file.pdf`
3. Open terminal / VS Code Terminal, `cd` into the folder that contains `file_sorter.py`.
4. Run:

   ```bash
   python file_sorter.py
   ```
5. Check the new `sorted/` folder — it should have `Apple/`, `Intel/`, `Dell/`, `Others/`. Files moved accordingly.

---

## 6 — How to find indentation / syntax errors

* Quick syntax check:

  ```bash
  python -m py_compile file_sorter.py
  ```

  * If there is a syntax or indentation error, Python prints it (e.g., `IndentationError: expected an indented block`).
  * If no output, syntax is OK.

* Use a linter (reports style and errors):

  ```bash
  pip install flake8
  flake8 file_sorter.py
  ```

  * Fix issues reported by linter.

* Use an editor with Python support:

  * **VS Code** with the Python extension and the Pylance language server will highlight indentation and syntax mistakes as you type.
  * **PyCharm** also highlights problems.

* Add debug prints to see control flow:

  ```python
  print("Looping over:", filename)
  ```

  If it prints only once, your loop may be broken by wrong indentation.

---

## 7 — .gitignore content (recommended)

Create a `.gitignore` file in your repo with this content:

```
# Python cache and compiled files
__pycache__/
*.pyc

# Common IDE/editor folders
.vscode/
.idea/

# OS files
.DS_Store
Thumbs.db
```


## 8 — Final tips & small checklist before running

* ✅ Confirm `file_sorter.py` and `export/` are in the same folder (or use full paths).
* ✅ Run `python -m py_compile file_sorter.py` to catch syntax/indentation errors.
* ✅ Use VS Code highlighting or `flake8` for style mistakes.