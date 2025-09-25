import os 
from colorama import Fore, Style

PATH = "Results/"


if __name__ == "__main__":
    if not os.path.exists(PATH):
        assert os.makedirs(PATH) is None
    PATH_CPP = PATH + "log_cpp.txt"
    PATH_VHD = PATH + "log_vhd.txt"
    assert os.path.exists(PATH_CPP), f"{PATH_CPP} does not exist"
    assert os.path.exists(PATH_VHD), f"{PATH_VHD} does not exist"

    print("Comparing results from C++ and VHDL implementations...")
    with open(PATH_CPP, "r") as f_cpp, open(PATH_VHD, "r") as f_vhd:
        lines_cpp = f_cpp.readlines()
        lines_vhd = f_vhd.readlines()
        max_lines = max(len(lines_cpp), len(lines_vhd))
        for i in range(max_lines):
            line_cpp = lines_cpp[i].strip() if i < len(lines_cpp) else "N/A"
            line_vhd = lines_vhd[i].strip() if i < len(lines_vhd) else "N/A"
            if line_cpp == line_vhd:
                print(f"{Fore.GREEN}Line {i + 1}: MATCH{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}Line {i + 1}: MISMATCH")
                print(f"  C++: {line_cpp}")
                print(f"  VHDL: {line_vhd}{Style.RESET_ALL}")
    print("Comparison done.")
