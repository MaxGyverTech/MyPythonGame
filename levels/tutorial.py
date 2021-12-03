# Auto-generated, can be edited
from game import *

spawn_pos = (40,40)
background = 'game\content/bg2.png'
guns = []

####DONT TOUCH####
# Auto-generated in game.level
ais = [
	enemies.MeleeAI(x=3382, y=915),
	enemies.MeleeAI(x=4580, y=900),
	enemies.ShoterAI(x=5926, y=911, gun='rifle')
]
actors = [
	objects.Image(x=160, y=805, image='game/content/ui/key.png', rotation=0, scale=1.0),
	objects.Image(x=85, y=880, image='game/content/ui/key.png', rotation=0, scale=1.0),
	objects.Image(x=160, y=880, image='game/content/ui/key.png', rotation=0, scale=1.0),
	objects.Image(x=235, y=880, image='game/content/ui/key.png', rotation=0, scale=1.0),
	objects.Text(x=178, y=815, text='W', size=45, color='black'),
	objects.Text(x=178, y=890, text='S', size=45, color='black'),
	objects.Text(x=105, y=890, text='A', size=45, color='red'),
	objects.Text(x=258, y=890, text='D', size=45, color='red'),
	objects.Text(x=98, y=749, text='Press A/D to move', size=30, color='white'),
	objects.Image(x=627, y=873, image='game/content/ui/space_key.png', rotation=0, scale=1.0),
	objects.Text(x=680, y=883, text='Space', size=45, color='black'),
	objects.Text(x=616, y=823, text='Press Space to jump', size=30, color='white'),
	objects.Image(x=1298, y=870, image='game/content/ui/space_key.png', rotation=0, scale=1.0),
	objects.Text(x=1353, y=878, text='Space', size=45, color='black'),
	objects.Text(x=1272, y=835, text='Press Space two times', size=30, color='white'),
	objects.Text(x=1323, y=943, text='to double jump', size=30, color='white'),
	objects.Text(x=1510, y=883, text='x2', size=40, color='white'),
	objects.Image(x=842, y=819, image='game/content/ui/arrow.png', rotation=15, scale=1.0),
	objects.Image(x=1507, y=695, image='game/content/ui/arrow.png', rotation=60, scale=1.0),
	objects.Text(x=1804, y=900, text='Press A/D when you`re on wall', size=30, color='white'),
	objects.Text(x=1987, y=944, text='to wall jump', size=30, color='white'),
	objects.Image(x=2154, y=878, image='game/content/ui/arrow.png', rotation=60, scale=1.0),
	objects.Image(x=2137, y=748, image='game/content/ui/arrow.png', rotation=150, scale=1.0),
	objects.Text(x=1927, y=735, text='Do it non-stop', size=30, color='white'),
	objects.Image(x=1931, y=599, image='game/content/ui/arrow.png', rotation=25, scale=1.0),
	objects.Image(x=1931, y=433, image='game/content/ui/arrow.png', rotation=150, scale=1.0),
	objects.Image(x=1928, y=351, image='game/content/ui/arrow.png', rotation=25, scale=1.0),
	objects.Ammo(x=2542, y=974, ammo={'pistol': 80}),
	objects.Text(x=2347, y=875, text='Take ammo for your pistol', size=30, color='white'),
	objects.Text(x=3366, y=734, text='And      your first enemy', size=30, color='white'),
	objects.Text(x=3413, y=734, text='kill', size=30, color='red'),
	objects.Text(x=2582, y=811, text='You can destroy glass', size=30, color='white'),
	objects.Image(x=2718, y=838, image='game/content/ui/arrow.png', rotation=-20, scale=1.0),
	objects.Text(x=3004, y=750, text='Press Right mouse button', size=30, color='white'),
	objects.Text(x=2968, y=781, text='to activate slow mothion', size=30, color='white'),
	objects.Text(x=2436, y=908, text='Press R to reload', size=30, color='white'),
	objects.Grenades(x=3941, y=971, amount=10),
	objects.Text(x=3856, y=850, text='Try using grenades', size=30, color='white'),
	objects.Text(x=4001, y=909, text='Warning!', size=30, color='red'),
	objects.Image(x=3916, y=897, image='game/content/ui/arrow.png', rotation=-80, scale=0.75),
	objects.Text(x=3998, y=939, text='You can damage yourself', size=30, color='white'),
	objects.Image(x=4208, y=746, image='game/content/ui/arrow.png', rotation=80, scale=1.0),
	objects.GunsCase(x=5025, y=965, guns=['rifle']),
	objects.Text(x=4822, y=831, text='Warning!', size=30, color='red'),
	objects.Text(x=4806, y=867, text='Some of your enemies can have guns too', size=30, color='white'),
	objects.Text(x=5006, y=903, text='So take this gun and ammo', size=30, color='white'),
	objects.Image(x=5094, y=921, image='game/content/ui/arrow.png', rotation=-160, scale=1.0),
	objects.Ammo(x=5057, y=963, ammo={'rifle': 120})
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
	level.Block(280,1000,'-'),
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
	level.Block(880,960,'='),
	level.Block(880,920,'='),
	level.Block(880,880,'='),
	level.Block(1920,1000,'-'),
	level.Block(1960,1000,'-'),
	level.Block(2000,1000,'-'),
	level.Block(2040,1000,'-'),
	level.Block(2080,1000,'-'),
	level.Block(2120,1000,'-'),
	level.Block(2160,1000,'-'),
	level.Block(2200,1000,'-'),
	level.Block(2240,1000,'-'),
	level.Block(2280,1000,'-'),
	level.Block(2320,1000,'-'),
	level.Block(2360,1000,'-'),
	level.Block(2400,1000,'-'),
	level.Block(2440,1000,'-'),
	level.Block(2480,1000,'-'),
	level.Block(2520,1000,'-'),
	level.Block(2560,1000,'-'),
	level.Block(2600,1000,'-'),
	level.Block(2640,1000,'-'),
	level.Block(2680,1000,'-'),
	level.Block(2720,1000,'-'),
	level.Block(2760,1000,'-'),
	level.Block(2800,1000,'-'),
	level.Block(2840,1000,'-'),
	level.Block(2880,1000,'-'),
	level.Block(2920,1000,'-'),
	level.Block(2960,1000,'-'),
	level.Block(3000,1000,'-'),
	level.Block(3040,1000,'-'),
	level.Block(3080,1000,'-'),
	level.Block(3120,1000,'-'),
	level.Block(3160,1000,'-'),
	level.Block(3200,1000,'-'),
	level.Block(3240,1000,'-'),
	level.Block(3280,1000,'-'),
	level.Block(3320,1000,'-'),
	level.Block(3360,1000,'-'),
	level.Block(3400,1000,'-'),
	level.Block(3440,1000,'-'),
	level.Block(3480,1000,'-'),
	level.Block(3520,1000,'-'),
	level.Block(3560,1000,'-'),
	level.Block(3600,1000,'-'),
	level.Block(3640,1000,'-'),
	level.Block(3680,1000,'-'),
	level.Block(3720,1000,'-'),
	level.Block(3760,1000,'-'),
	level.Block(3800,1000,'-'),
	level.Block(3840,1000,'-'),
	level.Block(3880,1000,'-'),
	level.Block(3920,1000,'-'),
	level.Block(3960,1000,'-'),
	level.Block(1560,960,'='),
	level.Block(1560,920,'='),
	level.Block(1560,880,'='),
	level.Block(1560,840,'='),
	level.Block(1560,800,'='),
	level.Block(1560,760,'='),
	level.Block(2240,960,'='),
	level.Block(2240,920,'='),
	level.Block(2240,880,'='),
	level.Block(2240,840,'='),
	level.Block(2240,800,'='),
	level.Block(2240,760,'='),
	level.Block(2240,720,'='),
	level.Block(2240,680,'='),
	level.Block(2240,640,'='),
	level.Block(2040,800,'='),
	level.Block(2000,800,'='),
	level.Block(1960,800,'='),
	level.Block(1920,800,'='),
	level.Block(1880,800,'='),
	level.Block(1880,760,'='),
	level.Block(1880,720,'='),
	level.Block(1880,680,'='),
	level.Block(1880,640,'='),
	level.Block(1880,600,'='),
	level.Block(2200,640,'='),
	level.Block(2160,640,'='),
	level.Block(2120,640,'='),
	level.Block(2080,640,'='),
	level.Block(2040,640,'='),
	level.Block(2040,600,'='),
	level.Block(2040,560,'='),
	level.Block(2040,520,'='),
	level.Block(2040,480,'='),
	level.Block(1880,440,'='),
	level.Block(1880,400,'='),
	level.Block(1880,360,'='),
	level.Block(2840,680,'/'),
	level.Block(2840,720,'/'),
	level.Block(2840,760,'/'),
	level.Block(2840,800,'/'),
	level.Block(2840,840,'/'),
	level.Block(2840,880,'/'),
	level.Block(2840,920,'/'),
	level.Block(2840,960,'/'),
	level.Block(3160,960,'='),
	level.Block(3200,960,'='),
	level.Block(3240,960,'='),
	level.Block(3280,960,'='),
	level.Block(3200,920,'='),
	level.Block(3240,920,'='),
	level.Block(3280,920,'='),
	level.Block(3280,880,'='),
	level.Block(3240,880,'='),
	level.Block(3280,840,'='),
	level.Block(4000,1000,'-'),
	level.Block(4040,1000,'-'),
	level.Block(4080,1000,'-'),
	level.Block(4120,1000,'-'),
	level.Block(4160,1000,'-'),
	level.Block(4200,1000,'-'),
	level.Block(4240,1000,'-'),
	level.Block(4280,1000,'-'),
	level.Block(4320,1000,'-'),
	level.Block(3280,800,'='),
	level.Block(3240,840,'='),
	level.Block(3200,880,'='),
	level.Block(3160,920,'='),
	level.Block(3120,960,'='),
	level.Block(4360,1000,'-'),
	level.Block(4400,1000,'-'),
	level.Block(4440,1000,'-'),
	level.Block(4480,1000,'-'),
	level.Block(4520,1000,'-'),
	level.Block(4560,1000,'-'),
	level.Block(4600,1000,'-'),
	level.Block(4640,1000,'-'),
	level.Block(4680,1000,'-'),
	level.Block(4720,1000,'-'),
	level.Block(4760,1000,'-'),
	level.Block(4800,1000,'-'),
	level.Block(4840,1000,'-'),
	level.Block(4880,1000,'-'),
	level.Block(4920,1000,'-'),
	level.Block(4960,1000,'-'),
	level.Block(5000,1000,'-'),
	level.Block(5040,1000,'-'),
	level.Block(5080,1000,'-'),
	level.Block(5120,1000,'-'),
	level.Block(5160,1000,'-'),
	level.Block(5200,1000,'-'),
	level.Block(5240,1000,'-'),
	level.Block(5280,1000,'-'),
	level.Block(5320,1000,'-'),
	level.Block(5360,1000,'-'),
	level.Block(5400,1000,'-'),
	level.Block(5440,1000,'-'),
	level.Block(5480,1000,'-'),
	level.Block(5520,1000,'-'),
	level.Block(5560,1000,'-'),
	level.Block(5600,1000,'-'),
	level.Block(5640,1000,'-'),
	level.Block(5680,1000,'-'),
	level.Block(5720,1000,'-'),
	level.Block(5760,1000,'-'),
	level.Block(5800,1000,'-'),
	level.Block(5840,1000,'-'),
	level.Block(5880,1000,'-'),
	level.Block(5920,1000,'-'),
	level.Block(5960,1000,'-'),
	level.Block(6000,1000,'-'),
	level.Block(6040,1000,'-'),
	level.Block(6080,1000,'-'),
	level.Block(6120,1000,'-'),
	level.Block(6160,1000,'-'),
	level.Block(6200,1000,'-'),
	level.Block(6240,1000,'-'),
	level.Block(6280,1000,'-'),
	level.Block(6320,1000,'-'),
	level.Block(6360,1000,'-'),
	level.Block(6400,1000,'-'),
	level.Block(6440,1000,'-'),
	level.Block(6480,1000,'-'),
	level.Block(6520,1000,'-'),
	level.Block(6560,1000,'-'),
	level.Block(6600,1000,'-'),
	level.Block(6640,1000,'-'),
	level.Block(6680,1000,'-'),
	level.Block(6680,960,'='),
	level.Block(6680,920,'='),
	level.Block(6680,880,'='),
	level.Block(6680,840,'='),
	level.Block(6680,800,'='),
	level.Block(6680,760,'='),
	level.Block(6680,720,'='),
	level.Block(3800,960,'/'),
	level.Block(3800,920,'/'),
	level.Block(3800,880,'/'),
	level.Block(3800,840,'/'),
	level.Block(3800,800,'/'),
	level.Block(3800,760,'/'),
	level.Block(1920,-40,'-'),
	level.Block(1960,-40,'-'),
	level.Block(2000,-40,'-'),
	level.Block(2040,-40,'-'),
	level.Block(2080,-40,'-'),
	level.Block(2120,-40,'-'),
	level.Block(2160,-40,'-'),
	level.Block(2200,-40,'-'),
	level.Block(2240,-40,'-'),
	level.Block(2280,-40,'-'),
	level.Block(2320,-40,'-'),
	level.Block(2360,-40,'-'),
	level.Block(2400,-40,'-'),
	level.Block(2440,-40,'-'),
	level.Block(2480,-40,'-'),
	level.Block(2520,-40,'-'),
	level.Block(2560,-40,'-'),
	level.Block(2600,-40,'-'),
	level.Block(2640,-40,'-'),
	level.Block(2680,-40,'-'),
	level.Block(2720,-40,'-'),
	level.Block(2760,-40,'-'),
	level.Block(2800,-40,'-'),
	level.Block(2840,-40,'-'),
	level.Block(2880,-40,'-'),
	level.Block(2920,-40,'-'),
	level.Block(2960,-40,'-'),
	level.Block(3000,-40,'-'),
	level.Block(3040,-40,'-'),
	level.Block(3080,-40,'-'),
	level.Block(3120,-40,'-'),
	level.Block(3160,-40,'-'),
	level.Block(3200,-40,'-'),
	level.Block(3240,-40,'-'),
	level.Block(3280,-40,'-'),
	level.Block(3320,-40,'-'),
	level.Block(3360,-40,'-'),
	level.Block(3400,-40,'-'),
	level.Block(3440,-40,'-'),
	level.Block(3480,-40,'-'),
	level.Block(3520,-40,'-'),
	level.Block(3560,-40,'-'),
	level.Block(3600,-40,'-'),
	level.Block(3640,-40,'-'),
	level.Block(3680,-40,'-'),
	level.Block(3720,-40,'-'),
	level.Block(3760,-40,'-'),
	level.Block(3800,-40,'-'),
	level.Block(3840,-40,'-'),
	level.Block(3880,-40,'-'),
	level.Block(3920,-40,'-'),
	level.Block(3960,-40,'-'),
	level.Block(4000,-40,'-'),
	level.Block(4040,-40,'-'),
	level.Block(4080,-40,'-'),
	level.Block(4120,-40,'-'),
	level.Block(4160,-40,'-'),
	level.Block(4200,-40,'-'),
	level.Block(4240,-40,'-'),
	level.Block(4280,-40,'-'),
	level.Block(4320,-40,'-'),
	level.Block(4360,-40,'-'),
	level.Block(4400,-40,'-'),
	level.Block(4440,-40,'-'),
	level.Block(4280,960,'='),
	level.Block(4280,920,'='),
	level.Block(4280,880,'='),
	level.Block(4280,840,'='),
	level.Block(4280,800,'='),
	level.Block(4280,760,'='),
	level.Block(4280,720,'='),
	level.Block(4720,880,'='),
	level.Block(4720,800,'='),
	level.Block(4720,760,'='),
	level.Block(4720,840,'='),
	level.Block(4720,920,'='),
	level.Block(4720,960,'='),
	level.Block(3560,800,'='),
	level.Block(5360,960,'='),
	level.Block(5400,960,'='),
	level.Block(5440,960,'='),
	level.Block(5480,960,'='),
	level.Block(5480,920,'='),
	level.Block(5480,880,'='),
	level.Block(5480,840,'='),
	level.Block(5440,840,'='),
	level.Block(5440,880,'='),
	level.Block(5440,920,'='),
	level.Block(5400,920,'='),
	level.Block(5400,880,'='),
	level.Block(5360,920,'='),
	level.Block(5320,960,'='),
	level.Block(5480,800,'='),
	level.Block(3600,800,'='),
	level.Block(4120,800,'='),
	level.Block(4120,760,'='),
	level.Block(4120,720,'='),
	level.Block(4120,680,'=')
]
