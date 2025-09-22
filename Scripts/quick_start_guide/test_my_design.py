import cocotb
from cocotb.triggers import RisingEdge, Timer
from cocotb.clock import Clock


@cocotb.test()
async def test_counter_increments(dut):
    """Simple test: reset then check the counter increments."""

    # Crée un clock 10ns
    cocotb.start_soon(Clock(dut.clk, 10, units="ns").start())

    # Reset
    dut.rst.value = 1
    await Timer(20, units="ns")
    dut.rst.value = 0
    await RisingEdge(dut.clk)

    # Vérifie que le compteur démarre bien à 0
    assert dut.count.value == 0, f"Counter not reset! Got {dut.count.value}"

    # Attendre quelques cycles et vérifier l’incrémentation
    for i in range(1, 6):
        await RisingEdge(dut.clk)
        assert dut.count.value == i, f"Expected {i}, got {dut.count.value}"
