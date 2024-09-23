# Automated Chess Bot Using Stockfish and PyAutoGUI

This project is an automated chess bot that can play live chess games by calculating the best move using the Stockfish chess engine. It captures the current chessboard state via screenshots, retrieves the board position using FEN notation, and performs moves automatically using PyAutoGUI. Random sleep intervals are added to make the bot's behavior more human-like.

## Personal Use

This project has not been adapted for other users due to potential for use in rated games. I do not condone cheating on Chess.com or any other chess platform.

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
