from game import *

spawn_pos = (40, 840)
background = 'game\\content/bg2.png'
guns = [
	
]
ais = [
	enemies.ShoterAI(x=976, y=900, gun='rifle')
]
actors = [
	objects.Aid(x=468, y=969, hp=50),
	objects.Ammo(x=410, y=977, ammo={'shootgun': 20}),
	objects.GunsCase(x=365, y=976, guns=['rifle', 'shootgun', 'minigun', 'sniper']),
	objects.Image(x=100, y=850, image='game/content/ui/arrow.png', rotation=225, scale=1.0),
	objects.Image(x=340, y=860, image='game/content/ui/arrow.png', rotation=0, scale=1),
	objects.Image(x=190, y=710, image='game/content/ui/arrow.png', rotation=180, scale=1.0),
	objects.Grenades(x=410, y=580, amount=10),
	objects.Grenades(x=230, y=580, amount=10),
	objects.LevelTravelTriger(x=1840, y=883, w=40, h=120, levelname='empty'),
	objects.Aid(x=507, y=972, hp=50),
	objects.CameraTargetTriger(x=47, y=654, w=400, h=400, target_x=1000, target_y=800, timer=5000)
]
blocks = [
	level.Block(0,-40,'-'),
	level.Block(0,0,'-'),
	level.Block(0,40,'-'),
	level.Block(0,80,'-'),
	level.Block(0,120,'-'),
	level.Block(0,160,'-'),
	level.Block(0,200,'-'),
	level.Block(0,240,'-'),
	level.Block(0,280,'-'),
	level.Block(0,320,'-'),
	level.Block(0,400,'-'),
	level.Block(0,480,'-'),
	level.Block(0,640,'-'),
	level.Block(0,600,'-'),
	level.Block(0,560,'-'),
	level.Block(0,520,'-'),
	level.Block(0,440,'-'),
	level.Block(0,360,'-'),
	level.Block(0,840,'-'),
	level.Block(0,800,'-'),
	level.Block(0,760,'-'),
	level.Block(0,720,'-'),
	level.Block(0,680,'-'),
	level.Block(0,880,'-'),
	level.Block(0,920,'-'),
	level.Block(0,960,'-'),
	level.Block(0,1000,'-'),
	level.Block(40,1000,'-'),
	level.Block(280,1000,'-'),
	level.Block(240,1000,'-'),
	level.Block(200,1000,'-'),
	level.Block(160,1000,'-'),
	level.Block(120,1000,'-'),
	level.Block(80,1000,'-'),
	level.Block(320,1000,'-'),
	level.Block(360,1000,'-'),
	level.Block(400,1000,'-'),
	level.Block(440,1000,'-'),
	level.Block(480,1000,'-'),
	level.Block(520,1000,'-'),
	level.Block(560,1000,'-'),
	level.Block(600,1000,'-'),
	level.Block(640,1000,'-'),
	level.Block(680,1000,'-'),
	level.Block(720,1000,'-'),
	level.Block(760,1000,'-'),
	level.Block(800,1000,'-'),
	level.Block(840,1000,'-'),
	level.Block(880,1000,'-'),
	level.Block(920,1000,'-'),
	level.Block(960,1000,'-'),
	level.Block(1160,1000,'-'),
	level.Block(1200,1000,'-'),
	level.Block(1000,1000,'-'),
	level.Block(1040,1000,'-'),
	level.Block(1080,1000,'-'),
	level.Block(1120,1000,'-'),
	level.Block(1200,640,'-'),
	level.Block(1200,600,'-'),
	level.Block(1200,560,'-'),
	level.Block(1200,520,'-'),
	level.Block(1200,440,'-'),
	level.Block(1200,360,'-'),
	level.Block(1200,320,'-'),
	level.Block(1200,240,'-'),
	level.Block(1200,280,'-'),
	level.Block(1200,400,'-'),
	level.Block(1200,480,'-'),
	level.Block(1200,200,'-'),
	level.Block(1200,160,'-'),
	level.Block(1200,120,'-'),
	level.Block(1200,80,'-'),
	level.Block(1200,40,'-'),
	level.Block(1200,0,'-'),
	level.Block(1200,-40,'-'),
	level.Block(1160,-40,'-'),
	level.Block(1120,-40,'-'),
	level.Block(1080,-40,'-'),
	level.Block(1040,-40,'-'),
	level.Block(1000,-40,'-'),
	level.Block(960,-40,'-'),
	level.Block(920,-40,'-'),
	level.Block(880,-40,'-'),
	level.Block(840,-40,'-'),
	level.Block(800,-40,'-'),
	level.Block(760,-40,'-'),
	level.Block(720,-40,'-'),
	level.Block(40,-40,'-'),
	level.Block(80,-40,'-'),
	level.Block(120,-40,'-'),
	level.Block(160,-40,'-'),
	level.Block(200,-40,'-'),
	level.Block(240,-40,'-'),
	level.Block(280,-40,'-'),
	level.Block(320,-40,'-'),
	level.Block(360,-40,'-'),
	level.Block(400,-40,'-'),
	level.Block(440,-40,'-'),
	level.Block(480,-40,'-'),
	level.Block(520,-40,'-'),
	level.Block(560,-40,'-'),
	level.Block(600,-40,'-'),
	level.Block(640,-40,'-'),
	level.Block(680,-40,'-'),
	level.Block(1240,1000,'-'),
	level.Block(1280,1000,'-'),
	level.Block(1320,1000,'-'),
	level.Block(1360,1000,'-'),
	level.Block(1400,1000,'-'),
	level.Block(1640,1000,'-'),
	level.Block(1880,1000,'-'),
	level.Block(1840,1000,'-'),
	level.Block(1800,1000,'-'),
	level.Block(1760,1000,'-'),
	level.Block(1440,1000,'-'),
	level.Block(1480,1000,'-'),
	level.Block(1520,1000,'-'),
	level.Block(1560,1000,'-'),
	level.Block(1600,1000,'-'),
	level.Block(1680,1000,'-'),
	level.Block(1720,1000,'-'),
	level.Block(1880,960,'-'),
	level.Block(1880,920,'-'),
	level.Block(1880,880,'-'),
	level.Block(1880,840,'-'),
	level.Block(1880,800,'-'),
	level.Block(1880,760,'-'),
	level.Block(1880,720,'-'),
	level.Block(1840,720,'-'),
	level.Block(1840,680,'-'),
	level.Block(1840,640,'-'),
	level.Block(1840,600,'-'),
	level.Block(1800,600,'-'),
	level.Block(1760,600,'-'),
	level.Block(1720,600,'-'),
	level.Block(1680,600,'-'),
	level.Block(1640,600,'-'),
	level.Block(1600,600,'-'),
	level.Block(1560,600,'-'),
	level.Block(1520,600,'-'),
	level.Block(1480,600,'-'),
	level.Block(1440,600,'-'),
	level.Block(1400,600,'-'),
	level.Block(1360,600,'-'),
	level.Block(1320,600,'-'),
	level.Block(1280,600,'-'),
	level.Block(1240,600,'-'),
	level.Block(1160,600,'-')
]
