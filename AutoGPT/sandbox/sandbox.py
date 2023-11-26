import subprocess
import shlex
from typing import Tuple


def execute_program_routine(script_name: str) -> Tuple[str, str]:
    # Prepare the command to run the Python script
    script_path = f"AutoGPT/sandbox/{script_name}"
    command = f"python3 {script_path}"

    # Use shlex to safely split the command string
    args = shlex.split(command)

    try:
        # Execute the script in a new process
        # stdout and stderr capture the output and errors
        result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=30)

        # Check if the script ran successfully
        if result.returncode == 0:
            print("Script executed successfully.")
            print("Output:\n", result.stdout)
        else:
            print("Script execution failed.")
            print("Error:\n", result.stderr)

        return result.stdout, result.stderr

    except subprocess.TimeoutExpired:
        print("Script execution exceeded the time limit.")

    except Exception as e:
        print(f"An error occurred: {e}")
