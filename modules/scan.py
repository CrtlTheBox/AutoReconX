import subprocess
import os

def run_light_scans(target, output_dir):
    print(f"[+] Running LIGHT scans for {target}")

    scans = {
        "FastTCP_Scan.txt": f"nmap -Pn -sSV -T4 {target} -oN {os.path.join(output_dir, 'FastTCP_Scan.txt')}",
        "FastUDP_Scan.txt": f"nmap -Pn -sU --top-ports 20 -T4 {target} -oN {os.path.join(output_dir, 'FastUDP_Scan.txt')}"
    }

    for name, cmd in scans.items():
        print(f"[*] Running {name} (Expected: ~1-3 min)...")
        subprocess.run(cmd, shell=True)
        print(f"[+] {name} completed.")

    print(f"[+] Light scan results saved in '{output_dir}'")

def run_enum_scans(target, output_dir):
    print(f"[+] Running FULL ENUMERATION scans for {target}")

    # Fast scans first
    run_light_scans(target, output_dir)

    # Background full scans
    background_scans = {
        "FullTCP_Scan.txt": f"nmap -Pn -p- -sSV -T4 {target} -oN {os.path.join(output_dir, 'FullTCP_Scan.txt')}",
        "FullUDP_Scan.txt": f"nmap -Pn -p- -sU -T4 {target} -oN {os.path.join(output_dir, 'FullUDP_Scan.txt')}",
        "vuln_Scan.txt": f"nmap -Pn -sV -sC --script=vuln {target} -oN {os.path.join(output_dir, 'vuln_Scan.txt')}"
    }

    for name, cmd in background_scans.items():
        print(f"[*] Launching {name} in background (will take 10–20 mins)...")
        subprocess.Popen(f"{cmd} &", shell=True)

    print(f"[+] Background scans launched. Monitor '{output_dir}' for results.")

