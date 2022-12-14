import os
import shutil
import glob

data_path = os.getenv('DATA_PATH', '/data')
outputs_path = os.path.join(data_path, 'outputs')
if not os.path.exists(outputs_path):
    os.mkdir(outputs_path)
paths = os.getenv('FILE_PATHS', 'file.txt')
folder = os.path.join(outputs_path, os.getenv('FOLDER_NAME', 'folder'))

if not os.path.exists(folder):
    os.mkdir(folder)

for path in paths.split(','):
    files = glob.glob(data_path + '/**/' + path, recursive = True)
    dest = os.path.join(folder, os.path.basename(files[0]))
    shutil.move(os.path.join(data_path, 'inputs',files[0]), dest)
