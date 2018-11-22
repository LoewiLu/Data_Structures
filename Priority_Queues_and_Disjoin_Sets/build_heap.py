# python3
'''
Convert an array of integers into a heap.
Note that you will need to use a min-heap instead of a max-heap in this problem.

Samples1:
    
input:
5
[5, 4, 3, 2, 1]

output:
3
1 4
0 1
1 3

>>> heap.swaps
[(1, 4), (0, 1), (1, 3)]

Explanation: 
After swapping elements 4 in position 1 and 1 in position 4 the array becomes 5 1 3 2 4. 
After swapping elements 5 in position 0 and 1 in position 1 the array becomes 1 5 3 2 4. 
After swapping elements 5 in position 1 and 2 in position 3 the array becomes 1 2 3 5 4, 
which is already a heap, 
because a[0] = 1 < 2 = a[1], a[0] = 1 < 3 = a[2], a[1] = 2 < 5 = a[3], a[1] = 2 < 4 = a[4].

Samples2:
input: [1, 2, 3, 4, 5]
ouput:
[]
Explanation: The input array is already a heap, because it is sorted in increasing order.
    
'''

#%%
class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []

  def ReadData(self):
    n = int(input())
    self._data = [int(s) for s in input().split()]
    assert n == len(self._data)

  def WriteResponse(self):
    print(len(self._swaps))
    for swap in self._swaps:
      print(swap[0], swap[1])
      
  def SiftDown(self, i):
    parent = i
    left_child = 2 * i +1
    right_child = 2 * i + 2
    
    if left_child <= len(self._data) - 1 and self._data[left_child] < self._data[parent]:
        parent = left_child
        
    if right_child <= len(self._data) - 1 and self._data[right_child] < self._data[parent]:
        parent = right_child
    
    if i != parent:
        self._swaps.append((i, parent))
        self._data[i], self._data[parent] = self._data[parent], self._data[i]
        self.SiftDown(parent)
            
  def GenerateSwaps(self):
    for i in range((len(self._data) - 1) // 2, -1, -1):
        self.SiftDown(i)

  def Solve(self):
    self.ReadData()
    self.GenerateSwaps()
    self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()

    
    