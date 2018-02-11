# Autogram
### Information
- The image file name is going to be the caption that will be posted
- The file should be `.jpg` (For some reason Instagram only accepts `.jpg`)
- After an image is posted, it is renamed to `[imagename].used` to make sure it is not reposted

### Instructions:
1. Put images in `/images` or any folder that is specified
    - The image name is the caption that is going to be posted
    - Do this again if the folder is out of images, if the folder is empty the script won't work
2. Schedule script via a crontab or a windows scheduled task
### Usage:
`python3 bot.py [username] [password] [image directory]`

`python3 bot.py "john_56" "iHate_Donuts" "images"`
#### Requires:
> instapy-cli https://github.com/b3nab/instapy-cli
