<img width="595" alt="Screenshot 2024-07-30 at 16 12 34" src="https://github.com/user-attachments/assets/48bd88e7-16d6-467f-9276-199493ae603b">
# Tic Tac Toe with AI

This project implements a Tic Tac Toe game with an AI opponent using the Minimax algorithm. The game is developed using Python and the Pygame library for the graphical user interface.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Features](#features)
- [License](#license)

## Installation

1. **Clone the repository**:
   git clone https://github.com/your-username/tictactoe.git
   cd tictactoe

2. **Create and activate a virtual environment**:
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install the required dependencies**:
pip install -r requirements.txt

Note: Make sure to include a requirements.txt file in your repository listing all dependencies, such as pygame.

## Usage

- Run the game using the following command:
python runner.py

Note: The game will start in a window where you can choose to play as either 'X' or 'O'. The AI will play as the other player. Click on the grid to make your moves.

## Project Structure
- runner.py: Main script to start the game. It handles the game loop, user interface, and interactions with the AI.
- tictactoe.py: Contains the game logic, including functions to determine the game state, possible moves, and the AI's Minimax algorithm.

## Features
- Graphical User Interface: Developed using Pygame, the GUI allows for easy interaction and a pleasant gaming experience.
- AI Opponent: The AI uses the Minimax algorithm to play optimally. It can be configured to play as either 'X' or 'O'.
- Game States and Rules: The game follows the standard rules of Tic Tac Toe, including win, lose, and draw conditions.

<img width="593" alt="Screenshot 2024-07-30 at 16 12 46" src="https://github.com/user-attachments/assets/add61acd-87da-48b5-94c8-b725d3b9c7ff">
<img width="590" alt="Screenshot 2024-07-30 at 16 12 57" src="https://github.com/user-attachments/assets/2c79f1f2-72cd-4fdb-8b9c-3997a3a18174">

