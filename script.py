import os
import shutil
import glob

import random
import string
import logging
from pathlib import Path
from os.path import isfile, join, isdir

data_path = os.getenv('DATA_PATH', '/data')
outputs_path = os.path.join(data_path, 'outputs')
if not os.path.exists(outputs_path):
    os.mkdir(outputs_path)
paths = os.getenv('FILE_PATHS', 'file.txt')
folder = os.path.join(outputs_path, os.getenv('FOLDER_NAME', 'folder'))

# Set up log file
logger = logging.getLogger('move-files')
logger.setLevel(logging.INFO)
log_file_name = 'move-files-%s.log' %(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6)))
fh = logging.FileHandler( Path(join(data_path, outputs_path)) / log_file_name)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

logger.info('Log file established!')
logger.info('--------')

logger.info('Paths have been setup')  

print(paths)
logger.info(paths)
print(folder)
logger.info(folder)


if not os.path.exists(folder):
    os.mkdir(folder)

for path in paths.split(','):
    files = glob.glob(data_path + '/**/' + path, recursive = True)
    print(files)
    logger.info(files)
    dest = os.path.join(folder, os.path.basename(files[0]))
    shutil.move(os.path.join(data_path, 'inputs',files[0]), dest)
