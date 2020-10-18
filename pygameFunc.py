class TextBox:
    def __init__ (self, text, x, y , width, fontSize):
        pygame.sprite.Sprite.__init__(self)
        self.text = ""
        self.width = width
        self.initialText = text
        self.maxLength = maxLength
        self.boxSize = int(fontSize * 1.7)
        self.image = pygame.Surface((width, self.boxSize))
        self.image.fill((255, 255, 255))
        pygame.draw.rect(self.image, (0, 0, 0), [0, 0, width - 1, self.boxSize - 1], 2)
        self.rect = self.image.get_rect()
        self.fontFace = pygame.font.match_font("Arial")
        self.fontColour = pygame.Color("black")
        self.initialColour = (180, 180, 180)
        self.font = pygame.font.Font(self.fontFace, fontSize)
        self.rect.topleft = [xpos, ypos]
        newSurface = self.font.render(self.initialText, True, self.initialColour)
        self.image.blit(newSurface, [10, 5])
