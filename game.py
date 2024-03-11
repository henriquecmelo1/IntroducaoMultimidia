import pygame, random
from audio import get_microphone_frequency
from time import sleep
 
WIDTH = 1200
HEIGHT = 600
SPEED = 10
GAME_SPEED = 10
GROUND_WIDTH = 2 * WIDTH
GROUND_HEIGHT = 30

button_img = pygame.image.load('sprites/coin.png')
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_run = [pygame.image.load('sprites/Run__000.png').convert_alpha(),
                          pygame.image.load('sprites/Run__001.png').convert_alpha(),
                          pygame.image.load('sprites/Run__002.png').convert_alpha(),
                          pygame.image.load('sprites/Run__003.png').convert_alpha(),
                          pygame.image.load('sprites/Run__004.png').convert_alpha(),
                          pygame.image.load('sprites/Run__005.png').convert_alpha(),
                          pygame.image.load('sprites/Run__006.png').convert_alpha(),
                          pygame.image.load('sprites/Run__007.png').convert_alpha(),
                          pygame.image.load('sprites/Run__008.png').convert_alpha(),
                          pygame.image.load('sprites/Run__009.png').convert_alpha(),
                          ]
        self.image_fall = pygame.image.load('sprites/Fall.png').convert_alpha()
        self.image = pygame.image.load('sprites/Run__000.png').convert_alpha()
        self.rect = pygame.Rect(100, 100, 100, 100)
        self.mask = pygame.mask.from_surface(self.image)
        self.current_image = 0
 
 
    def update(self, *args):
        def move_player(self):
            key = pygame.key.get_pressed()
            self.current_image = (self.current_image + 1) % 10
            self.image = self.image_run[self.current_image]
            self.image = pygame.transform.scale(self.image,[100, 100])
        move_player(self)
 
        def move(self):
            var = get_microphone_frequency()
            var = var * 1000
            if var < 5:
                self.image = self.image_fall
                self.rect[1] += 30
                if pygame.sprite.groupcollide(playerGroup, groundGroup, False, False):
                    self.rect[1] = HEIGHT - GROUND_HEIGHT - 100
            else:
                self.rect[1] -= 30
                if self.rect[1] < 0:
                    self.rect[1] = 0
            print(var)
            sleep(0.03)
            self.image = pygame.transform.scale(self.image,[100, 100])
        move(self)
 
 
class Ground(pygame.sprite.Sprite):
    def __init__(self, xpos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('sprites/ground.png').convert_alpha()
        self.image = pygame.transform.scale(self.image,(GROUND_WIDTH, GROUND_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect[0] = xpos
        self.rect[1] = HEIGHT - GROUND_HEIGHT
 
    def update(self, *args):
        self.rect[0] -= GAME_SPEED
 
class Obstacles(pygame.sprite.Sprite):
    def __init__(self, xpos, ysize):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('sprites/Box.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, [100, 100])
        self.rect = pygame.Rect(100, 100, 100, 100)
        self.rect[0] = xpos
        self.mask = pygame.mask.from_surface(self.image)
        self.rect[1] = HEIGHT - ysize
 
    def update(self, *args):
        self.rect[0] -= GAME_SPEED
 
class Coins(pygame.sprite.Sprite):
    def __init__(self, xpos, ysize):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('sprites/coin.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, [40, 40])
        self.rect = pygame.Rect(100, 100, 20, 20)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect[0] = xpos
        self.rect[1] = HEIGHT - ysize
 
    def update(self, *args):
        self.rect[0] -= GAME_SPEED

class Button():
	def __init__(self, x, y, image):
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)

	def draw(self):
		action = False

		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1:
				action = True

		#draw button
		game_window.blit(self.image, (self.rect.x, self.rect.y))

		return action
    
button = Button((WIDTH // 2) - 60, HEIGHT // 2, button_img)

def reset_game():
    global placar, GAME_SPEED, playerGroup, groundGroup, coinsGroup, obstacleGroup, gameover

    # Reset score and game speed
    placar = 0
    GAME_SPEED = 10

    # Recreate the player group and player instance
    playerGroup = pygame.sprite.Group()
    player = Player()
    playerGroup.add(player)

    # Recreate the ground group with initial ground positions
    groundGroup = pygame.sprite.Group()
    for i in range(2):
        ground = Ground(WIDTH * i)
        groundGroup.add(ground)

    # Recreate the coins group with initial positions
    coinsGroup = pygame.sprite.Group()
    for i in range(2):
        coin = get_random_coins(WIDTH * i + 1000)
        coinsGroup.add(coin)

    # Recreate the obstacle group with initial positions
    obstacleGroup = pygame.sprite.Group()
    for i in range(2):
        obstacle = get_random_obstacles(WIDTH * i + 1000)
        obstacleGroup.add(obstacle)

    # Reset the gameover flag to restart the game loop
    gameover = False

    gameloop()

    # Return the initial game state if needed
    return True  # You can customize this part based on your needs


def get_random_obstacles(xpos):
    size = random.randint(120, 600)
    box = Obstacles(xpos, size)
    return box
 
def get_random_coins(xpos):
    size = random.randint(60, 500)
    coin = Coins(xpos, size)
    return coin
 
def is_off_screen(sprite):
    return sprite.rect[0] < -(sprite.rect[2])
 
pygame.init()
game_window = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Jogo 01')
 
BACKGROUND = pygame.image.load('sprites/background_03.jpg')
BACKGROUND = pygame.transform.scale(BACKGROUND,[WIDTH, HEIGHT])
 
playerGroup = pygame.sprite.Group()
player = Player()
playerGroup.add(player)
 
groundGroup = pygame.sprite.Group()
for i in range(2):
    ground = Ground(WIDTH * i)
    groundGroup.add(ground)
 
coinsGroup = pygame.sprite.Group()
for i in range(2):
    coin = get_random_coins(WIDTH * i + 1000)
    coinsGroup.add(coin)
 
obstacleGroup = pygame.sprite.Group()
for i in range(2):
    obstacle = get_random_obstacles(WIDTH * i + 1000)
    obstacleGroup.add(obstacle)
 
gameover = False
def draw():
    playerGroup.draw(game_window)
    groundGroup.draw(game_window)
    obstacleGroup.draw(game_window)
    coinsGroup.draw(game_window)
def update():
    groundGroup.update()
    playerGroup.update()
    obstacleGroup.update()
    coinsGroup.update()
clock = pygame.time.Clock()


 
def rodando(placar):
        game_window.blit(BACKGROUND, (0, 0))
        font = pygame.font.SysFont('Arial',30)
        text = font.render('Placar', True, [255,255,255])
        game_window.blit(text, [1100, 20])
        contador = font.render(f'{placar}', True, [255,255,255])
        game_window.blit(contador, [1125, 50])
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break
    
        if is_off_screen(groundGroup.sprites()[0]):
            groundGroup.remove(groundGroup.sprites()[0])
            newGround = Ground(WIDTH - 40)
            groundGroup.add(newGround)
    
        if is_off_screen(obstacleGroup.sprites()[0]):
            obstacleGroup.remove(obstacleGroup.sprites()[0])
            newObstacle = get_random_obstacles(WIDTH * 1.5)
            obstacleGroup.add(newObstacle)
            newCoin = get_random_coins(WIDTH * 2)
            newCoin1 = get_random_coins(WIDTH * 2.2)
            newCoin2 = get_random_coins(WIDTH * 2.4)
            newCoin3 = get_random_coins(WIDTH * 2.6)
            newCoin4 = get_random_coins(WIDTH * 2.8)
            coinsGroup.add(newCoin)
            coinsGroup.add(newCoin1)
            coinsGroup.add(newCoin2)
            coinsGroup.add(newCoin3)
            coinsGroup.add(newCoin4)
    
        if pygame.sprite.groupcollide(playerGroup, groundGroup, False, False):
            SPEED = 0
            print('collision')
        else:
            SPEED = 10
    
        if pygame.sprite.groupcollide(playerGroup, coinsGroup, False, True):
            placar += 1
    
        if placar % 5 == 0 and placar != 0:
            GAME_SPEED += 0.02
            print('GAMESPEED ALTERADA')
    
        if pygame.sprite.groupcollide(playerGroup, obstacleGroup, False, False):
            return True
        update()
        draw()
        pygame.display.update()

def gameloop(placar=0):
    while True:
        gameover = rodando(placar)
        if gameover:
            break
    reset_game()
reset_game()




