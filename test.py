from digit_sum import digit_sum
from test_methods import *
import pickle

file = open('Library/Knowledge/Method/Code/' + '1' + '.txt', 'wb')
pickle.dump(vertical_add, file)
file.close()
file = open('Library/Knowledge/Method/Info/' + '1' + '.txt', 'wb')
pickle.dump(vertical_add, file)
file.close()
