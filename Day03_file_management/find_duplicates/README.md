
```markdown
# Duplicate File Cleaner Script

## 💡 Use Case

Imagine you are managing a folder with hundreds or thousands of files. Sometimes, duplicates appear automatically with names like:

```

file_abc.jpg
file_abc(1).jpg
file_xyz.jpg
file_xyz(1).jpg

```

- The duplicates have `(1)` at the end of their names.  
- Manually finding and deleting them is **time-consuming** and prone to errors.  
- You want a **safe way to remove duplicates** while keeping the original files intact.  

This script automates the detection and deletion of such duplicate files, saving time and reducing mistakes.

---

## 🎯 Purpose of the Script

- **Automation**: No manual deletion required.  
- **Accuracy**: Only deletes files ending with `(1)` if the original exists.  
- **Safety**: Includes a dry-run mode to test which files would be deleted before actual removal.  
- **Recursive**: Checks all subfolders automatically.

---

## 🔧 Modules Used

1. **`os`**
   - Handles file system operations.
   - Functions used:
     - `os.walk()` → Traverse all folders and subfolders.
     - `os.path.join()` → Create file paths correctly across platforms.
     - `os.path.exists()` → Check if the original file exists.
     - `os.remove()` → Delete files.

---

## 🖥 How It Works

1. The script loops through all files in the given folder (and subfolders).  
2. For each file, it checks if the filename contains `(1)` (indicating a duplicate).  
3. If a duplicate is found:
   - It constructs the path to the duplicate file.
   - It constructs the path to the original file by removing `(1)` from the filename.
   - Checks if the original exists:
     - **Dry-run mode** → Prints what would be deleted.
     - **Delete mode** → Deletes the duplicate file.  
4. If the original file is missing, the script skips the duplicate.

---

## 📂 Example Scenario

**Before Running Script:**

```

images/
├── holiday1.jpg
├── holiday1(1).jpg
├── holiday2.jpg
├── holiday2(1).jpg

```

**Dry-Run Mode Output:**

```

(Dry-run) Would delete: images/holiday1(1).jpg
(Dry-run) Would delete: images/holiday2(1).jpg

```

**After Delete Mode:**

```

images/
├── holiday1.jpg
├── holiday2.jpg

````


````

---

## ⚡ How to Run

1. Open terminal or command prompt.
2. Navigate to the folder where the script is saved:

```bash
cd C:\Users\YourName\Downloads\python_automation
```

3. Run in **dry-run mode** (safe testing):

```bash
python file.py
```

4. Run in **delete mode** (actual deletion):

```python
delete_duplicate_files(base_folder, delete=True)
```

---

---

## 🌟 Summary

This script is a **simple and safe way to clean duplicate files**. It automates what would be a repetitive and error-prone task, saves time, and ensures that your original files are never deleted by mistake.

`