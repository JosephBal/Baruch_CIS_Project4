# Baruch_CIS_Project4
This was my 5th project in my CIS 2300 "Programming and Computational Thinking" led by professor Sadat Chowdhury

# Project Description


Write a program that finds out how many numbers between 1 and 10,000 (inclusive) are divisible by any of the unique non-zero digits of K, where K = (your 5 digit number) x 19

Here is an example of what Jane, whose 5 digit number is 12340 should do:
For Jane, K = 234460, and her unique non-zero digits are: 2, 3, 4, and 6.
Therefore, Jane needs to write a program that calculates how many (count) of numbers between 1 and 10,000 are divisible by 2, 3, 4, or 6

My program shows only one numeric answer (the count)

Here is some sample code to help you understand:

```python

count = 0

# count all the numbers between 1 and 10,000 (inclusive) that are even (divisible by 2)
for n in range(1,10_000+1):
  if n % 2 == 0:
    count += 1

print(count)
```
