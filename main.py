
print('Welcome to Tic-Tac-Toe')

#p1=input('Enter 1st player name:')
#p2=input('Enter 2nd player name:')
#
mtx=[[0,0,0],[0,0,0],[0,0,0]]
p1=0
p2=0
l1=0
l2=0
#if(mtx[0]==[1,1,1] or mtx[1]==[1,1,1] or mtx[2]==[1,1,1] or (mtx[0][0]==1 and mtx[1][0]==1 and mtx[2][0]==1) or (mtx[0][1]==1 and mtx[1][1]==1 and mtx[2][1])==1) or (mtx[0][2]==1 and mtx[1][2]==1 and mtx[2][2]==1) or (mtx[0][0]==1 and mtx[1][1]==1 and mtx[2][2]==1) or (mtx[0][2]==1 and mtx[1][1]==1 and mtx[2][0]==1):
def get_location1():
    p1 = int(input('\n(1)Enter the location to tic:\n'))
    p2 = int(input())
    mtx[p1][p2]=1

def get_location2():
    l1 = int(input('\n(2)Enter the location to tic:\n'))
    l2 = int(input())
    mtx[l1][l2]=2

for i in range(0,9):

    if(i%2==0):
        p1 = int(input('\n(1)Enter the location to tic:\n'))
        p2 = int(input())

        if (mtx[p1][p2] == 0):
            mtx[p1][p2] = 1
            if (mtx[0] == [1, 1, 1] or mtx[1] == [1, 1, 1] or mtx[2] == [1, 1, 1] or (
                                mtx[0][0] == 1 and mtx[1][0] == 1 and mtx[2][0] == 1) or (
                                mtx[0][1] == 1 and mtx[1][1] == 1 and mtx[2][1]) == 1) or (
                                mtx[0][2] == 1 and mtx[1][2] == 1 and mtx[2][2] == 1) or (
                                mtx[0][0] == 1 and mtx[1][1] == 1 and mtx[2][2] == 1) or (
                                mtx[0][2] == 1 and mtx[1][1] == 1 and mtx[2][0] == 1):
                print('\nPlayer one is winner')
                break
        else:
            print('wrong location')



    elif(i%2==1):
        l1 = int(input('\n(2)Enter the location to tic:\n'))
        l2 = int(input())

        if (mtx[l1][l2] == 0):
            mtx[l1][l2] = 2
            if (mtx[0] == [2, 2, 2] or mtx[1] == [2, 2, 2] or mtx[2] == [2, 2, 2] or (
                                mtx[0][0] == 2 and mtx[1][0] == 2 and mtx[2][0] == 2) or (
                                mtx[0][1] == 2 and mtx[1][1] == 2 and mtx[2][1]) == 2) or (
                                mtx[0][2] == 2 and mtx[1][2] == 2 and mtx[2][2] == 2) or (
                                mtx[0][0] == 2 and mtx[1][1] == 2 and mtx[2][2] == 2) or (
                                mtx[0][2] == 2 and mtx[1][1] == 2 and mtx[2][0] == 2):
                print('\nPlayer two is winner')
                break
        else:
            print('wrong location')



    print(mtx[0])
    print(mtx[1])
    print(mtx[2])


