# Patch Catcher V1

A Python-based Linux patch management utility for system information, update detection, security update filtering, and package upgrades.

## Project Overview

Patch Catcher is a Python command-line application designed to simplify basic Linux system patching and update tasks.

Version 1 was developed to provide a simple menu-driven interface for checking system information, identifying available package updates, detecting security-related updates, and installing system upgrades.

The application was developed in Python and tested in a Kali Linux virtual machine.

## Features

- Display system information
- Check available package updates
- Filter upgradeable packages for security-related updates
- Install available system updates
- Handle update failures
- Interactive command-line menu

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

- Version 1 successfully implements the core patching and update functionality and has been tested in a Kali Linux environment.

- Future Development

- Future versions may include:

- Improved security update detection
- Logging
- Update history
- System health checks
- Improved error handling
- More detailed update reporting
- Additional Linux distribution support
- Automated patch scheduling