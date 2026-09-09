x,y,z=map(int,input().split())
cost1=12*x
cost2=12*y+z
print(min(cost1,cost2))