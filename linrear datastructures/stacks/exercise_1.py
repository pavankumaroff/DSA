# reversing a string using stack

class String_Reverser:
    def reverse(self, input):
        stack = []
        for char in input:
            stack.append(char)

        reversed_string = ""
        while len(stack) != 0:
            char = stack.pop()
            reversed_string += char

        return reversed_string


reverser = String_Reverser()
result = reverser.reverse("abcde")
print(result)
