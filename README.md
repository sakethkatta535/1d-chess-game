# 1D Chess Game

**Course:** CSC 110 - Introduction to Computer Programming  
**Programming Language:** Python  
**Project Type:** Game Development & Logic Implementation  
**Semester:** Fall 2023

## Overview

A Python implementation of a simplified chess variant played on a 1×9 board. This project demonstrates fundamental programming concepts including function decomposition, list manipulation, control flow, and game state management. Players control kings and knights with unique movement rules in a turn-based strategy game.

## Game Rules

### Board Setup
The game is played on a **1×9 linear board** with the following starting configuration:

+-----------------------------------------------------+
| WKi | WKn | WKn | | | | BKn | BKn | BKi |
+-----------------------------------------------------+

- **White pieces:** Left side (indices 0-2)
- **Black pieces:** Right side (indices 6-8)
- Each player has: **1 King (Ki)** and **2 Knights (Kn)**

### Movement Rules

**King Movement:**
- Moves **left or right** continuously until hitting:
  - Another piece (captures it and takes its position)
  - The edge of the board
- Can capture opponent pieces or accidentally capture own pieces

**Knight Movement:**
- **Jumps exactly 2 spaces** left or right
- Can jump over other pieces
- Captures any piece (including own) on the landing square
- If landing position is out of bounds, knight doesn't move

### Win Condition
The game ends when one player's king is captured. The player whose king remains wins.

## Implementation

### Core Functions

| Function | Purpose |
|----------|---------|
| `create_board()` | Initializes 1×9 board with starting positions |
| `printable_board(board)` | Formats board for text-based display |
| `is_valid_move(board, pos, player)` | Validates move legality (bounds & ownership) |
| `move_king(board, pos, direction)` | Executes king movement logic |
| `move_knight(board, pos, direction)` | Executes knight jump movement |
| `move(board, pos, direction)` | Delegates to appropriate movement function |
| `is_game_over(board)` | Checks for king capture (win condition) |
| `whos_the_winner(board)` | Determines winning player |

### Technical Features

**Data Structures:**
- Board represented as a **list of strings**
- Piece encoding: `"WKi"`, `"WKn"`, `"BKi"`, `"BKn"`, `"EMPTY"`
- Index-based position tracking (0-8)

**Control Flow:**
- Conditional logic for move validation
- Loops for king movement (until collision)
- String matching for piece type identification

**Input Validation:**
- Boundary checking (0 ≤ position ≤ 8)
- Piece ownership verification
- Out-of-bounds prevention for knight moves

## How to Run

### Prerequisites
- Python 3.x

### Execution
python one_d_chess.py


### Example Game Sequence
board = create_board()
print(printable_board(board))

move(board, 2, "RIGHT") # White knight jumps right
print(printable_board(board))

move(board, 6, "LEFT") # Black knight jumps left
print(printable_board(board))

move(board, 0, "RIGHT") # White king advances
print(printable_board(board))

if is_game_over(board):
winner = whos_the_winner(board)
print(f"{winner} wins!")


## Skills Demonstrated

### Python Fundamentals
- **Function design:** Modular decomposition with single responsibilities
- **List operations:** Indexing, slicing, modification, membership testing
- **String manipulation:** Formatting, concatenation, character matching
- **Control structures:** if/elif/else, for loops, range iteration

### Problem-Solving
- **Game state representation:** Mapping real-world game to data structure
- **Movement algorithms:** Different logic for kings vs. knights
- **Edge case handling:** Boundary checking, invalid moves
- **Win condition logic:** King presence detection

### Code Quality
- **Documentation:** Comprehensive docstrings for all functions
- **Comments:** Inline explanations for complex logic
- **Style compliance:** Adheres to CSC 110 style guide
- **Clean code:** Readable variable names, logical organization

## Design Decisions

### Why Lists Instead of Classes?
This project intentionally uses **functional programming** with lists to focus on foundational Python concepts before introducing object-oriented programming.

### Movement Implementation
- **King:** Uses a loop to simulate continuous movement until collision
- **Knight:** Direct index arithmetic (`position ± 2`)

### Board Display
The `printable_board()` function creates an ASCII art representation with borders and spacing for visual clarity.

## Learning Outcomes

This project taught:
- Breaking down complex problems into smaller functions
- Managing mutable state (list modifications)
- Handling edge cases and invalid inputs
- Writing clean, documented, maintainable code

## Project Context

This was my **first major Python project** in CSC 110, marking the beginning of my journey in computer science. It demonstrates the progression from basic programming concepts to more advanced work in later courses:

**Author:** Saketh Katta  
**University:** University of Arizona  
**Major:** Computer Science (Junior)  
**Course:** CSC 110 - Introduction to Computer Programming
