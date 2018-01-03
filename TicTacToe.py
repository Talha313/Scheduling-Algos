import os #To clear console
name1="PLayer1 "
name2="Player2 "
field=['0','1','2','3','4','5','6','7','8']
count1=0
count2=0
def Board():
	os.system('clear')	
	print "  Tic Tac Toe\n\n"
	print "Player 1=X","  ","Player 2=O"	 
	print field[0],"  |  ",field[1],"  |  ",field[2]
	print "____|_______|_____"
	print field[3],"  |  ",field[4],"  |  ",field[5]
	print "____|_______|_____" 
	print field[6],"  |  ",field[7],"  |  ",field[8]
	print "____|_______|_____"
	print name1,count1," ",name2,count2	
def  Winner():
	if field[0]==field[1] and field[1]==field[2]:
            if field[0]=='X':
	        return 1
	    else:
		return 2
	elif field[3]==field[4] and field[4]==field[5]:
            if field[3]=='X':
	        return 1
	    else:
		return 2
	elif field[6]==field[7] and field[7]==field[8]:
            if field[6]=='X':
	        return 1
	    else:
		return 2
	elif field[0]==field[3] and field[3]==field[6]:
            if field[0]=='X':
	        return 1
	    else:
		return 2
	elif field[1]==field[4] and field[4]==field[7]:
            if field[1]=='X':
	        return 1
	    else:
		return 2
	elif field[2]==field[5] and field[5]==field[8]:
            if field[2]=='X':
	        return 1
	    else:
		return 2
	elif field[0]==field[4] and field[4]==field[8]:
            if field[0]=='X':
	        return 1
	    else:
		return 2
	elif field[2]==field[4] and field[4]==field[6]:
            if field[2]=='X':
	        return 1
	    else:
		return 2
	
def Play():
	turn=0
	n=0
        while 1:	
		    Board()
		    if turn==0:
		        i=input('Player 1 Enter a number from 1 to 9: ')
			if i>=0 and i<=10 and (field[i]!='X' or field[i]!='O'):
			    field[i]='X'
			    Board()
			    turn=1
			else:
		        	print "Wrong Choice\n"
			if Winner()==1:
			    #count1=count1+1;
			    print("Player 1 wins")
			    break
		    if turn==1:
		        n=input('Player 2 turn,Enter a number from 1 to 9: ')
			if n>=0 and n<=10 and (field[n]!='X' or field[n]!='O'):
			    field[n]='0'
			    Board()
			    turn=0	
		    else:
			print("Wrong Choice Turn Lost")
		 
		    if Winner()==2:
			#count2=count2+1
			print("Player 2 wins")	
		        break
	 		
						
Play()


