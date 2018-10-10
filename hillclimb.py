x=[]
y=[]
z=[]
import copy

def calc_cost(N,x,y,z):
	
	cost=0
	for i in range(N-1):
		cost+=((x[z[i+1]]-x[z[i]])*(x[z[i+1]]-x[z[i]])) + ((y[z[i+1]]-y[z[i]])*(y[z[i+1]]-y[z[i]]))
	return cost

def hillclimb(n,cost,x,y,z):
	px,py=-1,-1
	for i in range(n):
		for j in range(i):
			xx = copy.deepcopy(z)
			xx[i],xx[j]=xx[j],xx[i]
			ncost = calc_cost(n,x,y,xx)
			if cost> ncost:
				cost = ncost
				px,py=i,j
	if px==-1:
		return
	z[px],z[py]=z[py],z[px] 
	hillclimb(n,cost,x,y,z)







def main_():
	N = int(input())
	x = [0]*N
	y=[0]*N
	z=[0]*N
	for i in range(N):
		x[i] = int(input())
	for i in range(N):
		y[i] = int(input())
		z[i] = i
	cost = 0

	hillclimb(N,calc_cost(N,x,y,z),x,y,z)
	print(z)



main_()