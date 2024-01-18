#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(boxes)
print(canUnlockAll(boxes))
print(boxes)
print("----")

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
#             0       1       2          3       4      5     6
print(boxes)
print(canUnlockAll(boxes))
print(boxes)
print("----")

boxes = [[1, 4], [2], [0, 4, 1], [5], [], [4, 1], [5, 6]]
#           0      1       2       3    4    5        6
print(boxes)
print(canUnlockAll(boxes))
print(boxes)
print("----")

boxes = [[]]
print(boxes)
print(canUnlockAll(boxes))
print(boxes)
print("----")

boxes = [[1, 1], []]
print(boxes)
print(canUnlockAll(boxes))
print(boxes)
print("----")

boxes = [[], [], [], []]
print(boxes)
print(canUnlockAll(boxes))
print(boxes)
print("----")

boxes = 2
print(boxes)
print(canUnlockAll(boxes))
print(boxes)
print("----")

boxes = ([], [], [], [])
print(boxes)
print(canUnlockAll(boxes))
print(boxes)
print("----")

boxes = []
print(boxes)
print(canUnlockAll(boxes))
print(boxes)
print("----")

boxes = [[7, 9, 1, 2, 3, 4, 5, 6, 7, 8], [4], [3], [4, 5, 6], [2], [], [], [], [], [8]]
print(boxes)
print(canUnlockAll(boxes))
print(boxes)
