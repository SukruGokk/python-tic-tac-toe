#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author: Şükrü Erdem Gök
# @date: 07/21/2020
# @os: Linux Mint 20
# @version: Python 3.8.2

# TIC-TAC-TOE GAME

# Lib
from tkinter import Tk, Button, messagebox, PhotoImage # GUI
from random import choice, randint
from math import ceil
from os import execl             # To
from sys import argv, executable # Restart
from winsound import Beep # Sound effects

# Main class
class tic_tac_toe(Tk):

    # Constructor
    def __init__(self):

        super().__init__()# Initialization of super class (Tk)

        self.geometry("311x255") # Size 130 pixel width, 135 pixel height
        self.title("TTT") # Title (blank)

        self.iconphoto(False, PhotoImage(file = "icon.png"))

        for buttonNumber in range(1, 10): # Definiton of buttons
            if buttonNumber == 1:col = row = 1
            elif buttonNumber == 4:col = 2; row = 1
            elif buttonNumber == 7:col = 3; row = 1
           
            exec("self.button{} = Button(activebackground='gray', bd = 1, fg = 'white', bg = 'black', width = 4, height = 1, command = self.button{}c, font = ('Berlin Sans FB', 30, 'bold'))".format(buttonNumber, buttonNumber))
            exec("self.button{}.grid(row = {}, column = {})".format(buttonNumber, row, col)); row += 1 # Grid the buttons

        self.tableList =[["", "", ""], ["", "", ""], ["", "", ""]] # Table's character list

        self.player_win_msg = "!! YOU WON !!" # Player win msg
        self.cpu_win_msg = "!! CPU WON !!" # Cpu win msg
        self.draw_msg = "!! NO ONE WON !!" # Draw msg

        self.sqrNum = len(self.tableList) * len(self.tableList[0])

        if randint(0, 2): # Random. maybe cpu will play first move maybe player will
            rand = randint(0, 3)
            if rand == 1:self.cpu_play()
            elif rand == 2:self.replace_horizontal()
            else: self.replace_random()

    def win(self, msg): # Win method
        messagebox.showinfo("GAME OVER", msg) # Show a alert box that containing parameter as message
        execl(executable, executable, *argv)

    def control(self, symbol): # Control if there same symbol connected
        if symbol == "X":msg = self.player_win_msg # If connected symbol equals 'X' that means; player won. That's why, send ~player win message~ as parameter to win method
        else:msg = self.cpu_win_msg # Else, send ~cpu win message~ as parameter to win method

        # Check if the symbols are cross-linked 
        if self.tableList[0][0] == symbol and self.tableList[1][1] == symbol and self.tableList[2][2] == symbol:
            self.win(msg)

        elif self.tableList[2][0] == symbol and self.tableList[1][1] == symbol and self.tableList[0][2] == symbol:
            self.win(msg)

        # Check if the symbols connected vertically            
        elif (self.tableList[0][0] == symbol and self.tableList[0][1] == symbol and self.tableList[0][2] == symbol) or (self.tableList[1][0] == symbol and self.tableList[1][1] == symbol and self.tableList[1][2] == symbol) or (self.tableList[2][0] == symbol and self.tableList[2][1] == symbol and self.tableList[2][2] == symbol):
            self.win(msg)

        # Check if the symbols connected horizontally
        elif (self.tableList[0][0] == symbol and self.tableList[1][0] == symbol and self.tableList[2][0] == symbol) or (self.tableList[0][1] == symbol and self.tableList[1][1] == symbol and self.tableList[2][1] == symbol) or (self.tableList[0][2] == symbol and self.tableList[1][2] == symbol and self.tableList[2][2] == symbol):
            self.win(msg)

    # Check if the player that given as parameter won
    def control_plyr(self, plyer):
        if plyer == "player":self.control("X")
        else:self.control("O")

    # Block the player
    def block_player(self):
        doit = False
        for colNumber in range(len(self.tableList)):

            # String that containing horizontal squares' symbols
            col = self.tableList[colNumber][0] + self.tableList[colNumber][1] + self.tableList[colNumber][2]

            # Check opponent symbol
            if col == "XX":
                doit = True
                break

        if doit:
            for rown in range(0, 3):
                if self.tableList[colNumber][rown] == "":
                    self.tableList[colNumber][rown] = "O"
                    exec("self.button{}['state'] = 'disabled';self.button{}['text'] = 'O'".format(colNumber*3 + rown+1, colNumber*3 + rown+1))
                    break

            self.control_plyr("cpu")
        else:
            # Choose goal row
            for rowNumber in range(len(self.tableList)):

                # String that containing horizontal squares' symbols
                row = self.tableList[0][rowNumber] + self.tableList[1][rowNumber] + self.tableList[2][rowNumber]

                #Check opponent symbol
                if row == ("XX"):
                    doit = True
                    break

                if rowNumber == 2:
                    self.replace_horizontal()

            if doit:
                for coln in range(0, 3):
                    if self.tableList[coln][rowNumber] == "":
                        self.tableList[coln][rowNumber] = "O"
                        exec("self.button{}['state'] = 'disabled';self.button{}['text'] = 'O'".format(coln*3 + rowNumber+1, coln*3 + rowNumber+1))
                        break

            self.control_plyr("cpu")

        self.sqrNum = len(self.tableList) * len(self.tableList[0])

        for i in self.tableList:
            for j in i:
                if j != "": self.sqrNum -= 1

        if self.sqrNum == 0:
            self.win(self.draw_msg)
        else:
            self.sqrNum = len(self.tableList) * len(self.tableList[0])

    # Replace symbol randomly
    def replace_random(self):
        emptySqrList = [] # List that containing empty square coordinates

        # Appending empty squares' coordinates to list
        for colNum in range(len(self.tableList)):
            for rowNum in range(len(self.tableList[0])):
                if self.tableList[colNum][rowNum]== "":emptySqrList.append([colNum, rowNum])
        try:
            chosenOne = choice(emptySqrList)
            self.tableList[chosenOne[0]][chosenOne[1]] = "O"
            exec("self.button{}['state'] = 'disabled';self.button{}['text'] = 'O'".format(chosenOne[0]*3 + chosenOne[1] + 1, chosenOne[0]*3 + chosenOne[1] + 1))

        except: # Draw
            self.win(self.draw_msg)

        self.control_plyr("cpu")

        self.sqrNum = len(self.tableList) * len(self.tableList[0])

        for i in self.tableList:
            for j in i:
                if j != "": self.sqrNum -= 1

        if self.sqrNum == 0:
            self.win(self.draw_msg)
        else:
            self.sqrNum = len(self.tableList) * len(self.tableList[0])

    # Replace symbol horizontally
    def replace_horizontal(self):
        # Choose goal row
        for rowNumber in range(len(self.tableList)):

            # String that containing horizontal squares' symbols
            row = self.tableList[0][rowNumber] + self.tableList[1][rowNumber] + self.tableList[2][rowNumber]

            #Check opponent symbol
            if row.find("X") == -1:break

            if rowNumber == 2:
                self.replace_random()
                return

        for coln in range(0, 3):
            if self.tableList[coln][rowNumber] == "":
                self.tableList[coln][rowNumber] = "O"
                exec("self.button{}['state'] = 'disabled';self.button{}['text'] = 'O'".format(coln*3 + rowNumber+1, coln*3 + rowNumber+1))
                break

        self.sqrNum = len(self.tableList) * len(self.tableList[0])

        for i in self.tableList:
            for j in i:
                if j != "": self.sqrNum -= 1

        if self.sqrNum == 0:
            self.win(self.draw_msg)
        else:
            self.sqrNum = len(self.tableList) * len(self.tableList[0])

        self.control_plyr("cpu")# Check if cpu won

    # Create functions that run whena button clicked
    for butNum in range(1, 10):
        exec('def button{}c(self):\n' \
             '   self.tableList[{}][{}] = "X"\n'\
             '   self.button{}["text"] = "X"\n'\
             '   self.button{}["state"] = "disabled"\n'\
             '   Beep(5000, 70)\n'\
             '   self.control_plyr("player")\n'\
             '   self.cpu_play()'.format(butNum, ceil(butNum/3) - 1, butNum - (ceil(butNum/3) - 1) * 3 - 1, butNum, butNum, butNum))

    def cpu_play(self):# Cpu play
        if randint(0, 2): self.block_player()
        else:
            doit = False
            colNumber = 0

            # Choose goal column
            for colNumber in range(len(self.tableList)):

                # String that containing horizontal squares' symbols
                col = self.tableList[colNumber][0] + self.tableList[colNumber][1] + self.tableList[colNumber][2]

                # Check opponent symbol
                if col.find("X") == -1:
                    doit = True
                    break

                if colNumber == 2:
                    if randint(1, 2):self.block_player()
                    else:self.replace_horizontal()

            if doit:
                for rown in range(0, 3):
                    if self.tableList[colNumber][rown] == "":
                        self.tableList[colNumber][rown] = "O"
                        exec("self.button{}['state'] = 'disabled';self.button{}['text'] = 'O'".format(colNumber*3 + rown+1, colNumber*3 + rown+1))
                        break

            for i in self.tableList:
                for j in i:
                    if j != "":self.sqrNum -= 1

            if self.sqrNum == 0:self.win(self.draw_msg)
            else: self.sqrNum = len(self.tableList) * len(self.tableList[0])

            self.control_plyr("cpu")# Check if the cpu won

if __name__ == "__main__":

    game = tic_tac_toe()# Game object
    
    game.mainloop()# Loop game object
