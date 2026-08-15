from functions.get_files_info import get_files_info

dir = "."
print(f'Result for current directory:\n{get_files_info("calculator", dir)}\n')
dir = "pkg"
print(f'Result for \'{dir}\' directory:\n{get_files_info("calculator", dir)}\n')
dir = "/bin"
print(f'Result for \'{dir}\' directory:\n{get_files_info("calculator", dir)}\n')
dir = "../"
print(f'Result for \'{dir}\' directory:\n{get_files_info("calculator", dir)}\n')
