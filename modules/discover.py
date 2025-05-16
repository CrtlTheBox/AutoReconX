import subprocess
import os

def run_discovery(target, output_dir):
    print(f"[+] Starting host discovery on {target}")

    # Nmap ping scan
    nmap_output = os.path.join(output_dir, "Livehosts_Nmap.txt")
    print("[*] Running Nmap ping scan...")
    subprocess.run(f"nmap -sn {target} -oN {nmap_output}", shell=True)
    print(f"[+] Nmap ping scan saved to {nmap_output}")

    # NBTSCan (UnixWiz version)
    nbtscan_output = os.path.join(output_dir, "NBtscan.txt")
    print("[*] Running nbtscan-unixwiz...")
    subprocess.run(f"nbtscan-unixwiz {target} | tee {nbtscan_output}", shell=True)
    print(f"[+] NBtscan output saved to {nbtscan_output}")

    print(f"\n[+] Discovery complete. Results saved in: {output_dir}")

