# reversing a string using stack
import io


class String_Reverser:
    def reverse(self, input):
        stack = []
        for char in input:
            stack.append(char)

        buffer = io.StringIO()
        while len(stack) != 0:
            char = stack.pop()
            buffer.write(char)

        return buffer.getvalue()


reverser = String_Reverser()
result = reverser.reverse("abcde")
print(result)
