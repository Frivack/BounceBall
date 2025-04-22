# UI
# TODO: 스코어 업데이트하고, 필요한 텍스트 출력

import pygame
import time

# 스코어 계산 및 관리하는 클래스
class Score:
    def __init__(self):
        self.score = 0

    # 기본적으로 1씩 증가하도록 설정
    def update(self, delta_time):
        self.increase_score(1)

    # 점수를 증가시키는 함수
    def increase_score(self, amount):
        self.score += amount

    # 현재 점수를 반환하는 함수
    def get_score(self):
        return self.score

class GameUI:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)
        self.t = 31
        self.tc = time.time() + self.t
        self.score = 0
    # 연산을 한번에 처리하는 함수
    def update(self, delta_time):
       self.t=self.tc - time.time()

    # 텍스트 출력을 한번에 처리하는 함수
    def draw(self, screen):
        self.example_display(screen)
        self.display_timer(screen,self.t)

    def example_display(self, screen):
        # score_text에 (글자, 안티엘리어스, 색상)을 지정
        score_text = self.font.render(f"SCORE: {self.score}", True, (255, 255, 255))
        # score_text를 출력
        screen.blit(score_text, (10, 10))

    def display_score(self, screen):
        score_text = self.font.render(f"SCORE: {self.score}",
                                      True, (255, 255, 255))
        # score_text를 출력
        screen.blit(score_text, (15, 15))

    def display_timer(self, screen, time_left):
        time_left_text = self.font.render(f"TIME: "
                                          f"{(int)(time_left)}",
                                          True,
                                          (255, 255, 255))
        screen.blit(time_left_text, (10, 30))

    def add_score(self, score):
        self.score += score

    def sub_score(self, score):
        self.score -= score

    def reset_time(self):
        self.t = 31
        self.tc = time.time() + self.t
