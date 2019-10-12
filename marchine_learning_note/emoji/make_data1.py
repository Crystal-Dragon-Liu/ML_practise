import numpy as np
import pickle
import os

NN = 4 ### number of categories

zero10 = np.zeros(NN)

N = 27




for i in range(N):
    if i<9:
        filename='F:/python/marchine_learning_note/emoji/t0'+str(i+1)+'.txt'
    if i>=9:
        filename='F:/python/marchine_learning_note/emoji/t'+str(i+1)+'.txt'
    if i==0:
         with open(filename,'rb') as f:
            train_img,train_lab  = pickle.load(f) #train_img[12,1024],train_lab[12,4]
    if i>0:
        with open(filename,'rb') as f:
            print(filename)
            x0,t_lab  = pickle.load(f)
        train_img =np.vstack((train_img, x0))
        train_lab = np.vstack((train_lab,t_lab))

with open('F:/python/marchine_learning_note/emoji/train_ABCD.txt','wb') as f:
    pickle.dump([train_img,train_lab],f)

#with open('train_lab.txt','wb') as f:
#    pickle.dump(train_lab,f)
