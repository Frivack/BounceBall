# 담당: 송현준
# 레벨 디자인 및 스테이지 선택
# TODO: 스테이지 별로 장애물, 아이템 출력

from obstacle import Obstacle
from item import Item

# 스테이지를 관리하는 클래스
class Stage:
    def __init__(self, ball, level_number):
        self.level_number = level_number
        self.obstacles = []
        self.items = []
        self.stage1 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        self.stage2 = [[0, 0, 1, 0, 2, 0, 1, 0, 2, 0, 0, 0, 1, 0, 0, 0, 0],
                       [0, 1, 0, 2, 1, 0, 0, 1, 0, 0, 2, 1, 0, 1, 0, 0, 0],
                       [1, 0, 0, 1, 0, 0, 1, 2, 0, 1, 1, 0, 2, 0, 0, 1, 0],
                       [2, 0, 1, 0, 0, 2, 0, 2, 1, 0, 0, 1, 0, 2, 0, 0, 0],
                       [0, 2, 1, 1, 0, 1, 0, 1, 0, 1, 0, 2, 0, 0, 1, 1, 0],
                       [1, 0, 1, 9, 0, 0, 2, 1, 0, 0, 0, 2, 0, 5, 0, 0, 0],
                       [0, 1, 0, 0, 2, 1, 2, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0],
                       [2, 0, 1, 2, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0],
                       [1, 1, 1, 0, 2, 1, 0, 0, 0, 1, 0, 1, 2, 0, 0, 0, 0],
                       [0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 2, 0, 2, 0, 0, 0],
                       [0, 2, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1],
                       [0, 1, 1, 0, 0, 2, 0, 1, 2, 0, 1, 0, 0, 1, 0, 0, 0]]

        self.stage3 = [[1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0],
                        [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0],
                        [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                        [1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 5, 1, 1],
                        [1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0],
                        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
                        [0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
                        [0, 9, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
                        [1, 0, 2, 2, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 2, 0, 0],
                        [1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
                        [0, 1, 0, 1, 1, 1, 0, 0, 2, 0, 1, 1, 1, 0, 1, 1, 0]]

        self.stage4 =  [[1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 3, 1, 1, 0, 1, 0],
                        [0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1],
                        [1, 1, 0, 0, 1, 0, 1, 0, 3, 1, 1, 2, 0, 1, 0, 0, 0],
                        [1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1],
                        [0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0],
                        [1, 0, 0, 1, 1, 0, 3, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1],
                        [1, 1, 0, 0, 3, 1, 0, 0, 0, 0, 1, 1, 5, 1, 1, 0, 1],
                        [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                        [1, 9, 0, 1, 2, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1],
                        [1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0],
                        [0, 1, 1, 1, 1, 0, 2, 2, 1, 1, 0, 1, 1, 1, 0, 1, 3]]


        if self.level_number == 1:
            self.create_stage(self.stage1, ball)

        elif self.level_number == 2:
            self.create_stage(self.stage2, ball)

        elif self.level_number == 3:
            self.create_stage(self.stage3, ball)

        elif self.level_number == 4:
            self.create_stage(self.stage4, ball)

        # 아이템 예시
        # self.star = Item(x=600, y=300)

    # 연산을 한번에 처리하는 함수
    def update(self, delta_time, ball, ui):
        coli_count = [False, False, False, False] # 좌 상 우 하
        for obstacle in self.obstacles:
            obstacle.update()
            if ball.collision_obstacle(obstacle):
                rect = obstacle.rect

                # 충돌 전과 후의 위치를 사용하여 충돌 축 결정
                # 공의 이동 방향을 기반으로 충돌 축을 판단
                overlap_left = ball.x + ball.radius - rect.left
                overlap_right = rect.right - (ball.x - ball.radius)
                overlap_top = ball.y + ball.radius - rect.top
                overlap_bottom = rect.bottom - (ball.y - ball.radius)

                # 가장 작은 오버랩을 가진 축을 충돌 축으로 선택
                min_overlap = min(overlap_left, overlap_right, overlap_top, overlap_bottom)

                if min_overlap == overlap_left and not coli_count[0]:
                    # 왼쪽 충돌
                    coli_count[0] = True
                    ball.x = rect.left - ball.radius
                    print("왼쪽 충돌")
                elif min_overlap == overlap_right and not coli_count[1]:
                    # 오른쪽 충돌
                    coli_count[1] = True
                    ball.x = rect.right + ball.radius
                    print("오른쪽 충돌")
                elif min_overlap == overlap_top and not coli_count[2]:
                    # 위쪽 충돌
                    coli_count[2] = True
                    ball.y = rect.top - ball.radius
                    ball.apply_collision_y()
                    print("위쪽 충돌")
                elif min_overlap == overlap_bottom and not coli_count[3]:
                    # 아래쪽 충돌
                    coli_count[3] = True
                    ball.y = rect.bottom + ball.radius
                    ball.apply_collision_y()
                    print("아래쪽 충돌")

        for i in self.items:
            i.update(delta_time, ball)
            if i.check_apply():
                self.level_number += 1
                self.reset_stage(ball)
                ui.add_score(50)

        if ball.y > 600:
            self.reset_stage(ball)
            ui.reset_time()
            ui.sub_score(10)

        if ui.t < 0:
            ui.reset_time()
            ui.sub_score(10)
            self.reset_stage(ball)


    # 이미지 출력을 한번에 처리하는 함수
    def draw(self, screen):
        for i in self.obstacles:
            i.draw(screen)
        for i in self.items:
            i.draw(screen)

    def create_stage(self, stage, ball):
        self.obstacles = []
        self.items = []
        for i in range(0,len(stage)):
            for j in range(0,len(stage[i])):
                if stage [i][j]==1:
                    self.obstacles.append(Obstacle(j * 50, i * 50, 50, 50))
                elif stage [i][j]==2:
                    self.obstacles.append(Obstacle(j * 50, i * 50, width=50, height=50, movement_type= "horizontal"))
                elif stage [i][j]==3:
                    self.obstacles.append(Obstacle(j * 50, i * 50, width=50, height=50, movement_type= "vertical"))
                elif stage[i][j] == 5:
                    self.items.append(Item(j * 50, i * 50))
                elif stage[i][j] == 9:
                    ball.x = j * 50
                    ball.y = i * 50


    def reset_stage(self, ball):
        if self.level_number == 1:
            stage = self.stage1

        elif self.level_number == 2:
            stage = self.stage2

        elif self.level_number == 3:
            stage = self.stage3

        elif self.level_number == 4:
            stage = self.stage4
        else:
            stage = self.stage4

        self.create_stage(stage, ball)
