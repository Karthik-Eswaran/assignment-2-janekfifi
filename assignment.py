def read_file(file_path: str) -> str:
    with open(file_path, 'r') as file:
        return file.read()
    


def write_file(file_path: str, content: str) -> None:
    with open(file_path, 'w') as file:
        file.write(content)
    


def list_files_in_directory(directory_path: str) -> list:
    """
    Returns a list of files in the specified directory.
    """
    raise NotImplementedError()


def generate_numbers(n: int) -> iter:
    return iter(range(n))


def use_function_from_module(module_name: str, function_name: str, *args) -> any:
    module = importlib.import_module(module_name)
    func = getattr(module, function_name)
    return func(*args)
