import pygame as pg
import math
from . import enemies, core, fx, level
from .UI import HBox, Interface, Button,ProgressBar, VBox, RIGHT,LEFT,FILL,DOWN,UP
from . utils import *
from random import randint as rd
import cfg

IMGS = {
    'PLAYER':pg.image.load('game/content/player2/player.png'),
    'BACK':pg.image.load('game/content/player2/back.png'),
    'GRENADE':pg.image.load('game/content/player2/guns/grenade.png')
}

PLAYER_IMG = pg.image.load('game/content/player2/player.png')
BACK_IMG = pg.image.load('game/content/player2/back.png')
PLAYER_IMG_DEAD = pg.image.load('game/content/player2/player_dead.png')
PLAYER_LEGS_IDLE = pg.image.load('game/content/player2/legs/idle.png')
PLAYER_ARMS = pg.image.load('game/content/player2/arms.png')
PLAYER_LEGS_AIR = pg.image.load('game/content/player/legs/air.png')
PLAYER_LEGS_L = pg.image.load('game/content/player/legs/left.png')
PLAYER_LEGS_R = pg.image.load('game/content/player/legs/right.png')
BULLET_IMG = pg.image.load('game/content/player/guns/bullet.png')

# parts
PART_BACK = pg.image.load('game/content/player2/died/back.png')
PART_HEAD = pg.image.load('game/content/player2/died/head.png')
PART_LEGS = pg.image.load('game/content/player2/died/legs.png')

PLAYER_ACCELERATION = 5
PLAYER_AIR_ACCELERATION = 3
PLAYER_MAX_SPEED = 5
JUMP_FORCE = 10
WALL_JUMP_FORCE = 6
GRAVITY = 0.4

RED_TINT = pg.Surface(PLAYER_IMG.get_size())
RED_TINT.fill('red')

sounds = not pg.mixer.get_init() is None
# print('sound',sounds)
if sounds:
    SOUNDS = {
        'jump':pg.mixer.Sound('game/content/sounds/jump.wav'),
        'hurt':pg.mixer.Sound('game/content/sounds/hurt.wav'),
        'shoot':pg.mixer.Sound('game/content/sounds/shoot.wav'),
        'expl':pg.mixer.Sound('game/content/sounds/explosion.wav'),
    }


GUNS = {
    'rifle': {'img': pg.image.load('game/content/player/guns/rifle.png'),
              'hold_img': 0,
              'pos': (29, 29),
              'offx':0,
              'offy':0,
              'bull_pos': (0, 0),
              'bull_img':pg.image.load('game/content/player/guns/bullet.png'),
              'speed': 20,
              'mag': 30,
              'amount': 1,
              'reload':1500,
              'dmg':15,
              'kd':100,
              'acc':2,
              'auto': True,
              'shake':7,
              'back':1,
              'recoil':10},
    'pistol': {'img': pg.image.load('game/content/player2/guns/pistol.png'),
               'hold_img': 0,
               'pos': (29, 29),
               'offx':0,
               'offy':0,
               'bull_pos': (0, 0),
               'bull_img':pg.image.load('game/content/player/guns/bullet.png'),
               'speed': 25,
               'mag': 10,
               'amount': 1,
               'reload': 1000,
               'dmg':35,
               'kd':300,
               'acc':1,
               'auto': False,
               'shake':9,
               'back':3,
               'recoil':50},
    'shootgun': {'img': pg.image.load('game/content/player2/guns/shootgun.png'),
            'hold_img': 0,
            'pos': (29, 29),
            'offx':0,
            'offy':-2,
            'bull_pos': (0, 0),
            'bull_img':pg.image.load('game/content/player/guns/bullet.png'),
            'speed': 25,
            'mag': 5,
            'amount': 5,
            'reload': 3000,
            'dmg':15,
            'kd':350,
            'acc':2,
            'auto': False,
            'shake':15,
            'back':10,
            'recoil':70},
    'minigun': {'img': pg.image.load('game/content/player2/guns/minigun.png'),
            'hold_img': 0,
            'pos': (29, 29),
            'offx':0,
            'offy':-5,
            'bull_pos': (0, 0),
            'bull_img':pg.image.load('game/content/player/guns/bullet.png'),
            'speed': 25,
            'mag': 100,
            'amount': 1,
            'reload': 3000,
            'dmg':7,
            'kd':50,
            'acc':1,
            'auto': True,
            'shake':5,
            'back':1,
            'recoil':4},
    'sniper': {'img': pg.image.load('game/content/player2/guns/sniper.png'),
            'hold_img': 0,
            'pos': (29, 29),
            'offx':7,
            'offy':-5,
            'bull_pos': (0, 0),
            'bull_img':pg.image.load('game/content/player/guns/bullet.png'),
            'speed': 30,
            'mag': 5,
            'amount': 1,
            'reload': 2000,
            'dmg':130,
            'kd':600,
            'acc':1,
            'auto': False,
            'shake':20,
            'back':7,
            'recoil':90},
}

def convert():
    for key, val in IMGS.items():
        IMGS[key] = val.convert_alpha()
    for d in GUNS.values():
        d['img'] = d['img'].convert_alpha()
        d['bull_img'] = d['bull_img'].convert_alpha()
class Bullet(core.Actor):
    def __init__(self, x, y, xv,yv, img, rot, dmg, parent):
        w,h = img.get_size()
        super().__init__(x, y, w, h,gravity=0.1, friction=0)
        self.autodel(20)
        self.parent = parent
        self.damage = dmg
        self.img = pg.transform.rotate(img, abs(rot)).convert_alpha()
        self.speed = Vec(xv,yv)
        if xv < 0:
            self.img = pg.transform.flip(self.img,True,False)
        if yv > 0:
            self.img = pg.transform.flip(self.img,False,True)
        self.ignore_tmr = 200
        self.pre_rect = pg.Rect(x-50,y-50,w+50,h+50)
        # self.trale = pg.Surface((20,20))
        # pg.draw.circle(self.trale,'yellow',(10,10),20)
        # self.trale.set_colorkey('black')

    def update(self, delta, blocks, actors):
        if self.ignore_tmr>0: self.ignore_tmr-=delta
        return super().update(delta, blocks, actors)
    
    def draw(self, screen: pg.Surface, camera):
        
        # pg.draw.line(screen,'yellow', real(self.rect.center, camera),real(self.rect.center+self.speed*-2, camera),2)
        # pg.draw.line(screen,'orange', real(self.rect.center, camera),real(self.rect.center+self.speed*-1, camera),2)
        screen.blit(self.img, (self.rect.x - camera.x, self.rect.y - camera.y, self.rect.w, self.rect.h))
        # screen.blit(self.trale, real(self.rect.center, camera), special_flags=pg.BLEND_RGB_ADD)
        # screen.blit(self.img, self.rect.topleft, special_flags=pg.BLEND_RGB_ADD)
    def hit(self, actor):
        if actor == self.parent and self.ignore_tmr>0:
            return
        if isinstance(actor, enemies.BaseAI) and not isinstance(self.parent, enemies.BaseAI):
            actor.hp -= self.damage
            self.parent.game.stats['done damage']+=self.damage
            # write_stat('done damage', get_stat('done damage')+self.damage)
            if not cfg.potato:
                fx.blood(self.rect.center,self.parent.world, int(self.damage*1.5/10))
                fx.damage(self.rect.center,self.damage,self.parent.world)
            if sounds: SOUNDS['hurt'].play()
            if self.parent.aim_time < self.parent.AIM_TIME_MAX: self.parent.aim_time+=self.damage*10
            self._delete = True
        if isinstance(actor, Player):
            actor.damage(self.damage)
            self.parent.game.stats['received damage']+=self.damage
            # write_stat('received damage', get_stat('received damage')+self.damage)
            actor.dmg_timer = 100
            self._delete = True
        if isinstance(actor, level.Block):
            if actor.type in [i for i in level.block_s if level.block_s[i]['dest']]: 
                # actor.set_type('0')
                actor.delete()
                self.delete()
            else:
                self._delete = True
        
    def reset(self):
        self.img = pg.transform.flip(self.img,False,True)
            
class Grenade(core.Actor):
    def __init__(self, x, y, xv,yv, game):
        super().__init__(x, y, 9,11, bounce=0.45, friction=0.1,image=IMGS['GRENADE'])
        self.speed = Vec(xv,yv)
        self.explose_tmr = 3500
        self.game =game
        r=120
        self.pre_rect = pg.Rect(x-r,y-r, r*2,r*2)
        
    def update(self, delta, blocks, actors):
        self.explose_tmr-=delta
        if self.explose_tmr<=0: self.explose(blocks,actors)
        return super().update(delta, blocks, actors)
    
    def explose(self,blocks, actors):
        r = 230
        dest = [key for key, val in level.block_s.items() if val['dest']]
        for a in actors+blocks:
            if isinstance(a, core.Actor):
                d = distanse(self.rect.center, a.rect.center)
                if d<r:
                    dmg=int(remap(r-d, (0,r), (20,120)))
                    xv,yv = vec_to_speed(dmg/5, 180-angle(a.rect.center,self.rect.center,))
                    a.speed.xy = xv if self.rect.x>a.rect.x else -xv,(yv if self.rect.x>a.rect.x else -yv)-1
                    a.on_fire = rd(5000,8000)
                    if isinstance(a, Player) or isinstance(a, enemies.BaseAI):
                        self.game.stats['done damage']+=dmg
                        a.hp -= dmg
                        if not cfg.potato: fx.damage(a.rect.center, dmg, self.game.world)
            if isinstance(a, level.Block) and a.type in dest:
                a.delete()
        self.game.shake=20
        if sounds: SOUNDS['expl'].play()
        if not cfg.potato: fx.explosion(self.rect.center,self.game.world, 30)
        self.delete()
        

class Player(core.Actor):
    AIM_TIME_MAX=5000
    def __init__(self, x, y, n=0, game_inst=None):
        super().__init__(x, y, 35,63, friction=0.2)
        self.n = n
        self.s = {}
        self.game = game_inst
        self.img = PLAYER_IMG
        self.ui = Interface(anims=False)
        convert()
        
        self.move_left, self.move_right, self.jump, self.tp = False, False, False, False
        self.move_speed = 0
        self.look_r = True
        self.r_leg = True
        self.double = True
        self.aiming = False
        self.aim_time=self.AIM_TIME_MAX
        self.timer = 0
        self.angle = 0
        self.hp = 200
        self.max_hp = 200
        self.dmg_timer = 0
        self.world = None
        self.shoot = False
        self.shoot_kd = 0
        self.inventory_kd = 1000
        self.font = pg.font.Font(cfg.font, 14)
        self.need_sides = True
        self.to_ang=0
        self.recoil=0
        self.wall_jump_kd = 0
        self.m_coords = (0,0)

        self.gun = 0
        self.guns = ['pistol']
        self.ammo = {'rifle': [30, 60], 'pistol': [10,50],'shootgun':[5,15], 'minigun':[100,100], 'sniper':[5,15]}
        self.grenades = 40
        self.grenade=False
        self._reload = False
        self.reload_kd = 0
        
        self.bonus = {
            'Double gun':0,
            'Armor':0,
            'Time stop':0,
        }

        self.dead = False
        self.dead_kd = 2000

        self.event_ui = VBox(0,(700,0), (154,400), anchor_h=RIGHT, anchor_v=DOWN)
        self.hp_bar= ProgressBar((40,380), pg.image.load('game/content/ui/hp_full.png').convert_alpha(), pg.image.load('game/content/ui/hp_empty.png').convert_alpha(), colorkey='black')
        self.time_bar = ProgressBar((40,380), pg.image.load('game/content/ui/time_full.png').convert_alpha(), pg.image.load('game/content/ui/time_empty.png').convert_alpha(), colorkey='black')
        self.ammo_but = Button((790,428),'yellow','', 20)
        self.reload_but = Button((790,418),'red','', 15)
        self.gun_but = Button((790,445),'white','', 15)
        self.grenades_but = Button((760,460),'white','', 15)
        self.ui.set_ui([
            self.hp_bar,
            self.time_bar,
            self.ammo_but,
            self.reload_but,
            self.gun_but,
            self.grenades_but,
            self.event_ui,
            Button((750,420),'white','',1,img='game/content/ui/ammo.png'),
            Button((20,422),'white','',1,img='game/content/ui/heart.png'),
            Button((30,410),'white','',1,img='game/content/ui/clock.png'),
            Button((750,463),'white','',1,img='game/content/ui/grenade.png'),
        ])

    def process_move(self, d: dict):
        if d.get('right') is not None:
            self.move_right = d['right']
        if d.get('left') is not None:
            self.move_left = d['left']
        if d.get('up') is not None:
            self.jump = d['up']
        # if d.get('look_r') is not None:
        #     self.look_r = d['look_r']
        # if d.get('angle') is not None:
        #     self.angle = d['angle']
        if d.get('shoot') is not None:
            self.shoot = d['shoot']
        if d.get('tp') is not None:
            self.tp = d['tp']
        if d.get('grenade') is not None:
            self.grenade = d['grenade']
        if d.get('wheel') is not None:
            self.gun += d['wheel']
            self.gun = self.gun % len(self.guns)
            self.inventory_kd = 1000
            self._reload = False
        if d.get('reload') is not None:
            self.reload()
        if d.get('aim') is not None:
            self.aiming = d['aim']
        if d.get('coords') is not None:
            self.m_coords = d['coords']
        


    def to_death(self):
        self.dead=True
        self.autodel(3)
        self.game.death()
        prts = [
            core.Actor(self.rect.centerx, self.rect.centery, 40,30,0.5,friction=0.1, image=PART_BACK),
            core.Actor(self.rect.centerx, self.rect.centery, 40,30,0.5,friction=0.1, image=PART_HEAD),
            core.Actor(self.rect.centerx, self.rect.centery, 40,30,0.5,friction=0.1, image=PART_LEGS),
        ]
        for i in prts:
            i.speed.xy = self.speed.x+rd(-3,3),self.speed.y-5
            # i.xspeed = self.xspeed+rd(-3,3)
            # i.yspeed = self.yspeed-5
        self.game.world.actors += prts
        fx.blood(self.rect.center, self.game.world, 50)

    def update_control(self,delta, blocks, level, tick=1):
        # HP MANAGEMENT
        # UI
        self.ui.update(delta=delta)
        if self.dead and self.die_kd<1500:self.game.v=0
        if self.dead:
            return
        # if self.hp <= 0: 
        #     self.death()
        if self.hp<=0: self.to_death()
        if self.ammo.get(self.guns[self.gun]) is None: self.ammo[self.guns[self.gun]]=[0,0]

        #UI UPDATE
        amm = self.ammo[self.guns[self.gun]]
        self.hp_bar.value = remap(self.hp, (0,self.max_hp))
        self.time_bar.value = remap(self.aim_time, (0, self.AIM_TIME_MAX))
        self.ammo_but.text = f'{amm[0]}/{amm[1]}'
        self.grenades_but.text = str(self.grenades)
        for w in self.event_ui.widgets:
            for k, v in self.bonus.items():
                if w.text.startswith(k):
                    if v>0:w.text = f'{k}: {v/1000:.1f}'
                    else: w.delete()

    
        if self.reload_kd>0 and self._reload:
            self.reload_but.text = f'{self.reload_kd/1000:.2f}'
        else:
            self.reload_but.text = ''
        self.gun_but.text = self.guns[self.gun].title()

        # TIMERS
        if self.dmg_timer >0: self.dmg_timer-=delta
        if self.shoot_kd >0: self.shoot_kd -= delta
        if self.inventory_kd>0: self.inventory_kd -= delta
        if not self.aiming and self.aim_time<self.AIM_TIME_MAX: self.aim_time += delta/30
        if self.wall_jump_kd>0: self.wall_jump_kd-=delta
        for k,v in self.bonus.items():
            if v>0: self.bonus[k]-=delta

        # ANGLE AND LOOK DIRECTION
        x,y = self.m_coords
        w,h = self.game.frame.get_size()
        x,y = remap(x, (0, cfg.screen_h), (0,w)), remap(y, (0, cfg.screen_v), (0,h))
        x, y =x+self.game.camera.x - self.rect.centerx, self.rect.centery - y - self.game.camera.y

        self.look_r = x>=0
        self.angle = angle((abs(x),-y))

        # RELOAD
        if self._reload:
            if self.reload_kd>0: 
                self.reload_kd -= delta
                self.to_ang = remap(self.reload_kd, (0, GUNS[self.guns[self.gun]]['reload']/GUNS[self.guns[self.gun]]['amount']), (0,360))
            else:
                amm = self.ammo[self.guns[self.gun]]
                if amm[1]>0:
                    m = GUNS[self.guns[self.gun]]['mag']
                    for i in range(1,m+1):
                        if amm[1]-i<=0: 
                            m=i
                            break
                    self.ammo[self.guns[self.gun]] = [m, self.ammo[self.guns[self.gun]][1]-m]
                self._reload = False
        else:self.to_ang=0

        if self.on_ground:
            self.double = True
        self.world = level

        # SIDE MOVE
        ACCEL = PLAYER_ACCELERATION
        if self.move_right and not self.right: self.speed.x += ACCEL -self.speed.x
        if self.move_left and not self.left: self.speed.x -= ACCEL+self.speed.x

        #AIM
        if self.aiming:
            if self.aim_time<=0:self.aiming=False
            else:   self.aim_time-=delta

        # TELEPORT ABIL.
        if self.tp:
            self.tp = False
            # self.rect.center = self.get_point(level, 200)
            xv, yv = vec_to_speed(15, -self.angle)
            self.speed.x += xv if self.look_r else -xv
            self.speed.y = yv

        self.game.world.neo_mode = self.bonus['Time stop']>0
        
        # JUMP
        self._jump(tick)
        if not self.on_ground and 450>self.wall_jump_kd>0 and (self.right or self.left): self.wall_jump_kd = 0

        # SHOOT
        if self.shoot and self.shoot_kd<=0: self._shoot()
        
        # grenades
        if self.grenade: self.throw_genade()
        
        if self.game and self.on_fire>0: fx.fire(self.rect.center,self.game.world,6)
    
    def damage(self, hp):
        if self.bonus['Armor']: hp/=4
        self.hp -= hp
        self.damaged(hp)
        

    def _jump(self, tick):
        if self.jump:
            # if not self.on_ground and self.double:
            #     self.double = False
                # self.xspeed = 0
            if not self.on_ground:
                if self.left and self.move_left and self.look_r and self.wall_jump_kd<=0:
                    self.wall_jump_kd=500
                    self.move_left = False
                    self.speed.x += WALL_JUMP_FORCE
                    self.double = True
                elif self.right and self.move_right and not self.look_r and self.wall_jump_kd<=0:
                    self.wall_jump_kd=500
                    self.move_right = False
                    self.speed.x -= WALL_JUMP_FORCE
                    self.double = True
                elif self.double:
                    fx.fire((self.rect.centerx,self.rect.bottom),self.game.world,20)
                    self.double = False
                else:return
            self.jump = False
            self.speed.y = -JUMP_FORCE
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
        gun = GUNS[self.guns[self.gun]]
        acc = gun['acc'] if self.aiming else gun['acc']*2
        for i in range(gun['amount'] if not self.bonus['Double gun']>0 else gun['amount']*2):
            xvel, yvel = vec_to_speed(gun['speed'], self.angle+(rd(-acc*5, acc*5)/3))
            d = gun['dmg']
            b = Bullet(self.rect.centerx,
                    self.rect.centery,
                    xvel if self.look_r else -xvel,
                    -yvel,
                    gun['bull_img'], self.angle,rd(int(d-(d*0.2)), int(d+(d*0.2))), self
            )
            self.game.world.actors.append(b)

        self.ammo[self.guns[self.gun]][0] -= 1
        xv,yv=vec_to_speed(gun['back'] if not self.bonus['Double gun']>0 else gun['back']*2, self.angle-180)
        self.speed.x, self.speed.y = self.speed.x+(xv if self.look_r else-xv), self.speed.y-yv
        if self.shoot and self.game: self.game.shake = gun['shake']

        self.recoil=gun['recoil']
        self.shoot_kd = gun['kd']
        self.shoot = gun['auto']
        if sounds: SOUNDS['shoot'].play()
        self.game.stats['shoots']+=1
        # write_stat('shoots', get_stat('shoots')+1)
    
    def throw_genade(self):
        self.grenade=False
        if self.grenades<=0: return
        self.grenades-=1
        xv,yv = vec_to_speed(20 if self.aiming else 15, self.angle)
        self.game.world.actors.append(Grenade(self.rect.centerx,self.rect.y+10,xv if self.look_r else -xv, -yv, self.game))
    
    # def hit(self, actor):
    #     if isinstance(actor,level.Block):self.wall_jump_kd=0
    #     return super().hit(actor)

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

    def rotate(self):
        self.img = pg.transform.flip(self.img, True, False)
        
    def debug_draw(self, screen, camera):
        x,y = pg.mouse.get_pos()
        pg.draw.line(screen,'yellow', real(self.rect.center, camera),pg.mouse.get_pos())
        return super().debug_draw(screen, camera)

    def draw(self, screen: pg.Surface, camera: pg.Rect):
        self.img = IMGS['BACK'].copy()
        self.img.blit(IMGS['PLAYER'].copy(), (0,0))
        # if self.on_ground:
        #     if self.xspeed == 0:
        #         self.img.blit(PLAYER_LEGS_IDLE, (0, 53))
        #     else:
        #         self.img.blit(PLAYER_LEGS_R if self.r_leg else PLAYER_LEGS_L, (0, 53))
        # else:
        #     self.img.blit(PLAYER_LEGS_AIR, (0, 53))
        # self.img.blit(PLAYER_LEGS_AIR, (0, 0))
        
        off = 0 if self.look_r else -30
        offy = 0 if not self.aiming else -5
        if not self.on_ground and ((self.left and self.move_left and self.look_r) or (self.right and self.move_right and not self.look_r)) and self.wall_jump_kd<=0:
            self.img = pg.transform.rotate(self.img, -30)
            off = -15 if self.look_r else -55
        
        # GUN IMG PROCC.
        gun_img = pg.transform.rotate(GUNS[self.guns[self.gun]]['img'].copy(), self.angle-self.to_ang+(self.recoil*remap(self.shoot_kd, (0,GUNS[self.guns[self.gun]]['kd']))))
        w,h=gun_img.get_width()/2,gun_img.get_height()/2
        self.img.blit(gun_img, (gun_img.get_rect().x+30+GUNS[self.guns[self.gun]]['offx']-w, gun_img.get_rect().y+35+offy+GUNS[self.guns[self.gun]]['offy']-h))
        if self.bonus['Double gun']>0: self.img.blit(gun_img, (gun_img.get_rect().x+35+GUNS[self.guns[self.gun]]['offx']-w, gun_img.get_rect().y+30+offy+GUNS[self.guns[self.gun]]['offy']-h))
        # if not self.look_r and self.xspeed > 0: self.rotate()
        # if self.look_r and self.xspeed < 0: self.rotate()

        # WALL JUMP ROTATE
        dw,dh=0,0
        if self.wall_jump_kd>0:
            w,h = self.img.get_size()
            wall_ang = remap(self.wall_jump_kd, (0,500),(0,360))
            pivot = (12,10) if self.look_r else (5, 10)
            self.img = pg.transform.rotate(self.img, wall_ang)
            dw,dh =(self.img.get_width()/2, self.img.get_height()/2)- pg.math.Vector2(*pivot).rotate(-wall_ang)-(24,20)
        
        if self.dead: self.img = PLAYER_IMG_DEAD
        if not self.look_r: self.rotate()
        if not self.dead:
            if self.dmg_timer > 0: self.img.blit(RED_TINT,(0,0),special_flags=pg.BLEND_RGB_ADD)
            # if self.inventory_kd>0:self.img.blit(self.font.render(f'[{self.guns[self.gun]}]',False,'white'), (-off,0))
        # screen.fill('green',(self.pre_rect.x - camera.x, self.pre_rect.y + camera.y, self.pre_rect.w, self.pre_rect.h))
        
        # if self.game.world.neo_mode:
        #     neg = pg.Surface(self.img.get_size(), pg.SRCALPHA)
        #     neg.fill((255, 255, 255))
        #     neg.blit(self.img, (0, 0), special_flags=pg.BLEND_SUB)
        #     self.img = neg

        mask = pg.mask.from_surface(self.img).to_surface()
        mask.set_colorkey('black')
        if not self.dead and self.visible:
            if self.bonus['Armor']>0:
                screen.blit(mask, (self.rect.x - camera.x+off-3-dw-2, self.rect.y - camera.y-dh))
                screen.blit(mask, (self.rect.x - camera.x+off-3-dw+2, self.rect.y - camera.y-dh))
                screen.blit(mask, (self.rect.x - camera.x+off-3-dw, self.rect.y - camera.y-dh-2))
                screen.blit(mask, (self.rect.x - camera.x+off-3-dw, self.rect.y - camera.y-dh+2))
            screen.blit(self.img, (self.rect.x - camera.x+off-3-dw, self.rect.y - camera.y-dh))
        self.ui.render(self.game.screen)
