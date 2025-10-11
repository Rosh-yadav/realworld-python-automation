# 📂 Python File Renaming Automation 

## 💡 Problem Scenario

In file management, a common need is to **rename multiple files** in bulk.
For example:

* You have files: `pic1.jpg, pic2.jpg, pic3.jpg …`
* You want to rename them as: `holiday-1-pic1.jpg, holiday-2-pic2.jpg, holiday-3-pic3.jpg`.

Doing this manually for hundreds of files is **slow and error-prone**.
👉 With Python, we can **automate** this task using a simple script.

---

## ⚙️ Python Concepts Used

### 1. `import os`

We use Python’s built-in **`os` module** for:

* Reading files inside a folder.
* Joining folder path and filenames (`os.path.join`).
* Renaming files (`os.rename`).

---

### 2. Functions (`def`)

We put our logic inside a **function** so the code is reusable.

```python
def bulk_rename_files(folder_path, new_name_prefix, file_extension):
    ...
```

Here:

* `folder_path` → folder where files exist.
* `new_name_prefix` → new prefix for renamed files.
* `file_extension` → filter (like `.jpg` or `.txt`).

---

### 3. Listing & Filtering Files

```python
files = sorted([f for f in os.listdir(folder_path) if f.endswith(file_extension)])
```

* `os.listdir(folder_path)` → lists everything in the folder.
* `f.endswith(file_extension)` → only keep files like `.jpg`.
* `sorted(...)` → ensures files are renamed in order (`pic1.jpg, pic2.jpg, …`).

---

### 4. `enumerate`

```python
for index, filename in enumerate(files, start=1):
```

* `enumerate` gives both the **index** and the **filename**.
* Example:

  ```
  (1, "pic1.jpg")
  (2, "pic2.jpg")
  (3, "pic3.jpg")
  ```

---

### 5. Building Paths

```python
old_path = os.path.join(folder_path, filename)
new_filename = f"{new_name_prefix}-{index}-{filename}"
new_path = os.path.join(folder_path, new_filename)
```

* `old_path` → where the file is right now.
* `new_filename` → what we want to rename it to.
* `new_path` → full new path including folder.

---

### 6. Renaming Files

```python
os.rename(old_path, new_path)
```

This renames/moves the file from `old_path` to `new_path`.

### Before:

```
images/
├── pic1.jpg
├── pic2.jpg
├── pic3.jpg
```

### After:

```
images/
├── holiday-1-pic1.jpg
├── holiday-2-pic2.jpg
├── holiday-3-pic3.jpg
```

---


