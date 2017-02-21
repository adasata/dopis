import pygame


class BasicMenu:
    def __init__(self,
                 x,
                 y,
                 bar_width,
                 bar_height,
                 options,
                 color_unaimed,
                 color_script,
                 color_aimed=None,
                 color_script_aimed=None,
                 color_clicked=None,
                 color_script_clicked=None,
                 edge_width=(1/10),
                 font_address="./fonts/risaltyp.ttf"):
        self.x = x
        self.y = y
        self.pos = [x, y]
        self.bar_width = bar_width
        self.bar_height = bar_height
        self.options = options
        self.font_address = font_address

        self.colors = {'unaimed':color_unaimed,
                       'script unaimed':color_script}

        if color_aimed is not None: self.colors['aimed'] = color_aimed
        else: self.colors['aimed'] = self.colors['unaimed']

        if color_clicked is not None: self.colors['clicked'] = color_clicked
        else: self.colors['clicked'] = self.colors['unaimed']

        if color_script_aimed is not None: self.colors['script aimed'] = color_script_aimed
        else: self.colors['script aimed'] = self.colors['script']

        if color_script_clicked is not None: self.colors['script clicked'] = color_script_clicked
        else: self.colors['script clicked'] = self.colors['script']

        self.aimed_option = -1
        self.visible = True
        self.clicked = False
        self.edge_width_k = edge_width

    def set_visibility(self, vis): self.visible = vis

    def get_option(self, index): return self.options[index]

    def set_aimed_option(self, value=None, clicked=None):
        if value is not None: self.aimed_option = value
        if clicked is not None: self.clicked = clicked

    def get_option_poss(self):
        return [[self.x, self.y + i*self.bar_height, self.x + self.bar_width, self.y + (i+1)*self.bar_height] for i in range(len(self.options))]

    def move(self, x, y):
        self.x = x
        self.y = y
        self.pos = [x, y]

    def draw(self, surface):
        if self.visible:
            for i in range(len(self.options)):
                pos = [self.x,
                       self.y + i*self.bar_height,
                       self.bar_width,
                       self.bar_height]

                if self.aimed_option == i:
                    if self.clicked:
                        color = self.colors['clicked']
                        scolor = self.colors['script clicked']
                    else:
                        color = self.colors['aimed']
                        scolor = self.colors['script aimed']
                else:
                    color = self.colors['unaimed']
                    scolor = self.colors['script unaimed']

                pygame.draw.rect(surface, color, pos)
                if self.aimed_option == i:
                    w = int(self.bar_height * self.edge_width_k)
                    pygame.draw.rect(surface, scolor,
                                     [self.x + w, self.y + i*self.bar_height + w, self.bar_width - 2*w, self.bar_height - 2*w],
                                     w)

                size = int(3 * self.bar_height / 5)
                font = pygame.font.Font(self.font_address, size)
                surf = font.render(self.options[i], 0, scolor)

                x = self.x + ((self.bar_width - surf.get_width()) / 2)
                y = self.y + (i*self.bar_height) + int(self.bar_height / 5)
                surface.blit(surf, [x, y])
