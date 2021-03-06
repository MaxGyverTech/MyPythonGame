from game import *

spawn_pos = (1960, 40)
background = 'game\\content/bg2.png'
guns = [
	
]
sun_level = 0

#### Dont delete this comment, edit only script inside ####

# called once on level loading
def load(game):
	pass

# called every frame update
def update(game):
	pass

###########################################################

ais = [
	enemies.ShoterAI(x=2175, y=382, gun='shootgun'),
	enemies.MeleeAI(x=1392, y=114),
	enemies.MeleeAI(x=1280, y=30),
	enemies.ShoterAI(x=1080, y=80, gun='rifle'),
	enemies.MeleeAI(x=1820, y=-1090),
	enemies.MeleeAI(x=1710, y=-1090),
	enemies.MeleeAI(x=1430, y=-1200),
	enemies.MeleeAI(x=1230, y=-1140),
	enemies.MeleeAI(x=1390, y=-940),
	enemies.MeleeAI(x=2920, y=-1153),
	enemies.ShoterAI(x=1680, y=-990, gun='rifle'),
	enemies.ShoterAI(x=3260, y=-1179, gun='minigun'),
	enemies.ShoterAI(x=1368, y=-1046, gun='shootgun'),
	enemies.MeleeAI(x=3340, y=-980),
	enemies.MeleeAI(x=3600, y=-850),
	enemies.MeleeAI(x=3850, y=-1100),
	enemies.MeleeAI(x=3600, y=-1170),
	enemies.MeleeAI(x=2820, y=-980),
	enemies.ShoterAI(x=3190, y=-980, gun='rifle'),
	enemies.ShoterAI(x=2900, y=-890, gun='shootgun')
]
actors = [
	objects.GunsCase(x=2080, y=88, guns=['rocket_gun']),
	objects.Ammo(x=2113, y=92, ammo={'rocket_gun': 15, 'rifle': 120}),
	objects.Text(x=2062, y=7, text='New gun: rocket gun', size=30, color='white'),
	objects.Text(x=2145, y=36, text='Warning!', size=30, color='red'),
	objects.Text(x=2133, y=67, text='You can damage yourself', size=30, color='white'),
	objects.Text(x=1789, y=1, text=' try to', size=30, color='white'),
	objects.Text(x=1731, y=1, text="Don't", size=30, color='red'),
	objects.Text(x=1749, y=36, text='break glass', size=30, color='white'),
	objects.Text(x=1773, y=71, text='with rockets', size=30, color='white'),
	objects.TimeStopBonus(x=2413, y=-1084, time=25000),
	objects.Portal(x1=958, y1=-1397, x2=1000, y2=-160, w=80, h=40),
	objects.Aid(x=2261, y=-1075, hp=150),
	objects.Ammo(x=2307, y=-1070, ammo={'minigun': 200, 'shootgun': 20, 'rifle': 150}),
	objects.DoubleGunBonus(x=980, y=-870, time=5000),
	objects.ArmorBonus(x=1024, y=-876, time=5000),
	objects.Portal(x1=2759, y1=-760, x2=3720, y2=-760, w=120, h=40),
	objects.LevelTravelTriger(x=4241, y=-1239, w=40, h=80, levelname='arena2')
]
blocks = [
	level.Block(1920,-40,'#'),
	level.Block(1920,0,'#'),
	level.Block(1920,40,'#'),
	level.Block(1920,80,'#'),
	level.Block(1920,120,'#'),
	level.Block(1960,120,'#'),
	level.Block(2000,120,'#'),
	level.Block(2040,120,'#'),
	level.Block(2080,120,'#'),
	level.Block(2120,120,'#'),
	level.Block(2160,120,'#'),
	level.Block(2200,120,'#'),
	level.Block(2240,120,'#'),
	level.Block(2280,120,'#'),
	level.Block(1960,-40,'#'),
	level.Block(2000,-40,'#'),
	level.Block(2040,-40,'#'),
	level.Block(2080,-40,'#'),
	level.Block(2120,-40,'#'),
	level.Block(2160,-40,'#'),
	level.Block(2200,-40,'#'),
	level.Block(2240,-40,'#'),
	level.Block(2280,-40,'#'),
	level.Block(2320,-40,'#'),
	level.Block(2320,120,'#'),
	level.Block(2360,-40,'#'),
	level.Block(2400,-40,'#'),
	level.Block(2440,-40,'#'),
	level.Block(2440,0,'#'),
	level.Block(2440,40,'#'),
	level.Block(2440,80,'#'),
	level.Block(2440,120,'#'),
	level.Block(2440,160,'#'),
	level.Block(2440,200,'#'),
	level.Block(2440,240,'#'),
	level.Block(2440,280,'#'),
	level.Block(2440,320,'#'),
	level.Block(2440,360,'#'),
	level.Block(2440,400,'#'),
	level.Block(2440,440,'%'),
	level.Block(2400,440,'%'),
	level.Block(2360,440,'%'),
	level.Block(2320,440,'%'),
	level.Block(2280,440,'%'),
	level.Block(2240,440,'%'),
	level.Block(2200,440,'%'),
	level.Block(2160,440,'%'),
	level.Block(2120,440,'%'),
	level.Block(2080,440,'%'),
	level.Block(2040,440,'%'),
	level.Block(2000,440,'%'),
	level.Block(1960,440,'%'),
	level.Block(2320,160,'#'),
	level.Block(2320,200,'#'),
	level.Block(2320,240,'#'),
	level.Block(2280,240,'#'),
	level.Block(2240,240,'#'),
	level.Block(2200,240,'#'),
	level.Block(2160,240,'#'),
	level.Block(2120,240,'#'),
	level.Block(2080,240,'#'),
	level.Block(2040,240,'#'),
	level.Block(2000,240,'#'),
	level.Block(1960,240,'#'),
	level.Block(1920,240,'#'),
	level.Block(1920,440,'%'),
	level.Block(1880,440,'%'),
	level.Block(1840,440,'%'),
	level.Block(1800,440,'%'),
	level.Block(1800,400,'#'),
	level.Block(1800,360,'#'),
	level.Block(1800,320,'#'),
	level.Block(1800,280,'#'),
	level.Block(1800,240,'#'),
	level.Block(1800,200,'#'),
	level.Block(1920,160,'#'),
	level.Block(1920,200,'#'),
	level.Block(1760,200,'#'),
	level.Block(1720,200,'#'),
	level.Block(1680,200,'#'),
	level.Block(1640,200,'#'),
	level.Block(1600,200,'#'),
	level.Block(1560,200,'#'),
	level.Block(1520,200,'#'),
	level.Block(1480,200,'#'),
	level.Block(1440,200,'#'),
	level.Block(1360,200,'#'),
	level.Block(1320,200,'#'),
	level.Block(1240,200,'#'),
	level.Block(1200,200,'#'),
	level.Block(1120,200,'#'),
	level.Block(1080,200,'#'),
	level.Block(1040,200,'#'),
	level.Block(1160,200,'#'),
	level.Block(1280,200,'#'),
	level.Block(1400,200,'#'),
	level.Block(1920,-80,'#'),
	level.Block(1920,-120,'#'),
	level.Block(1920,-160,'#'),
	level.Block(1880,-160,'#'),
	level.Block(1840,-160,'#'),
	level.Block(1800,-160,'#'),
	level.Block(1760,-160,'#'),
	level.Block(1720,-160,'#'),
	level.Block(1680,-160,'#'),
	level.Block(1640,-160,'#'),
	level.Block(1600,-160,'#'),
	level.Block(1560,-160,'#'),
	level.Block(1520,-160,'#'),
	level.Block(1480,-160,'#'),
	level.Block(1440,-160,'#'),
	level.Block(1400,-160,'#'),
	level.Block(1360,-160,'#'),
	level.Block(1320,-160,'#'),
	level.Block(1280,-160,'#'),
	level.Block(1240,-160,'#'),
	level.Block(1200,-160,'#'),
	level.Block(1160,-160,'#'),
	level.Block(1120,-160,'#'),
	level.Block(1080,-160,'#'),
	level.Block(960,-160,'#'),
	level.Block(1000,200,'#'),
	level.Block(960,200,'#'),
	level.Block(1680,160,'/'),
	level.Block(1680,120,'/'),
	level.Block(1680,80,'/'),
	level.Block(1680,-120,'/'),
	level.Block(1680,40,'/'),
	level.Block(1680,0,'/'),
	level.Block(1680,-40,'/'),
	level.Block(1680,-80,'/'),
	level.Block(1760,-40,'#'),
	level.Block(960,160,'#'),
	level.Block(960,120,'#'),
	level.Block(960,80,'#'),
	level.Block(960,40,'#'),
	level.Block(960,0,'#'),
	level.Block(960,-120,'#'),
	level.Block(960,-80,'#'),
	level.Block(960,-40,'#'),
	level.Block(960,-200,'#'),
	level.Block(1000,-200,'#'),
	level.Block(1040,-200,'#'),
	level.Block(1080,-200,'#'),
	level.Block(1120,-200,'#'),
	level.Block(920,-840,'%'),
	level.Block(960,-840,'%'),
	level.Block(1000,-840,'%'),
	level.Block(1040,-840,'%'),
	level.Block(1080,-840,'%'),
	level.Block(1120,-840,'%'),
	level.Block(1160,-840,'%'),
	level.Block(1200,-840,'%'),
	level.Block(1240,-840,'%'),
	level.Block(1280,-840,'%'),
	level.Block(1320,-840,'%'),
	level.Block(1360,-840,'%'),
	level.Block(1400,-840,'%'),
	level.Block(1440,-840,'%'),
	level.Block(1480,-840,'%'),
	level.Block(1520,-840,'%'),
	level.Block(1560,-840,'%'),
	level.Block(1600,-840,'%'),
	level.Block(1640,-840,'%'),
	level.Block(1680,-840,'%'),
	level.Block(1720,-840,'%'),
	level.Block(1760,-840,'%'),
	level.Block(1800,-840,'%'),
	level.Block(1840,-840,'%'),
	level.Block(1880,-840,'%'),
	level.Block(1920,-840,'%'),
	level.Block(1960,-840,'%'),
	level.Block(2000,-840,'%'),
	level.Block(2040,-840,'%'),
	level.Block(2080,-840,'%'),
	level.Block(2120,-840,'%'),
	level.Block(920,-880,'#'),
	level.Block(920,-920,'#'),
	level.Block(920,-960,'#'),
	level.Block(920,-1000,'#'),
	level.Block(920,-1040,'#'),
	level.Block(920,-1080,'#'),
	level.Block(920,-1120,'#'),
	level.Block(920,-1160,'#'),
	level.Block(920,-1200,'#'),
	level.Block(920,-1240,'#'),
	level.Block(920,-1280,'#'),
	level.Block(920,-1320,'#'),
	level.Block(920,-1360,'#'),
	level.Block(920,-1400,'#'),
	level.Block(920,-1440,'#'),
	level.Block(960,-1440,'#'),
	level.Block(1000,-1440,'#'),
	level.Block(1040,-1440,'#'),
	level.Block(1040,-1400,'#'),
	level.Block(1080,-1400,'#'),
	level.Block(1120,-1400,'#'),
	level.Block(1160,-1400,'#'),
	level.Block(1200,-1400,'#'),
	level.Block(1240,-1400,'#'),
	level.Block(1280,-1400,'#'),
	level.Block(1320,-1400,'#'),
	level.Block(1440,-1400,'#'),
	level.Block(1480,-1400,'#'),
	level.Block(1520,-1400,'#'),
	level.Block(1560,-1400,'#'),
	level.Block(1600,-1400,'#'),
	level.Block(1640,-1400,'#'),
	level.Block(1680,-1400,'#'),
	level.Block(1400,-1400,'#'),
	level.Block(1360,-1400,'#'),
	level.Block(1720,-1400,'#'),
	level.Block(1760,-1400,'#'),
	level.Block(1800,-1400,'#'),
	level.Block(1840,-1400,'#'),
	level.Block(1880,-1400,'#'),
	level.Block(1920,-1400,'#'),
	level.Block(1960,-1400,'#'),
	level.Block(2000,-1400,'#'),
	level.Block(2040,-1400,'#'),
	level.Block(2080,-1400,'#'),
	level.Block(2120,-1400,'#'),
	level.Block(2120,-1360,'#'),
	level.Block(2120,-1320,'#'),
	level.Block(2120,-1280,'#'),
	level.Block(2120,-1240,'#'),
	level.Block(2120,-1200,'#'),
	level.Block(2120,-1160,'/'),
	level.Block(2120,-1120,'/'),
	level.Block(2120,-1080,'/'),
	level.Block(2120,-1040,'#'),
	level.Block(2120,-1000,'#'),
	level.Block(2120,-960,'#'),
	level.Block(2120,-920,'#'),
	level.Block(2120,-880,'#'),
	level.Block(2160,-1040,'#'),
	level.Block(2200,-1040,'#'),
	level.Block(2240,-1040,'#'),
	level.Block(2280,-1040,'#'),
	level.Block(2320,-1040,'#'),
	level.Block(2360,-1040,'#'),
	level.Block(2400,-1040,'#'),
	level.Block(2440,-1040,'-'),
	level.Block(2480,-1040,'-'),
	level.Block(2480,-1000,'-'),
	level.Block(2480,-960,'-'),
	level.Block(2480,-920,'-'),
	level.Block(2480,-880,'-'),
	level.Block(2480,-840,'-'),
	level.Block(2480,-800,'-'),
	level.Block(2480,-760,'-'),
	level.Block(2520,-760,'-'),
	level.Block(2560,-760,'-'),
	level.Block(2600,-760,'-'),
	level.Block(2640,-760,'-'),
	level.Block(2680,-760,'-'),
	level.Block(2720,-760,'-'),
	level.Block(2880,-760,'-'),
	level.Block(2920,-760,'-'),
	level.Block(2960,-760,'-'),
	level.Block(3000,-760,'-'),
	level.Block(3040,-760,'-'),
	level.Block(3080,-760,'-'),
	level.Block(3280,-760,'-'),
	level.Block(3320,-760,'-'),
	level.Block(3360,-760,'-'),
	level.Block(3400,-760,'-'),
	level.Block(3440,-760,'-'),
	level.Block(3480,-760,'-'),
	level.Block(3240,-760,'-'),
	level.Block(3200,-760,'-'),
	level.Block(3120,-760,'-'),
	level.Block(3520,-760,'-'),
	level.Block(3560,-760,'-'),
	level.Block(3600,-760,'-'),
	level.Block(3160,-760,'-'),
	level.Block(3640,-760,'-'),
	level.Block(3680,-760,'-'),
	level.Block(2720,-720,'-'),
	level.Block(2760,-720,'-'),
	level.Block(2800,-720,'-'),
	level.Block(2840,-720,'-'),
	level.Block(2880,-720,'-'),
	level.Block(3880,-760,'-'),
	level.Block(3680,-720,'-'),
	level.Block(3720,-720,'-'),
	level.Block(3760,-720,'-'),
	level.Block(3800,-720,'-'),
	level.Block(3840,-720,'-'),
	level.Block(3840,-760,'-'),
	level.Block(3920,-760,'-'),
	level.Block(3960,-760,'-'),
	level.Block(4000,-760,'-'),
	level.Block(4000,-800,'-'),
	level.Block(4000,-840,'-'),
	level.Block(4000,-880,'-'),
	level.Block(4000,-920,'-'),
	level.Block(4000,-960,'-'),
	level.Block(4000,-1000,'-'),
	level.Block(4000,-1040,'-'),
	level.Block(4000,-1080,'-'),
	level.Block(4000,-1120,'-'),
	level.Block(4000,-1160,'-'),
	level.Block(4000,-1200,'/'),
	level.Block(4000,-1240,'/'),
	level.Block(4000,-1280,'/'),
	level.Block(4000,-1320,'/'),
	level.Block(4000,-1360,'-'),
	level.Block(4000,-1400,'-'),
	level.Block(2160,-1200,'#'),
	level.Block(2200,-1200,'#'),
	level.Block(2240,-1200,'#'),
	level.Block(2280,-1200,'#'),
	level.Block(2320,-1200,'#'),
	level.Block(2360,-1200,'#'),
	level.Block(2400,-1200,'#'),
	level.Block(2440,-1200,'-'),
	level.Block(2480,-1200,'-'),
	level.Block(2480,-1240,'-'),
	level.Block(2480,-1280,'-'),
	level.Block(2480,-1320,'-'),
	level.Block(2480,-1360,'-'),
	level.Block(2480,-1400,'-'),
	level.Block(2480,-1440,'-'),
	level.Block(2480,-1480,'-'),
	level.Block(2480,-1520,'-'),
	level.Block(2480,-1560,'-'),
	level.Block(2480,-1600,'-'),
	level.Block(2480,-1640,'-'),
	level.Block(2480,-1680,'-'),
	level.Block(2520,-1680,'-'),
	level.Block(2560,-1680,'-'),
	level.Block(2600,-1680,'-'),
	level.Block(2640,-1680,'-'),
	level.Block(2680,-1680,'-'),
	level.Block(2720,-1680,'-'),
	level.Block(2760,-1680,'-'),
	level.Block(2800,-1680,'-'),
	level.Block(2840,-1680,'-'),
	level.Block(2880,-1680,'-'),
	level.Block(3000,-1680,'-'),
	level.Block(3040,-1680,'-'),
	level.Block(3080,-1680,'-'),
	level.Block(3120,-1680,'-'),
	level.Block(3160,-1680,'-'),
	level.Block(3200,-1680,'-'),
	level.Block(3240,-1680,'-'),
	level.Block(3280,-1680,'-'),
	level.Block(2920,-1680,'-'),
	level.Block(2960,-1680,'-'),
	level.Block(3720,-1680,'-'),
	level.Block(3680,-1680,'-'),
	level.Block(3600,-1680,'-'),
	level.Block(3560,-1680,'-'),
	level.Block(3480,-1680,'-'),
	level.Block(3400,-1680,'-'),
	level.Block(3360,-1680,'-'),
	level.Block(3320,-1680,'-'),
	level.Block(3440,-1680,'-'),
	level.Block(3640,-1680,'-'),
	level.Block(3760,-1680,'-'),
	level.Block(3800,-1680,'-'),
	level.Block(3840,-1680,'-'),
	level.Block(3880,-1680,'-'),
	level.Block(3920,-1680,'-'),
	level.Block(4000,-1640,'-'),
	level.Block(4000,-1600,'-'),
	level.Block(4000,-1560,'-'),
	level.Block(4000,-1520,'-'),
	level.Block(4000,-1480,'-'),
	level.Block(4000,-1680,'-'),
	level.Block(4000,-1440,'-'),
	level.Block(3960,-1680,'-'),
	level.Block(3520,-1680,'-'),
	level.Block(2760,-1440,'!'),
	level.Block(2800,-1440,'!'),
	level.Block(2840,-1440,'!'),
	level.Block(3520,-1440,'!'),
	level.Block(3560,-1440,'!'),
	level.Block(3600,-1440,'!'),
	level.Block(3640,-1440,'!'),
	level.Block(2360,-1280,'!'),
	level.Block(3760,-1360,'#'),
	level.Block(3760,-1320,'#'),
	level.Block(3760,-1280,'#'),
	level.Block(3760,-1240,'#'),
	level.Block(3760,-1200,'#'),
	level.Block(3760,-1160,'#'),
	level.Block(3760,-1120,'#'),
	level.Block(4040,-1160,'-'),
	level.Block(4080,-1160,'-'),
	level.Block(4120,-1160,'-'),
	level.Block(4160,-1160,'-'),
	level.Block(4200,-1160,'-'),
	level.Block(4240,-1160,'-'),
	level.Block(4280,-1160,'-'),
	level.Block(4280,-1200,'-'),
	level.Block(4280,-1240,'-'),
	level.Block(4280,-1280,'-'),
	level.Block(4280,-1320,'-'),
	level.Block(4280,-1360,'-'),
	level.Block(4240,-1360,'-'),
	level.Block(4200,-1360,'-'),
	level.Block(4160,-1360,'-'),
	level.Block(4120,-1360,'-'),
	level.Block(4080,-1360,'-'),
	level.Block(4040,-1360,'-'),
	level.Block(360,-160,'%')
]
