import os
import subprocess
import shutil
import re

downloadcmd = ''

def getostype():
    global downloadcmd  
    ostype = input('Give type of linux: ')
    if ostype.lower() in ['debian', 'ubuntu']:
        downloadcmd = 'apt'
    else:
        downloadcmd = 'yum'
    return downloadcmd

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout + result.stderr

def update_system():
    print("Updating system packages...")
    return run_command(f"sudo {downloadcmd} update && sudo {downloadcmd} upgrade -y")

def install_packages():
    print("Installing essential packages...")
    packages = "nginx ufw curl vim git fail2ban"
    return run_command(f"sudo {downloadcmd} install -y {packages}")

def configure_firewall():
    print("Configuring firewall...")
    commands = [
        "sudo ufw allow OpenSSH",
        "sudo ufw allow 'Nginx Full'",
        "sudo ufw enable"
    ]
    return "\n".join(run_command(cmd) for cmd in commands)

def setup_fail2ban():
    print("Configuring Fail2Ban...")
    return run_command("sudo systemctl enable fail2ban && sudo systemctl start fail2ban")

def create_webpage():
    print("Setting up a basic web page...")
    html_content = "<h1>Server is up and running!</h1>"
    with open("/var/www/html/index.html", "w") as f:
        f.write(html_content)
    return "Web page created."

def restart_nginx():
    print("Restarting Nginx...")
    return run_command("sudo systemctl restart nginx")

def analyze_logs(log_file):
    print(f"Analyzing logs from file {log_file}...")
    if not os.path.exists(log_file):
        return "Log file does not exist."
    with open(log_file, "r") as f:
        logs = f.readlines()
    ip_count = {}
    for line in logs:
        match = re.search(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', line)
        if match:
            ip = match.group()
            ip_count[ip] = ip_count.get(ip, 0) + 1
    sorted_ips = sorted(ip_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_ips[:10] if sorted_ips else "No significant IP activity detected."

def main():
    getostype() 
    update_system()
    install_packages()
    configure_firewall()
    setup_fail2ban()
    create_webpage()
    restart_nginx()
    log_analysis = analyze_logs("/var/log/nginx/access.log")
    print("Top IPs from logs:", log_analysis)

if __name__ == "__main__":
    main()
