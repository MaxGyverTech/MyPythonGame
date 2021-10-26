import pygame as pg
import math
from . import enemies, core, fx, level
from . utils import *
from random import randint as rd

import cfg

PLAYER_IMG = pg.image.load('game/content/player2/player.png')
PLAYER_LEGS_IDLE = pg.image.load('game/content/player2/legs/idle.png')
PLAYER_ARMS = pg.image.load('game/content/player2/arms.png')
PLAYER_LEGS_AIR = pg.image.load('game/content/player/legs/air.png')
PLAYER_LEGS_L = pg.image.load('game/content/player/legs/left.png')
PLAYER_LEGS_R = pg.image.load('game/content/player/legs/right.png')
BULLET_IMG = pg.image.load('game/content/player/guns/bullet.png')

PLAYER_ACCELERATION = 5
PLAYER_AIR_ACCELERATION = 3
PLAYER_MAX_SPEED = 5
JUMP_FORCE = 10
WALL_JUMP_FORCE = 6
GRAVITY = 0.4

RED_TINT = pg.Surface(PLAYER_IMG.get_size())
RED_TINT.fill('red')



sounds = not pg.mixer.get_init() is None
print('sound',sounds)
if sounds:
    print('load sound')
    SOUNDS = {
        'jump':pg.mixer.Sound('game/content/sounds/jump.wav'),
        'hurt':pg.mixer.Sound('game/content/sounds/hurt.wav'),
        'shoot':pg.mixer.Sound('game/content/sounds/shoot.wav'),
    }

GUNS = {
    'rifle': {'img': pg.image.load('game/content/player/guns/rifle.png'),
              'hold_img': 0,
              'pos': (29, 29),
              'bull_pos': (0, 0),
              'speed': 30,
              'mag': 30,
              'reload':2000,
              'dmg':15,
              'kd':100,
              'auto': True},
    'pistol': {'img': pg.image.load('game/content/player2/guns/pistol.png'),
               'hold_img': 0,
               'pos': (29, 29),
               'bull_pos': (0, 0),
               'speed': 30,
               'mag': 10,
               'reload': 1000,
               'dmg':35,
               'kd':300,
               'auto': False},
}


class Bullet(core.Actor):
    def set(self,img, rot, dmg, parent):
        self.autodel(20)
        self.parent = parent
        self.damage = dmg
        self.img = pg.transform.rotate(img, abs(rot))
        if self.xspeed < 0:
            self.img = pg.transform.flip(self.img,True,False)
        if self.yspeed > 0:
            self.img = pg.transform.flip(self.img,False,True)

    def draw(self, screen: pg.Surface, camera):
        screen.blit(self.img, (self.rect.x - camera.x, self.rect.y - camera.y, self.rect.w, self.rect.h))
        # screen.blit(self.img, self.rect.topleft, special_flags=pg.BLEND_RGB_ADD)
    def hit(self, actor):
        if actor == self.parent:
            return
        if isinstance(actor, enemies.AI):
            actor.hp -= self.damage
            write_stat('done damage', get_stat('done damage')+self.damage)
            fx.blood(self.rect.center,self.parent.world, 5)
            fx.damage(self.rect.center,-self.damage,self.parent.world)
            if sounds: SOUNDS['hurt'].play()
            self._delete = True
        if isinstance(actor, level.Block):
            if actor.type in [i for i in level.block_s if level.block_s[i]['dest']]: actor.set_type('0')
            self._delete = True


class Player(core.Actor):
    def __init__(self, x, y, n=0, game_inst=None):
        super().__init__(x, y, 35,80, friction=0.2)
        self.n = n
        self.s = {}
        self.game = game_inst
        # pg.sprite.Sprite.__init__(self)
        self.img = PLAYER_IMG

        self.move_left, self.move_right, self.jump, self.tp = False, False, False, False
        self.move_speed = 0
        self.look_r = True
        self.r_leg = True
        self.double = True
        self.timer = 0
        self.angle = 0
        self.hp = 100
        self.dmg_timer = 0
        self.world = None
        self.shoot = False
        self.shoot_kd = 0
        self.inventory_kd = 1000
        self.font = pg.font.Font(cfg.font, 14)

        self.gun = 0
        self.guns = ['pistol', 'rifle']
        self.ammo = {'rifle': [30, 30], 'pistol': [10,50]}
        self._reload = False
        self.reload_kd = 0
        self.bullets = []

    def process_move(self, d: dict):
        if d.get('right') is not None:
            self.move_right = d['right']
        if d.get('left') is not None:
            self.move_left = d['left']
        if d.get('up') is not None:
            self.jump = d['up']
        if d.get('look_r') is not None:
            self.look_r = d['look_r']
        if d.get('angle') is not None:
            self.angle = d['angle']
        if d.get('shoot') is not None:
            self.shoot = d['shoot']
        if d.get('tp') is not None:
            self.tp = d['tp']
        if d.get('wheel') is not None:
            self.gun += d['wheel']
            self.gun = self.gun % len(self.guns)
            self.inventory_kd = 1000
            self._reload = False
        if d.get('reload') is not None:
            self.reload()

    def update_control(self,delta, blocks, level):
        if self.hp <= 0: self.delete()
        if self.dmg_timer >0: self.dmg_timer-=delta
        if self.shoot_kd >0: self.shoot_kd -= delta
        if self.inventory_kd>0: self.inventory_kd -= delta
        if self._reload:
            if self.reload_kd>0: self.reload_kd -= delta
            else:
                amm = self.ammo[self.guns[self.gun]]
                if amm[1]>0:
                    m = GUNS[self.guns[self.gun]]['mag']
                    print(amm)
                    for i in range(1,m+1):
                        if amm[1]-i<=0: 
                            m=i
                            break
                    self.ammo[self.guns[self.gun]] = [m, self.ammo[self.guns[self.gun]][1]-m]
                self._reload = False
        # self.on_ground = self.check_on_ground(blocks)
        if self.on_ground:
            self.double = True
        self.world = level
        # self.
        # багованый вариант с инерцией
        # self.timer += delta
        # if self.timer >=250:
        #     self.timer = 0
        #     if self.move_right and self.xspeed < PLAYER_MAX_SPEED: self.xspeed += PLAYER_ACCELERATION
        #     if self.move_left and self.xspeed > -PLAYER_MAX_SPEED: self.xspeed -= PLAYER_ACCELERATION
        #     if not self.move_right and not self.move_left:
        #         if self.xspeed > 0: self.xspeed -= PLAYER_ACCELERATION * 2
        #         if self.xspeed < 0: self.xspeed += PLAYER_ACCELERATION * 2
        # MOVE R/L
        # ACCEL = PLAYER_ACCELERATION if self.on_ground else PLAYER_AIR_ACCELERATION
        ACCEL = PLAYER_ACCELERATION
        if self.move_right and not self.right: self.xspeed += ACCEL -self.xspeed
        if self.move_left and not self.left: self.xspeed -= ACCEL+self.xspeed
        # if not self.move_right and not self.move_left: self.xspeed = 0
        # if (self.right and self.xspeed > 0) or (self.left and self.xspeed < 0): self.xspeed = 0

        if self.tp:
            self.tp = False
            # self.rect.center = self.get_point(level, 200)
            xv, yv = vec_to_speed(15, -self.angle)
            self.xspeed += xv if self.look_r else -xv
            self.yspeed = yv

        # if self.jump and not self.on_ground:
        #     if self.left and self.move_left:
        #         self.move_left = False
        #         self.xspeed += 10
        #         print('l')
        #     if self.right and self.right:
        #         self.move_right = False
        #         self.xspeed -= 10
        #         print('r')
        # JUMP
        self._jump()
        # if self.jump and (self.on_ground or self.double):
        #     if not self.on_ground and self.double:
        #         self.double = False
        #         # self.xspeed = 0
        #     self.jump = False
        #     self.yspeed = -JUMP_FORCE
        #     self.on_ground = False
        # if not self.on_ground: self.yspeed += GRAVITY
        if self.shoot and self.shoot_kd<=0: self._shoot()
        # self.update(delta, blocks, level.actors)

    def _jump(self):
        if self.jump:
            # if not self.on_ground and self.double:
            #     self.double = False
                # self.xspeed = 0
            if not self.on_ground:
                if self.left and self.move_left and self.look_r:
                    self.move_left = False
                    self.xspeed += WALL_JUMP_FORCE
                    self.double = True
                elif self.right and self.move_right and not self.look_r:
                    self.move_right = False
                    self.xspeed -= WALL_JUMP_FORCE
                    self.double = True
                elif self.double: self.double = False
                else:return
            self.jump = False
            self.yspeed = -JUMP_FORCE
            self.on_ground = False
            if sounds: SOUNDS['jump'].play()
    def reload(self):
        self._reload = True
        self.ammo[self.guns[self.gun]] = [0, self.ammo[self.guns[self.gun]][0]+self.ammo[self.guns[self.gun]][1]]
        self.reload_kd = GUNS[self.guns[self.gun]]['reload']

    def _shoot(self):
        if self._reload: 
            self.shoot = False
            return
        if self.ammo[self.guns[self.gun]][0]<=0:
            self.shoot = False
            self.reload()
            return
        xvel, yvel = vec_to_speed(GUNS[self.guns[self.gun]]['speed'], self.angle)
        # b = Bullet(self.rect.x + GUNS[self.gun]['pos'][0],
        #            self.rect.y + GUNS[self.gun]['pos'][1],
        #            xvel if self.look_r else -xvel,
        #            yvel,
        #            self.angle,
        #            BULLET_IMG)
        # self.bullets.append(b)
        b = Bullet(self.rect.x + GUNS[self.guns[self.gun]]['pos'][0],
                  self.rect.y + GUNS[self.guns[self.gun]]['pos'][1],
                  10,10, gravity=0, friction=0, bounce=0)
        b.xspeed = xvel if self.look_r else -xvel
        b.yspeed = -yvel
        # b.set(BULLET_IMG, self.angle,GUNS[self.gun]['dmg'], self)
        d = GUNS[self.guns[self.gun]]['dmg']
        b.set(BULLET_IMG, self.angle,rd(int(d-(d*0.2)), int(d+(d*0.2))), self)
        self.game.world.actors.append(b)

        self.ammo[self.guns[self.gun]][0] -= 1

        self.shoot_kd = GUNS[self.guns[self.gun]]['kd']
        self.shoot = GUNS[self.guns[self.gun]]['auto']
        if sounds: SOUNDS['shoot'].play()
        write_stat('shoots', get_stat('shoots')+1)

    def get_point(self, world, rad, ang=None):
        r = rad
        rect = self.rect.copy()
        while r>=0:
            rect.center = self.rect.center
            angle = rd(-180, 0) if ang is None else ang
            x, y = vec_to_speed(r, angle)
            rect.x += x; rect.y+=y
            if not world.get_blocks(rect):
                return rect.center
            r-=1
        return self.rect.center

    def rotate(self):
        self.img = pg.transform.flip(self.img, True, False)

    def draw(self, screen: pg.Surface, camera: pg.Rect):
        self.img = PLAYER_IMG.copy()
        # if self.on_ground:
        #     if self.xspeed == 0:
        #         self.img.blit(PLAYER_LEGS_IDLE, (0, 53))
        #     else:
        #         self.img.blit(PLAYER_LEGS_R if self.r_leg else PLAYER_LEGS_L, (0, 53))
        # else:
        #     self.img.blit(PLAYER_LEGS_AIR, (0, 53))
        # self.img.blit(PLAYER_LEGS_AIR, (0, 0))
        off = 0 if self.look_r else -30
        if not self.on_ground and ((self.left and self.move_left and self.look_r) or (self.right and self.move_right and not self.look_r)):
            self.img = pg.transform.rotate(self.img, -30)
            off = -10 if self.look_r else -60
        gun_img = pg.transform.rotate(GUNS[self.guns[self.gun]]['img'].copy(), self.angle)
        # debug(gun_img.get_rect().center, screen)
        self.img.blit(gun_img, (gun_img.get_rect().x+20, gun_img.get_rect().y+30))
        # if not self.look_r and self.xspeed > 0: self.rotate()
        # if self.look_r and self.xspeed < 0: self.rotate()
        if not self.look_r: self.rotate()
        if self.dmg_timer > 0:
            self.img.blit(RED_TINT,(0,0),special_flags=pg.BLEND_RGB_ADD)
        if self.inventory_kd>0:
            self.img.blit(self.font.render(f'[{self.guns[self.gun]}]',False,'white'), (-off,0))
        # screen.fill('green',(self.pre_rect.x - camera.x, self.pre_rect.y + camera.y, self.pre_rect.w, self.pre_rect.h))
        screen.blit(self.img,
                    (self.rect.x - camera.x+off, self.rect.y - camera.y))
        for b in self.bullets:
            screen.blit(b.img, (b.rect.x - camera.x, b.rect.y + camera.y))
