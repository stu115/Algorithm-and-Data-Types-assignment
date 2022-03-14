# -*- coding: utf-8 -*-
"""
Created on Sun May 19 15:04:14 2019

@author: 21359035
"""
class Stack:
   def __init__(self):
       self.items = []
   def isEmpty(self):
       return self.items == []
   def push(self,item):
        self.items.append(item)
   def pop(self):
        return self.items.pop()
   def peek(self):
        return self.items[len(self.items)-1]
   def size(self):
        return len(self.items)
    
class Queue:
   def __init__(self):
       self.items = []
   def is_empty(self):
       return self.items == []
   def size(self):
       return len(self.items)
   def enqueue(self, item):
       self.items.insert(0,item)  
   def dequeue(self):
       return self.items.pop()

def Stack:   
    s1 = Stack()

def Queue:
    q = Queue()
    
s1.push(1)
s1.push(2)
s1.push(3)
while not s1.isEmpty():
    (q.enqueue(s1.pop))
    print(q.dequeue(), end = ' ')
    print(q.dequeue(), end = ' ')
    print(q.dequeue(), end = ' ')
    
    
