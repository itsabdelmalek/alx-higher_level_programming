#!/usr/bin/python3

"""
This program prints all the names defined in the compiled module hidden_4.pyc.
"""

import dis
import types

if __name__ == "__main__":
    with open("hidden_4.pyc", "rb") as file:
        code_object = types.CodeType.from_traceback(file.read()[16:], file.read())
        names = set()

        for instruction in dis.get_instructions(code_object):
            if instruction.opname == "LOAD_GLOBAL":
                name = instruction.argval
                if not name.startswith("__"):
                    names.add(name)

    for name in sorted(names):
        print(name)
