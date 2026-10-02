import pygame;
from constants import SCREEN_WIDTH, SCREEN_HEIGHT;
from logger import log_state;
def main():   
   pygame.init(); 
   screen = pygame.display.set_mode((SCREEN_WIDTH , SCREEN_HEIGHT));
   while True:
    log_state();
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return;
    screen.fill("black") #fill the screen with black
    pygame.display.flip(); #update the display (refresh the screen)


if __name__ == "__main__":
    main()
