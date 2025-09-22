import cocotb
from cocotb.triggers import Timer
from cocotb.result import TestFailure

@cocotb.test()
async def adder_basic_test(dut):
    """Test additionneur 4 bits → sortie 5 bits"""
    
    # tester quelques combinaisons
    test_vectors = [
        (0, 0),
        (1, 1),
        (7, 8),
        (15, 15)
    ]
    
    for a_val, b_val in test_vectors:
        # appliquer stimulus
        dut.a.value = a_val
        dut.b.value = b_val

        # attendre un petit délai (10 ns)
        await Timer(10, units="ns")

        # vérifier la sortie
        expected = a_val + b_val
        if int(dut.sum.value) != expected:
            raise TestFailure(f"Erreur: {a_val} + {b_val} = {int(dut.sum.value)}, attendu {expected}")
