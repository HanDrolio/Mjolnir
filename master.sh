
#!/bin/bash

# 🌌 Master Venv Script by Han aka gone2soon

echo "🔧 Creating virtual environment named 'cosmos_venv'..."
python3 -m venv cosmos_venv

echo "✅ Virtual environment created."

# Add alias to .bashrc or .zshrc depending on shell
SHELL_TYPE=$(basename "$SHELL")
PROFILE_FILE="$HOME/.bashrc"
if [ "$SHELL_TYPE" = "zsh" ]; then
    PROFILE_FILE="$HOME/.zshrc"
fi

echo "alias environment='source ~/cosmos_venv/bin/activate'" >> $PROFILE_FILE

echo "📌 Alias 'environment' added to $PROFILE_FILE"
echo "💡 Run 'source $PROFILE_FILE' or restart terminal to activate alias."

echo "🧠 Next time, just type: environment"
