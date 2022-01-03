from game import *

spawn_pos = (40, 40)
background = 'game\\content/bg2.png'
guns = [
	'sniper'
]
ais = [
	enemies.ShoterAI(x=1140, y=600, gun='rifle'),
	enemies.MeleeAI(x=960, y=580),
	enemies.MeleeAI(x=960, y=580),
	enemies.MeleeAI(x=960, y=580),
	enemies.ShoterAI(x=1310, y=680, gun='shootgun'),
	enemies.ShoterAI(x=1180, y=820, gun='rifle'),
	enemies.ShoterAI(x=1360, y=650, gun='rifle'),
	enemies.ShoterAI(x=1280, y=440, gun='rifle'),
	enemies.ShoterAI(x=1080, y=430, gun='rifle'),
	enemies.MeleeAI(x=950, y=700),
	enemies.MeleeAI(x=1420, y=520)
]
actors = [
	objects.Portal(x1=280, y1=1000, x2=600, y2=1000, w=80, h=40),
	objects.Aid(x=60, y=860, hp=50),
	objects.Ammo(x=400, y=860, ammo={'minigun': 300, 'rifle': 120}),
	objects.GunsCase(x=224, y=969, guns=['minigun', 'rifle', 'shootgun']),
	objects.Text(x=200, y=800, text='lol some text', size=30, color='white'),
	objects.Image(x=250, y=700, image='game/content/ui/ammo.png', rotation=50, scale=2.0),
	objects.Grenades(x=680, y=380, amount=10),
	objects.ArmorBonus(x=127, y=966, time=50000),
	objects.DoubleGunBonus(x=158, y=977, time=5000),
	objects.CameraTargetTriger(x=102, y=346, w=700, h=800, target_x=520, target_y=800, timer=0),
	objects.ZoomTriger(x=102, y=360, w=700, h=700, zoom=1.5),
	objects.TimeStopBonus(x=201, y=967, time=50000)
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
	level.Block(0,360,'-'),
	level.Block(0,400,'-'),
	level.Block(0,440,'-'),
	level.Block(0,480,'-'),
	level.Block(0,520,'-'),
	level.Block(0,560,'-'),
	level.Block(0,600,'-'),
	level.Block(0,640,'-'),
	level.Block(0,680,'-'),
	level.Block(0,720,'-'),
	level.Block(0,760,'-'),
	level.Block(0,800,'-'),
	level.Block(0,840,'-'),
	level.Block(0,880,'-'),
	level.Block(0,920,'-'),
	level.Block(0,960,'-'),
	level.Block(0,1000,'-'),
	level.Block(40,1000,'-'),
	level.Block(80,1000,'-'),
	level.Block(120,1000,'-'),
	level.Block(160,1000,'-'),
	level.Block(200,1000,'-'),
	level.Block(240,1000,'-'),
	level.Block(360,1000,'-'),
	level.Block(400,1000,'-'),
	level.Block(440,1000,'-'),
	level.Block(480,1000,'-'),
	level.Block(520,1000,'-'),
	level.Block(560,1000,'-'),
	level.Block(680,1000,'-'),
	level.Block(720,1000,'-'),
	level.Block(760,1000,'-'),
	level.Block(800,1000,'-'),
	level.Block(840,1000,'-'),
	level.Block(880,1000,'-'),
	level.Block(920,1000,'-'),
	level.Block(960,1000,'-'),
	level.Block(1000,1000,'-'),
	level.Block(1040,1000,'-'),
	level.Block(1080,1000,'-'),
	level.Block(1120,1000,'-'),
	level.Block(1160,1000,'-'),
	level.Block(1200,1000,'-'),
	level.Block(1240,1000,'-'),
	level.Block(1280,1000,'-'),
	level.Block(1320,1000,'-'),
	level.Block(1360,1000,'-'),
	level.Block(1400,1000,'-'),
	level.Block(1440,1000,'-'),
	level.Block(1480,1000,'-'),
	level.Block(1520,1000,'-'),
	level.Block(1560,1000,'-'),
	level.Block(1600,1000,'-'),
	level.Block(1640,1000,'-'),
	level.Block(1680,1000,'-'),
	level.Block(1720,1000,'-'),
	level.Block(1760,1000,'-'),
	level.Block(1800,1000,'-'),
	level.Block(1840,1000,'-'),
	level.Block(1880,1000,'-'),
	level.Block(1880,960,'-'),
	level.Block(1880,920,'-'),
	level.Block(1880,880,'-'),
	level.Block(1880,840,'-'),
	level.Block(1880,800,'-'),
	level.Block(1880,760,'-'),
	level.Block(1880,720,'-'),
	level.Block(1880,680,'-'),
	level.Block(1880,640,'-'),
	level.Block(1880,600,'-'),
	level.Block(1880,560,'-'),
	level.Block(1880,520,'-'),
	level.Block(1880,480,'-'),
	level.Block(1880,440,'-'),
	level.Block(1880,400,'-'),
	level.Block(1880,360,'-'),
	level.Block(1880,320,'-'),
	level.Block(1880,280,'-'),
	level.Block(1880,240,'-'),
	level.Block(1880,200,'-'),
	level.Block(1880,160,'-'),
	level.Block(1880,120,'-'),
	level.Block(1880,80,'-'),
	level.Block(1880,40,'-'),
	level.Block(1880,0,'-'),
	level.Block(1880,-40,'-'),
	level.Block(1840,-40,'-'),
	level.Block(1800,-40,'-'),
	level.Block(1760,-40,'-'),
	level.Block(1720,-40,'-'),
	level.Block(1680,-40,'-'),
	level.Block(1640,-40,'-'),
	level.Block(1600,-40,'-'),
	level.Block(1560,-40,'-'),
	level.Block(1520,-40,'-'),
	level.Block(1480,-40,'-'),
	level.Block(1440,-40,'-'),
	level.Block(1400,-40,'-'),
	level.Block(1360,-40,'-'),
	level.Block(1320,-40,'-'),
	level.Block(1280,-40,'-'),
	level.Block(1240,-40,'-'),
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
	level.Block(680,-40,'-'),
	level.Block(640,-40,'-'),
	level.Block(600,-40,'-'),
	level.Block(560,-40,'-'),
	level.Block(520,-40,'-'),
	level.Block(480,-40,'-'),
	level.Block(440,-40,'-'),
	level.Block(400,-40,'-'),
	level.Block(360,-40,'-'),
	level.Block(320,-40,'-'),
	level.Block(280,-40,'-'),
	level.Block(240,-40,'-'),
	level.Block(200,-40,'-'),
	level.Block(160,-40,'-'),
	level.Block(120,-40,'-'),
	level.Block(80,-40,'-'),
	level.Block(40,-40,'-'),
	level.Block(240,1040,'-'),
	level.Block(280,1040,'-'),
	level.Block(320,1040,'-'),
	level.Block(360,1040,'-'),
	level.Block(560,1040,'-'),
	level.Block(600,1040,'-'),
	level.Block(640,1040,'-'),
	level.Block(680,1040,'-'),
	level.Block(280,280,'='),
	level.Block(320,280,'=')
]
