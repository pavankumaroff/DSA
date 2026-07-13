class Balanced_Expression:
    def __init__(self):
        self.stack = []

    def validate_expression(self, string):
        pairs = {")": "(", "]": "[", "}": "{", ">": "<"}

        for char in string:
            if char in "([{<":
                self.stack.append(char)
            if char in ")]}>":
                if not self.stack or self.stack.pop() != pairs[char]:
                    return False

        return len(self.stack) == 0


be = Balanced_Expression()
result = be.validate_expression("[(a+[b])]")
print(result)
