# Check if zenity is installed
if ! command -v zenity &> /dev/null; then
    echo "Zenity is not installed. Attempting to install zenity."

    # Attempt to install zenity
    # You can adjust the installation command based on your distribution
    sudo apt-get install zenity -y

    # Check if zenity installation was successful
    if ! command -v zenity &> /dev/null; then
        echo "Failed to install zenity. Exiting script."
        exit 1
    fi
fi

# Zenity is now installed, prompt the user
if zenity --question --title="Confirmation" --text="Do you want to uninstall all pip packages?"; then
    pip freeze | xargs pip uninstall -y
fi
