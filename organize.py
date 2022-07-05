import os
import shutil
import argparse


def organize(dir_to_organize):

    files_list = os.listdir(dir_to_organize)  # files/dirs list in given dir

    for file in files_list:

        filepath = os.path.join(dir_to_organize, file)  # path to the file
        extension = os.path.splitext(file)[1].strip('.')  # get file extension

        # set dir for files with specific extension
        ext_folder_dir = os.path.join(dir_to_organize, extension)

        # check if dir for specific extension exists
        if os.path.exists(ext_folder_dir):
            try:
                shutil.move(filepath, ext_folder_dir)  # move file to its dir
            except shutil.Error:
                pass
        else:
            os.mkdir(ext_folder_dir)  # create new dir
            try:
                shutil.move(filepath, ext_folder_dir)
            except shutil.Error:
                pass

# define cmd arguments for the script
parser = argparse.ArgumentParser()
parser.add_argument("-directory", type=str)
args = parser.parse_args()
dir_to_organize = args.directory
