#!/usr/bin/env python

import angr
import claripy

# Function to locate the address of psa_sign_hash
def locate_function(project, func_name):
    cfg = project.analyses.CFGFast()
    for func_addr, func in cfg.kb.functions.items():
        if func.name == func_name:
            return func_addr
    return None

project = angr.Project('../binaries/tfm_integration/psa_crypto/bin/zephyr.elf', load_options={'auto_load_libs': False})
# p = angr.Project('../binaries/tfm_integration/psa_crypto/bin/tfm_s.elf', load_options={'auto_load_libs': False})
cfg = project.analyses.CFGFast()
# cfg = project.analyses.CFGEmulated(keep_state=True)
print("This is the graph:", cfg.graph)
print("It has %d nodes and %d edges" % (len(cfg.graph.nodes()), len(cfg.graph.edges())))

# Locate the psa_sign_hash function
func_addr = locate_function(project, 'psa_sign_hash')
if func_addr is None:
    raise Exception("Function psa_sign_hash not found in the binary")

# # Create a state at the start of the psa_sign_hash function
state = project.factory.blank_state(addr=func_addr)

# Define function arguments
key = claripy.BVS('key', 32)  # Assume 32-bit key ID
alg = claripy.BVS('alg', 32)  # Assume 32-bit algorithm ID
hash_ptr = claripy.BVV(0x10000000, 32)  # Assume a hash pointer at 0x10000000
hash_length = claripy.BVS('hash_length', 32)  # Size of the hash buffer
signature_ptr = claripy.BVV(0x20000000, 32)  # Assume a signature buffer pointer at 0x20000000
signature_size = claripy.BVS('signature_size', 32)  # Size of the signature buffer
signature_length_ptr = claripy.BVV(0x30000000, 32)  # Assume a pointer to the signature length

# # Set registers or stack values for the function arguments
# state.regs.r0 = key
# state.regs.r1 = alg
# state.regs.r2 = hash_ptr
# state.regs.r3 = hash_length
# state.regs.r4 = signature_ptr
# state.regs.r5 = signature_size
# state.regs.r6 = signature_length_ptr

# # Define constraints for valid parameters
# state.solver.add(key != 0)
# state.solver.add(alg != 0)
# state.solver.add(hash_ptr != 0)
# state.solver.add(hash_length > 0)
# state.solver.add(signature_ptr != 0)
# state.solver.add(signature_size > 0)
# state.solver.add(signature_length_ptr != 0)

# Simulate the function
simgr = project.factory.simulation_manager(state)
simgr.explore(find=lambda s: s.addr == func_addr + 4)  # Adjust the offset as needed

# Check results
if simgr.found:
    for found_state in simgr.found:
        print("Assertions satisfied at address:", hex(found_state.addr))
else:
    print("No paths found that satisfy the assertions.")


def map_state_args( state, arch, num_args, obj):

	if (arch == "arm"):
		for x in range (num_args):
			# Set registers or stack values for the function arguments
			# state.regs.r{x} = obj[x]
			setattr(state.regs, f"r{x}", obj[x])

	return state


def add_state_consts( state, num_args, constraints):
	for constraint in constraints:
		state.solver.add(constraint)
	return state

def init_reg_vars (num_args):
	

