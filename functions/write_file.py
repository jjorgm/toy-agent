import os

schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Writes content to a specified file relative to the working directory",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the file to write, relative to the working directory",
                },
                "content": {
                    "type": "string",
                    "description": "Content to write to the file",
                },
            },
            "required": ["file_path", "content"],
        },
    },
}

def write_file(working_directory:str, file_path: str, content: str) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_dir = os.path.commonpath([working_dir_abs, target_path]) == working_dir_abs
        if not valid_target_dir:
            raise ValueError(f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory')
        if os.path.isdir(target_path):
            raise ValueError(f'Error: Cannot write to "{file_path}" as it is a directory')
        os.makedirs(os.path.dirname(target_path), exist_ok=True)
        with open(target_path, 'w') as file:
            file.write(content)  # pyright: ignore[reportUnusedCallResult]
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except (OSError, ValueError) as e:
        return f"Error: {e!s}"
