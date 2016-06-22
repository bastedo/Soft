# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 12:34:54 2016

@author: student
"""

class Node:
    def __init__(self,game_board, move_number, turn, name, wcastle, bcastle, en_passent ):
        self.game_coordinationX = ["A", "B", "C", "D", "E", "F", "G", "H"]
        self.game_coordinationY = ["1", "2", "3", "4", "5", "6", "7", "8"]
        self.name = name
        self.turn = turn
        self.en_passent = en_passent
        self.move_number = move_number
        self.wcastle = wcastle
        self.bcastle = bcastle
        self.game_board = list(game_board)
        self.moves = []
        self.captures = []
        self.nodes = []
        #print(self.name)
        #print(self.turn)
        #print(self.game_board)
        
        
        if self.is_checkmated():
            print(self.name)
            print(self.game_board)
            
        else:   
            #print("Nije")
            self.generate_nodes()

        #self.generate_moves(5)
        #print(self.captures)
    
    def generate_moves (self, location):
        del self.moves[:]
        del self.captures[:]


    # Notes:
    # this function is so complicated because it finds where the newly selected piece can move and capture

    # Remove illegal selections
        if self.game_board[location] == None or self.game_board[location][1] != str(self.turn):
            return
    
        selected = location

    
        # Pawn for player 1
        if self.game_board[selected] == 'P1':
            if self.game_board[selected+8] == None:
                self.moves.append(selected+8)
                if selected//8 == 1 and self.game_board[selected+16] == None:
                    self.moves.append(selected+16)
            if selected%8 != 0 and ((self.game_board[selected+7] != None and self.game_board[selected+7][1] == '2') or \
                                    (self.game_board[selected-1] == 'P2' and self.en_passent == selected-1)):
                self.captures.append(selected+7)
            if selected%8 != 7 and ((self.game_board[selected+9] != None and self.game_board[selected+9][1] == '2') or \
                                    (self.game_board[selected+1] == 'P2' and self.en_passent == selected+1)):
                self.captures.append(selected+9)
    
        # Pawn for player 2
        if self.game_board[selected] == 'P2':
            if self.game_board[selected-8] == None:
                self.moves.append(selected-8)
                if selected//8 == 6 and self.game_board[selected-16] == None:
                    self.moves.append(selected-16)
            if selected%8 != 7 and ((self.game_board[selected-7] != None and self.game_board[selected-7][1] == '1') or \
                                    (self.game_board[selected+1] == 'P1' and self.en_passent == selected+1)):
                self.captures.append(selected-7)
            if selected%8 != 0 and ((self.game_board[selected-9] != None and self.game_board[selected-9][1] == '1') or \
                                    (self.game_board[selected-1] == 'P1' and self.en_passent == selected-1)):
                self.captures.append(selected-9)
    
        # Rook and half of Queen for both players
        if self.game_board[selected][0] in 'RQ':
            x,y = selected%8,selected//8
    
            for i in range(x+1,8,1):
                if self.game_board[i+y*8] == None:   # Check if no blocking piece
                    self.moves.append(i+y*8)
                elif self.game_board[i+y*8][1] != str(self.turn): # Check if is attacking
                    self.captures.append(i+y*8)
                    break
                else:
                    break
    
            for i in range(x-1,-1,-1):
                if self.game_board[i+y*8] == None:
                    self.moves.append(i+y*8)
                elif self.game_board[i+y*8][1] != str(self.turn):
                    self.captures.append(i+y*8)
                    break
                else:
                    break
    
            for i in range(y+1,8,1):
                if self.game_board[x+i*8] == None:
                    self.moves.append(x+i*8)
                elif self.game_board[x+i*8][1] != str(self.turn):
                    self.captures.append(x+i*8)
                    break
                else:
                    break
    
            for i in range(y-1,-1,-1):
                if self.game_board[x+i*8] == None:
                    self.moves.append(x+i*8)
                elif self.game_board[x+i*8][1] != str(self.turn):
                    self.captures.append(x+i*8)
                    break
                else:
                    break
    
        # Bishop and other half of Queen for both players
        if self.game_board[selected][0] in 'BQ':
    
            i = selected+7
            while (i-7)%8 != 0 and (i-7)//8 != 7:   # Check if valid move
                if self.game_board[i] == None:   # Check if no blocking piece
                    self.moves.append(i)
                elif self.game_board[i][1] != str(self.turn): # Check if is attacking
                    self.captures.append(i)
                    break
                else:
                    break
                i += 7
    
            i = selected+9
            while (i-9)%8 != 7 and (i-9)//8 != 7:
                if self.game_board[i] == None:
                    self.moves.append(i)
                elif self.game_board[i][1] != str(self.turn):
                    self.captures.append(i)
                    break
                else:
                    break
                i += 9
    
            i = selected-7
            while (i+7)%8 != 7 and (i+7)//8 != 0:
                if self.game_board[i] == None:
                    self.moves.append(i)
                elif self.game_board[i][1] != str(self.turn):
                    self.captures.append(i)
                    break
                else:
                    break
                i -= 7
    
            i = selected-9
            while (i+9)%8 != 0 and (i+9)//8 != 0:
                if self.game_board[i] == None:
                    self.moves.append(i)
                elif self.game_board[i][1] != str(self.turn):
                    self.captures.append(i)
                    break
                else:
                    break
                i -= 9
    
        # Knight for both players
        if self.game_board[selected][0] == 'N':
            x,y = selected%8,selected//8
    
            if x >= 2 and y <= 6:   # Check if valid move
                if self.game_board[(x-2)+(y+1)*8] == None:   # Check if no blocking piece
                    self.moves.append((x-2)+(y+1)*8)
                elif self.game_board[(x-2)+(y+1)*8][1] != str(self.turn): # Check if is attacking
                    self.captures.append((x-2)+(y+1)*8)
            if x >= 1 and y <= 5:
                if self.game_board[(x-1)+(y+2)*8] == None:
                    self.moves.append((x-1)+(y+2)*8)
                elif self.game_board[(x-1)+(y+2)*8][1] != str(self.turn):
                    self.captures.append((x-1)+(y+2)*8)
    
            if x <= 6 and y <= 5:
                if self.game_board[(x+1)+(y+2)*8] == None:
                    self.moves.append((x+1)+(y+2)*8)
                elif self.game_board[(x+1)+(y+2)*8][1] != str(self.turn):
                    self.captures.append((x+1)+(y+2)*8)
            if x <= 5 and y <= 6:
                if self.game_board[(x+2)+(y+1)*8] == None:
                    self.moves.append((x+2)+(y+1)*8)
                elif self.game_board[(x+2)+(y+1)*8][1] != str(self.turn):
                    self.captures.append((x+2)+(y+1)*8)
    
            if x <= 5 and y >= 1:
                if self.game_board[(x+2)+(y-1)*8] == None:
                    self.moves.append((x+2)+(y-1)*8)
                elif self.game_board[(x+2)+(y-1)*8][1] != str(self.turn):
                    self.captures.append((x+2)+(y-1)*8)
            if x <= 6 and y >= 2:
                if self.game_board[(x+1)+(y-2)*8] == None:
                    self.moves.append((x+1)+(y-2)*8)
                elif self.game_board[(x+1)+(y-2)*8][1] != str(self.turn):
                    self.captures.append((x+1)+(y-2)*8)
    
            if x >= 1 and y >= 2:
                if self.game_board[(x-1)+(y-2)*8] == None:
                    self.moves.append((x-1)+(y-2)*8)
                elif self.game_board[(x-1)+(y-2)*8][1] != str(self.turn):
                    self.captures.append((x-1)+(y-2)*8)
            if x >= 2 and y >= 1:
                if self.game_board[(x-2)+(y-1)*8] == None:
                    self.moves.append((x-2)+(y-1)*8)
                elif self.game_board[(x-2)+(y-1)*8][1] != str(self.turn):
                    self.captures.append((x-2)+(y-1)*8)
    
        # King for both players
        if self.game_board[selected][0] == 'K':
            x,y = selected%8,selected//8
            attacked = self.attacked_spaces(1+self.turn%2,self.game_board)
    
            if selected == 3 and self.wcastle%2 == 0 and \
               self.game_board[1] == None and self.game_board[2] == None and\
               not 1 in attacked and not 2 in attacked and not 3 in attacked:
                self.moves.append(1)
            if selected == 3 and -1 < self.wcastle < 2 and \
               self.game_board[4] == None and self.game_board[5] == None and self.game_board[6] == None and\
               not 3 in attacked and not 4 in attacked and not 5 in attacked:
                self.moves.append(5)
    
            if selected == 59 and self.bcastle%2 == 0 and \
               self.game_board[58] == None and self.game_board[57] == None and\
               not 57 in attacked and not 58 in attacked and not 59 in attacked:
                self.moves.append(57)
            if selected == 59 and -1 < self.bcastle < 2 and \
               self.game_board[60] == None and self.game_board[61] == None and self.game_board[62] == None and\
               not 59 in attacked and not 60 in attacked and not 61 in attacked:
                self.moves.append(61)
    
            if x >= 1 and y <= 6: # Check if valid move
                if self.game_board[(x-1)+(y+1)*8] == None:   # Check if no blocking piece
                    self.moves.append((x-1)+(y+1)*8)
                elif self.game_board[(x-1)+(y+1)*8][1] != str(self.turn): # Check if is attacking
                    self.captures.append((x-1)+(y+1)*8)
            if y <= 6:
                if self.game_board[x+(y+1)*8] == None:
                    self.moves.append(x+(y+1)*8)
                elif self.game_board[x+(y+1)*8][1] != str(self.turn):
                    self.captures.append(x+(y+1)*8)
            if x <= 6 and y <= 6:
                if self.game_board[(x+1)+(y+1)*8] == None:
                    self.moves.append((x+1)+(y+1)*8)
                elif self.game_board[(x+1)+(y+1)*8][1] != str(self.turn):
                    self.captures.append((x+1)+(y+1)*8)
            if x <= 6:
                if self.game_board[(x+1)+y*8] == None:
                    self.moves.append((x+1)+y*8)
                elif self.game_board[(x+1)+y*8][1] != str(self.turn):
                    self.captures.append((x+1)+y*8)
            if x <= 6 and y >= 1:
                if self.game_board[(x+1)+(y-1)*8] == None:
                    self.moves.append((x+1)+(y-1)*8)
                elif self.game_board[(x+1)+(y-1)*8][1] != str(self.turn):
                    self.captures.append((x+1)+(y-1)*8)
            if y >= 1:
                if self.game_board[x+(y-1)*8] == None:
                    self.moves.append(x+(y-1)*8)
                elif self.game_board[x+(y-1)*8][1] != str(self.turn):
                    self.captures.append(x+(y-1)*8)
            if x >= 1 and y >= 1:
                if self.game_board[(x-1)+(y-1)*8] == None:
                    self.moves.append((x-1)+(y-1)*8)
                elif self.game_board[(x-1)+(y-1)*8][1] != str(self.turn):
                    self.captures.append((x-1)+(y-1)*8)
            if x >= 1:
                if self.game_board[(x-1)+y*8] == None:
                    self.moves.append((x-1)+y*8)
                elif self.game_board[(x-1)+y*8][1] != str(self.turn):
                    self.captures.append((x-1)+y*8)
    
        # Find the player's king
        for i in range(64):
            if self.game_board[i] != None and self.game_board[i][0] == 'K' and self.game_board[i][1] == str(self.turn):
                break
    
        # See if a move allows the king to be taken
        t_moves = list(self.moves)
        for j in t_moves:
            t_game = list(self.game_board)
            t_game[j] = t_game[selected]
            t_game[selected] = None
            if self.game_board[selected][0] == 'K':
                i = j
            if i in self.attacked_spaces(1+self.turn%2,t_game):
                self.moves.remove(j)
    
        # See if a capture allows the king to be taken
        t_captures = list(self.captures)
        for j in t_captures:
            t_game = list(self.game_board)
            t_game[j] = t_game[selected]
            t_game[selected] = None
            if self.game_board[selected][0] == 'K':
                i = j
            if i in self.attacked_spaces(1+self.turn%2,t_game):
                self.captures.remove(j)
    
    def attacked_spaces(self, player,board):
        attacked = []
    
        for i in range(64):
            if board[i] == None:
                continue
    
            # Pawn for player 1
            if board[i] == 'P1' and player == 1:
                if i%8 != 0:
                    attacked.append(i+7)
                if i%8 != 7:
                    attacked.append(i+9)
    
            # Pawn for player 2
            if board[i] == 'P2' and player == 2:
                if i%8 != 7:
                    attacked.append(i-7)
                if i%8 != 0:
                    attacked.append(i-9)
    
            # Rook and half of Queen for both players
            if board[i][0] in 'RQ' and board[i][1] == str(player):
                x,y = i%8,i//8
    
                for j in range(x+1,8,1):
                    attacked.append(j+y*8)
                    if board[j+y*8] != None:
                        break
    
                for j in range(x-1,-1,-1):
                    attacked.append(j+y*8)
                    if board[j+y*8] != None:
                        break
    
                for j in range(y+1,8,1):
                    attacked.append(x+j*8)
                    if board[x+j*8] != None:
                        break
    
                for j in range(y-1,-1,-1):
                    attacked.append(x+j*8)
                    if board[x+j*8] != None:
                        break
    
            # Bishop and other half of Queen for both players
            if board[i][0] in 'BQ' and board[i][1] == str(player):
    
                j = i+7
                while (j-7)%8 != 0 and (j-7)//8 != 7:
                    attacked.append(j)
                    if board[j] != None:
                        break
                    j += 7
    
                j = i+9
                while (j-9)%8 != 7 and (j-9)//8 != 7:
                    attacked.append(j)
                    if board[j] != None:
                        break
                    j += 9
    
                j = i-7
                while (j+7)%8 != 7 and (j+7)//8 != 0:
                    attacked.append(j)
                    if board[j] != None:
                        break
                    j -= 7
    
                j = i-9
                while (j+9)%8 != 0 and (j+9)//8 != 0:
                    attacked.append(j)
                    if board[j] != None:
                        break
                    j -= 9
    
            # Knight for both players
            if board[i][0] == 'N' and board[i][1] == str(player):
                x,y = i%8,i//8
    
                if x >= 2 and y <= 6:
                    attacked.append((x-2)+(y+1)*8)
                if x >= 1 and y <= 5:
                    attacked.append((x-1)+(y+2)*8)
    
                if x <= 6 and y <= 5:
                    attacked.append((x+1)+(y+2)*8)
                if x <= 5 and y <= 6:
                    attacked.append((x+2)+(y+1)*8)
    
                if x <= 5 and y >= 1:
                    attacked.append((x+2)+(y-1)*8)
                if x <= 6 and y >= 2:
                    attacked.append((x+1)+(y-2)*8)
    
                if x >= 1 and y >= 2:
                    attacked.append((x-1)+(y-2)*8)
                if x >= 2 and y >= 1:
                    attacked.append((x-2)+(y-1)*8)
    
            if board[i][0] == 'K' and board[i][1] == str(player):
                x,y = i%8,i//8
    
                if x >= 1 and y <= 6:
                    attacked.append((x-1)+(y+1)*8)
                if y <= 6:
                    attacked.append(x+(y+1)*8)
                if x <= 6 and y <= 6:
                    attacked.append((x+1)+(y+1)*8)
                if x <= 6:
                        attacked.append((x+1)+y*8)
                if x <= 6 and y >= 1:
                    attacked.append((x+1)+(y-1)*8)
                if y >= 1:
                    attacked.append(x+(y-1)*8)
                if x >= 1 and y >= 1:
                    attacked.append((x-1)+(y-1)*8)
                if x >= 1:
                    attacked.append((x-1)+y*8)
    
        return attacked
            
    def is_checkmated(self):
        """Returns 1 if the player with the current turn to move is checkmated"""
        brojpoteza = 0
        for i in range(64):
            if self.game_board != None:
                self.generate_moves(i)
                #print(len(self.moves)+len(self.captures))
                brojpoteza = brojpoteza + len(self.moves)+len(self.captures)
        #self.generate_moves(i)
        #print(self.game_board)
        if brojpoteza == 0:
            return 1
        else:
            return 0
        #print(len(self.moves)+len(self.captures))           

    def move_piece(self, destination, selected):
        """Moves the selected piece"""
        game_board = list(self.game_board)
    
    
        if self.game_board[selected][0] == 'P':
            # En-passent rule activation
            if abs(destination-selected) in (7,9) and self.en_passent != None and abs(self.en_passent-destination) == 8:
                self.game_board[self.en_passent] = None
    
            # En-passent rule initiation
            self.en_passent = None
            if abs(destination-selected) == 16:
                self.en_passent = destination
    

            if destination < 8 and self.turn == 2:
               # 
                print ("DA2222")
            if destination > 55 and self.turn == 1:
                print ("DA11111")
                
        #game_board[destination]=None
        game_board[destination] = game_board[selected]
        game_board[selected] = None
        
        return game_board
        
    def generate_nodes(self):
        if self.move_number<3:
            for i in range(len(self.game_board)):
               if self.game_board[i] != None and self.game_board[i][1] == str(self.turn) :
                    self.generate_moves (i)
                    if len(self.moves) != 0:
                        #print(self.game_board[i])
                        #print (self.moves)
                        #print (self.captures)
                        for j in range(len(self.moves)):
                            #print (self.moves[j])
                            #print(self.game_coordinationX[self.moves[j]/8])
                            self.nodes.append(Node(self.move_piece(self.moves[j],i), self.move_number+1, 1+self.turn%2, str(self.name)+str(self.game_board[i])+"->"+str(self.game_coordinationX[self.moves[j]%8])+str(self.game_coordinationY[self.moves[j]/8])+"---", self.wcastle, self.bcastle, self.en_passent))
                    if len(self.captures) != 0:
                        #print(self.game_board[i])
                        #print (self.moves)
                        #print("capture")
                        #print (self.captures)
                        
                        for k in range(len(self.captures)):
                            #print (self.captures[k])
                            #print(self.move_piece(self.captures[k],i))
                            self.nodes.append(Node(self.move_piece(self.captures[k],i), self.move_number+1, 1+self.turn%2, str(self.name)+str(self.game_board[i])+"->"+str(self.game_coordinationX[self.captures[k]%8])+str(self.game_coordinationY[self.captures[k]/8])+"---", self.wcastle, self.bcastle, self.en_passent))
                            
                        #str(self.game_coordinationX[self.moves[j]/8])+str(self.game_coordinationY[self.moves[j]%8])+
                
                
                
    
                