# https://leetcode.com/problems/design-an-ordered-stream/description/

class OrderedStream(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.stream = [None]*n
        self.ptr = 0
        

    def insert(self, idKey, value):
        """
        :type idKey: int
        :type value: str
        :rtype: List[str]
        """
        idKey = idKey - 1
        self.stream[idKey] = value

        if self.ptr < idKey:
            return []
        else:
            while self.ptr < len(self.stream) and self.stream[self.ptr] is not None:
                self.ptr += 1
            return self.stream[idKey:self.ptr]
        
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)