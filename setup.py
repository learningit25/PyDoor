import sys
from cx_Freeze import setup, Executable

base = None

if sys.platform == "win32":
    base = "Win32GUI"

build_exe_options = {
    # Packages to include
    'includes': [],
    # Files to include
    'include_files': []
}

setup(name="puzzle",
      version="0.1",
      description="Fun computer game",
      options={'build_exe': build_exe_options},
      executables=[Executable("client.py", base=base)])

# python setup.py build
