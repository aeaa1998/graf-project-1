from Renderer import *
from shaders import *

r = Render(1000, 1000)

r.light = V3(1, 0, 0.4)


r.lookAt(V3(1, 0, 1), V3(0, 0, 0), V3(0, 1, 0))

# Load bg
r.shade_canvas(skyShader)
r.shade_canvas_conditioned(grassShader,  half_down_condition)


# Load grass
grass_colors = [Color(126, 200, 80), Color(79, 121, 66)]
grass_range =range(8)
grass_offset = 0.45
for i in grass_range:
    r.set_color(grass_colors[i % 2])
    grassSize = 1.05
    r.load('./models/grass.obj', translate=(0 - i * grass_offset, -0.7, 0.8), scale=(grassSize - 0.07 * i, grassSize - 0.07 * i, grassSize - 0.07 * i), rotate=(0, 0, 0))
    r.draw_arrays('TRIANGLES')
for i in grass_range:
    r.set_color(grass_colors[i % 2])
    grassSize = 1.1
    r.load('./models/grass.obj', translate=(0 - i * grass_offset, -0.75, 0.7), scale=(grassSize - 0.07 * i, grassSize - 0.07 * i, grassSize - 0.07 * i), rotate=(0, 0, 0))
    r.draw_arrays('TRIANGLES')
for i in grass_range:
    r.set_color(grass_colors[i % 2])
    grassSize = 1.25
    r.load('./models/grass.obj', translate=(0 - i * grass_offset, -0.85, 0.5), scale=(grassSize - 0.07 * i, grassSize - 0.07 * i, grassSize - 0.07 * i), rotate=(0, 0, 0))
    r.draw_arrays('TRIANGLES')
for i in grass_range:
    r.set_color(grass_colors[i % 2])
    grassSize = 1.3
    r.load('./models/grass.obj', translate=(0 - i * grass_offset, -0.95, 0.3), scale=(grassSize - 0.07 * i, grassSize - 0.07 * i, grassSize - 0.07 * i), rotate=(0, 0, 0))
    r.draw_arrays('TRIANGLES')
for i in grass_range:
    r.set_color(grass_colors[i % 2])
    grassSize = 1.45
    r.load('./models/grass.obj', translate=(0 - i * grass_offset, -1.05, 0.1), scale=(grassSize - 0.07 * i, grassSize - 0.07 * i, grassSize - 0.07 * i), rotate=(0, 0, 0))
    r.draw_arrays('TRIANGLES')
for i in grass_range:
    r.set_color(grass_colors[i % 2])
    grassSize = 1.65
    r.load('./models/grass.obj', translate=(0 - i * grass_offset, -1.15, -0.3), scale=(grassSize - 0.07 * i, grassSize - 0.07 * i, grassSize - 0.07 * i), rotate=(0, 0, 0))
    r.draw_arrays('TRIANGLES')
for i in grass_range:
    r.set_color(grass_colors[i % 2])
    grassSize = 1.8
    r.load('./models/grass.obj', translate=(0 - i * grass_offset, -1.25, -0.5), scale=(grassSize - 0.07 * i, grassSize - 0.07 * i, grassSize - 0.07 * i), rotate=(0, 0, 0))
    r.draw_arrays('TRIANGLES')
for i in grass_range:
    r.set_color(grass_colors[i % 2])
    grassSize = 2
    r.load('./models/grass.obj', translate=(0 - i * grass_offset, -1.45, -0.9), scale=(grassSize - 0.07 * i, grassSize - 0.07 * i, grassSize - 0.07 * i), rotate=(0, 0, 0))
    r.draw_arrays('TRIANGLES')
for i in grass_range:
    r.set_color(grass_colors[i % 2])
    grassSize = 2.7
    r.load('./models/grass.obj', translate=(0 - i * grass_offset, -1.85, -1.7), scale=(grassSize - 0.07 * i, grassSize - 0.07 * i, grassSize - 0.07 * i), rotate=(0, 0, 0))
    r.draw_arrays('TRIANGLES')
for i in grass_range:
    r.set_color(grass_colors[i % 2])
    grassSize = 3.5
    r.load('./models/grass.obj', translate=(0 - i * grass_offset, -2.45, -2.8), scale=(grassSize - 0.07 * i, grassSize - 0.07 * i, grassSize - 0.07 * i), rotate=(0, 0, 0))
    r.draw_arrays('TRIANGLES')
for i in grass_range:
    r.set_color(grass_colors[i % 2])
    grassSize = 4
    r.load('./models/grass.obj', translate=(0 - i * grass_offset, -2.55, -3.5), scale=(grassSize - 0.07 * i, grassSize - 0.07 * i, grassSize - 0.07 * i), rotate=(0, 0, 0))
    r.draw_arrays('TRIANGLES')
for i in grass_range:
    r.set_color(grass_colors[i % 2])
    grassSize = 4.5
    r.load('./models/grass.obj', translate=(0 - i * grass_offset, -2.7, -4.5), scale=(grassSize - 0.07 * i, grassSize - 0.07 * i, grassSize - 0.07 * i), rotate=(0, 0, 0))
    r.draw_arrays('TRIANGLES')
#
# for i in range(7):
#     r.set_color(grass_colors[i % 2])
#     r.load('./models/grass.obj', translate=(0 - i * 0.15, -2.7, -3.5), scale=(3.9, 3.9, 3.9), rotate=(0, 0, 0))
#     r.draw_arrays('TRIANGLES')

#
# Cub bear
bear_texture = Texture('./models/clear_texture.bmp')
r.set_texture(bear_texture)
r.load('./models/bear.obj', translate=(-0.3, -1, 0), scale=(0.2, 0.2, 0.2), rotate=(0, 1.2, 0))
r.draw_arrays('TRIANGLES')
#Cub bear 2
#
r.load('./models/bear.obj', translate=(-0.2, -0.8, 0.4), scale=(0.15, 0.15, 0.15), rotate=(0, 1, 0))
r.draw_arrays('TRIANGLES')
#Father bear
bear_texture = Texture('./models/bearTxt.bmp')
r.set_texture(bear_texture)
r.load('./models/bear.obj', translate=(-1, -1.1, 0.5), scale=(0.4, 0.4, 0.4), rotate=(0, 1.7, 0))
r.draw_arrays('TRIANGLES')
#
#load fox
fox_texture = Texture('./models/foxTxt.bmp')
r.set_texture(fox_texture)
fox_size = 0.0025
r.load('./models/fox.obj', translate=(0.4, -0.5, 0), scale=(fox_size, fox_size, fox_size), rotate=(0, 0, 0))
r.draw_arrays('TRIANGLES')
r.load('./models/fox.obj', translate=(0.2, -0.5, 0), scale=(fox_size, fox_size, fox_size), rotate=(0, 0, 0))
r.draw_arrays('TRIANGLES')

# Load moons
normal_earth = Texture('./models/blackFur.bmp')
r.set_texture(normal_earth)
r.load('./models/sphere.obj', translate=(0, 0.6, 0.8), scale=(0.4, 0.4, 0.4), rotate=(0, 0, 0))
r.draw_arrays('TRIANGLES')

# Load mountains
normal_earth = Texture('./models/SnowyMountainTexture.bmp')
r.set_texture(normal_earth)
# r.load('./models/mountain-rock.obj', translate=(0, -0.3, 0), scale=(0.7, 0.3, 0.3), rotate=(1, 0, 0))
r.load('./models/mountain.obj', translate=(-2.3, -0.3, -1.4), scale=(0.02, 0.02, 0.02), rotate=(0, -0.6, 0))
r.draw_arrays('TRIANGLES')
r.load('./models/mountain.obj', translate=(0, -0.3, -2), scale=(0.02, 0.02, 0.02), rotate=(0, -0.6, 0))
r.draw_arrays('TRIANGLES')




r.display('out.bmp')




