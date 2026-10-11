"""
Patch Catcher V2

An automated Linux systems maintenance and package management utility.
Engineered with a centralized logging framework to provide continuous audit
trails, automated package discovery, and security-event filtering.

Features:
- Centralized system telemetry and host auditing logs.
- Dynamic error trapping and exception logging for subprocess execution.
- Security-specific repository update tracking.

Developed and tested in Kali Linux.
Started: 08 October 2026
"""

import platform
import sys
import socket
import subprocess
import logging
logging.basicConfig(filename="patchcatcher.log",
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("PatchCatcherLogger")


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
        results = subprocess.run("sudo apt-get upgrade -y",
                                 text=True,
                                 check=True,
                                 shell=True,
                                 capture_output=True)
        output = results.stdout
        print(output)
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


def logging_system_info():
    """
    Log system information to a file for auditing purposes.
    """
    try:
        logger.info(f"System Check: {sys.platform}")
        logger.info(f"OS Running: {platform.version()}")
        logger.info(f"Hostname: {socket.gethostname()}")
        logger.info(f"Kernel: {platform.release()}")
        print("System information logged successfully.")
    except Exception as e:
        logger.error(f"Failed to log system information: {e}")


def logging_patchable_list():
    """
    Log the list of upgradeable packages to a file for auditing purposes.
    """
    try:
        logger.info("Retrieving patchable list...")
        results = subprocess.run(["apt list --upgradable"],
                                 capture_output=True,
                                 check=True,
                                 text=True,
                                 shell=True)
        logger.info("Patchable list:")
        logger.info(results.stdout)
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to retrieve patchable list: {e.stderr}")
    except Exception as e:
        logger.error(f"Failed to log patchable list: {e}")


def logging_security_update():
    """
    Log the list of security-related upgradeable packages to a file for
    auditing purposes.
    """
    try:
        logger.info("Retrieving security update list...")
        results = subprocess.run(["apt list --upgradable | grep -i security"],
                                 capture_output=True,
                                 check=True, text=True,
                                 shell=True)
        output = results.stdout
        logger.info("Security update list:")
        logger.info(output)
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to retrieve security update list: {e.stderr}")
    except Exception as e:
        logger.error(f"Failed to log security update list: {e}")


def logging_patch_start():
    """
    Log the result of the patch installation process to a file for auditing
    purposes.
    """
    try:
        logger.info("Starting patch installation...")
        results = subprocess.run("sudo apt-get upgrade -y",
                                 capture_output=True,
                                 text=True,
                                 check=True,
                                 shell=True)
        output = results.stdout
        logger.info("Patch installation completed successfully.")
        logger.info(output)
    except subprocess.CalledProcessError as e:
        logger.error(f"Patch installation failed: {e.stderr}")
    except Exception as e:
        logger.error(f"Failed to log patch installation: {e}")


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
            logging_system_info()

        elif choice == "2":
            patchable_list()
            logging_patchable_list()

        elif choice == "3":
            security_update()
            logging_security_update()

        elif choice == "4":
            patch_start()
            logging_patch_start()

        elif choice == "5":
            print("Exiting Patch Catcher...")
            break

        else:
            print("Invalid option. Please choose 1-5.")


if __name__ == "__main__":
    main()