import angr
import claripy
from angrutils import *

# Load the binary
project = angr.Project("./buffer", auto_load_libs=False)

# Define the symbolic variable for user input
argv1 = claripy.BVS("argv1", 8 * 100)  # Assuming max input length of 20 bytes for example

# Create an initial state with the symbolic input
initial_state = project.factory.entry_state(args=["./buffer", argv1])

# Set up a simulation manager
simgr = project.factory.simulation_manager(initial_state)

# Define the address of the 'secret_function' (found via disassembly or symbols)
# This would be the address where the print statement "Unauthorized access to secret function!" is located.


# Explore the binary, looking for paths that reach 'secret_function'
simgr.explore(find=0x500018)

# # found = simgr.found[0]
# # #ask to the symbolic solver to get the value of argv1 in the reached state as a string
# # solution = found.solver.eval(argv1, cast_to=bytes)

# # print(repr(solution))
# # solution = solution[:solution.find(b"\x00")]
# # print(solution)

print(simgr.found)

# # Check if we found any paths
# if len(simgr.found) > 0:
#     print("Potential unauthorized memory access detected!")
#     found = simgr.found[0]
#     # Retrieve the concrete value for the symbolic input that causes the issue
#     input_value = found.solver.eval(argv1, cast_to=bytes)
#     print("Input causing the issue:", input_value)
# else:
#     print("No issues detected.")



main = project.loader.main_object.get_symbol("main")
print (main)
start_state = project.factory.blank_state(addr=main.rebased_addr)
cfg = project.analyses.CFGEmulated(fail_fast=True, starts=[main.rebased_addr], initial_state=start_state)
plot_cfg(cfg, "main", format="svg", asminst=True, remove_imports=True, remove_path_terminator=True)
# Generate the control flow graph
# cfg = project.analyses.CFGFast()

# Iterate over all discovered functions
print("List of functions in the binary:")
for func_addr, func in cfg.kb.functions.items():
    print(f"Function name: {func.name}, Address: {hex(func_addr)}")