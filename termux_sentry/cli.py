"""
Termux-Sentry CLI - Real-Time Android Hardware & Process Telemetry Radar
"""

import sys
import argparse
from termux_sentry.telemetry.hardware import HardwareTelemetry

def banner():
    print("""\033[38;2;204;255;0m
  ███████╗███████╗███╗   ██╗████████╗██████╗ ██╗   ██╗
  ██╔════╝██╔════╝████╗  ██║╚══██╔══╝██╔══██╗╚██╗ ██╔╝
  ███████╗█████╗  ██╔██╗ ██║   ██║   ██████╔╝ ╚████╔╝ 
  ╚════██║██╔══╝  ██║╚██╗██║   ██║   ██╔══██╗  ╚██╔╝  
  ███████║███████╗██║ ╚████║   ██║   ██║  ██║   ██║   
  ╚══════╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝   
      [ Real-Time Android Hardware Telemetry & Process Radar ]
                        Velorio Labs Flagship\033[0m
""")

def main():
    parser = argparse.ArgumentParser(description="Termux-Sentry - Android Hardware & Process Telemetry")
    subparsers = parser.add_subparsers(dest="command", help="Operational commands")

    # Radar
    subparsers.add_parser("radar", help="Display real-time process radar and listening sockets")

    # Thermal
    subparsers.add_parser("thermal", help="Inspect CPU/GPU thermal zones and temperature curves")

    # Battery
    subparsers.add_parser("battery", help="Profile battery power consumption and discharge rate")

    args = parser.parse_args()

    if not args.command:
        banner()
        parser.print_help()
        sys.exit(0)

    if args.command == "radar":
        banner()
        print("\033[96m[*] Active Process & Listening Socket Radar:\033[0m\n")
        procs = HardwareTelemetry.get_process_radar()
        for p in procs:
            print(f"  • PID: \033[93m{p['pid']:<6}\033[0m | Name: \033[92m{p['name']:<18}\033[0m | Port: \033[96m{p['port']:<6}\033[0m | {p['protocol']} ({p['status']})")

    elif args.command == "thermal":
        banner()
        print("\033[96m[*] Hardware Thermal Sensor Zones:\033[0m\n")
        zones = HardwareTelemetry.read_thermal_zones()
        for z in zones:
            temp = z['temp_c']
            color = "\033[91m" if temp >= 45 else "\033[93m" if temp >= 40 else "\033[92m"
            print(f"  • {z['zone']:<20}: {color}{temp}°C\033[0m")

    elif args.command == "battery":
        banner()
        b = HardwareTelemetry.get_battery_profile()
        print("\033[96m[*] Android Battery Power Profile:\033[0m\n")
        print(f"  • Battery Level:      \033[92m{b['percentage']}%\033[0m ({b['status']})")
        print(f"  • Bus Voltage:        \033[93m{b['voltage_mv']} mV\033[0m")
        print(f"  • Current Draw:       \033[91m{b['current_now_ma']} mA\033[0m")
        print(f"  • Total Consumption:  \033[96m{b['power_consumption_w']} W\033[0m")

if __name__ == "__main__":
    main()
