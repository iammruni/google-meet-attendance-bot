# Google Meet Attendance Bot
With the increase in online classes due to COVID-19, every step of the whole process seems like a big chore since one has to visit multiple websites to find the time table for the day and the hyperlinks for classes, and this was my attempt to automate the task.


This a browser automation script written in Python using Selenium. The principal purpose of this script/bot was to automate the task of joining classes. The general procedure was, checking the day order followed by the time table for the specific day order. Then checking the lecture and finally searching its Google Meet link.

The script is written specifically for SRM IST, KTR.
## Pre-requisites and Installation
Modules required are:
+ Time
+ Schedule
+ Socket
+ Selenium

Note: If any package is missing, install it using package manager pip.
Example:
```bash
pip install selenium
```
## Setup
In `backbone.py` starting at **line 55** change the variable names to all your subject names. You will also have to replace it everywhere the variable is used.
**You can use *Refactor* if you're using PyCharm.**
In the same file, check methods named `do_1()` through `do_5()` and change it according to your time table.

Now add your encrypted username and password files for Google Meet and Academia (you will also have to save the key, that you used to encrypt the text). In `encr.py` you can change the filename for the specific username or password.

I have saved the key as file1.bin and username and password for Google Meet as file2.bin and file3.bin. Similarly file4e.bin and file4p.bin for Academia

Read https://cryptography.io/en/latest/fernet.html on how to create a key and encrypt your text

## License
[The MIT License](LICENSE.md)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE.md)
 
 ## Project Status
 I do not intend to work on this any further. This was a fun project that I wanted to do, which anyone can do in a few hours. If you want to share your views regarding this you may contact me [here](https://iammruni.github.io/#form1-e), although please do not expect a response.
