import os
import subprocess

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Runs a specified Python file relative to the working directory",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the Python file to run, relative to the working directory",
                },
                "args": {
                    "type": "array",
                    "items": {
                        "type": "string",
                    },
                    "description": "Optional arguments to pass to the Python file",
                },
            },
            "required": ["file_path"],
        },
    },
}

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_dir = os.path.commonpath([working_dir_abs, target_path]) == working_dir_abs
        if not valid_target_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not file_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'
        command = ["python", target_path]
        if args:
            command.extend(args)
        result = subprocess.run(command, cwd=working_dir_abs, capture_output=True, timeout=30, text=True)  # noqa: PLW1510
        final_output = []
        if result.returncode != 0:
            final_output.append(f'Process exited with code {result.returncode}')  # pyright: ignore[reportUnknownMemberType]
        if not result.stdout and not result.stderr:
            final_output.append("No output produced")  # pyright: ignore[reportUnknownMemberType]
        if result.stdout:
            final_output.append(f'STDOUT: {result.stdout}')  # pyright: ignore[reportUnknownMemberType]
        if result.stderr:
            final_output.append(f'STDERR: {result.stderr}')  # pyright: ignore[reportUnknownMemberType]
        return '\n'.join(final_output)  # pyright: ignore[reportUnknownArgumentType]
    except Exception as e:  # noqa: BLE001
        return f"Error: executing Python file: {e}"
