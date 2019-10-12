
import numpy as np
import sys
import os
path = os.path.abspath(os.path.dirname(sys.argv[0]))
data_path = path+'\\data_1.txt'
data = open(data_path,'r').read()
print(data)
print(set(data))
chars = list(set(data))
print(chars)
print(len(data), len(chars))
data_size,vocab_size = len(data),len(chars)
print('data has %d characters,%d unique' % (data_size,vocab_size) )

chars_to_ix = {ch: i for i, ch in enumerate(chars)}
ix_to_chars = {i: ch for i, ch in enumerate(chars)}

#hyperparameters
hidden_size = 100
seq_length = 25
learning_rate = 1e-1

#model paremeters
wxh = np.random.randn(hidden_size, vocab_size)*0.01
whh = np.random.randn(hidden_size, hidden_size)*0.01
why = np.random.randn(vocab_size, 1)
bh = np.zeros((hidden_size, 1))
by = np.zeros((vocab_size, 1))

def lossFun(inputs, targets, hprev):
    xs,hs,ys,ps = {}, {}, {}, {}
    hs[-1] = np.copy(hprev)
    loss = 0
    #forward pass
    for t in range(len(inputs)):
        xs[t] = np.zeros((vocab_size, 1))
        xs[t][inputs[t]] = 1
        hs[t] = np.tanh(np.dot(wxh, xs[t])+np.dot(whh, hs[t-1]) + bh)
        ys[t] = np.dot(whh, hs[t]) +by
        ps[t] = np.exp(ys[t]) / np.sum(np.exp(ys[t]))
        loss += -np.log(ps[t][targets[t], 0])

    #backward pass
    dwxh,dwhh,dwhy = np.zeros_like(wxh), np.zeros_like(whh), np.zeros_like(why)
    dbh, dby =np.zeros_like(bh),np.zeros_like(by)
    dhnext = np.zeros_like(hs[0])


    for t in reversed(range(len(inputs))):
        dy = np.copy(ps[t])
        dy[targets[t]] -= 1 #loss 对 score 的导数
        dwhy += np.dot(dy, hs[t].T)
        dby += dy
        dh = np.dot(why.T, dy) + dhnext
        dhraw = (1 - hs[t] * hs[t]) * dh





