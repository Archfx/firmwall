import angr

class MemoryTracker:
	def __init__(self):
		self.allocations = {}  # Stores allocated pointers and their sizes
		self.freed_addresses = set()  # Stores addresses that have been freed

	def log_allocation(self, ptr, size):
		if ptr in self.freed_addresses:
			self.freed_addresses.remove(ptr)
		self.allocations[ptr] = size
		print(f"Allocated memory at {ptr} with size {size}")

	def log_free(self, ptr):
		if ptr in self.allocations:
			del self.allocations[ptr]
			self.freed_addresses.add(ptr)
			print(f"Freed memory at {ptr}")
		else:
			print(f"Tried to free unallocated or already freed memory at {ptr}")

	def log_read(self, addr, length):
		if any(start <= addr < start + size for start, size in self.allocations.items()):
			print(f"Read {length} bytes from memory at {addr}")
		else:
			print(f"Invalid read from {addr}")

	def log_write(self, addr, length):
		if any(start <= addr < start + size for start, size in self.allocations.items()):
			print(f"Write {length} bytes to memory at {addr}")
		else:
			print(f"Invalid write to {addr}")

def on_mem_read(state):
	addr = state.inspect.mem_read_address
	length = state.inspect.mem_read_length

	try:
		addr_val = state.solver.eval(addr, cast_to=int)
		length_val = state.solver.eval(length, cast_to=int)
	except:
		addr_val = addr  # Symbolic address
		length_val = length  # Symbolic length

	state.globals['memory_tracker'].log_read(addr_val, length_val)

def on_mem_write(state):
	addr = state.inspect.mem_write_address
	length = state.inspect.mem_write_length

	try:
		addr_val = state.solver.eval(addr, cast_to=int)
		length_val = state.solver.eval(length, cast_to=int)
	except:
		addr_val = addr  # Symbolic address
		length_val = length  # Symbolic length

	state.globals['memory_tracker'].log_write(addr_val, length_val)

class FreeDetector(angr.SimProcedure):
	def run(self, ptr):
		try:
			addr_val = self.state.solver.eval(ptr, cast_to=int)
		except:
			addr_val = ptr  # Symbolic address

		self.state.globals['memory_tracker'].log_free(addr_val)


class MallocDetector(angr.SimProcedure):
	def run(self, size):
		if self.state.solver.symbolic(size):
			size_val = self.state.solver.max(size)
		else:
			size_val = self.state.solver.eval(size)

		addr = self.state.heap._malloc(size_val)
		self.state.globals['memory_tracker'].log_allocation(addr, size_val)
		return addr