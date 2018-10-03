# Dynamic programming

Here I demonstrate a pratical example how dynamic programming can speed up the prossesing time.
<\br>
I used a function that calculates the Fibonacci sequence in a for loop from 0 to the number the user wants to.
<\br>
There are two python scripts. One using the Fibonacci function in a recursive way `times.py`, and other in a dynamic way `timesDym.py`.
<\br> 
You have to install the matplotlib package before running them. 
<\br>
Take a look how different is the processing time as you increase the number in the Fibonacci sequence. Bellow I display the output plots using the 35th position in the sequence. In a recursive way, the time spent to calculate increases exponentially whereas, in dynamic way, it's linear.
<\br>
![rec](http://143.107.196.146:3000/fiboRec.png)
![dym](http://143.107.196.146:3000/fiboDym.png)
