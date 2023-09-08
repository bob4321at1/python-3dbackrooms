from ursina import *
import panda3d
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader
import random

app = Ursina()

terrain = Entity()

def input(key):
    if key == "escape":
        quit()

amount = 0

for x in range(75):
    for y in range(75):
        rot = random.randint(1, 4) * 90
        flipped = random.randint(0, 1) * 180
        rom = Entity(model="art/room.obj", texture = "art/room.png", rotation=(flipped, rot, 0), position=(x * 10, 0, y * 10))
        rom.parent = terrain
        rom = None
        amount += 1
tex = panda3d.core.Texture("art/room.png")
terrain.combine()
terrain.collider = 'mesh'
terrain.texture = "art/room.png"
terrain.set_color(color.rgba(255, 255, 255, 255))
terrain.shader = lit_with_shadows_shader
terrain.double_sided = True
player = FirstPersonController(position=(0, 10, 0), speed=16, sensitivity = 1000)
Sky(texture=tex, color=color.rgba(255, 246, 148, 255))

app.run()