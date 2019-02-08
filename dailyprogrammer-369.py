# https://www.reddit.com/r/dailyprogrammer/comments/a0lhxx/20181126_challenge_369_easy_hex_colors/
def hexcolor(r, g, b):
    r = hex(r)[2:]
    g= hex(g)[2:]
    b = hex(b)[2:]
    # this is dumb
    if len(r) == 1:
        r = "00"
    if len(g) == 1:
        g = "00"
    if len(b) == 1:
        b = "00"

    return "#" + r + g + b

print(hexcolor(255, 99, 71)) #ff6347
print(hexcolor(184, 134, 11)) #b88600
print(hexcolor(189, 183, 107)) #bdb76b
print(hexcolor(0, 0, 205)) #0000cd