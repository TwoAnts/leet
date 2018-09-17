#!/usr/bin/env python3
#-*- coding : utf-8-*-

def print_lru_list(head):
    if not head:
        print('None')
        return
    it = head
    res = []
    while it:
        res.append('(%s, %s)' %(it.key, it.val))
        it = it.next
        if it is head:
            break
    print('->'.join(res))

class LRUCacheNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None
        
    def move_to_head(self, head):
        if head is self:
            return self
        if head is None:
            self.next = self
            self.pre = self
            return self
        if self.pre:
            self.pre.next = self.next
        if self.next:
            self.next.pre = self.pre
        self.next = head
        self.pre = head.pre
        if self.pre:
            self.pre.next = self
        if self.next:
            self.next.pre = self
        return self
        

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.dict = {}
        self.lru_list = None

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        #print('----get %s' %key)
        node = self.dict.get(key, None)
        if node is None:
            return -1
        self.lru_list = node.move_to_head(self.lru_list)
        #print_lru_list(self.lru_list)
        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        #print('----put %s %s' %(key, value))
        #print_lru_list(self.lru_list)
        node = self.dict.get(key, None)
        if not node:
            if len(self.dict) >= self.cap:
                node = self.lru_list.pre 
                #print('drop %s %s' %(node.key, node.val))
                del self.dict[node.key]
                node.key = key
                node.val = value
            else:
                node = LRUCacheNode(key, value)
            self.dict[key] = node
        else:
            node.val = value
        self.lru_list = node.move_to_head(self.lru_list)
        #print_lru_list(self.lru_list)
            
def test():
    lru_cache = LRUCache(3)
    print(lru_cache.get(2))
    lru_cache.put(1, 1)
    lru_cache.put(2, 2)
    lru_cache.put(3, 3)
    lru_cache.put(4, 4)
    print(lru_cache.get(2))
    print(lru_cache.get(1))
    print(lru_cache.get(4))
    
    
if __name__ == '__main__':
    test()