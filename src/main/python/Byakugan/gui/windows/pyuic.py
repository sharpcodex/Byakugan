import os
from pathlib import Path

cwd = os.getcwd()
print('Working on : {}'.format(cwd))

if __name__ == '__main__':
    all_count = 0
    changed_count = 0

    for filename in Path(cwd).glob('**/*.ui'):
        all_count += 1
        ui_filename = str(filename)
        py_filename = str.replace(ui_filename, '.ui', '.py')

        if Path(py_filename).is_file():
            ui_date = os.path.getmtime(ui_filename)
            py_date = os.path.getmtime(py_filename)

            if ui_date <= py_date:
                continue

        changed_count += 1
        pyuic_cmd = 'pyuic5 {} -o {}'.format(ui_filename, py_filename)
        os.system(pyuic_cmd)
        print(ui_filename)

    print('Changed {} out of {} Files'.format(changed_count, all_count))
