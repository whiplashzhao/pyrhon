def make_change(amount, coins=[10, 15, 25], hand=None):
    hand = [] if hand is None else hand
    if amount == 0:
        yield hand
    for coin in coins:
        if coin > amount or (len(hand) > 0 and hand[-1] < coin):
            continue
            # Python continue 语句跳出本次循环，而break跳出整个循环。
            # continue 语句用来告诉Python跳过当前循环的剩余语句，然后继续进行下一轮循环。
            # continue语句用在while和for循环中。

        for result in make_change(amount-coin, coins=coins, hand=hand+[coin]):
            # print(result)
            yield result


# print(list(make_change(40)))
for aa in make_change(40):
    print(aa)
