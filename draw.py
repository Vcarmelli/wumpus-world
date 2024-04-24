import pygame as pg

space = 90
mg_x = 90
mg_y = 150

AQUA = (49, 255, 255)
WHITE = (255, 255, 255)
GREEN = (67, 83, 24)
LIGHT_GREEN = (194, 203, 159)
BLUE = (6, 61, 81)

WORLD_SIZE = 4

class Draw:
    def __init__(self, screen):
        self.screen = screen
        

    def board(self):
        pg.draw.rect(self.screen, LIGHT_GREEN, pg.Rect(mg_x, mg_y, 360, 360), 7)

        i = 1
        while (i * space) < 360:
            line_width = 3 
            pg.draw.line(self.screen, LIGHT_GREEN, (mg_x, mg_y + i * space), (mg_x + 350, mg_y + i * space), line_width)
            pg.draw.line(self.screen, LIGHT_GREEN, (mg_x + i * space, mg_y), (mg_x + i * space, mg_y + 350), line_width)
            i += 1

    def fill_path(self, row, col):
        x = mg_x + col * space +10
        y = mg_y + row * space +20
        
        agent_img = pg.image.load("assets/agent.png")
        
        self.screen.blit(agent_img, (x, y))

    def environment(self, world):
        breeze_img = pg.image.load("assets/cell_breeze.png")
        breeze_stench_img = pg.image.load("assets/cell_breeze-stench.png")
        gold_img = pg.image.load("assets/cell_gold.png")
        pit_img = pg.image.load("assets/cell_pit.png")
        stench_img = pg.image.load("assets/cell_stench.png")
        wumpus_img = pg.image.load("assets/cell_wumpus.png")

        for row in range(WORLD_SIZE):
            for col in range(WORLD_SIZE):
                cell_type = world[row][col]

                x = mg_x + col * space
                y = mg_y + row * space

                if cell_type == 'B':
                    self.screen.blit(breeze_img, (x, y))
                elif cell_type == 'BS':
                    self.screen.blit(breeze_stench_img, (x, y))
                elif cell_type == 'G' or cell_type == 'BG'  or cell_type == 'GS' or cell_type == 'BGS':
                    self.screen.blit(gold_img, (x, y))
                elif cell_type == 'P' or cell_type == 'BP' or cell_type == 'PS' or cell_type == 'BPS':
                    self.screen.blit(pit_img, (x, y))
                elif cell_type == 'S':
                    self.screen.blit(stench_img, (x, y))
                elif cell_type == 'W' or cell_type == 'BW':
                    self.screen.blit(wumpus_img, (x, y))

    def fill_environment(self, row, col, world):
        breeze_img = pg.image.load("assets/cell_breeze.png")
        breeze_stench_img = pg.image.load("assets/cell_breeze-stench.png")
        gold_img = pg.image.load("assets/cell_gold.png")
        pit_img = pg.image.load("assets/cell_pit.png")
        stench_img = pg.image.load("assets/cell_stench.png")
        wumpus_img = pg.image.load("assets/cell_wumpus.png")

        cell_type = world[row][col]

        x = mg_x + col * space
        y = mg_y + row * space

        if cell_type == 'B':
            self.screen.blit(breeze_img, (x, y))
        elif cell_type == 'BS':
            self.screen.blit(breeze_stench_img, (x, y))
        elif cell_type == 'G' or cell_type == 'BG'  or cell_type == 'GS' or cell_type == 'BGS':
            self.screen.blit(gold_img, (x, y))
        elif cell_type == 'P' or cell_type == 'BP' or cell_type == 'PS' or cell_type == 'BPS':
            self.screen.blit(pit_img, (x, y))
        elif cell_type == 'S':
            self.screen.blit(stench_img, (x, y))
        elif cell_type == 'W' or cell_type == 'BW':
            self.screen.blit(wumpus_img, (x, y))
                    

        