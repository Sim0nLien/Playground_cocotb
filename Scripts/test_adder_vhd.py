import os
import json
import cocotb
from cocotb.triggers import RisingEdge, Timer
from cocotb.clock import Clock


def extract_all_stimuli(json_data):
    """
    Parcourt le JSON et retourne un dict {nom_signal: [stimuli]} 
    pour toutes les clés qui contiennent 'stimuli'.
    """
    result = {}
    for key, value in json_data.items():
        if isinstance(value, dict) and "stimuli" in value:
            result[key] = value["stimuli"]
    return result


JSON_PATH = "module.json"
with open(JSON_PATH, "r") as f:
    JSON_DATA = json.load(f)
stimuli_dict = extract_all_stimuli(JSON_DATA)
nb_stimuli = len(next(iter(stimuli_dict.values())))
print(f"Number of stimuli: {nb_stimuli}")
print(stimuli_dict)

@cocotb.test()
async def test_adder_vhd(dut):

    cocotb.start_soon(Clock(dut.clk, 10, unit="ns").start())


    dut.reset.value = 1
    await Timer(20, unit="ns")
    dut.reset.value = 0
    
    
    with open("Results/log_vhd.txt", "w") as f:
        for i in range(nb_stimuli):
            dut.a.value = stimuli_dict["a"][i]
            dut.b.value = stimuli_dict["b"][i]
            await Timer(20, unit="ns")
            await RisingEdge(dut.clk)


            # A ecrire dans le test
            expected_sum = stimuli_dict["a"][i] + stimuli_dict["b"][i]
            got_sum = int(dut.sum.value)

            assert got_sum == expected_sum, \
                f"Adder failed for {stimuli_dict['a'][i]} + {stimuli_dict['b'][i]}: expected {expected_sum}, got {got_sum}"

            cocotb.log.info(f"Tested {stimuli_dict['a'][i]} + {stimuli_dict['b'][i]}, got {got_sum}")

            f.write(f"{format(got_sum, '032b')}\n")
