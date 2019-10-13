import os
from pathlib import Path

for filename in Path(os.getcwd()).glob('**/*.ui'):
    ui_filename = str(filename)
    py_filename = str.replace(ui_filename, '.ui', '.py')

    if Path(py_filename).is_file():
        convert = False
        ui_date = os.path.getmtime(ui_filename)
        py_date = os.path.getmtime(py_filename)

        if ui_date < py_date:
            continue

    pyuic_cmd = 'pyuic5 {} -o {}'.format(ui_filename, py_filename)
    print(pyuic_cmd)
    os.system(pyuic_cmd)
