# Water Bucket Puzzle

This Python script is a console-based puzzle game where the goal is to measure exactly 4 liters of water using three buckets of capacities 8 liters, 5 liters, and 3 liters. The player can fill, empty, and pour water between the buckets in order to reach the solution.

## How It Works

The game presents three buckets with the following capacities:
- 8-liter bucket (initially empty)
- 5-liter bucket (initially empty)
- 3-liter bucket (initially empty)

The player is tasked with measuring exactly 4 liters of water in any of the buckets through a series of actions, which include:
1. Filling a bucket to its full capacity.
2. Emptying a bucket.
3. Pouring water from one bucket into another until the second bucket is full or the first bucket is empty.

The game continues until one of the buckets holds exactly 4 liters of water.

### Key Functions

- **`display_buckets(bucket_8L, bucket_5L, bucket_3L)`**:
  Displays the current state of the 8L, 5L, and 3L buckets using a visual representation of the water levels.
  
- **`fill(bucket, capacity)`**:
  Fills the specified bucket to its full capacity.
  
- **`empty(bucket)`**:
  Empties the specified bucket, returning its water content to 0.

- **`pour(from_bucket, to_bucket, to_capacity)`**:
  Pours water from one bucket to another without exceeding the capacity of the second bucket.

- **`water_bucket_puzzle()`**:
  The main game loop where players can choose to fill, empty, or pour water between buckets until they reach the goal of 4 liters.

## Features

- **Interactive Gameplay**: The player can input commands to perform actions such as filling, emptying, or pouring between buckets.
- **Visual Display**: The state of each bucket is shown visually, helping the player track the progress of the water levels.
- **Victory Condition**: The game checks if any of the buckets holds exactly 4 liters, at which point the puzzle is solved and the game ends.

## How to Play

1. Run the script.
2. The game will display the current water levels in all three buckets.
3. Choose an action:
   - `(F)ill`: Fill a bucket to its maximum capacity.
   - `(E)mpty`: Empty the water from a bucket.
   - `(P)our`: Pour water from one bucket to another.
   - `(Q)uit`: Exit the game.
4. Select which bucket you want to perform the action on (8L, 5L, or 3L).
5. Continue playing until one of the buckets contains exactly 4 liters of water.

## Enjoy Gameplay

