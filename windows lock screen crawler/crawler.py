import getpass
import os
from shutil import copyfile
import platform
import sys
from PIL import Image
import json

# TODO IDEA: Initial setup to set export directories and choose correct username, and automatically run every week or so
# external library needed? Pillow (PIL)

# Check letter of windows System Drive
drive_letter = os.environ['systemdrive']

# Check if user is running windows.
is_Windows = platform.system() == 'Windows'
if not is_Windows:
    print('We detected your operating system is not Windows. '
          'This program is designed to only work with Windows operating system.')
    input('Press any key to continue.')
    sys.exit()

# Check for silent mode
with open('setting.json') as s:
    setting = json.load(s)


# Check for username
your_username = getpass.getuser()

if not setting['silent']:
    prompt = 'Script detected "{}" is your username. Type "n" if incorrect. Press any key to continue...: '.format(
        your_username)
    raw_is_correct_username = input(prompt)

    # Prompt user to input username if the name script found is not the user's username
    if raw_is_correct_username == 'n':
        your_username = input('Please enter your username under C://Users/ directory: ')

# Process file and copy
file_dir = '{}/Users/{}/AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager' \
           '_cw5n1h2txyewy/LocalState/Assets'.format(drive_letter, your_username)
os.chdir(file_dir)
name_list = os.listdir(file_dir)
src_common = os.getcwd()

# Ask user where to copy the images
# is_default_dir = input(
#     'Default directory to copy image files is C:/Users/{}/Documents/Windows_spotlight/. Is this okay?: (y/n) '
#         .format(your_username))
# if is_default_dir == 'y':
dst_common = '{}/Users/{}/Documents/Windows_spotlight/'.format(drive_letter, your_username)
# else:
#     dst_common = 'Some directory'
#     # TODO open file dialog to ask user to select directory

# Ask which resolution to save.
# Normally icons are square (1x1)
# Wallpapers are generally 1920*1080 and 1080*1920

save_option = 0
# Check for silent, and if true then use orientation settings
if setting['silent']:
    save_option = setting['orientation']
else:
    while save_option not in ['1', '2', '3']:
        save_option = input('Which resolution would you save? \n1: Landscape (1920 * 1080)'
                            '\n2: Portrait (1080*1920)\n3: Both\n')

# Iterate through the target folder and copy any possible images.
for file in name_list:
    src = file_dir + '/' + file
    stat_info = os.stat(src)
    file_size = stat_info.st_size

    # filter out for files smaller than 50kb
    if file_size > 50000:
        new_image = file + '.jpg'
        src = os.path.join(src_common, file)
        src_ext = os.path.join(src_common, new_image)
        dst = os.path.join(dst_common, new_image)
        im = Image.open(src)
        width, height = im.size

        # filter out icons
        if width == height:
            continue

        # save only desired resolutions
        # portrait
        if save_option == '1':
            if width < height:
                continue
        # landscape
        elif save_option == '2':
            if width > height:
                continue

        if not os.path.exists(dst_common):
            os.makedirs(dst_common)

        copyfile(src, dst)

# Open the directory where the files are copied, and terminate the program
path = os.path.realpath(dst_common)
if setting['silent']:
    os.startfile(path)

sys.exit()
