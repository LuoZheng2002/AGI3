from digit_to_number import digit_to_number
from test_methods import *
import pickle

file = open('Library/Knowledge/Method/Code/' + '3' + '.txt', 'wb')
pickle.dump(digit_to_number, file)
file.close()
file = open('Library/Knowledge/Method/Info/' + '3' + '.txt', 'wb')
pickle.dump(digit_to_number, file)
file.close()
