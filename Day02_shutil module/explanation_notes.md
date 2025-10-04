
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
