import pygame, os, subprocess, sys, feedparser, time
pygame.init()

# read stdin from parent process and calculate widget screen position
baseXPos = int(sys.stdin.readline()) - 300 - 10
os.environ['SDL_VIDEO_WINDOW_POS'] = str(baseXPos) + "," + str(430)

# create the Pygame screen and text layer
screen = pygame.display.set_mode((300,150))
layerText = pygame.Surface(screen.get_size())

# fill each third of the widget's background with a different colour
pygame.draw.rect(screen,(80,140,80),(0,0,300,50))
pygame.draw.rect(screen,(80,80,80),(0,50,300,50))
pygame.draw.rect(screen,(160,160,160),(0,100,300,50))

font = pygame.font.SysFont('dejavuserif', 10, True)

while True:
    myFeed = feedparser.parse('http://www.raspberrypi.org/feed')

    # set the window title to be the name of the blog
    pygame.display.set_caption(myFeed['feed']['title']+" RSS")

    for i in range(0, 3):
        outputText = (myFeed['items'][i].title, myFeed['items'][i].updated,
        		 myFeed['items'][i].link, myFeed['items'][i].description)
        # clear the surface each loop by filling with transparent pixels
        layerText.set_colorkey((0,0,0))
        layerText.fill((0,0,0))

        j = 0
        # render the text
        for line in outputText:
            j = layerText.get_rect().y + j + 5
            text = font.render(line.rstrip('\n'), 0, (255,255,255))
            textpos = text.get_rect()
            textpos.x = layerText.get_rect().x + 5
            textpos.y = textpos.y+j
            layerText.blit(text, textpos)
            screen.blit(layerText, (0, 50*i))
            pygame.display.flip()
            j = j +5
    # sleep for an hour, do not spam the server!      
    time.sleep(3600)
