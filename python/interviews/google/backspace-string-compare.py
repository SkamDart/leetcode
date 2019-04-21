from collections import deque
class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        BACKSPACE = '#'
        def backspace(word):
            q = deque()
            for char in word:
                if char == BACKSPACE:
                    try:
                        q.pop()
                    except IndexError:
                        pass
                else:
                    q.append(char)
            return ''.join(q)
        return backspace(S) == backspace(T)
