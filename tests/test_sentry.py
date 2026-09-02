"""
Termux-Sentry Automated Unit Test Suite
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from termux_sentry.telemetry.hardware import HardwareTelemetry

class TestTermuxSentry(unittest.TestCase):
    def test_thermal_zones_read(self):
        zones = HardwareTelemetry.read_thermal_zones()
        self.assertGreater(len(zones), 0)
        self.assertIn("temp_c", zones[0])
        self.assertIsInstance(zones[0]["temp_c"], float)

    def test_battery_profile(self):
        profile = HardwareTelemetry.get_battery_profile()
        self.assertIn("percentage", profile)
        self.assertIn("voltage_mv", profile)
        self.assertEqual(profile["status"], "DISCHARGING")

    def test_process_radar(self):
        radar = HardwareTelemetry.get_process_radar()
        self.assertGreater(len(radar), 0)
        self.assertTrue(any("sshd" in p["name"] or "localdrop" in p["name"] for p in radar))

if __name__ == '__main__':
    unittest.main()
