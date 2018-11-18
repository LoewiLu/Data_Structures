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


--------

此层，数一个大人踢一个，由此人孩子排在此层大人后面，最后只剩孩子
孩子成长为大人，继续上一辈的遭遇
直到没娃了

"""

n = 10
parent = [9, 7 ,5, 5, 2 ,9, 9 ,9 ,2, -1]
root = parent.index(-1)
nodes = {}
for i in range(n):
    nodes[i] = [] 

for i in range(n):

    if parent[i] == -1:
        pass
    else:
       nodes[parent[i]] += [i] 
       
#print(nodes)
#{0: [], 1: [], 2: [4, 8], 3: [], 4: [], 5: [2, 3], 6: [], 7: [1], 8: [], 9: [0, 5, 6, 7]}

def treeHeight(root): 

    if root is None: 
        return 0
    
    q = [] #滕个层出来
      
    q.append(root) #初始层搞定
    
    height = 0 #初始设定
  
    while True: 
#        print('queue:',q)  
        
        nodeCount = len(q) #本层人数
#        print('nodeCount',nodeCount)
        
        if nodeCount == 0 : #全灭
            return height  #最后第几轮灭完的
      
        height += 1 #一层层向下（下一轮）
#        print('height', height) 
       
        while nodeCount > 0: #如果此层有人，进入此层
            
            node = q[0] #第一个大人
            
            q.pop(0) #灭掉此人
            
            if nodes[node]:
                for v in nodes[node]:
                    q.append(v) #找出这个人的孩子，排在此层大人后面
#            print(q) 
            
            nodeCount -= 1 #大人数量倒计时：当大人全灭只剩孩子，回到上一循环，让孩子变成大人
#            print('nodeCount:',nodeCount)
#            print()
    
treeHeight(root)   
    