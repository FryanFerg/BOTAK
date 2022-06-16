import sys
import os
from cx_Freeze import setup,Executable

files = ['botak.ico']

target = Executable(
    script ="botakGui.py",
    base="Win32GUI",    
    icon = "botak.ico"
    )

setup(
      name ="B.O.T.A.K",
      version = "1.0",
      description = "Build Online Technology About Knowledge",
      author = "Hamdan Fauzaan",
      options = {'build_exe' : {'include_files' : files}},
      executables = [target]
      )
import sys
from cx_Freeze import setup, Executable

options = {
'build_exe': {'path': sys.path + ['modules']}
}

executables = [
    Executable('script_1.py'),
    Executable('script_2.py')]

setup(
    name='two exe in one folder',
    version='0.1',
    description='Two exe in a single build folder',
    options=options,
    executables=executables)