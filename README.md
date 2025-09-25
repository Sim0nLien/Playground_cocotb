# Playground_cocotb

Learning and experimenting with **cocotb** for FPGA design validation.  
This project aims to build a verification framework comparing **C++ models** and **VHDL implementations**.

---

## 📂 Project Structure

- `Scripts/` : Python scripts to run cocotb tests and generate files for simulation and verification.  
- `Srcs/` : Source files for the FPGA design, including VHDL and C++ models.  
  - `cpp_model/` : Reference models written in C++.

---

## 🚀 Getting Started

### 1. Install Dependencies
Make sure you have **Python**, **cocotb**, and a VHDL simulator (e.g., **GHDL**) installed.  
Then install the required Python packages:

### 2. Add Your Design

Place your VHDL design files in the Srcs/rtl_model/ directory.
Place your C++ models in Srcs/cpp_model/.

### 3. Create Testbenches

Write your cocotb testbenches [this file](/Scripts/test_adder_vhd.py) in the Scripts/ directory.

### 4. Configure the Module

Define your module configuration and test stimuli in [module](Scripts/module.json).

### 5. Run Tests

Run : 

```bash
make
```
