import pygame
import Objects as obj

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

WIDTH, HEIGHT = 1280, 640

class World:
    def __init__(self, scale:float):
        # init
        pygame.init() 
        pygame.display.set_caption("Phys Simulation")  # set window caption
        self.clock = pygame.time.Clock() # set clock depending on fps
        self.FPS = 120 
        self.WINDOW = pygame.display.set_mode((WIDTH, HEIGHT)) # create my window surface 
        self.scale = scale # scale is dist per pixel

    def main(self):
        lune = obj.MecaPt([((WIDTH/2)*self.scale)-384400000, (HEIGHT/2)*self.scale], 7.437*10**(22))
        obj.objects.append(lune)

        terre = obj.Planet([(WIDTH/2)*self.scale, (HEIGHT/2)*self.scale], 5.9*10**(24), color=BLUE)
        obj.objects.append(terre)

        menu = True
        # Create menu loop
        while menu:
            self.clock.tick(self.FPS)
            self.WINDOW.fill([0, 0, 0])
            mousepos = pygame.mouse.get_pos()

            for objec in obj.objects:
                objec.update()
                pygame.draw.circle(self.WINDOW, objec.color, objec.coords/self.scale, round(objec.radius/self.scale, 0))
                print(objec.coords/self.scale)


            # Listen for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    menu = False
            pygame.display.update()

if __name__ == "__main__":
    MyWorld = World(3*384400000/HEIGHT) # trois fois distance terre lune / height
    MyWorld.main()
