A = [[0, 0.5, 0, 0.5, 0],
     [1./3, 0, 1./3, 0, 1./3],
     [0, 0, 0, 0.5, 0.5],
     [0, 1, 0, 0, 0],
     [0.5, 0, 0, 0.5, 0]]
B = []
for i in range(len(A)):
    for j in range(len(A[i])):
        B.append(((i,j), A[i][j]))
Ardd = sc.parallelize(B)
rrdd = sc.parallelize([(0, 0), (1, 0.5), (2, 0), (3, 0.5), (4, 0)])

rrdd = Ardd.union(rrdd\
    .flatMap(lambda x: [((x[0], i), x[1]) for i in range(5)]))\
    .reduceByKey(lambda x, y: x*y)\
    .map(lambda x: (x[0][1], x[1]))\
    .reduceByKey(lambda x, y: x+y)

rrdd.take(10)