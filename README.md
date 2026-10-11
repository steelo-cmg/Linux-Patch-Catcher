# Linux Patch Catcher

A Python-based Linux patch management utility for system information, update detection, security update filtering, and package upgrades.

## Project Overview

Linux Patch Catcher is a Python command-line application designed to simplify basic Linux system patching and update tasks.

Version 1 was developed to provide a simple menu-driven interface for checking system information, identifying available package updates, detecting security-related updates, and installing system upgrades.
Version 2 upgrades the utility into an automated auditing framework by integrating a centralized logging system. This version automatically captures system telemetry, records package state updates chronologically, and implements defensive error-trapping modules to log subprocess exception failures with automated system timestamps. 

The application was developed in Python and tested in a Kali Linux virtual machine.

## Features

- Display system information
- Check available package updates
- Filter upgradeable packages for security-related updates
- Install available system updates
- Handle update failures
- Interactive command-line menu
- - Implement a centralized logging framework using Python's native logger
- Automatically log system telemetry and host details to a master file
- Capture and log stdout raw text blocks directly from system execution
- Engineer explicit try-except loops to log subprocess exception failures
- Standardize log formatting with un-fakeable automated system timestamps


## Technologies Used

- Python
- Linux
- Kali Linux
- APT
- Bash / Linux command line
- Python subprocess module

## How to Run

### Requirements

- Linux environment
- Python 3
- APT package manager
- Sudo privileges for system updates

Clone the repository and navigate into the project directory.

Run:

```bash
python3 patchcatcher.py

## How It Works

- Patch Catcher provides a menu that allows the user to select different system management functions.

- System Information
- Check Available Updates
- Check Security Updates
- Install Updates
- Exit

## Project Status

- Version 1 — Complete
- Version 2 - Complete

- Version 1 successfully implements the core patching and update functionality and has been tested in a Kali Linux environment.
- Version 2 (Complete): Integrated a centralized logging framework using Python’s native logger to automatically track system checks, repository state changes, and error exceptions without manual file-handling overrides.

- Future Development

- Future versions may include:

- Improved security update detection
- Update history
- System health checks
- Improved error handling
- More detailed update reporting
- Additional Linux distribution support
- Automated patch scheduling
