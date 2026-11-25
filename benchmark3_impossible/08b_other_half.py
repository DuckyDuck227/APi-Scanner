from importlib import import_module

fragment_elsewhere = "Q4rS6tV8wX1yZ3aB5c"


def get_real_key():
    first_half = import_module("08_multi_file_split").fragment_here
    return first_half + fragment_elsewhere
