import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

# GUI applications require a different base on Windows (the default is for
# a console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "Exsae-Speak",
        version = "1.0",
        description = "This program was developed by Exsae Technologies. It creates an audio file out of the text given.",
        options = {"build_exe": build_exe_options},
        executables = [Executable("src/main.py", base=base)])
