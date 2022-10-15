chessboard = [[0,1,2,3,4,5,6,7],
			[8,9,10,11,12,13,14,15],
			[16,17,18,19,20,21,22,23],
			[24,25,26,27,28,29,30,31],
			[32,33,34,35,36,37,38,39],
			[40,41,42,43,44,45,46,47],
			[48,49,50,51,52,53,54,55],
			[56,57,58,59,60,61,62,63]]

def findindex(pos):
	for i in range(8):
		for j in range(8):
			if chessboard[i][j] == pos:
				return [i,j]
				
def knight(a,b):
	moveind = []
	movepos = []
	ib,ia = 0,0
	con = [[1,2],[1,-2],[-1,2],[-1,-2],[2,1],[2,-1],[-2,1],[-2,-1]]
	for i in range(8):
		ia = a-con[i][0]
		ib = b-con[i][1]
		moveind.append([ia,ib])
		if ia<0 or ib<0 or ib>7 or ia>7:
			continue
		else:
			movepos.append(chessboard[moveind[i][0]][moveind[i][1]])
	return movepos


def leastmove(moves):
	global visited,count,tmpcount,recount
	recount+=1
	tmp = moves
	for j in visited:
		if j in tmp:
			tmp.remove(j)

	position = tmp
	for i in position:
		if recount>=count and visited !=[] and count!=0:
			visited.pop()
			recount -=1
			return 0
		else:	
			if y in position:
				tmpcount = len(visited)
				if count==0:
					count = len(visited)
				elif count > tmpcount:
					count = tmpcount
				visited.pop()
				recount -=1
				return 0
			else:
				visited.append(i)
				index = findindex(i)
				positionx = knight(index[0],index[1])
				leastmove(positionx)
	if visited != []:
		visited.pop()
	recount -=1
	return 0

x = int(input("Enter the position of knight :"))
y = int(input("Enter the target position :"))
visited = []
count = 0
recount = 0
tmpcount = 0
z=leastmove([x])
print(" ",count," steps")