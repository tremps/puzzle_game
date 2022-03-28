import pygame, random, pickle, sys, time
from gen_board import Group, Board
from os.path import exists
from os import system

def get_positions(num, screen):
    ret = []

    width, height = screen.get_size()
    dim = (width // num) - (num*4)
    gap = ((width-(num*dim))/(num+1)) / 2

    for i in range(num):
        ret.append( ( (width*(i/num))+gap, (height//2)-(dim//2), dim, dim ) )
    return ret, dim


def draw_buttons(colors, pos, screen):
    for i in range(len(colors)):
        pygame.draw.rect(screen, colors[i],pos[i])
    
def main():

    red = (200,0,0)
    green = (0,200,0)

    with open(sys.argv[1], 'rb') as file:
        board = pickle.load(file)

    pygame.init()

    if exists('colors.data'):
        system(f'rm colors.data')

    screen = pygame.display.set_mode((400, 400), pygame.RESIZABLE)
    pygame.display.set_caption('Buttons')
    bg_color = [0, 0, 0]

    colors = [red]*board.button_count

    
    # run window
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # time.sleep(0.1)

        # update screen
        pos, dim = get_positions(board.button_count, screen)

        # fill background
        screen.fill(bg_color)

        # click buttons
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if click[0] == 1:
            for i in range(board.button_count):
                p = pos[i]
                if mouse[0] > p[0] and mouse[0] < p[0] + dim and mouse[1] > p[1] and mouse[1] < p[1] + dim:
                    if colors[i] == red:
                        colors[i] = green
                    else:
                        colors[i] = red
            if exists('colors.data'):
                system(f'rm colors.data')
            with open('colors.data', 'wb') as file:
                pickle.dump(colors, file)
            time.sleep(0.25)

        # add buttons
        draw_buttons(colors, pos, screen)

        pygame.display.flip()

    
    # quit pygame after closing window
    pygame.quit()
















if __name__ == '__main__':
    main()