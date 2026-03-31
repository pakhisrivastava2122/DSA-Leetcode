class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        res = ['?'] * (n + m - 1)
        locked = [False] * (n + m - 1)

        # Step 1: Apply 'T'
        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    if res[i + j] == '?' or res[i + j] == str2[j]:
                        res[i + j] = str2[j]
                        locked[i + j] = True
                    else:
                        return ""

        # Step 2: Fill remaining with 'a'
        for i in range(len(res)):
            if res[i] == '?':
                res[i] = 'a'

        # Step 3: Handle 'F'
        for i in range(n):
            if str1[i] == 'F':
                if ''.join(res[i:i+m]) == str2:
                    found = False
                    # 🔥 CHANGE: iterate from right
                    for j in range(m - 1, -1, -1):
                        if not locked[i + j]:
                            for c in 'abcdefghijklmnopqrstuvwxyz':
                                if c != str2[j]:
                                    res[i + j] = c
                                    found = True
                                    break
                            if found:
                                break
                    if not found:
                        return ""

        return ''.join(res)