# MAKEFLAGS += -s
# export MAKEFLAGS

# TOPTARGETS := all clean
FIRMWALL_HOME := $(shell pwd)
export FIRMWALL_HOME

# Filter to include only subdirectories from the binaries folder
# SUBDIRS := $(wildcard binaries/tfm_integration/*/.)
run: setup-venv activate-venv tfm-targets

setup-venv:
	$(FIRMWALL_HOME)/scripts/setup.sh

include binaries/tfm_integration/tfm.mk

activate-venv:
	chmod +x .venv/bin/activate
	. .venv/bin/activate && \
		$(MAKE) -C binaries/tfm_integration -f tfm.mk $(MAKECMDGOALS)



