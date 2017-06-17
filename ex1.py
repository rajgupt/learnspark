# existing collection in python 
data = [1, 2, 3, 4, 5]

# converted to RDD by parallelized
distData = sc.parallelize(data)

# find the sum by reduce
sum = distData.reduce(lambda a,b:a+b)

print sum

