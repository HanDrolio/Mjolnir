k#!/bin/bash
# chromebook_init.sh — lean dev + dev tools setup for Chromebook

echo "⚡️ Starting Chromebook lean init + dev tools setup..."

# Stop unneeded services to free RAM & CPU
SERVICES=(
  bluetooth
  cups-browsed
  modemmanager
  saned
  powerd
  upstart-dbus-bridge
)

for svc in "${SERVICES[@]}"; do
  echo "⏸️ Stopping $svc service..."
  sudo stop "$svc" 2>/dev/null || echo "⚠️ $svc not running or not found"
done

# Disable animations for better performance
echo "🖥️ Disabling animations..."
gsettings set org.gnome.desktop.interface enable-animations false 2>/dev/null || echo "⚠️ Can't disable animations (not GNOME)"

# Clean apt cache and update system
echo "🧹 Cleaning apt cache..."
sudo apt-get clean

echo "⬆️ Updating & upgrading packages..."
sudo apt-get update && sudo apt-get upgrade -y

echo "🗑️ Removing unnecessary packages and cleaning up..."
sudo apt-get autoremove -y
sudo apt-get autoclean -y

# Install dev essentials
echo "🛠️ Installing dev tools: git, python3, pip, build-essential, curl..."
sudo apt-get install -y git python3 python3-pip build-essential curl

echo "🖤 Installing Black (Python formatter)..."
pip3 install --user black

# Docker install steps
if ! command -v docker &>/dev/null; then
  echo "🐳 Installing Docker..."

  # Remove old versions
  sudo apt-get remove -y docker docker-engine docker.io containerd runc || true

  # Setup Docker repo
  sudo apt-get update
  sudo apt-get install -y \
    ca-certificates \
    gnupg \
    lsb-release

  curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

  echo \
    "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian \
    $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

  sudo apt-get update
  sudo apt-get install -y docker-ce docker-ce-cli containerd.io

  # Add current user to docker group
  sudo usermod -aG docker "$USER"

  echo "🐳 Docker installed. You may need to log out and back in."
else
  echo "🐳 Docker already installed."
fi

echo "✅ Chromebook init + dev tools setup complete. Ready to code and dockerize."

