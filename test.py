from test_methods import *
import pickle

file = open('Library/Knowledge/Method/Code/' + '4' + '.txt', 'wb')
pickle.dump(test_method, file)
file.close()
