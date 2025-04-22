# 물리 처리 + 애니메이션
# TODO: 공의 물리 처리 및 다른 오브젝트와 충돌 처리/상호작용
# TODO: 입력 받고 공의 움직임 처리

import pygame

# 공 클래스
class Ball:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.velocity = 0
        self.gravity = 0.98  # 중력

    def apply_physics(self):
        self.velocity += self.gravity
        self.y += self.velocity

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (int(self.x), int(self.y)), self.radius)

    def update(self, delta_time):
        self.apply_physics()
        self.keyboard_input()

    def get_center(self):
        return self.x, self.y

    # 입력을 통해 공을 조종
    def control_ball(self):
        self.velocity = -self.velocity

    # 장애물과 충돌 처리하고, 효과가 있다면 적용
    def collision_obstacle(self, obstacle):
        rect = obstacle.get_rect()  # obstacle에서 rect 정보 가져오기
        closest_x = max(rect.x, min(self.x, rect.x + rect.width))
        closest_y = max(rect.y, min(self.y, rect.y + rect.height))

        # 원의 중심과 직사각형의 가장 가까운 점 사이의 거리 계산
        distance_x = self.x - closest_x
        distance_y = self.y - closest_y
        distance_squared = distance_x ** 2 + distance_y ** 2

        # 충돌 여부 반환
        return distance_squared <= self.radius ** 2

    def apply_collision_y(self):
        if self.velocity >= 0:
            self.velocity = -13
        elif self.velocity < 0:
            self.velocity = 0.5

    # 아이템과 충돌 처리하고, 효과가 있다면 적용
    def collision_item(self, item):
        pass

    # 별과 충돌 처리하고, 효과가 있다면 적용
    def collision_star(self, star):
        pass

    def keyboard_input(self):
        keys = pygame.key.get_pressed()
        speed = 3.5  # 이동 속도

        if keys[pygame.K_a]:  # 왼쪽 키
            self.x -= speed
        if keys[pygame.K_d]:  # 오른쪽 키
            self.x += speed