import pygame, random, pickle
from os.path import exists
from os import system
import sys

class Group:
    def __init__(self, t):
        self.tiles = t

def make_partition(tiles, count):

    base = tiles[:count]
    fill = tiles[count:]

    partitions = []

    for t in base:
        partitions.append(Group([t]))
    
    for t in fill:
        index = random.randint(0,count-1)
        partitions[index].tiles.append(t)
    
    return partitions


class Board:
    def __init__(self, dim, button_count):

        self.dim = dim
        self.button_count = button_count
        
        # make 2 copies of tiles so board fills twice
        real_tiles = []
        for i in range(dim):
            for j in range(dim):
                real_tiles.append((i,j))
        fake_tiles = list(real_tiles)

        random.shuffle(real_tiles)
        random.shuffle(fake_tiles)
        fake_tiles = fake_tiles[:-2]

        real_button_count = (button_count // 2) + 1 - random.randint(0,2)
        fake_button_count = button_count - real_button_count

        real_group = make_partition(real_tiles, real_button_count)
        fake_group = make_partition(fake_tiles, fake_button_count)

        self.groups = real_group + fake_group
        random.shuffle(self.groups)





if __name__ == '__main__':

    dim = int(sys.argv[1])
    bc = int(sys.argv[2])

    board = Board(dim,bc)

    for g in board.groups:
        print(g.tiles)
    

    name = f'{dim},{bc}.board'

    if exists(name):
        system(f'rm {name}')
    with open(name, 'wb') as file:
        pickle.dump(board,file)


