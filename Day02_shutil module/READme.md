
🚀 **Python Real-World Use Case (Day 2)**

Today’s journey is all about the **`shutil` module** — Python’s *shell utilities* that make file & folder automation super easy.

### 🗂️ Use Case: File Sorting

Imagine you have an `export/` folder with hundreds of messy files like:

```
apple_invoice1.pdf
intel_report2.csv
random_file.pdf
```

You want them neatly organized into:

```
sorted/
  Apple/
  Intel/
  Others/
```

That’s where `shutil` comes in! With a small script, you can:
✅ Detect vendors from file names
✅ Create vendor folders automatically
✅ Move files into the right place
✅ Keep your `export/` folder clean

### ⚡ Common `shutil` Functions

* `shutil.copy()` → Copy files
* `shutil.copytree()` → Copy entire folders
* `shutil.move()` → Move (cut–paste) files/folders
* `shutil.rmtree()` → Delete folders
* `shutil.make_archive()` → Create zip/tar backups
* `shutil.unpack_archive()` → Extract archives

### 🔍 Pro Tips

* Use `python -m py_compile script.py` to catch syntax/indentation issues early.
* Ignore `__pycache__/` and `*.pyc` in git (Python auto-generates these).
* Pair with a linter like `flake8` for cleaner code.


This is useful for cleaning up exports from systems that dump many files into one folder.

---

## 2 — What this script does (high level)

* Reads every file from `export/`.
* For each file, detects vendor names from a given list.
* Creates a subfolder for the vendor in `sorted/` (if it does not exist).
* Moves the file into `sorted/<Vendor>/`.
* Prints what it moved.

---

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



## 8 — Example input and expected output (quick)

**Input `export/`:**

```
apple_invoice1.pdf
intel_report2.csv
random_file.pdf
```

**After running:**

```
sorted/
  Apple/
    apple_invoice1.pdf
  Intel/
    intel_report2.csv
  Others/
    random_file.pdf
```

Terminal output:

```
Moved apple_invoice1.pdf -> Apple/
Moved intel_report2.csv -> Intel/
No vendor match for random_file.pdf; moved -> Others/
```

---

## 9 — Final tips & small checklist before running

* ✅ Confirm `file_sorter.py` and `export/` are in the same folder (or use full paths).
* ✅ Run `python -m py_compile file_sorter.py` to catch syntax/indentation errors.
* ✅ Use VS Code highlighting or `flake8` for style mistakes.
* ✅ Add `__pycache__/` and `*.pyc` to `.gitignore` before committing.

---
