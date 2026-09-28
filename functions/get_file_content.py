import os
MAX_CHARS = 2000

def get_file_content(working_directory: str, file_path: str) -> str:
    try:    
        working_dir_abs = os.path.abspath(working_directory)
        target_file_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_file_path = os.path.commonpath([working_dir_abs, target_file_path]) == working_dir_abs


        if not valid_file_path: 
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
    
        with open(target_file_path, "r") as f:
            content = f.read(MAX_CHARS)
            if f.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

        return content

    except Exception as e:
        return f"Error: {e}" 

schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Gets content of files in and reading them up to 1000 chars if its more than 1000 it displays message that file content was truncated at 1000s character",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to a file that need to be read",
                },
            },
        },
    },
}