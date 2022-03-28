import pygame, random, pickle, sys, time
from gen_board import Group, Board
from os.path import exists

red = (200,0,0)
green = (0,200,0)
yellow = (200,200,0)
bg_color = [0, 0, 0]

def win(screen):
    width, height = screen.get_size()
    time.sleep(1)

    img = pygame.image.load('win.png')
    # imgrect = img.get_rect()

    iWidth = img.get_width()
    iHeight = img.get_height()

    screen.fill(bg_color)

    x = (width - iWidth) // 2
    y = (height - iHeight) // 2

    screen.blit(img, (x,y))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)






def get_positions(num, screen):
    ret = [[None for _ in range(num)] for _ in range(num)]

    width, height = screen.get_size()
    dim = min(width, height)
    dim = (dim // num) - (num*4)
    gap = ((min(width, height)-(num*dim))/(num+1)) / 2

    for j in range(num):
        for i in range(num):
            ret[i][j] = ( (width*(i/num))+gap, (height*(j/num))+gap, dim, dim )
    return ret, dim


def draw_tiles(board, colors, pos, screen):
    num_green = 0
    for j in range(board.dim):
        for i in range(board.dim):
            count = 0
            for x in range(len(colors)):
                if colors[x] == green:
                    for t in board.groups[x].tiles:
                        if t[0] == i and t[1] == j:
                            count += 1
            if count == 0:
                c = yellow
            elif count == 1:
                c = green
                num_green +=1
            elif count == 2:
                c = red
            else:
                print('BAD COUNT')
                exit(1)

            pygame.draw.rect(screen, c ,pos[i][j])
    if num_green == board.dim**2:
        return True
    else:
        return False
    
def main():


    with open(sys.argv[1], 'rb') as file:
        board = pickle.load(file)


    # testing
    # for g in board.groups:
    #     print(g.tiles)

    pygame.init()

    screen = pygame.display.set_mode((400, 400), pygame.RESIZABLE)
    pygame.display.set_caption('Tiles')

    colors = [red]*board.button_count

    
    # run window
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        

        # time.sleep(0.1)

        # update screen
        pos, dim = get_positions(board.dim, screen)

        try:
            with open('colors.data', 'rb') as file:
                colors = pickle.load(file)
        except:
            pass


        # fill background
        screen.fill(bg_color)

        # add tiles
        if draw_tiles(board, colors, pos, screen):
            pygame.display.flip()
            win(screen)

        pygame.display.flip()

    
    # quit pygame after closing window
    pygame.quit()
















if __name__ == '__main__':
    main()