import numpy as np
import json
import keras
from keras.layers.embeddings import Embedding
from keras.utils import to_categorical
from keras.layers import Bidirectional, Lambda
from keras.models import Model, Input
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM, Activation
from keras.utils import np_utils
from keras.callbacks import ModelCheckpoint

model = keras.models.load_model('model.h5')

f_test = open('rawData.json',)  
test = json.load(f_test) 

c_test = []
xraw_test = []
x_test = []
y_test = []

for i in test:
  xraw_test.append(i["ys"])
  y_test.append(int(i["label"]))

for i in xraw_test:
  tmp = []
  for id in i:
    tmp.append(id)
  x_test.append(tmp)

x_test = np.asarray(x_test)
x_test = x_test.reshape(x_test.shape[0],x_test.shape[1]//96,96)

print(len(x_test))

wrongTest = {}
wrongTest[0] = 0
wrongTest[1] = 0
wrongTest[2] = 0

label = {}
label[0] = 0
label[1] = 0
label[2] = 0

for i in range(0 , len(x_test) , 1):
  XX=np.reshape(x_test[i],(1,5,96))
  if y_test[i] != np.argmax(model.predict(XX)[0]):
    wrongTest[y_test[i]] += 1
    label[np.argmax(model.predict(XX)[0])] += 1

print(wrongTest)
print(label)
  