
setup_venv(){
	chmod +x scripts/setup.sh
	./scripts/setup.sh
}

activate_venv() {
	source .venv/bin/activate
}

run_read(){
	./src/list_func binaries/tfm_integration/tfm_ipc/bin/zephyr.elf
	# ./src/patch_ex 
}

# Call the function
setup_venv
activate_venv
make
# run_read