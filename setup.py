import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

options = {"build_exe": {"includes": "atexit"}}

executables = [Executable("calcy.py", base=base)]

setup(
    name="calcy",
    version="0.1",
    description="simple calculator app",
    options=options,
    executables=executables,
)