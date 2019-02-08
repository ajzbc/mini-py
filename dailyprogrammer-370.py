# https://www.reddit.com/r/dailyprogrammer/comments/a72sdj/20181217_challenge_370_easy_upc_check_digits/
def upc(n):
    if len(n) < 11:
        n = (11-len(n))*"0" + n
    odd =  n[0::2]
    sumOdd = sum([int(i) for i in odd])
    mult = sumOdd * 3
    even = n[1::2]
    sumEven = sum([int(i) for i in even])
    total = mult + sumEven
    m = total%10
    if m == 0:
        return 0
    else :
        return 10 - m

print(upc('4210000526')) # 4
print(upc('3600029145')) # 2
print(upc('12345678910')) # 4
print(upc('1234567')) # 0
