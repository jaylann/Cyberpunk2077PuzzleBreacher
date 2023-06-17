# Breach Protocol Solver

Breach Protocol Solver is a Python program designed to solve matrix-based sequence problems, mimicking the breach protocol mini-game found in the game Cyberpunk 2077. This program optimizes and calculates the most efficient sequences, within a given buffer size.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

To run this software, you need Python 3.7 or later and numpy library. If you do not have Python, you can download it from the official site - https://www.python.org/. 

To install numpy, use pip:

```bash
pip install numpy
```

### Installation

1. Clone the repo:
```bash
git clone https://github.com/your_username_/breach-protocol-solver.git
```

2. Navigate to the directory:
```bash
cd breach-protocol-solver
```

## Usage

The core function of the script is `solve_breach_protocol(code_matrix, sequences, buffer)`, where:
- `code_matrix` is the 2D matrix of codes.
- `sequences` is the dictionary containing sequence identifiers and their respective code sequences.
- `buffer` is the buffer size or the maximum length of the sequences.

You can run the script from the command line as follows:

```bash
python breach_protocol_solver.py
```

By default, the script uses predefined `CODE_MATRIX`, `SEQUENCES`, and `BUFFER`. You can change these values in the script to use your own data.

```python
CODE_MATRIX = np.array([
    [0xE9, 0xE9, 0x7A, 0xBD, 0x55, 0x55],
    [0x1C, 0x1C, 0x1C, 0x7A, 0x55, 0x39],
    [0x1C, 0x7A, 0x7A, 0x1C, 0x55, 0x1C],
    [0xBD, 0xE9, 0x55, 0x7A, 0x55, 0x7A],
    [0x55, 0x55, 0x55, 0x7A, 0x55, 0x1C],
    [0xBD, 0xBD, 0xE9, 0x1C, 0x55, 0xE9]
])

SEQUENCES = {
    0: [0x55, 0x55, 0xBD],
    1: [0xBD, 0xBD, 0xBD],
    2: [0x55, 0xE9, 0x55]
}

BUFFER = 5
```

After running the script, it will output the calculated sequence and print a visual representation of the moves in the matrix.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
