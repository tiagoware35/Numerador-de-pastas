from cx_Freeze import setup, Executable
 
setup(
    name="NumeracaoDePastas EXECUTABLE",
    version = "1.0",
    description = ".py to .exe",
    options = {"build_exe": {
        'packages': ["os","PyQt5.Core","PyQt5.QtGui","PyQt5.QtWidgets"],
    }},
    executables = [Executable("NumeracaoDePastas.py")])
