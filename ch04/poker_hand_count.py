# count poker hands

# 1. open the poker data file for reading
pokerFile = open("poker-hand-testing.data", "rU")

totalCount = 0  # 2. create variable to hold the count -- initialized it
pairCount = 0  # create and initialize variable to hold pair count
rankCount = [0] * 10
rankName = ['Nothing in hand',
            'One Pair',
            'Two Pairs',
            'Three of a kind',
            'Straight',
            'Flush',
            'Full house',
            'Four of a kind',
            'Straight flush',
            'Royal flush']

# 3. step through each line of the file
for line in pokerFile:
    totalCount = totalCount + 1  # at each line increment the counter

    handRank = line.split(',')[-1]  # rank: split on comma, get last item
    handRank = int(handRank)  # convert string input into an integer

    rankCount[handRank] += 1
    if handRank == 1:  # if handRank is 1 (it is a pair)
        pairCount = pairCount + 1  # add one to pair count

print("华丽的分割线".center(100, '*'))
print("Total hands in file: %d" % (totalCount,))
print("Count of pair hands: %7d" % (pairCount,))
print("Probability of pair: %5.2f %%." % (100 * pairCount / totalCount))
print("华丽的分割线".center(100, '*'))
for i in range(len(rankCount)):
    print("%d %15s hands count: %7d probability: %7.4f %%" % (
    i, rankName[i], rankCount[i], 100 * rankCount[i] / totalCount))
