import cx_Freeze
import sys 
import os
base = None

if sys.platform == "win32":
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Python36\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Python36\tcl\tk8.6"

executables = [cx_Freeze.Executable("Write Here.py", base = base, icon = "Icon.ico")]

cx_Freeze.setup(
    name = "Write Here",
    options = {"build.exe" : {"packages" : ["tkinter", "os"], "include_files":["icon.ico", "tcl86t.dll", "tk86t.dll", "Icons"]}},
    version = "1.0",
    # shortcutName = "Write Here",
    # shortcutDir = "DesktopFolder", 
    description = "Application",
    executables = executables
)