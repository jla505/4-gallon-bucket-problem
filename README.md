# Water Jug Problem Solver

## Overview
This project is a solution to the classic water jug problem. The objective is to fetch exactly 4 gallons of water using only a 3-gallon and a 5-gallon unmarked bucket, and to do so in less than 15 steps.

## Features
- Simulates the process of filling, emptying, and pouring between two buckets.
- Solves the problem using a systematic approach to ensure the correct amount of water is measured.
- Provides step-by-step instructions to reach the solution.

## Technologies Used
- Python

## How It Works
The solution involves a series of steps where water is poured between the two buckets, filled, and emptied as necessary to measure exactly 4 gallons. The program uses a simple algorithm to determine the sequence of actions.

## Installation and Setup
1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/water-jug-problem-solver.git
    cd water-jug-problem-solver
    ```

2. **Run the Program**:
    ```bash
    python water_jug_solver.py
    ```

## Usage
- Run the `water_jug_solver.py` script to execute the solution to the water jug problem.
- The program will display the steps taken to measure exactly 4 gallons of water.

## Detailed Steps Explained
1. **Define the Buckets Class**:
   - Represents the two buckets and provides methods to manipulate them.
   - `capacity1`, `capacity2`: Maximum capacities of the two buckets.
   - `current1`, `current2`: Current water levels in the buckets.

2. **Methods to Manipulate Buckets**:
   - `fill_bucket1()`, `fill_bucket2()`: Fill the respective buckets to their maximum capacities.
   - `empty_bucket1()`, `empty_bucket2()`: Empty the respective buckets.
   - `pour_bucket1_to_bucket2()`, `pour_bucket2_to_bucket1()`: Pour water from one bucket to another, ensuring the receiving bucket is either full or the pouring bucket is empty.
   - `is_solution()`: Check if either bucket contains exactly 4 gallons of water.

3. **Main Function (`water_jug_problem()`)**:
   - Initializes the buckets and performs the steps to solve the problem.
   - Iteratively fills, pours, and empties the buckets until the solution is found or 15 steps are executed.

## Contributing
Contributions are welcome! Please follow these steps to contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a Pull Request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


