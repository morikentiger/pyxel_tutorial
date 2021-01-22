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
		self.vec = 0
		self.img_cat = img_id

	def update(self, x, y, dx):
		self.pos.x = x
		self.pos.y = y
		self.vec = dx

class Ball:
	def __init__(self):
		self.pos = Vec2(0, 0)
		self.vec = 0
		self.size = 2
		self.speed = 3
		self.color = 10 # 0~15
		# self.life = 3

	def update(self, x, y, dx, size, color):
		self.pos.x = x
		self.pos.y = y
		self.vec = dx
		self.size = size
		self.color = color
		# if self.life > 0:
		# 	self.life -= 1

class App:
	def __init__(self):
		self.IMG_ID0 = 0
		self.IMG_ID1 = 1
		# self.IMG_ID2 = 2
		self.IMG_ID0_X = 60
		self.IMG_ID0_Y = 65

		self.MOUSE_X_PRE = 80
		self.MOUSE_Y_PRE = 0

		pyxel.init(WINDOW_W, WINDOW_H, caption="Cat Game")
		pyxel.image(self.IMG_ID0).load(0, 0, "assets/pyxel_logo_38x16.png")
		pyxel.image(self.IMG_ID1).load(0, 0, "assets/cat_16x16.png")

		# pyxel.mouse(True)

		# make instance
		self.mcat = cat(self.IMG_ID1)
		self.Balls = []

		# self.mouse_count = 0

		pyxel.run(self.update, self.draw)

	def update(self):
		if pyxel.btnp(pyxel.KEY_Q):
			pyxel.quit()

		# ====== ctrl cat ======
		dx = pyxel.mouse_x - self.mcat.pos.x		# x軸方向の移動量（マウス座標 - cat座標）
		dy = pyxel.mouse_y - self.mcat.pos.y		# y・・・〃・・・
		if dx != 0:
			self.mcat.update(pyxel.mouse_x, pyxel.mouse_y, dx)
		elif dy != 0:
			self.mcat.update(pyxel.mouse_x, pyxel.mouse_y, self.mcat.vec)

		# ====== ctrl Ball ======
		if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
			new_ball = Ball()
			if self.mcat.vec > 0:
				new_ball.update(self.mcat.pos.x + CAT_W/2 + 6,
												self.mcat.pos.y + CAT_H/2,
												self.mcat.vec, new_ball.size,
												new_ball.color)
			else:
				new_ball.update(self.mcat.pos.x + CAT_W/2 - 6,
												self.mcat.pos.y + CAT_H/2,
												self.mcat.vec, new_ball.size,
												new_ball.color)
			self.Balls.append(new_ball)
		
		ball_count = len(self.Balls)
		for i in range(ball_count):
			if 0 < self.Balls[i].pos.x and self.Balls[i].pos.x < WINDOW_W:
				# Ball update
				if self.Balls[i].vec > 0:
					self.Balls[i].update(self.Balls[i].pos.x + self.Balls[i].speed,
										self.Balls[i].pos.y,
										self.Balls[i].vec, self.Balls[i].size,
										self.Balls[i].color)
				else:
					self.Balls[i].update(self.Balls[i].pos.x - self.Balls[i].speed,
										self.Balls[i].pos.y,
										self.Balls[i].vec, self.Balls[i].size,
										self.Balls[i].color)
			else:
				del self.Balls[i]
				break
	
	def draw(self):
		pyxel.cls(0)
		
		pyxel.text(55, 40, "Are you Kururu?", pyxel.frame_count % 16)
		pyxel.blt(self.IMG_ID0_X, self.IMG_ID0_Y, self.IMG_ID0, 0, 0, 38, 16)

		# ====== draw cat =======
		if self.mcat.vec > 0:
			pyxel.blt(self.mcat.pos.x, self.mcat.pos.y, self.mcat.img_cat, 0, 0, -CAT_W, CAT_H, 13)
		else:
			pyxel.blt(self.mcat.pos.x, self.mcat.pos.y, self.mcat.img_cat, 0, 0, CAT_W, CAT_H, 13)
		
		# ====== draw Balls =======
		for ball in self.Balls:
			pyxel.circ(ball.pos.x, ball.pos.y, ball.size, ball.color)

App()