
WIDTH       = 1280
HEIGTH      = 720
FPS         = 60
TILESIZE    = 16

# user interface
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
UI_FONT = './Asset/Font/ChakraPetch-Medium.ttf'
UI_FONT_SIZE = 18

# general colors
WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'

# ui colors
HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue'
UI_BORDER_COLOR_ACTIVE = 'gold'

# mainmenu interface
MENU_WIDTH_CENTER = WIDTH // 2
MENU_BG_COLOR = 'green'
MENU_BUTTON_BG = '#363636'
MENU_BUTTON_COLOR = 'white'

# enemy
MONSTER_DATA = {
    "flying creature" : {'health' : 100, 'exp' : 150, 'damage' : 20, 'attack_type' : 'tackle', 'speed' : 1, 'resistance' : 3, 'attack_radius' : 10, 'notice_radius' : 300},
    "goblin" : {'health' : 150, 'exp' : 200, 'damage' : 25, 'attack_type' : 'slash', 'speed' : 1, 'resistance' : 2, 'attack_radius' : 20, 'notice_radius' : 200},
    "slime" : {'health' : 30, 'exp' : 50, 'damage' : 10, 'attack_type' : 'tackle', 'speed' : 1, 'resistance' : 1, 'attack_radius' : 10, 'notice_radius' : 100}
}

# weapons
weapon_data = {
    'sword' : {'cooldown' : 100, 'damage' : 50, 'graphic' : './Asset/dungeon/heroes/sword_1.png'},
    'lance': {'cooldown': 400, 'damage': 30,'graphic':'../graphics/weapons/lance/full.png'},
	'axe': {'cooldown': 300, 'damage': 20, 'graphic':'../graphics/weapons/axe/full.png'},
	'rapier':{'cooldown': 50, 'damage': 8, 'graphic':'../graphics/weapons/rapier/full.png'},
	'sai':{'cooldown': 80, 'damage': 10, 'graphic':'../graphics/weapons/sai/full.png'}}           