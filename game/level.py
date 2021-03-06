import re
from typing import List, Union
import pygame as pg
import sys,importlib, ctypes
from . import enemies,core, objects
from . utils import *
import cfg

img_rock = 'game/content/blocks/block_rock.png'
img_rock2 = 'game/content/blocks/block_rock2.png'
img_wood = 'game/content/blocks/block_wood.png'
img_leaves = 'game/content/blocks/block_leaves.png'
img_lastick = 'game/content/blocks/block_nthg.png'
img_metal = 'game/content/blocks/block_metal.png'
img_glass = 'game/content/blocks/block_glass.png'
img_brick = 'game/content/blocks/block_bricks.png'
img_concrete = 'game/content/blocks/block_concrete.png'
img_boards = 'game/content/blocks/block_boards.png'

block_s = {
    '0': {'img': img_lastick, 'dest': False},
    '=': {'img': img_rock, 'dest': False},
    '!': {'img': img_rock2, 'dest': False},
    '|': {'img': img_wood, 'dest': False},
    '+': {'img': img_leaves, 'dest': True},
    '-': {'img': img_metal, 'dest': False},
    '/': {'img': img_glass, 'dest': True},
    '#': {'img': img_brick, 'dest':False},
    '%': {'img': img_concrete, 'dest':False},
    '*': {'img': img_boards, 'dest':False},
}

script_conf = '''#### Dont delete this comment, edit only script inside ####

# called once on level loading
def load(game):
	pass

# called every frame update
def update(game):
	pass

###########################################################'''

conf = '''# Full auto-generated, can be edited
from game import *

spawn_pos = (40,40)
background = '{bg}'
guns = []
sun_level = 0

'''+script_conf+''''

ais = [

]

actors=[

]

blocks = [

]
'''
class Point(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_int),
        ('y', ctypes.c_int),
    ]
game_lib = ctypes.cdll.LoadLibrary('game/Game.dll')
c_ray_cast = game_lib[1]
c_ray_cast.argtypes = [ctypes.c_int,ctypes.c_int,ctypes.c_int,ctypes.c_int,ctypes.POINTER(Point), ctypes.c_size_t]
c_ray_cast.restype = Point


def write_list(name, arr):
    separator = ',\n\t'
    return f"{name} = [\n\t{separator.join(arr)}\n]\n"

# def get_copyes(arr):
#     return [copy(i) for i in arr]

class Block(core.Actor):
    def __init__(self, x, y, t):
        super().__init__(x,y,40,40, static=True)
        self.img: pg.Surface = None
        self.type = t
        self.set_type(t)

    def set_type(self, t):
        self.type = t
        self.img = pg.image.load(block_s[t]['img']).convert_alpha()

    def __str__(self):
        return f'level.Block({self.rect.x},{self.rect.y},{repr(self.type)})'

black_sf = pg.Surface((cfg.screen_h*2,cfg.screen_v*2), flags=pg.SRCALPHA)
black_sf.fill('black')
class World(core.Saving):
    slots = {
        # 'spawn_x':['spawn_pos[0]', int],
        # 'spawn_y':['spawn_pos[1]', int],
        # 'spawn_pos':['spawn_pos',list],
        'sun_debug_level':['sun',int],
        'background':['bg_name',str],
        'guns':['guns',list],
    }
    def __init__(self, level=None):
        self.levelname = level
        self.cur_level = None
        self.h, self.w = 0, 0
        self.blocks: List[Block] = []
        self.actors: List[core.Actor] = []
        self.ais: List[enemies.MeleeAI] = []
        self.images: List[pg.Surface] = []
        self.guns = []
        self.ignore_str = ''
        self.spawn_pos = (40,40)
        self.bg_name = 'game/content/blocks/bg.png'
        self.neo_mode = False
        self.sun = 0
        # self.bg = pg.image.load(self.bg_name).convert()
        self.rect: pg.Rect = None
        if level: self.open_world(level)

        self.black_sf = pg.Surface((cfg.screen_h*2,cfg.screen_v*2), flags=pg.SRCALPHA)
        self.black_sf.fill('black')
        self.lighting = pg.Surface((cfg.screen_h*2,cfg.screen_v*2), flags=pg.SRCALPHA)

    def open_world(self, levelname, game_inst=None, video=True):
        self.actors, self.images, self.ais, self.ignore_str = [],[], [], ''
        self.sun = 0
        self.neo_mode = False
        with open(f'levels/{levelname}.py', 'r') as file:
            r = re.search(r'#### Dont delete this comment, edit only script inside ####\n(.*\n)*###########################################################\n', file.read())
            if r: self.ignore_str = r.group(0)
            else: self.ignore_str = script_conf
        level = importlib.import_module(f'levels.{levelname}')
        importlib.reload(level)
        self.cur_level = level
        print(f'Open level - {levelname}, optimization = {video}')
        self.bg_name = level.background
        if video:self.bg = pg.image.load(level.background).convert()
        else:self.bg = pg.image.load(level.background)
        self.spawn_pos = level.spawn_pos
        self.guns = level.guns.copy()
        self.ais = level.ais.copy()
        self.actors = level.actors.copy()+self.ais
        self.sun = level.sun_level
        if game_inst: level.load(game_inst)
        [a.set_game(game_inst) for a in self.actors]
        # print([(a,a._delete) for a in self.actors])
        for a in self.actors: 
            if isinstance(a, objects.BaseTriger): a.game = game_inst
        self.blocks = level.blocks.copy()
        self.rect = pg.Rect(0, 0, self.get_size()[0], self.get_size()[1])
        # print(f'Level opened: {level}')
        return self.spawn_pos, self.guns

    def save_world(self, levelname):
        with open(f'levels/{levelname}.py', 'w') as file:
            file.write(f'from game import *\n\nspawn_pos = {repr(self.spawn_pos)}\nbackground = {repr(self.bg_name)}\n'+write_list('guns', [repr(i) for i in self.guns])+f'sun_level = {self.sun}\n\n{self.ignore_str}\n')
            # file.write('####DONT TOUCH####\n# Auto-generated in '+__name__+'\n')
            ais = write_list('ais',[i.save() for i in self.ais if isinstance(i,core.Saving)])
            acts = write_list('actors',[i.save() for i in self.actors if isinstance(i,core.Saving) and not isinstance(i, enemies.BaseAI)])
            bs = write_list('blocks', [b.__str__() for b in self.blocks])
            file.write(ais)
            file.write(acts)
            file.write(bs)

    def get_nearest(self, obj_class, pos):
        objcts = [a for a in self.actors if isinstance(a,obj_class)]
        if not objcts: return
        act, min_dist = objcts[0], distanse(objcts[0].rect, pos)
        for a in objcts:
            d = distanse(a.rect, pos)
            if d<min_dist:
                min_dist = d
                act = a
        return act
    
    def get_colliding(self, pos, obj_class=core.Actor):
        return [a for a in self.actors if isinstance(a,obj_class) and a.rect.collidepoint(*pos)]
    
    # def get_block_at(self, pos:Tuple[int,int], camera = None):
    #     for b in (self.blocks if not camera else self.get_blocks(camera)):
    #         if b.rect.collidepoint(*pos):
    #             return b
    #     return None

    def get_blocks(self, rect:pg.Rect=None):
        if rect is None:
            return self.blocks
        return [self.blocks[i] for i in rect.collidelistall(self.blocks)]
        # return self.blocks
    
    def raycast(self, pos, ang, max_dist = cfg.screen_h, camera = None):
        # """WARNING! BAD OPTIMIZATION"""
        # x, y = pos; dx,dy = vec_to_speed(1, ang)
        # bl = self.blocks if not camera else self.get_blocks(camera)
        # for w in range(0,max_dist):
        #     for b in bl:
        #         if b.rect.collidepoint(x,y):
        #             return pos, (x,y), w
        #     x,y = x+dx, y+dy
        # return pos, (x,y), max_dist
        """Using C"""
        ar_type = Point*len(self.blocks)
        ar_l = ar_type()
        for i in range(len(self.blocks)):
            ar_l[i] = Point()
            ar_l[i].x = self.blocks[i].rect.x
            ar_l[i].y = self.blocks[i].rect.y
        ar = ctypes.cast(ar_l, ctypes.POINTER(Point))
        p = c_ray_cast(int(pos[0]),int(pos[1]), int(ang), int(max_dist), ar, len(self.blocks))
        return pos, (p.x,p.y), max_dist
    
    def multi_ray_cast(self, pos, angles:List[int], max_dist = cfg.screen_h, camera = None):
        ar_type = Point*len(self.blocks)
        ar_l = ar_type()
        for i in range(len(self.blocks)):
            ar_l[i] = Point()
            ar_l[i].x = self.blocks[i].rect.x
            ar_l[i].y = self.blocks[i].rect.y
        ar = ctypes.cast(ar_l, ctypes.POINTER(Point))
        r = []
        for a in angles:
            p = c_ray_cast(int(pos[0]),int(pos[1]), int(a), int(max_dist), ar, len(self.blocks))
            r.append((p.x,p.y))
        return r

    
    def get_actors(self, rect:pg.Rect=None):
        if rect is None:
            return self.actors
        return [self.actors[i] for i in rect.collidelistall(self.actors)]

    def update_actors(self, delta, player = None):
        delta = limit(delta, max=30)
        for b in self.blocks:
            if b._delete:
                del self.blocks[self.blocks.index(b)]
        for a in self.actors:
            if a._delete:
                try: self.actors.remove(a)
                except ValueError:continue
            else:
                if self.neo_mode and not (isinstance(a, (objects.SpawningPortal, objects.BaseTriger)) or a is player): continue  
                
                if not a.static and a.collision:
                    a.update(delta, self.get_blocks(a.pre_rect), self.get_actors(a.pre_rect))
                else:
                    a.update(delta, [], self.actors)
        if self.ais and not self.neo_mode:
            [ai.update_ai(delta, self) for ai in self.ais]
        if player and player.game: self.cur_level.update(player.game)

    def set_blocks(self, blocks):
        self.blocks = blocks

    def set_block(self, pos, t):
        flag = True
        for b in self.blocks:
            if pg.Rect.collidepoint(b.rect, pos[0], pos[1]):
                if t == '0':
                    del self.blocks[self.blocks.index(b)]
                else:
                    b.set_type(t)
                    flag = False
        if flag and t != '0':
            b = Block(pos[0] // 40 * 40, pos[1] // 40 * 40, t)
            self.blocks.append(b)

    def get_size(self):
        return (self.w + 40), self.h
    
    def draw(self, screen: pg.Surface, camera: pg.Rect, debug=False):
        screen.blit(self.bg, (0,0))
        for i in self.get_blocks(camera):
            screen.blit(i.img, (i.rect.x - camera.x, i.rect.y - camera.y))
        for sf,_, pos in self.images: screen.blit(sf, real(pos, camera))
        [a.draw(screen, camera) for a in self.get_actors(camera)]

        if self.neo_mode:
            neg = pg.Surface(screen.get_size())
            neg.fill((255, 255, 255))
            neg.blit(screen, (0, 0), special_flags=pg.BLEND_SUB)
            screen.blit(neg,(0,0))

        if 0<self.sun:
            self.sun = limit(self.sun, 0, 255) 
            self.lighting.fill((0,0,0,0))
            [a.light_draw(self.lighting, camera) for a in self.get_actors(camera)]
            self.black_sf.fill('black')
            self.black_sf.set_alpha(self.sun)
            self.black_sf.blit(self.lighting,(0,0), special_flags=pg.BLEND_RGBA_SUB)
            screen.blit(self.black_sf, (0, 0))

        
        if debug: [a.debug_draw(screen, camera) for a in self.actors]


    def reset(self):
        self.bg = pg.image.load(self.bg_name).convert_alpha()