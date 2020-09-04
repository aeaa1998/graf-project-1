from lib import *
from Renderer import *
from random import randint
grassTxt = Texture('./models/grass_txt.bmp')
grass_colors = [color(79, 121, 66), color(86,125,70)]
def twoColors(color1, color2, percentage):
    return color1 + (color2 - color1) * percentage

def skyShader(width, height, x, y):
    percentageWidth = (x + (height - y))/(width + height)
    return color(twoColors(0, 15, percentageWidth), twoColors(0, 37, percentageWidth), twoColors(0, 39, percentageWidth))

def grassShader(width, height, x, y):
    return grass_colors[randint(0,2)]


def half_down_condition(width, height, x, y):
    return y/height <= 0.4
