import sys,pygame

# snake class(player)
class Snake(pygame.sprite.Sprite):
    def __init__(self, vector):
        pygame.sprite.Sprite.__init__(self)
    
    def update():
        pass


class Apple(pygame.sprite.Sprite):
    def __init__(self, vector):
        pass


def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('Snake')
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill("green")


    screen.blit(background, (0, 0))
    pygame.display.flip()

  

    while True:
        for event in pygame.event.get():
            if event.type == quit:
                return
            

        screen.blit(background, (0,0))
        pygame.display.flip()

    
if __name__ == '__main__':
    main()


