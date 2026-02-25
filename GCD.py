def gcd(a, b):
    assert a >= 0 and b >= 0
    while a and b:
        if a >= b: a %= b
        else: b %= a
    return max(a, b)


def main():
    a, b = map(int, input().split())
    print(gcd(a, b))


if __name__ == "__main__":
    main()