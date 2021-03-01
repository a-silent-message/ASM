import pygame # start pygame to code
import time # close window after
import speech_recognition as sr

print("A SILENT MESSAGE - RUNNING")
pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
alpha = (0,88,255)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)
blue = (12, 20, 26)

colour = white

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Speech Recognition - A Silent Message by Nivyan')

gameDisplay.fill(white)
carImg = pygame.image.load('img.jpg')
gameDisplay.blit(carImg,(0,0))

def close():
    pygame.quit()
    quit()

def message_display(text):
    largeText = pygame.font.SysFont('Agency FB',30)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/6))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()
    

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("Arial",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def s2t():
    gameDisplay.blit(carImg,(0,0))
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print ('Say Something!')
        audio = r.listen(source)
        print ('Done!')
     
    text = r.recognize_google(audio, language = "en-US")
    print(text)
    message_display(text)


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        button("Speak!",150,450,100,50,blue,black,s2t)
        button("Quit",550,450,100,50,blue,black,close)
        pygame.display.update()

if __name__ == '__main__':
    main()
