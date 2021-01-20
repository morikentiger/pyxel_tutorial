import pyxel

WINDOW_H = 120
WINDOW_W = 160
CAT_H = 16
CAT_W = 16

class Vec2:
	def __init__(self, x, y):
		self.x = x
		self.y = y

class cat:
	def __init__(self, img_id):
		self.pos = Vec2(0, 0)
		self.img_cat = img_id

	def update(self, x, y):
		self.pos.x = x
		self.pos.y = y

class App:
	def __init__(self):
		self.IMG_ID0 = 0
		self.IMG_ID1 = 1
		# self.IMG_ID2 = 2
		self.IMG_ID0_X = 60
		self.IMG_ID0_Y = 65

		pyxel.init(WINDOW_W, WINDOW_H, caption="Cat Game")
		pyxel.image(self.IMG_ID0).load(0, 0, "assets/pyxel_logo_38x16.png")
		pyxel.image(self.IMG_ID1).load(0, 0, "assets/cat_16x16.png")

		self.mcat = cat(self.IMG_ID1)

		# pyxel.mouse(True)
		pyxel.run(self.update, self.draw)

	def update(self):
		if pyxel.btnp(pyxel.KEY_Q):
			pyxel.quit()

		# ====== ctrl cat ======
		self.mcat.update(pyxel.mouse_x, pyxel.mouse_y)
	
	def draw(self):
		pyxel.cls(0)
		
		pyxel.text(55, 40, "Are you Kururu?", pyxel.frame_count % 16)
		pyxel.blt(self.IMG_ID0_X, self.IMG_ID0_Y, self.IMG_ID0, 0, 0, 38, 16)
		pyxel.blt(self.mcat.pos.x, self.mcat.pos.y, self.mcat.img_cat, 0, 0, -CAT_W, CAT_H, 13)
		

	# def cat(self):
	# 	x = pyxel.mouse_x
	# 	y = pyxel.mouse_y

	# 	if pyxel.btn(pyxel.MOUSE_LEFT_BUTTON):
	# 		pyxel.blt(x, y, self.IMG_ID1, 0, 0, -CAT_W, CAT_H, 13)
	# 	else:
	# 		pyxel.blt(x, y, self.IMG_ID1, 0, 0, CAT_W, CAT_H, 13)


App()