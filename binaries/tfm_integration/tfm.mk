TOPTARGETS := all

BOLD = \033[1m
YELLOW = \033[33m
RESET = \033[0m

# Define the Python scripts and their arguments
LIST_FN := $(FIRMWALL_HOME)/src/list_func
SYMB_FN := $(FIRMWALL_HOME)/src/symbolic_sim
SVG_FN := $(FIRMWALL_HOME)/src/save_svg
FIRMWALL := $(FIRMWALL_HOME)/src/firmwall
ELF_FILE := bin/zephyr.elf

# SUBDIRS := $(wildcard tfm_integration/*/.)
SUBDIRS := $(wildcard */)


# Further filter out unwanted directories if necessary
# For example:
# SUBDIRS := $(filter-out binaries/unwanted_subdir/., $(SUBDIRS))

$(TOPTARGETS): $(SUBDIRS)
$(SUBDIRS):
		@echo "$(BOLD)$(YELLOW)Processing $@"
		@echo "================================================= $(RESET)"
		mkdir -p $@/res
		start_time=$$(date +%s); \
		python3 $(FIRMWALL) -p $@; \
		end_time=$$(date +%s); \
		echo "$(BOLD)$(YELLOW)Elapsed time: $$((end_time - start_time)) seconds."
		@echo "================================================= $(RESET)"


# Clean target (optional)
clean:
	@echo "Cleaning up..."
	@for dir in $(SUBDIRS); do \
	    rm -rf $$dir/res; \
	done
	@echo "Cleanup complete."
	# Add any cleanup commands here, e.g., removing temporary files
	# rm -f *.tmp

.PHONY: $(TOPTARGETS) $(SUBDIRS) clean