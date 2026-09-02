#!/data/data/com.termux/files/usr/bin/bash
# ==============================================================================
# ⚡ Termux-Sentry - 1-Click Mobile Termux Installation
# Velorio Labs Flagship Real-Time Telemetry & Process Radar
# ==============================================================================

set -e

LIME='\033[38;2;204;255;0m'
CYAN='\033[38;2;56;189;248m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

clear
echo -e "${LIME}"
cat << "EOF"
  ███████╗███████╗███╗   ██╗████████╗██████╗ ██╗   ██╗
  ██╔════╝██╔════╝████╗  ██║╚══██╔══╝██╔══██╗╚██╗ ██╔╝
  ███████╗█████╗  ██╔██╗ ██║   ██║   ██████╔╝ ╚████╔╝ 
  ╚════██║██╔══╝  ██║╚██╗██║   ██║   ██╔══██╗  ╚██╔╝  
  ███████║███████╗██║ ╚████║   ██║   ██║  ██║   ██║   
  ╚══════╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝   
      [ Real-Time Android Hardware Telemetry & Process Radar ]
                        Velorio Labs Flagship
EOF
echo -e "${NC}"

echo -e "${CYAN}[*] Updating Termux packages...${NC}"
pkg update -y && pkg upgrade -y

echo -e "${CYAN}[*] Installing dependencies (python, termux-api, procps, git)...${NC}"
pkg install -y python python-pip termux-api procps git

mkdir -p "$HOME/.veloriolabs/termux_sentry"

if [ -d "./termux_sentry" ]; then
    cp -r ./termux_sentry "$HOME/.veloriolabs/termux_sentry/"
    cp ./pyproject.toml "$HOME/.veloriolabs/termux_sentry/" 2>/dev/null || true
else
    git clone https://github.com/VelorioLabs/Termux-Sentry.git "$HOME/.veloriolabs/termux_sentry_git"
    cp -r "$HOME/.veloriolabs/termux_sentry_git/termux_sentry" "$HOME/.veloriolabs/termux_sentry/"
fi

cd "$HOME/.veloriolabs/termux_sentry"
pip install -e . 2>/dev/null || pip install . 2>/dev/null || true

mkdir -p "$PREFIX/bin"
cat << 'EOF' > "$PREFIX/bin/sentry"
#!/data/data/com.termux/files/usr/bin/bash
export PYTHONPATH="$HOME/.veloriolabs/termux_sentry:$PYTHONPATH"
python -m termux_sentry.cli "$@"
EOF
chmod +x "$PREFIX/bin/sentry"

ln -sf "$PREFIX/bin/sentry" "$PREFIX/bin/termux-sentry" 2>/dev/null || true

echo -e "\n${GREEN}[✓] Termux-Sentry successfully installed in Termux!${NC}"
echo -e "${YELLOW}Usage Commands:${NC}"
echo -e "  • ${LIME}sentry radar${NC}   - Real-time listening sockets & process map"
echo -e "  • ${LIME}sentry thermal${NC} - Hardware thermal zones & throttles"
echo -e "  • ${LIME}sentry battery${NC} - Power draw, voltage & discharge current\n"
