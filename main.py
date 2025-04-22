import pygame
from ball import Ball
from stage import Stage
from ui import GameUI, Score

# Pygame 초기화
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

# 게임 오브젝트 생성
ball = Ball(x=400, y=300, radius=15)
stage = Stage(ball, level_number=1)
score = Score()
ui = GameUI()
FPS = 60

# 게임 루프
while running:
    screen.fill((0, 0, 0))  # 배경색
    delta_time = clock.tick(FPS) / 1000.0

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 연산 처리하기
    ball.update(delta_time)
    stage.update(delta_time, ball, ui)
    score.update(delta_time)
    ui.update(delta_time)

    # 화면에 그리기
    ball.draw(screen)
    stage.draw(screen)
    ui.draw(screen)

    # 프레임 조정 및 업데이트
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
