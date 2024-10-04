import pygame 
import sys 
from pygame.locals import * 
import numpy as np 
 
class Card(pygame.sprite.Sprite): 
    def __init__(self, x, y, card_state): 
        self.image = pygame.image.load('C://Users//black//Desktop//期末作業
//14.jpg') 
        self.image = pygame.transform.scale(self.image, (143, 138)) 
        width, height = self.image.get_size() 
        self.rect = (x, y, width, height) 
        self.card_state = card_state 
    def update(self): 
         
        if self.card_state == 2: 
            self.image = pygame.image.load('C://Users//black//Desktop//期末作
業//12.jpg') 
            self.image = pygame.transform.scale(self.image, (143, 138)) 
        if self.card_state == 3: 
            self.image = pygame.image.load('C://Users//black//Desktop//期末作
業//13.jpg') 
            self.image = pygame.transform.scale(self.image, (143, 138)) 
         
   
 
 
 
class Game: 
    def __init__(self): 
        pygame.init() 
        self.screen = pygame.display.set_mode((900, 600)) 
        pygame.display.set_caption("尋找幸運狗狗") 
        self.clock = pygame.time.Clock() 
 
        self.card_nums = 6 
        self.points = self.all_point() 
        self.click_list = [] 
        self.win_list = list(np.random.randint(0, 3, 6)) 
                              
    def set_bg(self): 
        bg = pygame.image.load('C://Users//black//Desktop//期末作業//01.png') 
   
        self.screen.blit(bg, (0, 0))         
 
    def all_point(self): 
        points = [] 
 
        for num in range(3 * 2): 
            if num // 3 == 0: 
                x = num * 300 + 40 
                y = 45 
            elif num // 3 == 1: 
                x = (num - 3) * 300 + 40 
                y = 305 
            points.append((x, y)) 
        return points 
 
    def set_card(self): 
 
        for i, num in enumerate(self.points): 
            x, y = num 
            card_state = 1 
            # 卡片是否被點選 
            if i in self.click_list: 
                card_state = 2 
            if i in self.click_list and self.win_list[i] == 1: 
                card_state = 3     
 
            card = Card(x, y, card_state) 
            card.update() 
            self.screen.blit(card.image, card.rect) 
 
    def run(self): 
 
        while True: 
            self.clock.tick(60) 
            for event in pygame.event.get(): 
                if event.type == QUIT: 
                    pygame.quit() 
                    sys.exit() 
 
                if event.type == MOUSEBUTTONDOWN: 
                    mosx, mosy = event.pos 
                    self.mouse_card(mosx, mosy) 
            self.set_bg() 
            self.set_card() 
 
            pygame.display.update() 
 
    def mouse_card(self, mosx, mosy): 
        for i, (x, y) in enumerate(self.points): 
 
            if (mosx >= x and mosx <= (x + 250)) and (mosy >= y and mosy <= (y + 
250)): 
                print("翻牌座標", i) 
                self.click_list.append(i) 
       
           
if __name__ == '__main__': 
    g = Game() 
    g.run() 