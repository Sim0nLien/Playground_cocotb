TOPLEVEL=adder
MODULE=test_adder
SIM=ghdl
GHDL_ARGS= ../Srcs/rtl/adder.vhd

all:
	python3 -m cocotb.simulator \
	    --top-level adder \
	    --python-modules . \
	    --sim ghdl \
	    --vcd \
	    --ghdl-args="../Srcs/rtl/adder.vhd"
