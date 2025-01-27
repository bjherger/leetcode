class Solution:
    """
    Requirements: S divides T if s is a concatenation of t with itself one or more times. Given two strings, return the largest x such that x divies both str 1 and strng 2.,
    Questions: 
      - At least one time
      - T of zero lenght? Allowed
      - t string must start at index zero
    Options
      - Brute force: Find longest shared string starting at index zero. Check if divides s1 and s2. If so, return. If not remove charatcter. T: O(max(n,m)**2) S: O(max(n,m))
      - Brute force: Add one character at a time starting at index zero. Check if divides s1 and s2. If so, continue. If not, return last valid t. T: O(max(n,m)**2) S: O(max(n,m))
      - Brute force: Remove characters from the shorter string, check s1 and s2 for condition. Can skip any substrings that do not have an integer multiple that matches the length of s1 and s2. T: O(min(n,m)) * (n+m) S: O(min(m,m))
      - Can we do better in space? no. Can we do better in time? nlgn or n? N seems difficult. 
      - Proof approach: Check if s1 + s2 = s2 + s1. If so, find greatest common denominator of s1 size and s2 size

      Implementing brute force 3, starting w/o optimization

      Time to implement: ~31 minutes
      Errors: (all cleaned up in final version)
       - In checkGCD used s_i istead of s[s_i] originally
       - Missed that shorter also needs to be a divisor of both strings (e.g. TAUXTAUX can't be valid for TAUX * 3 and TAUX * 6)
       - Originally mised that we can limit time to be less than len of longest string squared, and that we need to traverse both n and m to check 
      TODO: 
       - String slicing in check GCD isn't super clean. Could implement more cleanly
       - Could implement "proof" version more cleanly

    """
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        shorter = str1 if len(str1) < len(str2) else str2
        longer = str2 if len(str1) < len(str2) else str1

        while len(shorter) >= 0:

            if self.checkGCD(str1, shorter) and self.checkGCD(str2, shorter):
                return shorter
            shorter = shorter[:-1]

    def checkGCD(self, s, t):
        if t == '':
          return True
        
        if len(s)%len(t) != 0:
          return False
        
        s_i = 0
        t_i = 0
        while s_i <= len(s) - 1:
            if s[s_i] != t[t_i]:
                return False
            s_i += 1
            t_i += 1
            if t_i >= len(t):
                t_i = 0
        return True
    

s = Solution()
assert(s.gcdOfStrings('ABCABC', 'ABC'), 'ABC')
assert(s.gcdOfStrings('ABCABC', 'ABCD'), '')
assert(s.gcdOfStrings('ABCABCABCABCABCABC', 'ABCABC'), 'ABCABC')
