Date: 2013-08-29  16:30
Title: Python:list中のエントリの頻度
Type: post  
Excerpt: 


[How to count the occurrences of a list item in Python?](http://stackoverflow.com/questions/2600191/how-to-count-the-occurrences-of-a-list-item-in-python)

    >>> from collections import Counter
    >>> z = ['blue', 'red', 'blue', 'yellow', 'blue', 'red']
    >>> [(k,v) for k,v in Counter(z).items() if v >1 ]

    [('blue', 3), ('red', 2)]  

    >>> z.count('blue')
    3
    
    