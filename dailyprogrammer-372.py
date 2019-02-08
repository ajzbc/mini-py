# https://www.reddit.com/r/dailyprogrammer/comments/afxxca/20190114_challenge_372_easy_perfectly_balanced/
def balance(s):

    x = 0
    y = 0

    for i in s:
        if i == "x":
            x += 1
        else:
            y += 1
    
    return (x==y)

print(balance("xxyy"))
# True

print(balance("xyxyx"))
# False