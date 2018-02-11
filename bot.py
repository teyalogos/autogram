"""
Usage: bot.py [username] [password] [image_dir]

- The image file name is going to be the caption that is posted
- The file should be jpg (Instagram only accepts jpg for some reason)
- After an image is posted, it is renamed to [imagename].used to make sure it is not reposted

INSTRUCTIONS:
1. Put images in /images/ or any folder that is specified
    - The image name is the caption that is going to be posted
    - Do this again if the folder is empty, if the folder is empty the script won't work
2. Schedule script via a crontab or a windows scheduled task
"""

import instapy_cli as insta
from sys import argv
from pathlib import Path
import random
import os

_, username, password, image_dir = argv

def get_image_and_caption(image_dir):
    """Selects a random image and caption from the specified path"""

    # collect all files in the specified path
    images = Path(image_dir).glob('**/*.jpg')
    image_list = list()
    for f in images:
        image_list.append(str(f))

    # collect image path and name
    image = random.choice(image_list)
    caption = image.split('\\')[1].split('.')[0]

    return image, caption


if __name__ == '__main__':
    image, caption = get_image_and_caption(image_dir)
    print("Posting image '{}' with caption '{}'".format(image, caption))
    
    with insta.client(username, password) as client:
        client.upload(image, caption)
    
    # make sure image is not reposted
    os.rename(image, image + '.used')
