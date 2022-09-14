N = int(input())
stack = []

for _ in range(N):
    command = input().split(' ')
    if command[0] == '1':
        stack.append(int(command[1]))
    elif command[0] == '2':
        if stack:
            stack.pop()
    elif command[0] == '3':
        if stack:
            print(max(stack))
    else:
        if stack:
            print(min(stack))


while len(stack) > 1:
    print(str(stack.pop())+", ", end="")
print(stack.pop())




