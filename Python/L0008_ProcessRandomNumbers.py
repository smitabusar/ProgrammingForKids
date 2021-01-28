import random

#generate a random integer and float
# ints - start and end are required [start,end]
# floats - deafult range is 0<=n<1 [0,1)
print(f'''
    Random integers in range 1 to 10
    {random.randint(1,10)}
    {random.randint(1,10)}
    {random.randint(1,10)}
    Random floats
    {random.random()}
    {random.random()}
    {random.random()}
    Random floats from 10 to 20
    {random.uniform(10,20)}
    {random.uniform(10,20)}
    {random.uniform(10,20)}
    
''')