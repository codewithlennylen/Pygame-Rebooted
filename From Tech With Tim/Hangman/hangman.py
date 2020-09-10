import pygame
import math
import random
import os

# Setup display
pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game!")

# button variables
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) // 2)
starty = 400
A = 65
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13)) # i % 13 >> Logic for implementing Rows
    y =  starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x,y, chr(A + i), True])

# Fonts
LETTER_FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans', 60)
TITLE_FONT = pygame.font.SysFont('comicsans', 70)

# Load images
images = []
for i in range(7): # upto but excluding 7
    # image = pygame.image.load("hangman" + str(i) +".png")
    image = pygame.image.load("C:/Users/Lennylen/Documents/GitHub/Pygame-Rebooted/From Tech With Tim/Hangman/imgs/hangman" + str(i) + ".png")
    images.append(image)

# game variables
hangman_status = 0
words = ["PYTHON", "PYGAME","IDE","C","ALGORITHM"]
word = random.choice(words)
guessed = []

# Colors
WHITE = (255, 255, 255)
BLACK = (0 ,0 ,0 )


def draw():
    win.fill(WHITE)

    # Draw title
    text = TITLE_FONT.render("DEVELOPER HANGMAN", 1, BLACK)
    win.blit(text, (WIDTH//2 - text.get_width()//2, 20))
    
    # Draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (400,200))

    

    # Draw Buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            # A little more Logic
            win.blit(text, (x - text.get_width() // 2, y - text.get_height() // 2))

    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()

def display_message(message):
    pygame.time.delay(1000)
    win.fill(WHITE)
    text = WORD_FONT.render(message,1, BLACK)
    win.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()//2))
    pygame.display.update()
    pygame.time.delay(3000)

def main():
    global hangman_status

    # setup game loop
    FPS = 60
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos ()
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        # Determine the distance between two points
                        # Get the square root of the sum of the difference of the x-coordinates and y-coordinates
                        dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                        if dis < RADIUS:
                            letter[3] = False
                            guessed.append(ltr)
                            if ltr not in word:
                                hangman_status += 1

        draw()

        won = True
        for letter in word:
            if letter not in guessed:
                won = False
                break
        
        if won:
            display_message("You Won!")
            break

        if hangman_status == 6:
            display_message("You Loose!")
            break

main()
pygame.quit()