import pygame;
from constants import SCREEN_WIDTH, SCREEN_HEIGHT;
from logger import log_state;
from player import Player;
from asteroid import Asteroid;
from asteroidfield import AsteroidField;
from logger import log_event;
import sys as system;
from shot import Shot;
from explosion import Explosion;

def main():   
   pygame.init(); 
   clock = pygame.time.Clock();
   dt = 0.0;
   kill_counter =0;
   
  
   screen = pygame.display.set_mode((SCREEN_WIDTH , SCREEN_HEIGHT));
   updatable = pygame.sprite.Group();
   explosions = pygame.sprite.Group()
   drawable = pygame.sprite.Group();
   asteroids = pygame.sprite.Group();
   shots = pygame.sprite.Group();
   # Player is the name of the class, not an instance of it
   #This must be done before any Player objects are created
   Player.containers = (updatable , drawable); 
   Asteroid.containers = (asteroids , updatable , drawable);
   AsteroidField.containers = (updatable);
   Shot.containers = (shots , updatable , drawable);
   Explosion.containers = (updatable, drawable, explosions)
   asteroid_field = AsteroidField();


   player = Player(SCREEN_WIDTH/2 , SCREEN_HEIGHT/2);
   
   while True:
    log_state();
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return;
    screen.fill("black")#fill the screen with black
    updatable.update(dt); 
    for obj in drawable:
        obj.draw(screen); #update the player object with the initial delta time (dt) value of 0.0, which is passed as an argument to the update function.
    for smthg in asteroids:
        if player.collides_with(smthg):
            log_event("player_hit");
            player.kill();
            font = pygame.font.Font(None, 86)

            text = font.render(f"GAME OVER", True, "red")

            screen.blit(
                text,
                (SCREEN_WIDTH/2 - text.get_width()/2, SCREEN_HEIGHT/2 - text.get_height()/2)
            )
            
    for smthg in shots:
        for smthg2 in asteroids:
            if smthg.got_hit(smthg2):
                log_event("asteroid_hit");
                Explosion(smthg2.position)
                kill_counter += 1;
                smthg.kill();
                smthg2.kill();        

    font = pygame.font.Font(None, 36)

    text = font.render(f"SCORE: {kill_counter}", True, "white")

    screen.blit(
        text,
        (SCREEN_WIDTH - text.get_width() - 10, 10)
     )
    pygame.display.flip(); #update the display (refresh the screen)
    dt = clock.tick(60)/1000; #the tick method of the clock object is called to limit the frame rate to 60 frames per second. and  can be used to calculate the time elapsed between frames and update game logic accordingly.
    #print(f"dt: {dt:.4f} seconds"); #print the time elapsed between frames in seconds, formatted to four decimal places.
   
   
            
if __name__ == "__main__":
    main()
