# dijkstra
Python implementation of Dijkstra's Algorithm.
The method gets directed graph, weights and source and returns dictionary.

example:

 graph = {'a': ['b', 'c'],
          'b': ['d'], 
          'c': [],
          'd': ['c', 'e'], 
          'e': [], 
          'f': ['e'] }
 
 weights = { ('a', 'b'): 2,
             ('a', 'c'): 10,
             ('b', 'd'): 3,
             ('d', 'c'): 1,
             ('d', 'e'): 12,
             ('f', 'e'): 0
           }       
source = 'a'

The method will return:
{'a': 0, 'b': 2, 'c': 6, 'd': 5, 'e': 17, 'f': 'infinity'}


