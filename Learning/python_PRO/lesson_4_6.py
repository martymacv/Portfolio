import pickle
import shutil


shutil.

def filter_dump(filename, objects, typename):
    objects = list(filter(lambda x: type(x) == typename, objects))
    with open(filename, 'wb') as pkl_f:
        pickle.dump(objects, pkl_f)



filter_dump('numbers.pkl', [1, '2', 3, 4, '5'], int)

with open('numbers.pkl', 'rb') as pkl_f:
    print(pickle.load(pkl_f))
