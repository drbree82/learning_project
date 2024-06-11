

count = 9
for _ in range(4):
    print()
    for _ in range(3):
        if count >= 0:
            print(f"[{count}]", end='')
            count -= 1

