mat= [['1','|','2' ,'|','3' ],
		['_',' ','_',' ','_'],
		['4','|','5','|','6'],
		['_',' ','_',' ','_'],
		['7','|','8','|','9'],]

def printMatrix(m):
	for i in range(5):
		print(mat[i][0], mat[i][1], mat[i][2], mat[i][3], mat[i][4])


def changeMatrix(m):
	g= input("Are you X or O?")
	position= int(input("Select the number you want to play (1 to 9): "))
	if position == 1:
		m[0][0]= g
	elif position == 2:
		m[0][2]= g
	elif position == 3:
		m[0][4]= g
	elif position == 4:
		m[2][0]= g
	elif position == 5:
		m[2][2]= g
	elif position == 6:
		m[2][4]= g
	elif position == 7:
		m[4][0]= g
	elif position == 8:
		m[4][2]= g
	else:
		m[4][4]= g

def endGame(m):

	if m[0][0] == 'o' and m[0][2] == 'o' and m[0][4] == 'o':
		global end
		end= False
		print("Player O wins!")
		return end
	elif m[2][0] == 'o' and m[2][2] == 'o' and m[2][4] == 'o':
		global end
		end= False
		print("Player O wins!")
		return end
	elif m[4][0] == 'o' and m[4][2] == 'o' and m[4][4] == 'o':
		global end
		end= False
		print("Player O wins!")
		return end
	elif m[0][0] == 'o' and m[2][0] == 'o' and m[4][0] == 'o':
		global end
		end= False
		print("Player O wins!")
		return end
	elif m[0][2] == 'o' and m[2][2] == 'o' and m[4][2] == 'o':
		global end
		end= False
		print("Player O wins!")
		return end
	elif m[0][4] == 'o' and m[2][4] == 'o' and m[4][4] == 'o':
		global end
		end= False
		print("Player O wins!")
		return end
	elif m[0][0] == 'o' and m[2][2] == 'o' and m[4][4] == 'o':
		global end
		end= False
		print("Player O wins!")
		return end
	elif m[4][0] == 'o' and m[2][2] == 'o' and m[0][4] == 'o':
		global end
		end= False
		print("Player O wins!")
		return end
	elif m[0][0] == 'x' and m[0][2] == 'x' and m[0][4] == 'x':
		global end
		end= False
		print("Player X wins!")
		return end
	elif m[2][0] == 'x' and m[2][2] == 'x' and m[2][4] == 'x':
		global end
		end= False
		print("Player X wins!")
		return end
	elif m[4][0] == 'x' and m[4][2] == 'x' and m[4][4] == 'x':
		global end
		end= False
		print("Player X wins!")
		return end
	elif m[0][0] == 'x' and m[2][0] == 'x' and m[4][0] == 'x':
		global end
		end= False
		print("Player X wins!")
		return end
	elif m[0][2] == 'x' and m[2][2] == 'x' and m[4][2] == 'x':
		global end
		end= False
		print("Player X wins!")
		return end
	elif m[0][4] == 'x' and m[2][4] == 'x' and m[4][4] == 'x':
		global end
		end= False
		print("Player X wins!")
		return end
	elif m[0][0] == 'x' and m[2][2] == 'x' and m[4][4] == 'x':
		global end
		end= False
		print("Player X wins!")
		return end
	elif m[4][0] == 'x' and m[2][2] == 'x' and m[0][4] == 'x':
		global end
		end= False
		print("Player X wins!")
		return end

end= True
while end:

	printMatrix(mat)
	changeMatrix(mat)
	endGame(mat)

printMatrix(mat)
