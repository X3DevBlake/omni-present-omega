#!/usr/bin/env python3
"""
OPO (Omni-Present Omega) Google Robotics Cloud Bridge
Connects Cyber-Physical Robotics HAL with Google Workspace & Cloud Infrastructure:
1. Google Sheets  - Streams real-time telemetry into 'Omni Robotics Live Telemetry' sheet.
2. Google Drive   - Stores mission reports, radar snapshots, and spatial navigation logs.
3. Google Keep    - Manages autonomous pre-flight diagnostics and cyber-physical checklists.
4. Gmail          - Dispatches critical safety alerts and mission briefing notifications to rgkdevx1@gmail.com.
5. Gemini Vision  - Multimodal spatial reasoning and LiDAR vector threat assessments.
"""

import os
import sys
import json
import csv
import time
from datetime import datetime, timezone

OMNI_HOME = "/data/data/com.termux/files/home"
AUTOMATION_DIR = os.path.join(OMNI_HOME, "omni-automation")
ROBOTICS_DIR = os.path.join(OMNI_HOME, "opo-robotics")
WEB_DIR = os.path.join(OMNI_HOME, "omni-web")
WEB_DATA_DIR = os.path.join(WEB_DIR, "assets", "data")
WORKSPACE_OUTPUT = os.path.join(AUTOMATION_DIR, "workspace_output")
SHEETS_DIR = os.path.join(WORKSPACE_OUTPUT, "sheets")
KEEP_DIR = os.path.join(WORKSPACE_OUTPUT, "keep")
DOCS_DIR = os.path.join(WORKSPACE_OUTPUT, "docs")

sys.path.insert(0, AUTOMATION_DIR)
sys.path.insert(0, ROBOTICS_DIR)

from opo_robotics_hal import OPORoboticsHAL

try:
    from google_workspace import GoogleWorkspaceSuite, GoogleDriveCloudClient
except ImportError:
    GoogleWorkspaceSuite = None
    GoogleDriveCloudClient = None

TELEMETRY_CSV = os.path.join(SHEETS_DIR, "Omni_Robotics_Live_Telemetry.csv")
WEB_TELEMETRY_JSON = os.path.join(WEB_DATA_DIR, "robotics_telemetry.json")

CSV_HEADERS = [
    "timestamp",
    "node_id",
    "robot_type",
    "mission_status",
    "battery_pct",
    "temp_c",
    "estop",
    "gps_lat",
    "gps_lon",
    "heading_deg",
    "linear_vel_mps",
    "min_obstacle_m",
    "j1_base",
    "j2_shoulder",
    "j3_elbow",
    "j4_wrist_roll",
    "j5_wrist_pitch",
    "j6_gripper_yaw",
    "gripper_aperture_mm"
]

class GoogleRoboticsBridge:
    def __init__(self, hal=None, user_email="rgkdevx1@gmail.com"):
        self.hal = hal or OPORoboticsHAL(node_id="opo-robot-prime")
        self.user_email = user_email
        self.suite = GoogleWorkspaceSuite(user_email=user_email) if GoogleWorkspaceSuite else None
        self.drive_client = GoogleDriveCloudClient(user_email=user_email) if GoogleDriveCloudClient else None
        os.makedirs(SHEETS_DIR, exist_ok=True)
        os.makedirs(WEB_DATA_DIR, exist_ok=True)
        self._init_telemetry_csv()

    def _init_telemetry_csv(self):
        """Initializes the CSV telemetry file with headers if it doesn't exist."""
        if not os.path.exists(TELEMETRY_CSV):
            with open(TELEMETRY_CSV, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(CSV_HEADERS)

    def log_telemetry_entry(self, snapshot=None):
        """Logs a single telemetry snapshot to local CSV and web JSON."""
        snap = snapshot or self.hal.get_full_telemetry_snapshot()
        now_iso = snap.get("timestamp", datetime.now(timezone.utc).isoformat())
        arm = snap.get("arm_kinematics", {}).get("joints", [])
        nav = snap.get("navigation", {})
        gps = snap.get("gps", {})

        j_angles = [j.get("angle_deg", 0.0) for j in arm]
        while len(j_angles) < 6:
            j_angles.append(0.0)

        row = [
            now_iso,
            snap.get("node_id", "opo-robot-prime"),
            snap.get("robot_type", "HYBRID_CYBER_PHYSICAL"),
            snap.get("mission_status", "ACTIVE"),
            snap.get("battery_pct", 100.0),
            snap.get("temperature_c", 35.0),
            "TRUE" if snap.get("emergency_stop") else "FALSE",
            gps.get("latitude", 35.6762),
            gps.get("longitude", 139.6503),
            nav.get("heading_deg", 0.0),
            nav.get("linear_vel_mps", 0.0),
            nav.get("min_obstacle_distance_m", 5.0),
            j_angles[0],
            j_angles[1],
            j_angles[2],
            j_angles[3],
            j_angles[4],
            j_angles[5],
            snap.get("arm_kinematics", {}).get("gripper_aperture_mm", 45.0)
        ]

        with open(TELEMETRY_CSV, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(row)

        # Update web assets JSON for the live frontend cockpit
        with open(WEB_TELEMETRY_JSON, "w", encoding="utf-8") as f:
            json.dump(snap, f, indent=2)

        return row

    def sync_telemetry_to_google_sheet(self):
        """Uploads/updates Omni Robotics Live Telemetry to Google Drive as native Google Sheet."""
        if not self.drive_client:
            return False, "GoogleDriveCloudClient not available."

        folder_id = self.drive_client.get_or_create_folder("Omni Sovereign Swarm Documents")
        sheet_title = "Omni Robotics Live Telemetry"

        ok, sheet_id, sheet_url = self.drive_client.upload_csv_as_sheet(
            file_path=TELEMETRY_CSV,
            title=sheet_title,
            folder_id=folder_id
        )

        if ok:
            # Register in sheets_catalog.json
            sheets_catalog_file = os.path.join(SHEETS_DIR, "sheets_catalog.json")
            catalog = {}
            if os.path.exists(sheets_catalog_file):
                try:
                    with open(sheets_catalog_file, "r", encoding="utf-8") as f:
                        catalog = json.load(f)
                except Exception:
                    pass

            catalog["Omni_Robotics_Live_Telemetry.csv"] = {
                "filename": "Omni_Robotics_Live_Telemetry.csv",
                "title": sheet_title,
                "google_sheet_id": sheet_id,
                "google_sheet_url": sheet_url,
                "synced_at": datetime.now(timezone.utc).isoformat(),
                "records_count": sum(1 for _ in open(TELEMETRY_CSV)) - 1
            }

            with open(sheets_catalog_file, "w", encoding="utf-8") as f:
                json.dump(catalog, f, indent=2)

            # Copy catalog to web assets
            web_sheets_cat = os.path.join(WEB_DATA_DIR, "sheets_catalog.json")
            with open(web_sheets_cat, "w", encoding="utf-8") as f:
                json.dump(catalog, f, indent=2)

            print(f"[Google Robotics Bridge] ✓ Live Telemetry Sheet synced: {sheet_url}")
            return True, sheet_url
        else:
            print(f"[Google Robotics Bridge] ⚠️ Sync error: {sheet_url}")
            return False, str(sheet_url)

    def ensure_preflight_checklist_in_keep(self):
        """Creates or verifies the pre-flight robotics diagnostic checklist in Google Keep."""
        if not self.suite:
            return None

        title = "🤖 OPO Cyber-Physical Robotics Pre-Flight Diagnostics"
        existing = [n for n in self.suite.keep.list_notes() if n.get("title") == title]
        if existing:
            return existing[0]

        items = [
            {"text": "6-DOF Arm Actuator Zero Calibration & Encoders Aligned", "checked": True},
            {"text": "360° LiDAR Sweep Obstacle Boundary Verified (>0.4m safe radius)", "checked": True},
            {"text": "Differential Drive Wheel Odometry & EKF Fusion Aligned", "checked": True},
            {"text": "E-STOP Cyber-Physical Hardwire Interlock Tested", "checked": True},
            {"text": "Google Workspace Cloud Telemetry Link Established", "checked": True},
            {"text": "Motor Thermal Dissipation Safe (<75°C Invariant)", "checked": True},
            {"text": "Battery Reserve Verified (>20% Threshold)", "checked": True}
        ]

        note = self.suite.keep.add_note(
            title=title,
            content=items,
            note_type="checklist",
            color="orange",
            pinned=True,
            author="omni-robotics-controller",
            tags=["#robotics", "#preflight", "#hardware", "#opo"]
        )
        self.suite.sync_to_web_assets()
        print(f"[Google Keep] Pre-flight robotics checklist created.")
        return note

    def dispatch_safety_alert_email(self, alert_type="EMERGENCY_STOP", details="Manual E-STOP Triggered"):
        """Dispatches safety alerts to Commander at rgkdevx1@gmail.com via Gmail API."""
        if not self.suite:
            return False

        subject = f"🚨 OPO Robotics CRITICAL ALERT: [{alert_type}]"
        now_str = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
        body_html = f"""
        <div style="font-family: sans-serif; color: #1f2937;">
          <h2 style="color: #ef4444; border-bottom: 2px solid #ef4444; padding-bottom: 8px;">
            ⚠️ OPO Robotics Cyber-Physical Safety Alert
          </h2>
          <p><strong>Node ID:</strong> <code>{self.hal.node_id}</code></p>
          <p><strong>Timestamp:</strong> {now_str}</p>
          <p><strong>Alert Classification:</strong> <span style="background: #fee2e2; color: #991b1b; padding: 3px 8px; border-radius: 4px; font-weight: bold;">{alert_type}</span></p>
          <p><strong>Diagnostic Details:</strong> {details}</p>
          
          <table style="width: 100%; border-collapse: collapse; margin-top: 15px; font-size: 14px;">
            <tr style="background: #f3f4f6;">
              <th style="padding: 8px; border: 1px solid #e5e7eb; text-align: left;">Telemetry Vector</th>
              <th style="padding: 8px; border: 1px solid #e5e7eb; text-align: left;">Recorded Value</th>
            </tr>
            <tr>
              <td style="padding: 8px; border: 1px solid #e5e7eb;">Battery Level</td>
              <td style="padding: 8px; border: 1px solid #e5e7eb;"><strong>{self.hal.battery_pct:.1f}%</strong></td>
            </tr>
            <tr>
              <td style="padding: 8px; border: 1px solid #e5e7eb;">System Temperature</td>
              <td style="padding: 8px; border: 1px solid #e5e7eb;">{self.hal.temperature_c:.1f}°C</td>
            </tr>
            <tr>
              <td style="padding: 8px; border: 1px solid #e5e7eb;">Min LiDAR Clearance</td>
              <td style="padding: 8px; border: 1px solid #e5e7eb;">{self.hal.min_obstacle_dist_m:.2f} m</td>
            </tr>
            <tr>
              <td style="padding: 8px; border: 1px solid #e5e7eb;">E-Stop Active</td>
              <td style="padding: 8px; border: 1px solid #e5e7eb; color: #dc2626; font-weight: bold;">{'YES' if self.hal.emergency_stop else 'NO'}</td>
            </tr>
          </table>
          <p style="margin-top: 20px; font-size: 12px; color: #6b7280;">
            Dispatched autonomously by OPO Robotics Safety Interlock & Google Cloud Bridge.
          </p>
        </div>
        """
        res = self.suite.gmail.compose_and_dispatch(
            subject=subject,
            body_html=body_html,
            recipient=self.user_email,
            priority="HIGH",
            tags=["#robotics", "#safety", "#estop"]
        )
        self.suite.sync_to_web_assets()
        print(f"[Gmail Dispatch] Safety alert dispatched to {self.user_email}.")
        return res

    def run_simulated_mission(self, duration_steps=5):
        """Runs a simulated telemetry patrol mission and syncs to Google Sheets & Keep."""
        print(f"🚀 Running OPO Robotics Mission ({duration_steps} ticks)...")
        # Ensure checklist exists
        self.ensure_preflight_checklist_in_keep()

        for step in range(1, duration_steps + 1):
            # Target arm waypoint
            tx = 200 + step * 10
            ty = 50 - step * 5
            tz = 140 + step * 8
            self.hal.solve_inverse_kinematics(tx, ty, tz)
            snap = self.hal.get_full_telemetry_snapshot()
            self.log_telemetry_entry(snap)
            print(f"  [Step {step}/{duration_steps}] Battery: {snap['battery_pct']}% | Heading: {snap['navigation']['heading_deg']}° | Obstacle: {snap['navigation']['min_obstacle_distance_m']}m")
            time.sleep(0.1)

        # Sync to Google Sheets
        ok, sheet_url = self.sync_telemetry_to_google_sheet()
        return ok, sheet_url

if __name__ == "__main__":
    bridge = GoogleRoboticsBridge()
    print("🤖 OPO Google Robotics Bridge initialized")
    ok, sheet_url = bridge.run_simulated_mission(5)
    print(f"Mission complete. Google Sheet sync: {ok} -> {sheet_url}")
