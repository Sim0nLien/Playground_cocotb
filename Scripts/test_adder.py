import cocotb
from cocotb.triggers import RisingEdge, Timer
from cocotb.clock import Clock
import subprocess
import json
import subprocess

# TODO : faire attention ou l'on se trouve


@cocotb.test()
async def test_adder(dut):

    cocotb.start_soon(Clock(dut.clk, 10, unit="ns").start())

   
    test_vectors = [
        (0, 0),
        (1, 1),
        (7, 8),
        (15, 15)
    ]
    dut.reset.value = 1
    await Timer(20, unit="ns")
    dut.reset.value = 0
    
    
    for a_val, b_val in test_vectors:
        dut.a.value = a_val
        dut.b.value = b_val
        await Timer(20, unit="ns")
        await RisingEdge(dut.clk)
        expected_sum = a_val + b_val        
        assert dut.sum.value == expected_sum, f"Adder failed for {a_val} + {b_val}: expected {expected_sum}, got {dut.sum.value}"
        cocotb.log.info(f"Tested {a_val} + {b_val}, got {dut.sum.value}")
    
    print("All tests passed!")



    proc = subprocess.run(
        ["make"],                     # commande seule
        cwd="../build",               # change de dossier
        capture_output=True,
        text=True,
        check=False
    )

    print("Code de retour :", proc.returncode)
    print("stdout:\n", proc.stdout)
    print("stderr:\n", proc.stderr)

    proc = subprocess.run(
        ["./exe"],                     # commande seule
        cwd="../build",               # change de dossier
        capture_output=True,
        text=True,
        check=False
    )

    print("Code de retour :", proc.returncode)
    print("stdout:\n", proc.stdout)
    print("stderr:\n", proc.stderr)
