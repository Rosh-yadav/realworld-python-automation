# System Health Checker (Python)

## Overview

The **System Health Checker** is a Python automation project that monitors the health of a local system by checking CPU usage, memory usage, disk usage, and system uptime. It generates a health report that can be used for basic system monitoring.

This project was built as part of my **Python for DevOps** learning journey to understand how Python can automate routine system administration tasks.

---

## Features

* Monitor CPU usage
* Monitor Memory usage
* Monitor Disk usage
* Display System Uptime
* Generate a health report
* Display system status (Healthy, Warning, Critical)
* Execute system commands using the `subprocess` module

---

## Project Structure

```text
system-health-checker-python/

├── main.py
├── reports/
│   └── report_YYYY_MM_DD_HH_MM_SS.txt
└── README.md
```

---

## Technologies Used

* Python 3
* psutil
* datetime
* subprocess
* colorama
* File Handling

---

## How It Works

1. Collect system health metrics.
2. Compare resource usage against threshold values.
3. Display the health status.
4. Save the results into a report file.
5. Execute a system command using the `subprocess` module.

---

## Sample Report

```text
==============================
System Health Report
==============================

CPU Usage      : 21%
Memory Usage   : 48%
Disk Usage     : 62%

Status : Healthy

Generated At:
2026-07-10 10:30:25
```

---

## Python Concepts Practiced

* Functions
* File Handling
* Exception Handling
* psutil
* subprocess
* datetime
* Conditional Statements
* Report Generation

---

## Future Improvements

* HTML report generation
* Email notifications
* Configurable thresholds using JSON
* Continuous monitoring
* Export reports to CSV

---
