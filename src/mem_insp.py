import angr



def on_mem_read(state):
	addr = state.inspect.mem_read_address
	length = state.inspect.mem_read_length

	# Try to evaluate symbolic addresses and lengths to concrete values
	try:
		addr_val = state.solver.eval(addr, cast_to=int)
	except:
		addr_val = addr  # Symbolic address, print as symbolic

	try:
		length_val = state.solver.eval(length, cast_to=int)
	except:
		length_val = length  # Symbolic length, print as symbolic

	# Print address and length
	print(f"Memory read at address 0x{addr_val:x} with length {length_val}")

def on_mem_write(state):
	addr = state.inspect.mem_write_address
	length = state.inspect.mem_write_length

	# Try to evaluate symbolic addresses and lengths to concrete values
	try:
		addr_val = state.solver.eval(addr, cast_to=int)
	except:
		addr_val = addr  # Symbolic address, print as symbolic

	try:
		length_val = state.solver.eval(length, cast_to=int)
	except:
		length_val = length  # Symbolic length, print as symbolic

	# Print address and length
	print(f"Memory write at address 0x{addr_val:x} with length {length_val}")
