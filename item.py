# 아이템
# TODO: 아이템 만들고 효과 적용하거나 넘겨주기

import pygame


# 아이템 효과 등을 담당하는 클래스
class Item:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.collected = False
        self.radius = 10
        self.apply = False

        # 이미지 불러오는 예시
        # self.example_image = pygame.image.load("example_img.png")  # 'star.png' 파일 경로에 맞게 변경
        # self.example_image = pygame.transform.scale(self.example_image, (50, 50))  # 크기 조정 (필요시)

    # 연산을 한번에 처리하는 함수
    def update(self, delta_time, player):
        if not self.collected:
            # 플레이어와의 거리 계산
            distance = ((self.x - player.x) ** 2 + (self.y - player.y) ** 2) ** 0.5
            if distance <= self.radius + player.radius:
                self.collected = True  # 아이템 수집 상태 변경
                self.apply_effect()  # 아이템 효과 발동

    # 이미지 출력을 한번에 처리하는 함수
    def draw(self, screen):
        if not self.collected:
            # 원 그리기 예시
            pygame.draw.circle(screen, (255, 255, 0), (self.x, self.y), self.radius)

            # 이미지 출력 예시
            # screen.blit(self.example_image, (100, 300))

    def apply_effect(self):
        self.apply = True

    def check_apply(self):
        return self.apply
