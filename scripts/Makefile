# MAKEFLAGS += -s
# export MAKEFLAGS

# TOPTARGETS := all clean
FIRMWALL_HOME := $(shell pwd)/..
export FIRMWALL_HOME

VENV := $(FIRMWALL_HOME)/.venv/bin/activate
# Filter to include only subdirectories from the binaries folder
# SUBDIRS := $(wildcard binaries/tfm_integration/*/.)
run: analyse


include $(FIRMWALL_HOME)/binaries/tfm_integration/tfm.mk

analyse:
	chmod +x $(VENV)
	. $(VENV) && \
		$(MAKE) -C $(FIRMWALL_HOME)/binaries/tfm_integration -f tfm.mk $(MAKECMDGOALS)

