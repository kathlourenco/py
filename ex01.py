def soma(*args):
    print(args)
    for a in args:
        print(a)
    return sum(args)
print(f"soma: {soma(1, 2, 3)}")
print(f"soma: {soma(4, 5, 6)}")