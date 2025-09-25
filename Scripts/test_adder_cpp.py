import json
import subprocess

import os


if __name__ == "__main__":
    

    proc = subprocess.run(
        ["make"],                     # commande seule
        cwd="../build",               # change de dossier
        capture_output=True,
        text=True,
        check=False
    )

    proc = subprocess.run(
        ["./exe"],                     # commande seule
        cwd="../build",               # change de dossier
        capture_output=True,
        text=True,
        check=False
    )

    # create a folder Results if it does not exist
    if not os.path.exists("Results"):
        os.makedirs("Results")

    with open("Results/log_cpp.txt", "w") as f:
        f.write(proc.stdout)
        f.write(proc.stderr)
    
    