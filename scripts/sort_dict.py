#!/usr/bin/env python
# Orders the allowed words dictionary
DICT_PATH = '.github/actions/check-spelling/allowed_words.txt'

with open(DICT_PATH, mode='r') as f:
    file = f.read().split('\n')
    head = file[0]
    file_ordered = sorted(file[1:])
    last = file_ordered[-1]

with open(DICT_PATH, mode='w') as f:
    f.write(head+'\n')
    [f.write(l+'\n') for l in file_ordered[:-1]]
    f.write(last)