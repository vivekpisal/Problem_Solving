board=[' ' for x in range(10)]

def printboard(board):
    print('  |   | ')
    print(board[1],'|',board[2],'|',board[3])
    print('-----------')
    print('  |   | ')
    print(board[4],'|',board[5],'|',board[6])
    print('-----------')
    print('  |   | ')
    print(board[7],'|',board[8],'|',board[9])
    

printboard(board)

def isvalid(bo,pos):
    return bo[pos]==' '


def winner(bo,le):
    return bo[1]==le and bo[2]==le and bo[3]==le or bo[4]==le and bo[5]==le and bo[6]==le or bo[7]==le and bo[8]==le and bo[9]==le or bo[1]==le and bo[4]==le and bo[7]==le or bo[2]==le and bo[5]==le and bo[8]==le or bo[3]==le and bo[6]==le and bo[9]==le or bo[1]==le and bo[5]==le and bo[9]==le or bo[3]==le and bo[5]==le and bo[7]==le

def NextTurn(bo,pos,si):
    bo[pos]=si
    printboard(bo)


def isfull(bo):
    for i in range(1,len(bo)):
        if bo[i]!=' ':
            f=True
        else:
            f=False
            break
    return f
    


def main():
    while True:
        if isfull(board):
            print('Match is Tied')
            break
        x=int(input('First player chance'))
        if x<=9:
            if isvalid(board,x):
                NextTurn(board,x,'X')
        else:
            x=int(input('First player chance'))
            if x<=9:
                if isvalid(board,x):
                    NextTurn(board,x,'X')
        if winner(board,'X'):
            print('Player 1 is win the Match')
            break
        if isfull(board):
            print('Match is Tied')
            break
        o=int(input('Second player chance'))
        if o<=9:
            if isvalid(board,o):
                NextTurn(board,o,'O')
        else:
            o=int(input('Second player chance'))
            if o<=9:
                if isvalid(board,o):
                    NextTurn(board,o,'O')
        if winner(board,'O'):
            print('Player 2 win the Match')
        if isfull(board):
            print('Match is Tied')
            break
            
                
            
main()
