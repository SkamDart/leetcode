class Solution:
    def reverseString(self, s: 'List[str]') -> 'None':
        """
        Do not return anything, modify s in-place instead.
        """
        def _reverse(word, left, right):
            if left >= right:
                return
            word[left], word[right] = word[right], word[left]
            _reverse(word, left + 1, right - 1)
        _reverse(s, 0, len(s) - 1)
