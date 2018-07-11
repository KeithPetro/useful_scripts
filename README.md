# useful_scripts
A collection of scripts made for different purposes. Some of these were made for my own personal use-cases, others were made for specific courses in University. These scripts are made mostly in python, but there are also some batch, bash and other scripts. If you find anything that could be improved in any of these scripts, please let me know.

## CME_451
A collection of scripts I made for my CME 451 (Transport Networks) course.

## chrome_session_reader.sh
A simple script to read old `Current Session`, `Current Tabs`, `Previous Session` and `Previous Tabs` files I had lying around. These files were taken from chrome's data folder after crashes in order to preserve potentially lost session data.

## concat_mp4.bat
A simple script to concatenate n-part mp4 videos into a single video using ffmpeg. This script simply concatenates the video and audio streams, it does not do any re-encoding. I have found that there seems to be some bugs when it comes to this concatenation process, sometimes getting artifacting and lost frames after performing it, so double check any output from it. I will have to do more research and debugging to determine what exactly is causing these issues. Currently the script does not delete the intermediary files (the temporary .ts files). I hope to add options in the future including:
* Make script delete intermediary files by default with option to preserve
* Option to provide list of input files in order of concatenation
* Option to specify output filename
* Option to concatenate H.265 (HEVC) streams - Currently this script only supports H.264 streams

Current usage:

`concat_mp4.bat [n]` where n is the number of input files. All files must be named 1.mp4 through n.mp4, and the script will produce out.mp4 as well as the intermediary .ts files.

Please note that the files you are concatenating **must** be the same dimensions.

## make_respective_folders.bat
This script was made for a very specific application, but can be modified fairly easily to fit similar applications.

The script takes all files in the current directory (except .bat files) and moves them to a folder with the same name as them up until the first dash (-). This was because I had a bunch of files with the naming scheme `program-version`, and I wished to sort these into separate folders for each program.

## msn_chat_history_viewer.py
A script using BeautifulSoup4 in order to take old XML msn chat logs and convert them into a human readable textfile.

## rename_broadcasting_logs.py
A simple script I used to rename a collection of CRTC broadcasting logs into a standard naming scheme.
