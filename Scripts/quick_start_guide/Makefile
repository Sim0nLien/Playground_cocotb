# Choisir le simulateur
SIM ?= ghdl
TOPLEVEL_LANG ?= vhdl

# Indiquer les fichiers sources
VHDL_SOURCES += $(PWD)/counter.vhd

# Nom de l’entité top-level (ton DUT)
COCOTB_TOPLEVEL = counter

# Nom du fichier Python contenant le test (sans .py)
COCOTB_TEST_MODULES = test_my_design

# (Optionnel) génération d’un fichier VCD pour les waves
EXTRA_ARGS += --std=08
SIM_ARGS += --wave=wave.ghw
# Inclure les règles cocotb
include $(shell cocotb-config --makefiles)/Makefile.sim
