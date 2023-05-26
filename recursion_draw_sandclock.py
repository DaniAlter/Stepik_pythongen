def rec_sandclock(n=1, q=16):
    if n < 4:
        print((str(n) * q).center(16))
        rec_sandclock(n + 1, q - 4)
    print((str(n) * q).center(16))

