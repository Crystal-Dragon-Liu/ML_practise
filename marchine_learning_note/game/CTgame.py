
import sys
import pygame
from pygame.locals import *
import numpy as np

WIN_SIZE = [320, 400]
BAT_SIZE = [80, 2]  # the size of BAR
DOT_Rad = 10
color_b  = (0,0,0)
color_w  = (200,200,200)

W1=100
H1=30
W2=30
H2=50
W3=30
H3=80
def put_text1(score,screen):
	font=pygame.font.Font(None,20)
	scoretext=font.render("Score: "+str(score),1,(120,120,120))
	screen.blit(scoretext,(250, 340))
def put_text2(life,screen):
	font=pygame.font.Font(None,20)
	scoretext=font.render("Life:   "+str(life),1,(120,120,120))
	screen.blit(scoretext,(250, 360))
	font=pygame.font.Font(None,15)
	scoretext=font.render("by TC team of Clusetertech 2018",1,(100,100,100))
	screen.blit(scoretext,(100, 120))

class TCGAME(object):

	def __init__(self):
		pygame.init()
		self.clock = pygame.time.Clock()
		# TC
		self.C1_pos=pygame.Rect(50,0,W1,H1)
		self.C2_pos=pygame.Rect(50,H1,W2,H2)
		self.C3_pos=pygame.Rect(50,H1+H2,W1,H1)
		self.T1_pos=pygame.Rect(50+W1+10,0,W1,H1)
		self.T2_pos=pygame.Rect(50+W1+10+35,H1,W3,H3)
		self.screen = pygame.display.set_mode(WIN_SIZE)
		self.life = 3
		pygame.display.set_caption('TC BAT')
		self.dot_vec_x = -1
		self.dot_vec_y = -1
		self.dot_x = WIN_SIZE[0]//2
		self.dot_y = WIN_SIZE[1]//2
		self.dot_vec_x = np.random.randint(low=0,high=1)*2-1
		self.dot_vec_y = np.random.randint(low=0,high=1)*2-1
		self.dot_loc = [self.dot_x, self.dot_y]
		self.dot_loc[0] = np.random.randint(low=20,high=300) 
		self.dot_loc[1] = np.random.randint(low=150,high=350) 
		self.dot_loc = [self.dot_x, self.dot_y]
		self.score = 0
		self.B_x = WIN_SIZE[0]//2-BAT_SIZE[0]//2
		self.B_loc = pygame.Rect(self.B_x, WIN_SIZE[1]-BAT_SIZE[1], BAT_SIZE[0], BAT_SIZE[1])


	def Left_B(self):
		self.B_x = self.B_x - 2
	def Right_B(self):
		self.B_x = self.B_x + 2

	def game_start(self):
		b_left = 0
		b_right = 0
		while True:
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
				elif event.type==pygame.KEYDOWN and event.key==K_LEFT:
					b_left = True
				elif event.type==pygame.KEYDOWN and event.key==K_RIGHT:
					b_right = True
				elif event.type==pygame.KEYUP:
					b_left = False
					b_right = False

			if b_left == True and b_right == False:
				self.Left_B()
			if b_left == False and b_right == True:
				self.Right_B()

			self.screen.fill(color_b)
			self.B_loc.left = self.B_x
			pygame.draw.rect(self.screen, color_w, self.B_loc)

			self.dot_loc[0] += self.dot_vec_x * 2
			self.dot_loc[1] += self.dot_vec_y * 3
			pygame.draw.circle(self.screen, color_w, self.dot_loc,DOT_Rad)

			pygame.draw.rect(self.screen, color_w, self.C1_pos)
			pygame.draw.rect(self.screen, color_w, self.C2_pos)
			pygame.draw.rect(self.screen, color_w, self.C3_pos)
			pygame.draw.rect(self.screen, color_w, self.T1_pos)
			pygame.draw.rect(self.screen, color_w, self.T2_pos)
			#S1
			dright = self.dot_loc[0]+DOT_Rad
			dleft = self.dot_loc[0]-DOT_Rad
			dtop = self.dot_loc[1]-DOT_Rad
			dbottom = self.dot_loc[1]+DOT_Rad
			put_text1(self.score,self.screen)
			put_text2(self.life,self.screen)

			if dright >=50 and dright <=52 and dtop<=110:
				self.dot_vec_x = self.dot_vec_x * -1
			## S2
			if dright>=52 and dleft<=148 and dtop<=112 and dtop >=110:
				self.dot_vec_y = self.dot_vec_y * -1
			# S3
			if dleft <=150 and dleft >=148 and dtop<=110 and  dbottom>=80:
				self.dot_vec_x = self.dot_vec_x * -1
			## S4
			if dright>=82 and dleft<=148 and dbottom>=80 and dbottom<=82:
				self.dot_vec_y = self.dot_vec_y * -1
			# S5
			if dleft <=82 and dleft>=80 and dtop<=80 and  dbottom>=30:
				self.dot_vec_x = self.dot_vec_x * -1
			## S6
			if dleft>=82 and dright<=193 and dtop<=30:
				self.dot_vec_y = self.dot_vec_y * -1
			## S7
			if dright>=225 and dleft<=258 and dtop<=30:
				self.dot_vec_y = self.dot_vec_y * -1
			# S8
			if dright >=195 and dright <=197 and dtop<=110 and  dbottom>=30:
				self.dot_vec_x = self.dot_vec_x * -1
			# S9
			if dleft <=225 and dleft >=223 and dtop<=110 and  dbottom>=30:
				self.dot_vec_x = self.dot_vec_x * -1
			## S11
			if dleft<=260 and dleft>=258 and dtop<=30:
				self.dot_vec_x = self.dot_vec_x * -1
			## S10
			if dright>=197 and dleft<=223 and dtop<=112 and dtop>110:
				self.dot_vec_y = self.dot_vec_y * -1


			if dtop <= 0 or dbottom >= (WIN_SIZE[1] - BAT_SIZE[1]+1):
				self.dot_vec_y = self.dot_vec_y * -1
			if dleft <= 0 or dright >= (WIN_SIZE[0]):
				self.dot_vec_x = self.dot_vec_x * -1



			if self.B_loc.top <= dbottom and (self.B_loc.left < dright
			   and self.B_loc.right > dleft):
				self.score += 1
				print("SCORE: ", self.score,'  Life: ',self.life)

			elif self.B_loc.top <= dbottom and (self.B_loc.left > dright
			   or self.B_loc.right < dleft) and self.life > 1:
			   self.life-=1
			   print("SCORE: ", self.score,'  Life: ',self.life)



			elif self.B_loc.top <= dbottom and (self.B_loc.left > dright
			   or self.B_loc.right < dleft) and self.life == 1:
				print("Game Over: ", "SCORE: ", self.score,'  Life: ',self.life)
				return self.score

			pygame.display.update()
			self.clock.tick(60)

TCGAME().game_start()
