__author__ = 'dubuapt'

def main():
    import sys

    f = sys.stdin
    caseCount = f.readline()

    # print range(int(caseCount))
    result = []
    ret = 0
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

        i = 0
        while i < l :
            sum = 0
            for j in range(i,n0+1 ):
                sum = sum + int(cost[j])
                if(j - i +1 >= n0):
                    ret = min(ret, sum/float(j - i + 1))
            i = i+1;
            #print("%.10f" %ret)
            result.append(ret)

        print("%.10f\n" %min(result))

main()




