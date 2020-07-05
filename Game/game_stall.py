# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 08:28:03 2020

@author: plus
"""
import pgzrun
from PIL import Image
import time
#from pgzero.builtins import *

bkg = Image.open(".\\images\\1_p大东门.jpg")
w,h = bkg.size
WIDTH,HEIGHT = w,h

scene = Actor('1_p大东门')

button_game_st = Actor('sponge')
button_choose_scene = Actor('bt')
button_choose_goods = Actor('bt')
button_close_scene = Actor('bt')
button_close_goods = Actor('bt')
button_start_business = Actor('bt')
g_shell = Actor()
s_shell = Actor()



button_game_st.pos = w*3/4, h*3/4
button_choose_scene.pos = w*3/4,h*3/5
button_choose_goods.pos = w*3/4,h*4/5
button_start_business.pos = w/2,h/2
#button_close_scene.pos = s_shell.topright
#button_close_goods.pos = g_shell.top_right

is_game_st = False
is_home = True
is_menu = False
is_open_scene = False
is_open_goods = False
is_business_st = False
is_stall = False

#goods are stored in the form of {"name":(Actor("image",bool-taken-or-not)}
goods = {}   
scenes = {}
cur_scene = '1_p大东门'


def show_scene_list():
    pass
def show_godds_list():
    pass
def show_stall():
    pass


def draw():
    global is_game_st
    global is_home
    global is_menu
    global is_open_scene
    global is_open_goods
    global is_business_st
    
    screen.clear()
    scene.draw()
    if is_home:
        button_game_st.draw()
    
    if is_menu :
        button_choose_scene.draw()
        button_choose_goods.draw()
        button_start_business.draw()
        
    if is_open_scene:
        s_shell.draw()
        show_scene_list()
        button_close_scene.draw()

    if is_open_goods:
        g_shell.draw()
        show_goods_list()
        button_close_goods.draw()

    if is_business_st:
        show_stall()
        
def update():
    global is_game_st
    global is_home
    global is_menu
    global is_stall

    if is_game_st :
        scene.image = '5'
        is_game_st = False
        is_home = False
        is_menu = True
    
    if is_stall:
        scene.image = cur_scene
        

def on_mouse_down(pos):
    global is_game_st
    global is_open_scene
    global is_open_goods
    global is_business_st
    
    if button_game_st.collidepoint(pos):
        is_game_st = True
        
    if button_choose_scene.collidepoint(pos):
        is_open_scene = True
    
    if button_choose_goods.collidepoint(pos):    
        is_open_goods = True

    if button_close_scene.collidepoint(pos):
        is_open_scene = False
    
    if button_close_scene.collidepoint(pos):
        is_open_scene = False

    if button_start_business.collidepoint(pos):
        is_business_st = True
    
    
def on_key_down(key):
    pass



pgzrun.go()

