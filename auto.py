import webbrowser
import os

# This will open new browser if possible or
# open a new tab with specified url.
# Enter one more urls below to open.
# I mostly use stackoverflow and google :)

class browser:

    url = "http://stackoverflow.com"
    urlSecond = "https://www.google.com"

    webbrowser.open_new(url)
    webbrowser.open_new(urlSecond)

# This one opens an .exe file, you need to enter
# a ful path to program dir.
# Enter full path to youre program directory to
# automatically open it.
# Python will convert forward-slashed to backslashes on Windows.


def start_prog():

    filepath = "C:/Full/path/to_program/program.exe"
    os.startfile(filepath)
