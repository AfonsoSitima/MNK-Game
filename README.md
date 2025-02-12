# MNK-Game
My first university project 

## Introduction
An  m, n, k  game is an abstract board game in which two players take turns placing stones on the free positions of a board with dimensions  m x n . The first player to achieve  k  consecutive stones of their own color—horizontally, vertically, or diagonally (both main diagonal and antidiagonal) wins the game. 

This game is a generalization of popular games such as Tic-Tac-Toe ( m = n = k = 3 ) or Gomoku ( m = n = 15, k = 5 ). Since the stones, once placed, are neither moved nor removed from the board, it is often played with pen and paper, using the symbols ‘X’ and ‘O’ instead of black and white stones.

## Objective/GamePlay
In this project, I aimed to create three different difficulty levels for players to challenge themselves against, on a board with user-defined dimensions (up to a maximum of 100x100).
To start the game, you need to call the function `jogo_mnk()` in the file, passing three arguments:
- cfg → A tuple of three elements representing the mnk configuration.
-	jog → An integer (-1 for ‘O’ and 1 for ‘X’).
-	lvl → A string indicating the difficulty level—there are three options: 'facil', 'normal', and 'dificil'.

Once you’ve set this up, simply run the program.

The player using ‘X’ always starts the game. The program will then prompt you to enter the position where you want to play. Positions range from 1 to the maximum number determined by the board size, following a left-to-right, top-to-bottom order.

Have fun and good luck! :)
