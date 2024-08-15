"""
The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. It usually starts with 0 and 1. The sequence goes like this:
0,1,1,2,3,5,8,13,21,34,55,…

In general, the Fibonacci sequence can be defined by the recurrence relation:

F(n)=F(n−1)+F(n−2)
with initial conditions

F(0)=0 and
F(1)=1.
"""
def fibonacci():
    n1=0
    n2=1
    count=1
    n=int(input("Please Enter a number upto which you want series"))
    if n<0:
        print("Enter number greater than zero")
    else:
        while count<=n:
            print(n1,end=" ")
            next_number=n1+n2
            n1=n2
            n2=next_number
            count=count+1


fibonacci()

"""
he time complexity of the corrected Fibonacci program is O(n).

Explanation:
Loop Execution: The while loop runs n times, where n is the number of terms specified by the user.
Operations Inside the Loop: Inside the loop, the operations (printing a number, calculating the next number, and updating the variables) all take constant time, O(1).


Space Complexity of Your Fibonacci Program
In the Fibonacci program you provided, the space complexity is O(1). This is because the program uses a fixed and small amount of memory regardless of how large the input n is.

Breakdown:

Variables Used:
n1, n2, next_number, count, and n are all simple integer variables.
These variables take up a fixed amount of space, which does not grow as the input size (n) increases.
No Additional Data Structures:
The program does not use arrays, lists, or any other data structures that would require additional memory proportional to the input size.
Regardless of how many terms you want to generate (whether it's 5 or 5,000), the same fixed number of variables is used.

"""


