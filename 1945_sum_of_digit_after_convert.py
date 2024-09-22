'''
    DESCRIPTION:
    if s = "zbax" and k = 2, then the resulting integer would be 8 by the following operations:

    Convert: "zbax" ➝ "(26)(2)(1)(24)" ➝ "262124" ➝ 262124
    Transform #1: 262124 ➝ 2 + 6 + 2 + 1 + 2 + 4 ➝ 17
    Transform #2: 17 ➝ 1 + 7 ➝ 8
    Return the resulting integer after performing the operations described above.

'''

# Way 1
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        alpha_num = {"a": 1, "b": 2, "c": 3, "d":4, "e":5, "f":6, "g": 7, "h":8, "i":9 , "j":10, "k":11, "l":12, "m":13,"n":14, "o":15, "p":16, "q":17, "r":18, "s":19, "t":20, "u":21, "v":22, "w":23, "x":24, "y":25, "z":26}

        intS = ""

        #* Converting string to its number
        for i in s:
            intS += str(alpha_num[i])

        #* Adding digits 'k' times
        for i in range(k):
            sum = 0
            for i in range(len(intS)):
                sum += int(intS[i])
            intS = str(sum)

        return int(sum)
    

# Way 2
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        intS = ""

        # Using ASCII method to chnage from alphabet to integer
        for i in s:
            intS += str(ord(i) - ord('a') + 1)

        for i in range(k):
            sum = 0
            for i in intS:
                sum += int(i)
            intS = str(sum)

        return int(sum)
    