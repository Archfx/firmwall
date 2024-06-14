# Define the function
setup_venv() {
    # Check if .venv directory exists
    if [ ! -d ".venv" ]; then
        echo ".venv directory does not exist. Creating virtual environment..."
        python3 -m venv .venv
		sed -i.bak 's/PS1="(venv) ${PS1:-}"/PS1="\\\[\\033[1;33m\\\](FirmWall)\\\[\\033[0m\\\] ${PS1:-}"/' .venv/bin/activate

        # Activate the virtual environment
        if [ "$(uname)" == "Darwin" ] || [ "$(uname -s)" == "Linux" ]; then
            source .venv/bin/activate
        elif [ "$(uname -s | grep -i 'cygwin\|mingw\|msys')" ]; then
            source .venv/Scripts/activate
        else
            echo "Unsupported OS. Cannot activate virtual environment."
            return 1
        fi

        # Check if requirements.txt exists and install dependencies
        if [ -f "scripts/requirements.txt" ]; then
            echo "requirements.txt found. Installing dependencies..."
            pip install -r scripts/requirements.txt
        else
            echo "requirements.txt not found. Skipping dependency installation."
        fi

        # Deactivate the virtual environment
        deactivate
    else
        echo ".venv directory already exists. Skipping virtual environment setup."
    fi
}

activate_venv() {
	source .venv/bin/activate
}

run_read(){
	./src/list_func binaries/tfm_integration/tfm_ipc/bin/zephyr.elf
}

# Call the function
setup_venv
activate_venv
run_read