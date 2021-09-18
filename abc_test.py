def abc_reduce(string: str):
    stack = []
    for alphabet in string:
        if len(stack) != 0:
            b_alphabet = stack.pop()
            if len(stack) != 0 and b_alphabet == alphabet:
                a_alphabet = stack.pop()
                if a_alphabet == alphabet:
                    continue
                else:
                    stack.append(a_alphabet)
                    stack.append(b_alphabet)
            else:
                stack.append(b_alphabet)
        stack.append(alphabet)
    x = ''
    for i in stack:
        x += i
    return x


if __name__ == '__main__':
    print(abc_reduce('aabbcccbad'))
