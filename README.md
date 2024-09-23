# Automated Chess Bot Using Stockfish and PyAutoGUI

This project is an automated chess bot that can play live chess games by calculating the best move using the Stockfish chess engine. It captures the current chessboard state via screenshots, retrieves the board position using FEN notation, and performs moves automatically using PyAutoGUI. Random sleep intervals are added to make the bot's behavior more human-like.

## Features

- **Live Chess Game Play**: Automatically detects board state and makes moves in real time.
- **FEN Position Detection**: Uses Forsyth-Edwards Notation (FEN) to accurately track the chessboard state.
- **Stockfish Integration**: Calculates the best move using the Stockfish chess engine.
- **Automated Moves**: PyAutoGUI is used to simulate mouse clicks and move pieces on the chessboard.
- **Randomized Sleep Intervals**: Adds sleep intervals between moves to simulate human behavior and avoid robotic gameplay.

## Prerequisites

To run this project, you need the following installed:

- **Python 3.x**
- Python libraries:
  - `stockfish` (Stockfish integration)
  - `pyautogui` (for controlling the mouse and interacting with the screen)
  - `pillow` (for taking screenshots)

Install the required libraries by running:

pip install stockfish pyautogui pillow

You also need the **Stockfish chess engine**. Download it from [Stockfish's official website](https://stockfishchess.org/download/).

After downloading Stockfish, ensure that the executable is accessible in your system's environment path, or specify the path when creating the Stockfish instance in your Python script.

## How It Works

1. **Capture the Current Board State**:
   - The bot captures a screenshot of the chessboard using PyAutoGUI.
   - The `getFen()` function extracts the board's state in **FEN notation** (Forsyth-Edwards Notation), which includes the positions of all the pieces and whose turn it is to move.

2. **Calculate the Best Move**:
   - After getting the FEN string, the bot sets it in Stockfish using `stockfish.set_fen_position(fen_position)`.
   - The Stockfish engine then calculates the optimal move using `stockfish.get_best_move()`.

3. **Move the Pieces**:
   - The best move is extracted from Stockfish and is parsed to determine the source and destination squares.
   - Using PyAutoGUI, the bot moves the chess pieces by simulating mouse clicks on the calculated coordinates.

4. **Random Sleep Intervals**:
   - To make the bot's actions appear less robotic, random sleep intervals are introduced between moves using `time.sleep(random.randint(...))`.

5. **Repeat Until the Game Ends**:
   - The bot continuously monitors the board state and plays moves until the game is over.

## Usage

To run the bot, simply execute the Python script. Ensure that the chessboard is clearly visible on the screen and that Stockfish is properly configured.

```bash
python chess_bot.py
