# Q1: 232. Implement Queue using Stacks
class MyQueue:
    def __init__(self):
        self.stack1 = []  # for pushing
        self.stack2 = []  # for popping

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self) -> bool:
        return len(self.stack1) == 0 and len(self.stack2) == 0

class Solution:
    # Q2: 394. Decode String
    def decodeString(self, s: str) -> str:
        if not s:
            return ""
        stack = []
        for c in s:
            if c != ']':
                stack.append(c)
            else:
                string = ""
                while stack[-1] != '[':
                    string = stack.pop() + string
                stack.pop()
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                stack.append(int(num) * string)
        return "".join(stack)
    
    # Q3: 2327. Number of People Aware of a Secret
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
    
        know_secret = [0] * (n + 1)
        know_secret[1] = 1
        
        for i in range(2, n + 1):
            for j in range(max(1, i - forget + 1), i - delay + 1):
                know_secret[i] = (know_secret[i] + know_secret[j]) % MOD
                
        # Sum up people who haven't forgotten yet
        result = 0
        for i in range(max(1, n - forget + 1), n + 1):
            result = (result + know_secret[i]) % MOD
            
        return result