#!/usr/bin/env bash
# ==============================================================================
# OPO (Omni-Present Omega) Universal Sovereign Installer & Node Bootstrapper
# One-liner install: curl -sSL https://omni-network-39821.web.app/install.sh | bash
# ==============================================================================
set -e

# ANSI Color Codes
CYAN='\033[1;36m'
MAGENTA='\033[1;35m'
GREEN='\033[1;32m'
YELLOW='\033[1;33m'
RED='\033[1;31m'
BLUE='\033[1;34m'
BOLD='\033[1m'
NC='\033[0m' # No Color

OPO_VERSION="2.4.0-SOVEREIGN-OMEGA"
INSTALL_ROOT="${HOME}/.opo"
BIN_DIR="${INSTALL_ROOT}/bin"
ROBOTICS_DIR="${INSTALL_ROOT}/opo-robotics"
REPO_RAW_URL="https://omni-network-39821.web.app"

print_header() {
  printf "${CYAN}
  ██████╗ ██████╗  ██████╗     ${MAGENTA}OMNI-PRESENT OMEGA (OPO)${CYAN}
 ██╔═══██╗██╔══██╗██╔═══██╗    ${BLUE}Cyber-Physical Mesh & Robotics Engine${CYAN}
 ██║   ██║██████╔╝██║   ██║    ${GREEN}Universal One-Liner Installer v${OPO_VERSION}${CYAN}
 ██║   ██║██╔═══╝ ██║   ██║    ${YELLOW}Target: 11 Councils | 63 Swarm Agents${CYAN}
 ╚██████╔╝██║     ╚██████╔╝    ${BLUE}Google Workspace: rgkdevx1@gmail.com${CYAN}
  ╚═════╝ ╚═╝      ╚═════╝     ${NC}
\n"
}

# Dry run flag check
DRY_RUN=false
for arg in "$@"; do
  case "$arg" in
    --dry-run)
      DRY_RUN=true
      ;;
    --help|-h)
      printf "OPO Universal Installer\nUsage: curl -sSL ${REPO_RAW_URL}/install.sh | bash [options]\nOptions:\n  --dry-run   Simulate installation without making system modifications\n  --help      Show this help dialog\n"
      exit 0
      ;;
  esac
done

print_header

if [ "$DRY_RUN" = true ]; then
  printf "${YELLOW}>>> Running in --dry-run mode. No files will be permanently modified.${NC}\n"
fi

printf "${BOLD}[1/5] Detecting System Architecture & Environment...${NC}\n"
ARCH=$(uname -m)
OS_TYPE=$(uname -s | tr '[:upper:]' '[:lower:]')

IS_TERMUX=false
if [ -n "$PREFIX" ] && [ -d "$PREFIX/bin" ]; then
  IS_TERMUX=true
  printf "  ${GREEN}✓${NC} Detected Environment: ${BOLD}Termux (Android Linux)${NC} [${ARCH}]\n"
elif [ "$OS_TYPE" = "darwin" ]; then
  printf "  ${GREEN}✓${NC} Detected Environment: ${BOLD}macOS (Darwin)${NC} [${ARCH}]\n"
else
  printf "  ${GREEN}✓${NC} Detected Environment: ${BOLD}Linux Desktop / Cloud Node${NC} [${ARCH}]\n"
fi

printf "\n${BOLD}[2/5] Validating Runtime Dependencies...${NC}\n"
HAS_PYTHON=false
if command -v python3 >/dev/null 2>&1; then
  HAS_PYTHON=true
  PY_VER=$(python3 --version 2>&1)
  printf "  ${GREEN}✓${NC} Python 3 available: ${PY_VER}\n"
else
  printf "  ${RED}✗${NC} Python 3 is missing. Attempting automatic installation...\n"
  if [ "$IS_TERMUX" = true ]; then
    pkg update -y && pkg install -y python
  elif command -v apt-get >/dev/null 2>&1; then
    sudo apt-get update && sudo apt-get install -y python3 python3-pip
  elif command -v brew >/dev/null 2>&1; then
    brew install python
  fi
fi

if ! command -v curl >/dev/null 2>&1; then
  printf "  ${YELLOW}!${NC} curl is missing. Installing curl...\n"
  if [ "$IS_TERMUX" = true ]; then pkg install -y curl; fi
fi

printf "\n${BOLD}[3/5] Setting up OPO Sovereign Directory Structure...${NC}\n"
if [ "$DRY_RUN" = false ]; then
  mkdir -p "$BIN_DIR"
  mkdir -p "$ROBOTICS_DIR"
  printf "  ${GREEN}✓${NC} Initialized ${INSTALL_ROOT}\n"
fi

printf "\n${BOLD}[4/5] Deploying OPO Cyber-Physical Robotics & HAL Modules...${NC}\n"
# If running within existing repo, copy from local; otherwise write standalone HAL & CLI
LOCAL_SRC="/data/data/com.termux/files/home/opo-robotics"
if [ -d "$LOCAL_SRC" ]; then
  printf "  ${GREEN}✓${NC} Linking existing repository modules from ${LOCAL_SRC}...\n"
  if [ "$DRY_RUN" = false ]; then
    cp "$LOCAL_SRC/opo_robotics_hal.py" "$ROBOTICS_DIR/"
    cp "$LOCAL_SRC/google_robotics_bridge.py" "$ROBOTICS_DIR/"
    cp "$LOCAL_SRC/opo_cli.py" "$ROBOTICS_DIR/"
  fi
else
  printf "  ${GREEN}✓${NC} Fetching standalone OPO robotics package from cloud endpoint...\n"
  if [ "$DRY_RUN" = false ]; then
    curl -sSL "${REPO_RAW_URL}/opo/opo_robotics_hal.py" -o "$ROBOTICS_DIR/opo_robotics_hal.py" 2>/dev/null || true
    curl -sSL "${REPO_RAW_URL}/opo/google_robotics_bridge.py" -o "$ROBOTICS_DIR/google_robotics_bridge.py" 2>/dev/null || true
    curl -sSL "${REPO_RAW_URL}/opo/opo_cli.py" -o "$ROBOTICS_DIR/opo_cli.py" 2>/dev/null || true
  fi
fi

# Build wrapper binary
if [ "$DRY_RUN" = false ]; then
  cat << 'EOF' > "${BIN_DIR}/opo"
#!/usr/bin/env bash
SELF_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ROBOTICS_CLI="${SELF_DIR}/opo-robotics/opo_cli.py"

if [ -f "$ROBOTICS_CLI" ]; then
  exec python3 "$ROBOTICS_CLI" "$@"
elif [ -f "/data/data/com.termux/files/home/opo-robotics/opo_cli.py" ]; then
  exec python3 "/data/data/com.termux/files/home/opo-robotics/opo_cli.py" "$@"
else
  echo "Error: OPO CLI not found."
  exit 1
fi
EOF
  chmod +x "${BIN_DIR}/opo"

  # Link into system PATH
  if [ "$IS_TERMUX" = true ] && [ -d "$PREFIX/bin" ]; then
    cp "${BIN_DIR}/opo" "$PREFIX/bin/opo"
    chmod +x "$PREFIX/bin/opo"
    printf "  ${GREEN}✓${NC} Installed binary: ${BOLD}$PREFIX/bin/opo${NC}\n"
  elif [ -d "$HOME/.local/bin" ]; then
    cp "${BIN_DIR}/opo" "$HOME/.local/bin/opo"
    chmod +x "$HOME/.local/bin/opo"
    printf "  ${GREEN}✓${NC} Installed binary: ${BOLD}$HOME/.local/bin/opo${NC}\n"
  fi
fi

printf "\n${BOLD}[5/5] Running Self-Verification & Cyber-Physical Diagnostics...${NC}\n"
if [ "$DRY_RUN" = false ]; then
  if command -v opo >/dev/null 2>&1; then
    opo robot diagnostics
  elif [ -x "${BIN_DIR}/opo" ]; then
    "${BIN_DIR}/opo" robot diagnostics
  fi
else
  printf "  ${YELLOW}[DRY-RUN] Skipped diagnostic execution.${NC}\n"
fi

printf "\n======================================================================\n"
printf "${GREEN}${BOLD}🎉 OMNI-PRESENT OMEGA (OPO) INSTALLED SUCCESSFULLY!${NC}\n"
printf "======================================================================\n\n"
printf "You can now run ${BOLD}opo${NC} directly from any terminal!\n\n"
printf "Quickstart Commands:\n"
printf "  ${CYAN}opo status${NC}                     View node health, peers & robotics telemetry\n"
printf "  ${CYAN}opo robot ik 220 50 140${NC}        Solve 6-DOF inverse kinematics for end-effector\n"
printf "  ${CYAN}opo robot lidar${NC}                Perform 360° LiDAR radar sweep\n"
printf "  ${CYAN}opo robot teleop 1.5 0.2${NC}       Send rover velocity & yaw commands\n"
printf "  ${CYAN}opo robot estop engage${NC}         Trigger cyber-physical emergency stop\n"
printf "  ${CYAN}opo sync${NC}                       Sync telemetry to Google Sheets & Drive\n"
printf "  ${CYAN}opo start${NC}                      Launch persistent autonomous node daemon\n\n"
printf "Real-Time Web Interfaces:\n"
printf "  🌐 Robotics Cockpit:   ${BLUE}https://omni-network-39821.web.app/robotics.html${NC}\n"
printf "  📊 Google Sheets Feed:  ${BLUE}https://docs.google.com/spreadsheets/d/1vhxLHfFZEId4AOc5y1NWK3Oi7M3Wng2YzmsApoe8bjo/edit${NC}\n"
printf "  💻 Swarm Workspace:    ${BLUE}https://omni-network-39821.web.app/workspace.html${NC}\n\n"
