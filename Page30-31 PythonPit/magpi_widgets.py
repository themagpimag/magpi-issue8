# Python Widgets using pygame and subprocess
# By ColinD - 02 November 2012

import subprocess, os, signal, Tkinter, time

# run the widget subprocesses - feel free to add more here!
pImg = subprocess.Popen(["python","widget_image.py"],stdin=subprocess.PIPE)
pRss = subprocess.Popen(["python","widget_rss.py"],stdin=subprocess.PIPE)

# send the screen width to the sub processes
r = Tkinter.Tk()
width = r.winfo_screenwidth()
pImg.stdin.write(str(width)+"\n")
pRss.stdin.write(str(width)+"\n")

# Run until subprocesses killed with a single CTRL-C
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    os.kill(pImg.pid, signal.SIGKILL)
    os.kill(pRss.pid, signal.SIGKILL)
