#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 16:33:47 2018

@author: loewi

>>> tree = TreeHeight()
>>> tree.n = 5
>>> tree.parent = [-1, 0, 4, 0, 3]
>>> tree.compute_height()
4
Explanation:
The input means that there are 5 nodes with numbers from 0 to 4,
node 0 is the root, node 1 is a child of node 0, 
node 2 is a child of node 4, 
node 3 is a child of node 0
and node 4 is a child of node 3.

   root
     1
    /|
   1 3
     |
     4
     |
     2

--------------

>>> n = 10
>>> parent = [9, 7 ,5, 5, 2 ,9, 9 ,9 ,2, -1]

#output: temp = [2, 3, 3, 3, 4, 2, 2, 2, 4, 1]

给好了初始格子[0] * n，从top替换0为1，存住了，遇到之前存过的拿出来叠加1，再存好，以此类推

"""


import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))
        self.temp = [0] * self.n
    
    def level(self, i):  
                  
    #    print(i) 
        if self.parent[i] == -1:
            return 1
    
        if self.temp[i]:
            return self.temp[i]
    
        self.temp[i] = 1+ self.level(self.parent[i])
        
        return self.temp[i]
    #print([level(i) for i in range(n)])        
    
    def compute_height(self):
        
        return max([self.level(i) for i in range(self.n)])
                

def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()





