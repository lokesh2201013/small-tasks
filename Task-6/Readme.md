# Server Setup and Log Analyzer Script

This script automates the setup of a basic server with essential packages, firewall configuration, Fail2Ban installation, a basic web page, and Nginx setup. Additionally, it analyzes Nginx access logs to find the top 10 IP addresses with the most requests.

## Features

- **Detects the Linux OS type**: The script asks for the OS type (Debian/Ubuntu or others) and sets the appropriate package manager (`apt` for Debian/Ubuntu, `yum` for others).
- **System Updates**: Updates and upgrades system packages.
- **Installs Essential Packages**: Installs Nginx, UFW (firewall), curl, vim, git, and fail2ban.
- **Configures Firewall**: Configures UFW to allow OpenSSH and Nginx Full profile.
- **Installs and Configures Fail2Ban**: Sets up Fail2Ban for security.
- **Creates a Basic Web Page**: Sets up a simple web page with a message that the server is running.
- **Restarts Nginx**: Restarts Nginx to apply any configuration changes.
- **Log Analysis**: Analyzes Nginx access logs to find the top 10 IP addresses with the most requests.

## Prerequisites

- A Linux-based server with root or sudo access.
- Python 3.x installed.
- The script uses `apt` or `yum` package managers, so the OS must support one of these (Debian/Ubuntu or other Linux distributions).
- Nginx must be installed to generate logs (`/var/log/nginx/access.log`).

## How to Use

1. **Clone or Download the Script:**
   - Clone this repository or download the script to your server.

2. **Run the Script:**
   - Open a terminal and navigate to the directory where the script is located.
   - Run the script with root privileges:

   ```bash
   sudo python3 setup_server.py
