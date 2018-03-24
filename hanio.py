def hanioTower(a,b,c,n):
    if n<=1:
        print(a,"->",c)
    else:
        hanioTower(a,c,b,n-1)
        print(a,"->",c)
        hanioTower(b,a,c,n-1)

if __name__=="__main__":
    import sys
    hanioTower(str(sys.argv[1]),str(sys.argv[2]),str(sys.argv[3]),int(sys.argv[4]))