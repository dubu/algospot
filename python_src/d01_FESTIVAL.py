__author__ = 'dubuapt'

import sys

f = sys.stdin
# f.read()
caseCount = f.readline()

# print range(int(caseCount))
ret = []
for n in range(int(caseCount)):
    # print n
    line01 = f.readline()
    line02 = f.readline()
    ln = str(line01).strip().split()
    # print ln[0],  ln[1]
    # print line02

    cost = line02.strip().split()

    l = int(ln[0])
    n0 = int(ln[1])

    costs = []

    for j in xrange(n0, l+1):
        n = j

        #cost.inde[min(cost)]
        #cost.index(min(cost))

        for i in xrange((cost.index(min(cost))), l - n + 1):
            # print cost[0+i:i+n]
            # cost = sum([int(i) for i in cost[0+i:i+n]])/n
            aa = [int(i) for i in cost[0 + i:i + n]]
            #aa = map(int, cost[0 + i:i + n])
            #print(aa)
            # print sum(aa)/n
            temp = sum(aa) / float(n)

            if n == 0 :
                costs = temp
            if costs > temp :
                costs = temp
        # print "%.10f\n" %min(costs)
    # ret.append(min(costs))
    ret.append(costs)
for rs in ret:
    print("%.10f" %rs)








