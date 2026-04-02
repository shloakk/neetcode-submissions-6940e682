class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in ["(", "{", "["]:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                popped = stack.pop()
                if popped == "(" and char == ")":
                    continue
                elif popped == "{" and char == "}":
                    continue
                elif popped == "[" and char == "]":
                    continue
                return False
        if len(stack) > 0:
            return False
        return True