import os
import subprocess

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_dir = os.path.commonpath([working_dir_abs, target_file_path]) == working_dir_abs 

        if not valid_target_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'


        if not target_file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python3", target_file_path]
        if args :
            command.extend(args)

        process_result = subprocess.run(command, capture_output=True, timeout=30, text=True, cwd=working_dir_abs)
        res = ""
        if process_result.returncode != 0:
            res += f"Process exited with code {process_result.returncode}"
        
        if not process_result.stdout and not process_result.stderr:
            res+= "No output produced"
        else:
            res+= f"STDOUT: {process_result.stdout}\n STDERR: {process_result.stderr}"

        return res



    except Exception as e:
        return f"Error: executing Python file: {e}"

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Run a subprocces for running some python files with some timeout and caputre the stdin and stderr",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to a file that need to be executed",
                },
                "args": {
                    "type": "array",
                    "description": "Taking additional arguments for running python files. Arguments are string in an array",
                }
            },
        },
    },
}