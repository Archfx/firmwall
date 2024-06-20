TOPTARGETS := all

# Define the Python scripts and their arguments
LIST_FN := $(FIRMWALL_HOME)/src/list_func
ELF_FILE := bin/zephyr.elf

# SUBDIRS := $(wildcard tfm_integration/*/.)
SUBDIRS := $(wildcard */)


# Further filter out unwanted directories if necessary
# For example:
# SUBDIRS := $(filter-out binaries/unwanted_subdir/., $(SUBDIRS))

$(TOPTARGETS): $(SUBDIRS)
$(SUBDIRS):
		@echo "Processing $@"
		mkdir -p $@/res
		start_time=$$(date +%s); \
		python3 $(LIST_FN) $@/$(ELF_FILE) $@/res; \
		end_time=$$(date +%s); \
		echo "Elapsed time: $$((end_time - start_time)) seconds."



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