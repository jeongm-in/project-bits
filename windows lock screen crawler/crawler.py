import getpass
import os
from shutil import copyfile
# import PIL
# TODO: images normally come in two resolution: mobile and desktop
# Measure the picture sizes and ask user which image size to keep. (1, 2, or both)
# Mobile images are narrow and tall, desktop images are wide
# TODO: Ask which system drive user's system drive is
# TODO: Show default dir and prompt user if he or she wants to change it to custom
# TODO: Detect user OS and abort if not windows
# TODO: add known icon files in tuple to filter

your_username = getpass.getuser()
prompt = 'Is "{}" your username? (y / n): '.format(your_username)
raw_is_correct_username = input(prompt)
is_correct = True
if raw_is_correct_username == 'y':
    file_dir = 'C:/Users/{}/AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager' \
               '_cw5n1h2txyewy/LocalState/Assets'.format(your_username)
    os.chdir(file_dir)
    name_list = os.listdir(file_dir)
    dst_common = 'C:/Users/{}/Documents/Windows_spotlight/'.format(your_username)
    src_common = os.getcwd()
    for file in name_list:
        src = file_dir + '/' + file
        stat_info = os.stat(src)
        file_size = stat_info.st_size
        if file_size > 50000:
            src = os.path.join(src_common, file)
            dst = os.path.join(dst_common, file + '.jpg')
            if not os.path.exists(dst_common):
                os.makedirs(dst_common)

            copyfile(src, dst)

    path = os.path.realpath(dst_common)
    os.startfile(path)

