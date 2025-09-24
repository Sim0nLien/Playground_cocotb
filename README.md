# Playground_cocotb
Learning and experimenting with cocotb for FPGA design validation.

## Current Status

I am currently developing a Python script that generates a C++ wrapper for a given VHDL component.  
The script reads the component's input and output definitions from a JSON file and produces the necessary C++ code to interface with the component.

## Next Steps

- Use a script to compare the output of the VHDL component with the output of the C++ simulation to ensure consistency.  
- Create a deployable tool to automate the entire process: generating the C++ wrapper, running simulations, and comparing the results.  
- Finalize the README to document the project and its usage.  
- Complete the `requirements.txt` file with all necessary dependencies.  
- Package everything into a Docker container for easy deployment and usage.
