import os
import glob
from pkg_resources import resource_filename


def get_ff_path():
    return [resource_filename('oplsaafoyer', 'xml')]


def get_forcefields():
    for dir_path in get_ff_path():
        file_pattern = os.path.join(dir_path, '*.xml')
        file_paths = [file_path for file_path in glob.glob(file_pattern)]
    return file_paths
