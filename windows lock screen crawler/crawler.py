import getpass
import os
from shutil import copyfile
import platform
import sys
import imageio.imread

# TODO: images normally come in two resolution: mobile and desktop
# Measure the picture sizes and ask user which image size to keep. (1, 2, or both)
# Mobile images are narrow and tall, desktop images are wide
# DONE TODO: Detect which system drive user's system drive is
# DONE TODO: Show default dir and prompt user if he or she wants to change it to custom
# DONE TODO: Detect user OS and abort if not windows
# DONE TODO: add known icon files in tuple to filter

# TODO IDEA: Initial setup to set export directories and choose correct username, and automatically run every week or so
# external library needed? Preferably not...

# Check letter of windows System Drive
drive_letter = os.environ['systemdrive']

# Tuple to hold commonly know icon files
known_not_image = ('6981fe49f8861ed5fc2a9bbfda8433c94cc0effc29e5f39ee6ee5f0dcdb7cdb6',
                   '5a8986d2cb035b1101a5c42f36b02c0ffa398f2993c002d11c202bcd55423cfc',
                   '0c0eede1394421e9368ca381b006710a6eeaa6f59cfac0e2710847e01b6b9dec',
                   '9d97c0789c1a62b14031c0918cbc04eaebf6046b4c3ea9f0874d1346929b6889',
                   '62ec7a142f9bfa27d1c4f74e0b1f5c9297d1023f199577eff2c16d3100824d43',)

# Check if user is running windows.
is_Windows = platform.system() == 'Windows'
if not is_Windows:
    print('We detected your operating system is not Windows. '
          'This program is designed to only work with Windows operating system.')
    input('Press any key to continue.')
    sys.exit()

# Check for username
your_username = getpass.getuser()
prompt = 'Script detected "{}" is your username. Type "n" if incorrect: '.format(your_username)
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
is_default_dir = input(
    'Default directory to copy image files is C:/Users/{}/Documents/Windows_spotlight/. Is this okay?: (y/n) '
        .format(your_username))
if is_default_dir == 'y':
    dst_common = '{}/Users/{}/Documents/Windows_spotlight/'.format(drive_letter, your_username)
else:
    dst_common = 'Some directory'
    # TODO open file dialog to ask user to select directory

# Ask which resolution to save
# TODO: how to accept user prompts (e,g, out of 3 options)
# Normally icons are square (1x1)
# Wallpapers are generally 1920*1080 and 1080*1920
# So resolution filtering seems to be enough? No need to keep track of icons
# No need to change file name
# res_target = input()

# Iterate through the target folder and copy any possible images.
for file in name_list:
    src = file_dir + '/' + file
    stat_info = os.stat(src)
    file_size = stat_info.st_size

    # filter out for files smaller than 50kb
    if file_size > 50000:
        new_image = file + '.jpg'
        src = os.path.join(src_common, file)
        dst = os.path.join(dst_common, new_image)

        # TODO Check for dimensions and omit if it is square (icon)
        # TODO: Which library to use (or is one necessary at all?)
        # height, width, channels = imageio.imread(new_image).shape
        # if width == height:
        #     continue

        if not os.path.exists(dst_common):
            os.makedirs(dst_common)

        copyfile(src, dst)


# Open the directory where the files are copied, and terminate the program
path = os.path.realpath(dst_common)
os.startfile(path)
sys.exit()
