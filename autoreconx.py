import argparse
import os
from modules import discover, scan

def main():
    parser = argparse.ArgumentParser(description="AutoReconX - Lightweight Recon Wrapper for Nmap")
    parser.add_argument("target", help="Target IP or IP range (e.g. 10.10.10.0/24 or 10.10.10.5)")
    parser.add_argument("--discover", action="store_true", help="Run host discovery only")
    parser.add_argument("--enum", action="store_true", help="Run full enumeration scans")
    parser.add_argument("--light", action="store_true", help="Run fast/lightweight scans only")
    parser.add_argument("--output", default="output", help="Output folder for scan results")

    args = parser.parse_args()
    os.makedirs(args.output, exist_ok=True)

    if args.discover:
        discover.run_discovery(args.target, args.output)

    if args.enum:
        scan.run_enum_scans(args.target, args.output)

    if args.light:
        scan.run_light_scans(args.target, args.output)

if __name__ == "__main__":
    main()

