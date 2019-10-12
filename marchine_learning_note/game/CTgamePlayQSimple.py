
import pygame
from pygame.locals import *
from collections import deque
import cv2
import tensorflow as tf
import random
import numpy as np

WIN_SIZE = [320, 400]
BAT_SIZE = [50, 5]  # the size of BAR
DOT_Rad = 10
color_b  = (0,0,0)
color_w  = (200,200,200)
color_w1  = (0,100,100)

W1=100
H1=30
W2=30
H2=50
W3=30
H3=80
b_stay = [1, 0, 0]
b_left = [0, 1, 0]
b_right = [0, 0, 1]
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
	if life==1:
		font=pygame.font.Font(None,25)
		scoretext=font.render("WEAK!",1,(200,200,200))
		screen.blit(scoretext,(140, 200))

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
		self.episode=-1
		pygame.display.set_caption('TC BAT')
		self.dot_vec_x = -1
		self.dot_vec_y = -1
		self.dot_x = WIN_SIZE[0]//2
		self.dot_y = WIN_SIZE[1]//2
		self.dot_loc = [self.dot_x, self.dot_y]
		self.score = 0
		self.B_x = WIN_SIZE[0]//2-BAT_SIZE[0]//2
		self.B_loc = pygame.Rect(self.B_x, WIN_SIZE[1]-BAT_SIZE[1], BAT_SIZE[0], BAT_SIZE[1])

	def rungame(self, act):
		Change_episode=0
		total_score=0
		if act  == b_left:
			self.B_x = self.B_x - 4
		elif act == b_right:
			self.B_x = self.B_x + 4
		else:
			pass
		if self.B_x < 0:
			self.B_x = 0
		if self.B_x > WIN_SIZE[0] - BAT_SIZE[0]:
			self.B_x = WIN_SIZE[0] - BAT_SIZE[0]

		self.screen.fill(color_b)
		self.B_loc.left = self.B_x
		pygame.draw.rect(self.screen, color_w, self.B_loc)

		self.dot_loc[0] += self.dot_vec_x * 2
		self.dot_loc[1] += self.dot_vec_y * 3
		pygame.draw.rect(self.screen, color_w1, self.C1_pos)
		pygame.draw.rect(self.screen, color_w1, self.C2_pos)
		pygame.draw.rect(self.screen, color_w1, self.C3_pos)
		pygame.draw.rect(self.screen, color_w1, self.T1_pos)
		pygame.draw.rect(self.screen, color_w1, self.T2_pos)
		pygame.draw.circle(self.screen, color_w, self.dot_loc,DOT_Rad)


		dright = self.dot_loc[0]+DOT_Rad
		dleft = self.dot_loc[0]-DOT_Rad
		dtop = self.dot_loc[1]-DOT_Rad
		dbottom = self.dot_loc[1]+DOT_Rad
		put_text1(self.score,self.screen)
		put_text2(self.life,self.screen)

		CT_switch =False
		if CT_switch == True:
			## s1
			if dright >=50 and dright <=52 and dtop<=110:
				self.dot_vec_x = self.dot_vec_x * -1
			## S2
			if dright>=50 and dleft<=150 and dtop<=112 and dtop >=110:
				self.dot_vec_y = self.dot_vec_y * -1
			# S3
			if dleft <=150 and dleft >=148 and dtop<=110 and  dbottom>=80:
				self.dot_vec_x = self.dot_vec_x * -1
			## S4
			if dright>=80 and dleft<=150 and dbottom>=80 and dbottom<=82:
				self.dot_vec_y = self.dot_vec_y * -1
			# S5
			if dleft <=82 and dleft>=80 and dtop<=80 and  dbottom>=30:
				self.dot_vec_x = self.dot_vec_x * -1
			## S6
			if dleft>=80 and dright<=195 and dtop<=30:
				self.dot_vec_y = self.dot_vec_y * -1
			## S7
			if dright>=225 and dleft<=260 and dtop<=30:
				self.dot_vec_y = self.dot_vec_y * -1
			# S8
			if dright >=193 and dright <=196 and dtop<=110 and  dbottom>=30:
				self.dot_vec_x = self.dot_vec_x * -1
			# S9
			if dleft <=227 and dleft >=226 and dtop<=110 and  dbottom>=30:
				self.dot_vec_x = self.dot_vec_x * -1
			## S11
			if dleft<=263 and dleft>=261 and dtop<=30:
				self.dot_vec_x = self.dot_vec_x * -1
			## S10
			if dright>=195 and dleft<=225 and dtop<=110:
				self.dot_vec_y = self.dot_vec_y * -1


		if dtop <= 0:
			self.dot_vec_y = self.dot_vec_y * -1
		if dleft <= 0 or dright >= (WIN_SIZE[0]):
			self.dot_vec_x = self.dot_vec_x * -1

		reward = 0
		if self.B_loc.top <= dbottom and (self.B_loc.left <=self.dot_loc[0] and self.B_loc.right >=self.dot_loc[0]):
			reward = 1    #
			self.score +=1
			self.dot_vec_y = self.dot_vec_y * -1
		elif self.B_loc.top <= dbottom and (self.B_loc.left > self.dot_loc[0] or self.B_loc.right < self.dot_loc[0]):
			if self.life==1:
				reward = -1
				self.life  = 3 # another ep
				self.episode+=1
				Change_episode = 1
				total_score=self.score
				self.score = 0
				self.dot_vec_x = -1
				self.dot_vec_y = -1
				self.dot_loc = [self.dot_x, self.dot_y]
			elif self.life>1:
				reward = 0
				self.life-=1
				self.dot_vec_y = self.dot_vec_y * -1

		screen_image = pygame.surfarray.array3d(pygame.display.get_surface())
		pygame.display.update()

		return Change_episode,self.episode,total_score, reward, screen_image

### down below should be modified.
# gamma: r+gamma*Max_a' Q(s',a')
gamma = 0.992 # decay rate of past observations
# epsilon-greedy algorithm
INIT_EPSL = 1.0
FINAL_EPSL = 0.05
# train steps; obersve steps
TOT_STEPS=   6000000
EXPLORE = 1000000
OBSERVE =    50000  ## step<50000 observe
N_EPISODE =  100000
# size of D
REPLAY_TOT = 200000

BATCH_SIZE = 32
UPDATE_TIME = 10000

OUTPUT_SIZE = 3  # 3 possible actions
image_in = tf.placeholder('float',[None,80,100,4])
image_inT = tf.placeholder('float',[None,80,100,4])
action =      tf.placeholder("float", [None, OUTPUT_SIZE])

def weight_variable(shape):
  initial = tf.truncated_normal(shape, stddev=0.05)
  return tf.Variable(initial)
def bias_variable(shape):
  initial = tf.constant(0.1, shape=shape)
  return tf.Variable(initial)
# Q-network:
def createQN(x):
	#network weights
	w_conv1 = weight_variable([8, 8, 4, 32])
	b_conv1 = bias_variable([32])

	w_conv2 = weight_variable([4, 4,32, 64])
	b_conv2 = bias_variable([64])

	w_conv3 = weight_variable([3, 3,64, 64])
	b_conv3 = bias_variable([64])
	N_flat=6*9*64
	w_fc4 = weight_variable([N_flat, 512])
	b_fc4 = bias_variable([512])

	w_fc5 = weight_variable([512, OUTPUT_SIZE])
	b_fc5 = bias_variable([OUTPUT_SIZE])
    	## conv1:[19,24,32]  conv2 [8,11,64], conv3, [6,9,64]
	x1 = tf.nn.relu(tf.nn.conv2d(x,
		 w_conv1, strides = [1, 4, 4, 1], padding = "VALID") + b_conv1)
	x2 = tf.nn.relu(tf.nn.conv2d(x1, w_conv2, strides = [1, 2, 2, 1], padding = "VALID") + b_conv2)
	x3 = tf.nn.relu(tf.nn.conv2d(x2, w_conv3, strides = [1, 1, 1, 1], padding = "VALID") + b_conv3)

	x3_flat = tf.reshape(x3, [-1, N_flat])
	xfc4 = tf.nn.relu(tf.matmul(x3_flat, w_fc4) + b_fc4)

	Qa = tf.matmul(xfc4, w_fc5) + b_fc5
	return Qa,w_conv1,b_conv1,w_conv2,b_conv2,w_conv3,b_conv3,w_fc4,b_fc4,w_fc5,b_fc5



def AIPlayCT(image_in,image_inT):
	# define Qa and QaT
	Qa,w_conv1,b_conv1,w_conv2,b_conv2,w_conv3,b_conv3,w_fc4,b_fc4,w_fc5,b_fc5 = createQN(image_in)
	QaT,w_conv1T,b_conv1T,w_conv2T,b_conv2T,w_conv3T,b_conv3T,w_fc4T,b_fc4T,w_fc5T,b_fc5T = createQN(image_inT)
	copyTargetQN = [w_conv1T.assign(w_conv1),b_conv1T.assign(b_conv1),w_conv2T.assign(w_conv2),b_conv2T.assign(b_conv2),w_conv3T.assign(w_conv3),b_conv3T.assign(b_conv3),w_fc4T.assign(w_fc4),b_fc4T.assign(b_fc4),w_fc5T.assign(w_fc5),b_fc5T.assign(b_fc5)]

	Action_PI = tf.placeholder("float", [None, OUTPUT_SIZE])
	targ = tf.placeholder("float", [None])             # target input from reward + gam * Max_a' *Q(s';a')
    	# The real Q(s,a) = Qsa
	Qsa = tf.reduce_sum(tf.multiply(Qa, Action_PI), reduction_indices = 1)  # Qsa: Q(s,a)
	## L = E( (r+gamma*max_a' Q(s',a')-Q(s,a))^2)
	Loss =   tf.reduce_mean(tf.square(Qsa - targ))
	#optimizer = tf.train.AdamOptimizer(1e-6).minimize(Loss)
	optimizer = tf.train.RMSPropOptimizer(0.00025,0.99,0.0,1e-6).minimize(Loss)
	game = TCGAME()
	D = deque()
	_1,_2,_3,_4, img = game.rungame(b_stay)
	img = cv2.cvtColor(cv2.resize(img, (100, 80)), cv2.COLOR_BGR2GRAY)
	_, img = cv2.threshold(img, 1, 255, cv2.THRESH_BINARY)
	state_t = np.stack((img, img, img, img), axis = 2)
	with tf.Session() as sess:
		sess.run(tf.global_variables_initializer())
		saver = tf.train.Saver()
		step = 0
		score_ALL=np.zeros([N_EPISODE],dtype=np.int)
		saver.restore(sess, "data/game.cpk-2770001")
		epsl = INIT_EPSL
		while True:
			# get action
			if epsl > FINAL_EPSL:
				epsl -= (INIT_EPSL - FINAL_EPSL) / EXPLORE
			Qa_t = QaT.eval(feed_dict = {image_inT : [state_t]})[0]
			Action_take_t = np.zeros([OUTPUT_SIZE], dtype=np.int)
			epsl=0.05
			if(random.random() <= epsl): #INIT_EPSL):
				action_index = random.randrange(OUTPUT_SIZE)
			else:
				action_index = np.argmax(Qa_t)  # it is number

			Action_take_t[action_index] = 1   # it is vector
			# run game for one time and get one observation
			ch_ep=0
			ch_ep,episode,tot_score,reward, img = game.rungame(list(Action_take_t))
			if (ch_ep==1 and episode>=0 and episode<=N_EPISODE):
				score_ALL[episode] = tot_score
				print('total score: ', tot_score,' episode: ',step,ch_ep)
				ave_score = np.mean(score_ALL[0:episode+1])
				if (episode>9):
					ave_score = np.mean(score_ALL[0:episode+1])
			img = cv2.cvtColor(cv2.resize(img, (100, 80)), cv2.COLOR_BGR2GRAY)
			_, img = cv2.threshold(img, 1, 255, cv2.THRESH_BINARY)
			img = np.reshape(img, (80, 100, 1))
			state_next = np.append(img, state_t[:, :, 0:3], axis = 2)
			if step%1000==0:
				print('step: ',step, "epsilon:", epsl, " " ,"action:", action_index, " " ,"reward:", reward,' qa: ', Qa_t[:])
				if episode>1:
					print('episode: ', episode, 'average score: ',ave_score,'max score: ',score_ALL[0:episode+1].max())

			state_t = state_next
			step += 1









AIPlayCT(image_in,image_inT)
