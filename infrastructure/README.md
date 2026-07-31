# MediCore Infrastructure Configuration

This directory contains the foundational security configurations and setup scripts used to harden the Ubuntu host Virtual Machine prior to deploying the containerised applications.

## Files Included

* **`harden_vm.sh`**: A bash script containing the imperative Linux commands used to configure the host OS. This includes:
  * **Principle of Least Privilege:** Creation of isolated user accounts (`dboperator`, `auditor`, `dataanalyst`) to restrict root access.
  * **Discretionary Access Control (DAC):** Strict `chmod` and `chown` permissions applied to clinical data directories.
  * **Security Auditing:** Implementation of `auditd` rules to track read/write events on sensitive files.
  * **Network Security:** Uncomplicated Firewall (UFW) rules enforcing a default-deny policy, explicitly allowing only required operational ports (22, 80, 443).

## Usage
*Note: This script requires root privileges to execute.*
```bash
chmod +x harden_vm.sh
sudo ./harden_vm.sh
