# Baruch_CIS_Project4
This was my 5th project in my CIS 2300 "Programming and Computational Thinking" led by professor Sadat Chowdhury

# Project Description

Write a program that finds out how many numbers between 1 and M (inclusive) are divisible by 2, 3, and 5 but not by 7, and displays that count. In the program:
M = (your unique 5 digit number)

Here are some sample numbers to clarify the question: 
```
1 is not divisible by 2, so it should not be counted
2 is divisible by 2 but not by 3, so it should not be counted
3 is not divisible by 2, so it should not be counted
...
29 is not divisible by 2, so it should not be counted
30 is divisble by 2, 3, and 5 and is not divisible by 7, so it should be counted
...
90  is divisble by 2, 3, and 5 and is not divisible by 7, so it should be counted 
...
210 is divisible by 2, 3, 5, and 7, so it should *not* be counted
... (so on)
```

My program displays only one numeric answer (the count)

Here is some sample code to help you get started:
```python
# my id
M = 12345

# initialize count to 0
count = 0 

# count all the numbers between 1 and M that are even (divisible by 2) and divisible by 3 also
for n in range(1,M+1):
  if (n % 2 == 0) and (n % 3 == 0):
    count += 1

# display output
print(count)

```
