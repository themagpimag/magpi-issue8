import urllib, Image, pygame, os, argparse, sys, subprocess, time
from bs4 import BeautifulSoup

# read stdin from parent process and calculate widget screen position
baseXPos = int(sys.stdin.readline()) - 200 - 10
os.environ['SDL_VIDEO_WINDOW_POS'] = str(baseXPos) + "," + str(30)

while True:
    try:
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
        windowSurface = pygame.display.set_mode((200,200), pygame.NOFRAME)
        imgLoad = pygame.image.load(imgName)
        windowSurface.blit(imgLoad, (0,0))
        pygame.display.update()
    # if an error occurs skip the download on this iteration
    except (IOError, TypeError, RuntimeError):
        print "Error downloading, will try again later"

    # sleep for 8 hours as we do not want to spam the server!
    time.sleep(28800)
