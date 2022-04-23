'''
Brendan Devine
4/22/2022
Google Code Jam
Round 1A 2022
Test 1
Practice

Est Time: 5 hours
(to be fair, half that time was figuring out I/O)
Total Attempts: 19
(lots of these were I/O issues and me playing around)
# Code Jam Done: 1
'''

'''
**BAD MEMORY-INTENSIVE NAIVE APPROACH**
for word of length n
ex. RANT (n=4)
-------------
original word
0: RANT 
-------------------
double l-(n-0) letter from right
(these new words have length l)
1: RRANT 
-----------------------------------
double l-(n-1) letter in above lists
2: RAANT 
3: RRAANT
----------------------------------
double l-(n-2) letter in above lists
4: RANNT
5: RRANNT
6: RAANNT
7: RRAANNT
-----------------------------------
double l-(n-3) letter in above lists
8: RANTT
9: RRANTT
10: RRAANTT
11: RANNTT
12: RRANNTT
13: RAANNTT
14: RRAANNTT

Then just alphabetize and take first.

------------------------------------
Approach 2:
(This is way easier than I realized)
Essentially:
If the character to the right is equal
or further in the alphabet, double. 
'''

# bad way


def naive(a):
    n = len(a)
    wordList = [a]
    for i in range(n):
        subList = []
        for word in wordList:
            l = len(word)
            b = word[:l-(n-i)] + word[l-(n-i)] + word[l-(n-i)::]
            # can't append to wordList yet or will go on forever
            # probably not most efficient way to do it though
            subList.append(b)
        for word in subList:
            wordList.append(word)
    # this alphabetizing might be cheating but idk
    return sorted(wordList)[0]

# better way


def solve():
    # a is the original word, b is the new word
    a = str(input())
    n = len(a)
    b = ""
    for i in range(n-1):
        j = i + 1
        # if/while the next char is the same keep going till you find a diff. char
        while a[i] == a[j] and j < n-1:
            j += 1
        # if the char is behind the next (different) char in the alphabet, double it
        if a[i] < a[j]:
            b += a[i] + a[i]
        # otherwise don't double it
        else:
            b += a[i]
    # tack on the last char. Will always be single, not double.
    b += a[n-1]
    return b


if __name__ == '__main__':
    n = int(input())
    for case in range(1, n + 1):
        print("Case #" + str(case)+': ' + solve())
