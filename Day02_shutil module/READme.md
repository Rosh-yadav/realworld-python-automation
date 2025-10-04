# 📂 Day 02 – File Sorting Automation with `shutil`

This project demonstrates how to **automatically organize files** into vendor-based folders using Python’s `shutil` module.
It’s designed to clean up messy folders where files from different vendors are dumped together.

---

## 🔎 Scenario / Use Case

Imagine you receive hundreds of files from different vendors. For example:

```
export/
  apple_invoice1.pdf
  intel_report2.csv
  note_dell_01.txt
  samsung_receipt3.pdf
  random_file.pdf
```

Manually sorting these files into folders like `Apple/`, `Intel/`, `Dell/`, etc. is time-consuming.
This script automates the process:

✅ Detects vendor name inside the file name
✅ Creates a folder for that vendor (if not already present)
✅ Moves the file into the correct folder
✅ If no vendor matches → moves file to an **Others/** folder

---

## ⚡ Before vs After

**Before running script (all in one folder):**

```
export/
  apple_invoice1.pdf
  intel_report2.csv
  note_dell_01.txt
  samsung_receipt3.pdf
  random_file.pdf
```

**After running script (organized):**

```
sorted/
  Apple/
    apple_invoice1.pdf
  Intel/
    intel_report2.csv
  Dell/
    note_dell_01.txt
  Samsung/
    samsung_receipt3.pdf
  Others/
    random_file.pdf
```

Terminal output example:

```
Moved apple_invoice1.pdf -> Apple
Moved intel_report2.csv -> Intel
Moved note_dell_01.txt -> Dell
Moved samsung_receipt3.pdf -> Samsung
No vendor match for random_file.pdf; moved -> Others
```

---

## 🛠️ What the Script Does

1. Scans the `export/` folder for all files.
2. For each file:

   * Checks vendor name from a predefined list (`Apple`, `Intel`, `Samsung`, `Dell`).
   * Creates a vendor subfolder under `sorted/` if missing.
   * Moves the file to that folder.
3. If no vendor matches, moves it into `Others/`.

---

## 📥 Input Required

* A folder named **`export/`** containing the files you want to organize.
* Files should have vendor names in their filenames (e.g., `apple_invoice1.pdf`).
* Script will create a **`sorted/`** folder automatically for the output.

---

## 🚀 How to Run

1. Place the script `file_sorter.py` in your project folder.
2. In the same folder, create a subfolder named `export/`.
3. Add some test files into `export/`.
4. Open terminal, `cd` into the project folder, and run:

```bash
python file_sorter.py
```

5. Check the newly created `sorted/` folder to see organized files.

---

