# Define the Python scripts and their arguments
LIST_FN := $(FIRMWALL_HOME)/src/list_func
ELF_FILE := arg1 arg2 arg3

SCRIPT2 := script2.py
SCRIPT2_ARGS := arg4 arg5 arg6

SCRIPT3 := script3.py
SCRIPT3_ARGS := arg7 arg8 arg9

# Define targets for each script
.PHONY: all script1

# Default target to run all scripts
all: script1 script2 script3

# Target to run the first script
script1:
	@echo "Running $(LIST_FN) with arguments $(ELF_FILE)"
	python $(LIST_FN) $(ELF_FILE)


# Clean target (optional)
clean:
	@echo "Cleaning up..."
	# Add any cleanup commands here, e.g., removing temporary files
	# rm -f *.tmp
