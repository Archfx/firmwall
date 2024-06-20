install_deps() {

		cd .venv
		mkdir deps
		cd deps
		git clone https://github.com/angr/archinfo.git 
		git clone --recursive https://github.com/angr/pyvex.git
		git clone https://github.com/angr/cle.git
		git clone https://github.com/angr/claripy.git
		git clone https://github.com/angr/ailment.git
		git clone https://github.com/angr/angr.git
		git clone https://github.com/angr/angr-management.git
		git clone https://github.com/angr/binaries.git
		git clone https://github.com/axt/bingraphvis
		git clone https://github.com/axt/angr-utils
        git clone https://github.com/angr/patcherex.git # for patching binaries

		pip install -U pip wheel setuptools cffi "unicorn==2.0.1.post1"

		pip install -e ./archinfo
		pip install -e ./pyvex
		pip install -e ./cle 
		pip install -e ./claripy 
		pip install -e ./ailment 
		pip install --no-build-isolation -e ./angr --config-settings editable_mode=strict
		pip install -e ./angr-management --config-settings editable_mode=strict
		pip install -e ./bingraphvis
		pip install -e ./angr-utils
        pip install -e ./patcherex 

		cd ../../

		# rm -rf archinfo pyvex cle claripy ailment angr angr-management
}

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
			install_deps
        elif [ "$(uname -s | grep -i 'cygwin\|mingw\|msys')" ]; then
            source .venv/Scripts/activate
			install_deps
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

setup_venv