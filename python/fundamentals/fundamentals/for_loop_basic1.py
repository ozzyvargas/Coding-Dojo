"""
1. Basic 
- print all integers from 0 to 150
"""
for i in range(0, 151):
    print(i)

"""
2. Mulitples of Five 
- print all the multiples of 5 from 5 to 1,000
"""
for i in range(5,1001, 5):
    print(i)

""" 
3. Counting, the Dojo Way 
- print integers 1 to 100.
If divisible by 5, print "Coding" instead. 
If divisible by 10, print "Coding Dojo".
"""
for i in range(1,101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

"""
4. Whoa. That Sucker's Huge 
- Add odd integers from 0 to 500,000, and print the final sum.
"""
odd = []
def getting_oddNum():
    for i in range(0, 500001):
        if i % 2 == 0:
            continue
        elif i % 2 != 0:
            odd.append(i)
getting_oddNum()
def final_oddNum():
    total = sum(odd)
    print(total)
final_oddNum()

        
        
"""
5. Countdown by Fours
- print positive numbers starting at 2018, counting down by fours
"""
for i in range(2018,-1,-4):
    print(i)

"""
Flexible Counter
- Set three variables: lowNum, highNum, mult. Starting at lowNum
and going through highNum, print only the intergers that are a multiple
of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should
print 3,6,9 (on successive lines)
"""
lowNum = 2
highNum = 101
mult = 4
for i in range(lowNum,highNum):
    if i % mult != 0:
        continue
    elif i % mult == 0:
        print(i)