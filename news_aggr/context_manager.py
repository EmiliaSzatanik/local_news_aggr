import sys
sys.setrecursionlimit(2000)

print(sys.getrecursionlimit())

# sys.setrecursionlimit(10**7) # max depth of recursion
# threading.stack_size(2**27)  # new thread will get stack of such size
#

# class recursion_depth:
#     def __init__(self, limit):
#         self.limit = limit
#         self.default_limit = sys.getrecursionlimit()
#
#     def __enter__(self):
#         sys.setrecursionlimit(self.limit)
#
#     def __exit__(self, type, value, traceback):
#         sys.setrecursionlimit(self.default_limit)