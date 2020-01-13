# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import random


# 随机算法按需修改
def bingo(prize_group):
    random.shuffle(prize_group)
    return random.sample(prize_group, 1)[0]


# 获取奖池列表按需修改
def get_prize_group(*args, **kwargs):
    return [u"张三", u"李四", u"王五"]


# 默认关闭
MARK = False
WINNER = ""
WINNER = ""
TAG = "Start"

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((280, 500), 0, 32)
    pygame.display.set_caption("抽奖机1.0".decode('utf-8'))
    background = pygame.image.load(r"./Image/bg2.jpg").convert()
    font = pygame.font.SysFont("", 40)
    text_surface = font.render(TAG, True, (0, 0, 0))
    prize_font = pygame.font.SysFont("simhei", 40)
    clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            if text_rect.collidepoint(pos):
                # 开关按钮
                MARK = not MARK
                # 修改提示
                TAG = "Over" if MARK else "Start"
                text_surface = font.render(TAG, True, (0, 0, 0))
        elif event.type == pygame.KEYDOWN:
            pass
    # 每一帧产生一个奖品
    if MARK:
        WINNER = bingo(get_prize_group())
    WINNER_surface = prize_font.render(WINNER, True, (0, 0, 0))

    screen.blit(background, (0, 0))
    text_rect = screen.blit(text_surface, (screen.get_width() / 2 - 30, screen.get_height() / 2 + 150))
    # 渲染中奖名单
    screen.blit(WINNER_surface, (screen.get_width() / 2 - 30, screen.get_height() / 2 + 15))
    time_passed = clock.tick(30)
    pygame.display.update()
