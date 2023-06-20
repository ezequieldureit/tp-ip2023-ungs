class Button():
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text_surface = self.font.render(self.text_input, True, self.base_color)
        self.update_text()

        if self.image is None:
            self.image = self.text_surface
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text_surface, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text_surface = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text_surface = self.font.render(self.text_input, True, self.base_color)

    def update_text(self):
        self.text_surface = self.font.render(self.text_input, True, self.base_color)
        self.text_rect = self.text_surface.get_rect(center=(self.x_pos, self.y_pos))
