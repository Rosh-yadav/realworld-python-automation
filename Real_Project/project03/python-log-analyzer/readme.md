# Python Log Analyzer

## Overview

The **Python Log Analyzer** is a Python automation project that analyzes application log files and generates a summary report.

It counts log levels (INFO, WARNING, ERROR), extracts error messages, and reports the overall health of the application logs.

This project simulates a common DevOps task of monitoring and analyzing application logs.

---

## Features

* Read application log files
* Count INFO, WARNING, and ERROR entries
* Extract error messages
* Generate a log analysis report
* Display overall application status

---

## Project Structure

```text
python-log-analyzer/

├── application.log
├── analyzer.py
├── result.txt
└── README.md
```

---

## Technologies Used

* Python 3
* File Handling
* Lists
* Dictionary
* String Parsing

---

## How It Works

1. Read the log file.
2. Parse each log entry.
3. Count log levels.
4. Extract error messages.
5. Generate a report.

---

## Sample Report

```text
=================================
Log Analysis Report
=================================

Total Log Entries : 8

INFO : 4
WARNING : 2
ERROR : 2

Errors Found

Database Connection Failed
API Timeout

Status : ATTENTION REQUIRED
```

---

## Python Concepts Practiced

* File Handling
* String Manipulation
* Dictionary
* Lists
* Conditional Statements
* Report Generation

---

## Future Improvements

* Search logs by date
* Count repeated errors
* Generate HTML reports
* Export reports to CSV
* Support multiple log files
* Add command-line arguments

---

