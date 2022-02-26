# Auto-generated, can be edited
from game import *

spawn_pos = (40,40)
background = 'game\content/bg2.png'
guns = []
sun_level = 0

####DONT TOUCH####
# Auto-generated in game.level
ais = [
	enemies.ShoterAI(x=500, y=800, gun='minigun'),
	enemies.ShoterAI(x=550, y=620, gun='rifle')
]
actors = [
	objects.Portal(x1=40, y1=880, x2=300, y2=840, w=120, h=40),
	objects.ScreenConditionTriger(x=0, y=800, w=300, h=80, condition='game.player.xspeed!=0', image='game/content/ui/to_move.png'),
	objects.Aid(x=1400, y=975, hp=50),
	objects.Ammo(x=500, y=900, ammo={'shootgun': 20, 'rifle': 60}),
	objects.GunsCase(x=80, y=940, guns=['rifle', 'shootgun']),
	objects.Ammo(x=40, y=320, ammo={}),
	objects.LevelTravelTriger(x=560, y=840, w=40, h=120, levelname='ldld')
]
blocks = [
	level.Block(0,-40,'='),
	level.Block(0,0,'='),
	level.Block(0,40,'='),
	level.Block(0,80,'='),
	level.Block(0,120,'='),
	level.Block(0,160,'='),
	level.Block(0,200,'='),
	level.Block(0,240,'='),
	level.Block(0,280,'='),
	level.Block(0,320,'='),
	level.Block(0,360,'='),
	level.Block(0,400,'='),
	level.Block(0,440,'='),
	level.Block(0,480,'='),
	level.Block(0,520,'='),
	level.Block(0,560,'='),
	level.Block(0,600,'='),
	level.Block(0,640,'='),
	level.Block(0,680,'='),
	level.Block(0,720,'='),
	level.Block(0,760,'='),
	level.Block(0,800,'='),
	level.Block(0,840,'='),
	level.Block(0,880,'='),
	level.Block(0,920,'='),
	level.Block(0,960,'='),
	level.Block(40,960,'='),
	level.Block(80,960,'='),
	level.Block(120,960,'='),
	level.Block(160,960,'='),
	level.Block(200,960,'='),
	level.Block(240,960,'='),
	level.Block(280,960,'='),
	level.Block(320,960,'='),
	level.Block(360,960,'='),
	level.Block(400,960,'='),
	level.Block(440,960,'='),
	level.Block(480,960,'='),
	level.Block(520,960,'='),
	level.Block(560,960,'='),
	level.Block(600,960,'='),
	level.Block(600,920,'='),
	level.Block(600,880,'='),
	level.Block(600,840,'='),
	level.Block(600,800,'='),
	level.Block(600,760,'='),
	level.Block(600,720,'='),
	level.Block(600,680,'='),
	level.Block(600,640,'='),
	level.Block(600,600,'='),
	level.Block(600,560,'='),
	level.Block(600,520,'='),
	level.Block(640,480,'='),
	level.Block(640,440,'='),
	level.Block(640,400,'='),
	level.Block(640,360,'='),
	level.Block(600,320,'='),
	level.Block(600,280,'='),
	level.Block(600,240,'='),
	level.Block(600,200,'='),
	level.Block(600,160,'='),
	level.Block(600,120,'='),
	level.Block(600,80,'='),
	level.Block(600,40,'='),
	level.Block(600,0,'='),
	level.Block(600,-40,'='),
	level.Block(600,-80,'='),
	level.Block(560,0,'='),
	level.Block(560,80,'='),
	level.Block(560,120,'='),
	level.Block(560,160,'='),
	level.Block(560,200,'='),
	level.Block(560,240,'='),
	level.Block(560,280,'='),
	level.Block(560,320,'='),
	level.Block(560,360,'='),
	level.Block(560,400,'='),
	level.Block(560,440,'='),
	level.Block(600,440,'='),
	level.Block(600,480,'='),
	level.Block(600,400,'='),
	level.Block(600,360,'='),
	level.Block(280,280,'='),
	level.Block(240,280,'='),
	level.Block(-160,600,'='),
	level.Block(40,480,'='),
	level.Block(440,280,'='),
	level.Block(-40,600,'='),
	level.Block(-200,120,'='),
	level.Block(-240,120,'='),
	level.Block(360,280,'=')
]
