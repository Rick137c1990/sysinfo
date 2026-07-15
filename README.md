# Sysinfo

`Sysinfo` is a small system information utility written in Python.

It is designed to quickly collect basic information about a local computer or server.

## Features

The utility can display the following information:

1. **Operating System**

   Examples:

   * Linux
   * Darwin (macOS)

2. **Hostname**

   Example:

   * MacBook-Air.local

3. **Kernel Version**

4. **System Architecture**

   Example:

   * 64bit

5. **Python Version**

6. **IP Address**

7. **CPU Information**

   Example:

   * ARM

8. **Memory (RAM)**

   Displays:

   * Total memory
   * Available memory
   * Used memory
   * Free memory
   * Memory usage percentage

---

## Example Output

```text
=============== System ===============
OS             : Darwin
Hostname       : Sergej--MacBook-Air.local
Kernel         : 25.5.0
Architecture   : 64bit

=============== Python ===============
Version        : 3.11.7

=============== Network ===============
IP             : 192.168.1.109

=============== CPU ===============
CPU            : ARM

=============== RAM ===============
Total          : 8.00 GB
Available      : 1.61 GB
Used           : 2.92 GB
Free           : 0.07 GB
Percent        : 79.9%
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
```

Navigate to the project directory:

```bash
cd sysinfo
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment.

### Linux / macOS

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

Install the project dependencies:

```bash
pip install -e .
```

---

## Requirements

* Python >= 3.11

---

## Project Structure

```text
sysinfo/
│
├── src/
│   ├── main.py
│   └── sysinfo.py
│
├── README.md
├── pyproject.toml
├── .python-version
└── .gitignore
```

---

## Technologies Used

* Python 3
* psutil
* socket
* platform
* Git

---

## Author

Sergej Nazarov
