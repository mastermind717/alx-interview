# 0x00-lockboxes
For this interview practice algorithm, there are `n` number of locked boxes. Each box is numbered sequentially from `0` to `n - 1`. The first box `boxes[0]` is unlocked and all boxes may contain keys for that open other boxes.

[Lockboxes](/0x00-lockboxes/0-lockboxes.py)
* Write a Python method `def canUnlockAll(boxes)` that determines if all the boxes can be opened:
  * `boxes` is a list of lists, with the inner list representing the keys in the box.
  * A key with the same number as a box opens that box (all keys will be positive integers).
  * There can be boxes without keys or keys that do not have cooresponding boxes.
  * Returns `True` is all boxes can be unlocked, `False` otherwise

### test_files
The test_files/ directory contains files used to test the output of the algorithm locally.
