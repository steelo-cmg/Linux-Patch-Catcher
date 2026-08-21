"""
Patch Catcher V1

A Python-based Linux patch management utility that provides
system information, update detection, security update filtering,
and system package upgrades.

Developed and tested in Kali Linux.
Started: 17 August 2026
"""

import platform
import sys
import socket
import subprocess


def system_information():
    """
    Display basic information about the current Linux system.
    """
    # checking the operating system
    print("Operating System: ")
    print(sys.platform)
    # checking os version
    print("OS Running: ")
    print(platform.version())
    # checking the hostname
    hostname = socket.gethostname()
    print(f"Hostname: {hostname}")
    # checking the kernel version
    kernel_version = platform.release()
    print(f"Kernel: {kernel_version}")


def patchable_list():
    """
    Display packages that are available for upgrade.
    """
    # subprocess.run to run the commands, capture_output=True to catch the
    # output
    # shell=True talk to the shel directly without separating the commands

    results = subprocess.run(["sudo apt list --upgradable"],
                             capture_output=True,
                             check=True,
                             text=True,
                             shell=True)

    output = results.stdout
    print(output)


def patch_start():
    """
    Run the Linux package upgrade process and handle failures.
    """
    # start updating all updateable services on device.
    # handling download errors using CalledProcessError and outputing using st
    try:
        subprocess.run("sudo apt-get upgrade",
                       text=True,
                       check=True,
                       shell=True)

    except subprocess.CalledProcessError as e:
        print(f"Patch installation failed: {e.stderr}")
        print(f"Return code: {e.returncode}")


def security_update():
    """
    Display upgradeable packages containing security-related entries.
    """
    # checking only security upgradeables
    results = subprocess.run(["apt list --upgradable | grep -i security"],
                             capture_output=True,
                             check=True, text=True,
                             shell=True)
    output = results.stdout
    print(output)


def main():
    """
    Display the Patch Catcher menu and handle user selections.
    """
    while True:
        print("\n===== PATCH CATCHER =====")
        print("1. System Information")
        print("2. Check Available Updates")
        print("3. Check Security Updates")
        print("4. Install Updates")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            system_information()

        elif choice == "2":
            patchable_list()

        elif choice == "3":
            security_update()

        elif choice == "4":
            patch_start()

        elif choice == "5":
            print("Exiting Patch Catcher...")
            break

        else:
            print("Invalid option. Please choose 1–5.")


main()
