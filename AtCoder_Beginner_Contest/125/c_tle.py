#配列の中で一つの要素だけを除いた最大公約数の中で最大のものを返す
def gcd_exclude_1(A,N):
    seki = 1
    A.sort()
    Max = A[N-1]
    
    for x in reversed(range(2,)):
        count = 0
        
        #配列Aの中から1つの要素だけを除いた配列Aにおける最大の最大公約数をsekiを走査
        for y in reversed(range(2,N)):
            if A[y] % x != 0:
                break
        else:
            seki = x
            break

    return seki

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    
    print(gcd_exclude_1(A,N))

    
if __name__ == "__main__":
    main()


