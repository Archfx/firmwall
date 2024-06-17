
setup_venv(){
	./scripts/setup.sh
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