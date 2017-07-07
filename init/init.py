from keras.utils.data_utils import get_file
import os

datasets_path = os.getcwd()+'/datasets/'

print('> loading reuters data...')
get_file(datasets_path + 'reuters.npz', 
         origin='https://s3.amazonaws.com/text-datasets/reuters.npz')

print('> loading reuters word index...')
get_file(datasets_path + 'reuters_word_index.json', 
         origin='https://s3.amazonaws.com/text-datasets/reuters_word_index.json')

print('> testing keras...')
# TODO test keras somehow (train small test model?)

print('> testing sklearn')
# TODO test sklearn somehow (split and eval some data?)

print('Python setup done')


