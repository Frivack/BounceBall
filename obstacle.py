# 담당: 이지원
# 장애물
# TODO: 여러 종류의 장애물 생성

import pygame
import random


# 장애물 클래스
class Obstacle:
    def __init__(self, x, y, width, height, color=(0, 255, 0), movement_type="static"):
        # print("Before", self.rect)
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.movement_type = movement_type
        self.speed_x = 0
        self.speed_y = 0

        if movement_type == "vertical":
            self.speed_y = random.randint(2, 4)
        elif movement_type == "horizontal":
            self.speed_x = random.randint(2, 4)

    def update(self):
        if self.movement_type == "vertical":
            self.rect.y += self.speed_y
            if self.rect.top <= 0 or self.rect.bottom >= 600:
                self.speed_y *= -1
        elif self.movement_type == "horizontal":
            self.rect.x += self.speed_x
            if self.rect.left <= 0 or self.rect.right >= 800:
                self.speed_x *= -1

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def get_rect(self):
        return self.rect
