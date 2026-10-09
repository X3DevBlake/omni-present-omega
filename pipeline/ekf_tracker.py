#!/data/data/com.termux/files/usr/bin/python3
"""
OPO Extended Kalman Filter (EKF) Sensor Fusion Tracker
Fuses multi-rate camera tensors (1-2 fps) and high-rate IMU angular velocities/accelerations
to maintain local real-time spatial positioning without cloud roundtrips.
Supports pure-Python fallback for ultra-constrained edge runtime environments.
"""

import sys

try:
    import numpy as np
    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False

class ExtendedKalmanFilterPose:
    def __init__(self, dt=0.01):
        self.dt = dt
        self.has_numpy = HAS_NUMPY

        if self.has_numpy:
            # State vector: [x, y, z, vx, vy, vz]
            self.x = np.zeros((6, 1))

            # State transition matrix F
            self.F = np.eye(6)
            self.F[0, 3] = dt
            self.F[1, 4] = dt
            self.F[2, 5] = dt

            # Covariance matrix P
            self.P = np.eye(6) * 0.1

            # Process noise Q
            self.Q = np.eye(6) * 0.01

            # Measurement matrix H for camera (positions only: x, y, z)
            self.H_cam = np.zeros((3, 6))
            self.H_cam[0, 0] = 1.0
            self.H_cam[1, 1] = 1.0
            self.H_cam[2, 2] = 1.0

            # Measurement noise R for camera
            self.R_cam = np.eye(3) * 0.05
        else:
            # Pure Python state vector: [x, y, z, vx, vy, vz]
            self.state = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
            self.gain = 0.35  # Kalman blending gain for camera position innovation

    def predict(self, imu_accel=None):
        """High-rate prediction step using IMU linear accelerations (100 Hz)."""
        if self.has_numpy:
            if imu_accel is not None:
                ax, ay, az = imu_accel
                self.x[3] += ax * self.dt
                self.x[4] += ay * self.dt
                self.x[5] += az * self.dt

            self.x = self.F @ self.x
            self.P = self.F @ self.P @ self.F.T + self.Q
        else:
            if imu_accel is not None:
                ax, ay, az = imu_accel
                self.state[3] += ax * self.dt
                self.state[4] += ay * self.dt
                self.state[5] += az * self.dt

            # Position integration: x += vx * dt
            self.state[0] += self.state[3] * self.dt
            self.state[1] += self.state[4] * self.dt
            self.state[2] += self.state[5] * self.dt

    def update_camera(self, cam_pos):
        """Low-rate correction step from vision/camera tensors (1-2 Hz)."""
        if self.has_numpy:
            z = np.array(cam_pos).reshape(3, 1)
            y = z - (self.H_cam @ self.x)  # Innovation

            S = self.H_cam @ self.P @ self.H_cam.T + self.R_cam  # Innovation covariance
            K = self.P @ self.H_cam.T @ np.linalg.inv(S)  # Kalman gain

            self.x = self.x + (K @ y)
            self.P = (np.eye(6) - (K @ self.H_cam)) @ self.P
        else:
            # Innovation correction
            for i in range(3):
                innovation = cam_pos[i] - self.state[i]
                self.state[i] += self.gain * innovation
                # Update velocity towards observed displacement
                self.state[i + 3] += (self.gain * 0.5) * (innovation / max(self.dt, 0.001))

    def get_pose(self):
        if self.has_numpy:
            return {
                "x": float(self.x[0, 0]),
                "y": float(self.x[1, 0]),
                "z": float(self.x[2, 0]),
                "vx": float(self.x[3, 0]),
                "vy": float(self.x[4, 0]),
                "vz": float(self.x[5, 0]),
            }
        else:
            return {
                "x": float(self.state[0]),
                "y": float(self.state[1]),
                "z": float(self.state[2]),
                "vx": float(self.state[3]),
                "vy": float(self.state[4]),
                "vz": float(self.state[5]),
            }

if __name__ == "__main__":
    mode = "NumPy C-Accelerated" if HAS_NUMPY else "Pure-Python Edge Embedded"
    print(f"Testing OPO EKF Sensor Fusion Tracker [{mode}]...")
    ekf = ExtendedKalmanFilterPose(dt=0.01)
    # Simulate 50 IMU ticks
    for _ in range(50):
        ekf.predict(imu_accel=[0.1, 0.0, 0.0])
    # Simulate 1 camera update
    ekf.update_camera([0.25, 0.01, -0.02])
    print("Estimated fused pose:", ekf.get_pose())
    print("✓ EKF test completed successfully.")
