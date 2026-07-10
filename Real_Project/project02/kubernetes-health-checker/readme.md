# Kubernetes Health Checker (Python)

## Overview

The **Kubernetes Health Checker** is a Python project that analyzes Kubernetes pod information from a text file (simulating `kubectl get pods`) and generates a health report.

This project focuses on parsing command-line output and identifying unhealthy Kubernetes pods.

---

## Features

* Read Kubernetes pod information
* Count Running, Pending, and CrashLoopBackOff pods
* Identify unhealthy pods
* Generate a health report
* Practice parsing structured command output

---

## Project Structure

```text
kubernetes-health-checker/

├── main.py
├── pods.txt
├── report.txt
└── README.md
```

---

## Technologies Used

* Python 3
* File Handling
* Dictionary
* Lists
* Loops

---

## How It Works

1. Read pod information from `pods.txt`.
2. Parse each line.
3. Count pod statuses.
4. Identify unhealthy pods.
5. Generate a report.

---

## Sample Report

```text
==============================
Kubernetes Health Report
==============================

Total Pods : 5

Running : 3
Pending : 1
CrashLoopBackOff : 1

Unhealthy Pods

redis
mysql
```

---

## Python Concepts Practiced

* File Handling
* String Parsing
* Dictionary
* Lists
* Loops
* Conditional Statements
* Report Generation

---

## Future Improvements

* Read live output using `kubectl`
* Generate HTML reports
* Add namespace filtering
* Export reports to CSV
* Highlight unhealthy pods using colors

---