#!/bin/bash
# ==============================================================================
# MediCore Infrastructure Security Hardening Script
# Description: Automates the configuration of users, file permissions, 
# audit logging, and UFW firewall rules for the host VM.
# ==============================================================================

echo "[+] Starting MediCore VM Hardening Process..."

# 1. User Roles & Least Privilege
echo "[+] Configuring isolated user accounts..."
sudo useradd -m -s /bin/bash dboperator
sudo useradd -m -s /bin/bash auditor
sudo useradd -m -s /bin/bash dataanalyst
# Note: sysadmin user created during initial provisioning.

# 2. File Permissions & Security Auditing
echo "[+] Securing sensitive clinical data directories..."
sudo mkdir -p /data/clinicaldata
sudo chown -R sysadmin:sysadmin /data/clinicaldata
sudo chmod 770 /data/clinicaldata

echo "[+] Configuring auditd logging for clinical data access..."
# Monitor write and attribute changes to the secure directory
sudo auditctl -w /data -p wa -k clinical_data_access

# 3. Network Firewall Rules (UFW)
echo "[+] Configuring UFW default-deny firewall..."
sudo ufw default deny incoming
sudo ufw default allow outgoing

echo "[+] Opening essential operational ports..."
sudo ufw allow 22/tcp   # SSH Access
sudo ufw allow 80/tcp   # Standard Web Traffic
sudo ufw allow 443/tcp  # Secure Web Traffic

echo "[+] Enabling UFW..."
sudo ufw --force enable

echo "[+] Hardening complete! System secured."
