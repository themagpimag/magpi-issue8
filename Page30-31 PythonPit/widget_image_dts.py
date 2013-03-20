import urllib, Image, pygame, os, argparse, sys, subprocess, time, datetime
from bs4 import BeautifulSoup

# read stdin from parent process and calculate widget screen position
baseXPos = int(sys.stdin.readline()) - 200 - 10
os.environ['SDL_VIDEO_WINDOW_POS'] = str(baseXPos) + "," + str(30)
windowSurface = pygame.display.set_mode((200,200), pygame.NOFRAME)

# record the current date and time to determine if a new image should be downloaded
curDate = datetime.datetime.now()
oldDay = curDate.day-1
curDay = curDate.day

while True:
    try:
        # if the day has elapsed then we want to check to see if it is time
        # to download a new image. Note that as we are not considering
        # timezones it is possible that although we (locally) are in a new
        # day that the image on APOD has not yet been updated. This code
        # checks for this as well.
        if oldDay < curDay:
            soup = BeautifulSoup(
                urllib.urlopen('http://apod.nasa.gov/apod/astropix.html'))
            # APOD has one img tag so we can use find instead of findAll
            imgTag = soup.find('img')
            imgUrl = imgTag['src']
            imgName = os.path.basename(imgUrl)

            # if the image already exists then do not redownload
            if not os.path.exists(imgName):
                urllib.urlretrieve("http://apod.nasa.gov/apod/"+imgUrl,imgName)

            # download, resize and save the image for the widget
            imgOriginal = Image.open(imgName)
            imgResized = imgOriginal.resize((200, 200), Image.NEAREST)
            imgResized.save(imgName)

            # display a borderless window containing the resized image
            imgLoad = pygame.image.load(imgName)
            windowSurface.blit(imgLoad, (0,0))

        pygame.display.update()
        
        oldDay = curDay
        curDate = datetime.datetime.now()
        curDay = curDate.day
    # if an error occurs skip the download on this iteration
    except (IOError, TypeError, RuntimeError):
        print "Error downloading, will try again later"

    # sleep for 8 hours as we do not want to spam the server!
    time.sleep(1)
