#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll
#canUnlockAll2 = __import__('0-lockboxes_recursion').canUnlockAll

import random

boxes = []
for i in range(1000):
    boxes.append([])
    for j in range(1000):
        boxes[i].append(j)
kels = canUnlockAll(boxes)
# recur = canUnlockAll2(boxes)
print('kels: ', kels)
# print('recur: ', recur)
