#!/usr/bin/python3
""" defines method to solve lockboxes problem """


def canUnlockAll(boxes):
    """
    determines if all boxes can be unlocked

    parameters:
        boxes (list): list of list that represent boxes and any keys inside
            There are n num of boxes, labeled sequentially starting at 0.
            Keys with the same number as a box opens that box.
            All keys can be assumed to be positive integers(whole numbers).
             There can be boxes without keys and keys without boxes.
             The first box boxes[0] is the only unlocked box initially.

    returns:
        True, if all boxes can be unlocked
        False, if one or more boxes cannot be unlocked
    """
    from copy import deepcopy

    # checks if given valid list of boxes
    if type(boxes) is not list or len(boxes) < 1:
        return False
    # checks that all boxes contain a valid list of keys (empty boxes are OK)
    # keys can be assumed to be positive integers, type will be confirmed later
    for box in boxes:
        if type(box) is not list:
            return False
    # creates a copy of boxes to not affect the original list of lists
    unlockedBoxes = deepcopy(boxes)
    # calls unlockBox() method to open box 0
    # unlockBox() will recursively open any boxes with keys from the opened box
    unlockedBoxes = unlockBox(unlockedBoxes, 0)
    # after opening all possible boxes, check that total boxes have been opened
    # opened boxes are noted with a -1 flag
    for box in unlockedBoxes:
        if -1 not in box:
            # if a box is missing the -1 flag, it was not unlocked
            return False
    # returns true if all boxes in the previous loop were indicated as unlocked
    return True


def unlockBox(boxes, key):
    """
    unlocks the box corresponding to a given key, recursively

    parameters:
        boxes (list): list of list representing the boxes and any keys inside
        key (int): the index of the box to unlock

    returns:
        boxes, with marker (-1) indicating that the box has been opened
    """
    print(key)
    if type(key) is not int or key < 0:
        # if key is invalid
        return boxes
    # mark that the box has been opened by appeneding a -1 flag
    # since all keys are positive ints, -1 will not be mistaken for a valid key
    boxes[key].append(-1)
    # loop through any new keys found in the recently opened box
    # use new keys to potentially open more boxes with the unlockBox() method
    for new_key in boxes[key]:
        if new_key is -1:
            # if new key is the flag for an opened box, continue
            continue
        if new_key >= len(boxes):
            # if new key is out of range of the available boxes, continue
            continue
        if -1 in boxes[new_key]:
            # if the box has previously been opened, continue
            continue
        # update the list of boxes by calling unlockBox() to open new boxes
        boxes = unlockBox(boxes, new_key)
    # after unlocking all boxes with the available keys, return boxes
    return boxes
