from copy import deepcopy
import numpy as np


class BreachProtocol:
    def __init__(self, matrix, sequences, buffer):
        self.matrix = matrix
        self.sequences = sequences
        self.buffer = buffer

    @staticmethod
    def score_row(row, built_sequences, sequences):
        """ Calculate scores for each element in a given row.

        Parameters:
        row (list): List of elements in a row.
        built_sequences (list): Previously built sequences.
        sequences (list): Target sequences to compare with.

        Returns:
        tuple: A tuple containing the scores list and the updated built sequences.
        """

        # Initialize score array with zeros
        score = [0] * len(row)

        # Create a deep copy of built_sequences for each element in the row
        temp_sequences = [deepcopy(built_sequences) for _ in row]

        for i, value in enumerate(row):
            for j, built_sequence in enumerate(built_sequences):
                target_sequence = sequences[j]

                # Check if built_sequence can be extended by the current value
                if len(target_sequence) > len(built_sequence) and value == target_sequence[len(built_sequence)]:
                    temp_sequences[i][j].append(value)

                    # Increase score if built_sequence is shorter than target sequence
                    if len(temp_sequences[i][j]) < len(target_sequence):
                        score[i] += j + 1
                    else:
                        score[i] += (j + 1) * 9  # 3 ** 2 = 9
                else:
                    # Reset sequence if it cannot be extended to match target sequence
                    if len(temp_sequences[i][j]) < len(target_sequence):
                        temp_sequences[i][j] = []

        return score, temp_sequences

    def solve(self):
        return self.calculate_moves(self.matrix, (0, 0), [[], [], []], 0, 1)

    def calculate_moves(self, game_matrix, current_position, sequence_built, max_game_score, depth):
        """
        Calculate possible moves from a given position on the game matrix.

        Args:
            game_matrix (list): The matrix representing the game state.
            current_position (tuple): The current position in the game matrix.
            sequence_built (list): A list of sequences built so far.
            max_game_score (int): The maximum score obtained so far.
            depth (int): The current depth of the recursion.

        Returns:
            int: The new maximum score.
            list: The position map for achieving the maximum score.
        """

        new_positions_map = []
        current_score = max_game_score
        next_move = (0, 0)

        horizontal_movement = depth % 2 == 1
        game_row = game_matrix[current_position[1]] if horizontal_movement else [game_matrix[i][current_position[0]] for
                                                                                 i in range(len(game_matrix))]

        potential_scores, new_sequences = self.score_row(game_row, sequence_built, self.sequences)
        max_score = max(potential_scores)

        y_coordinates = [current_position[1]] * len(
            self.get_indexes(potential_scores, max_score)) if horizontal_movement else self.get_indexes(
            potential_scores, max_score)
        x_coordinates = self.get_indexes(potential_scores, max_score) if horizontal_movement else [current_position[
                                                                                                       0]] * len(
            y_coordinates)

        new_positions = [(x_coordinates[i], y_coordinates[i]) for i in range(len(x_coordinates))]
        if current_position in new_positions:
            new_positions.remove(current_position)

        if depth >= self.buffer:
            return max_game_score + max_score, [new_positions[0]] if new_positions else []

        for pos in new_positions:
            new_game_matrix = deepcopy(self.matrix)
            new_game_matrix[pos[1]][pos[0]] = 0

            new_max_score, temp_positions_map = self.calculate_moves(new_game_matrix, pos,
                                                                     new_sequences[
                                                                         pos[0] if horizontal_movement else pos[1]],
                                                                     max_score, depth + 1)

            if new_max_score + current_score > max_game_score:
                max_game_score = new_max_score + current_score
                next_move = pos
                new_positions_map = temp_positions_map

        return max_game_score, new_positions_map + [next_move]

    @staticmethod
    def get_indexes(lst, element):
        """
        Returns the indexes of an element in a list.

        Args:
            lst (list): The list to search.
            element (any): The element to find.

        Returns:
            list: A list of indexes at which the element can be found.
        """
        return [i for i, x in enumerate(lst) if x == element]

    def visualize(self, moves):
        code_matrix = deepcopy(self.matrix)
        for y in range(len(code_matrix)):
            for x in range(len(code_matrix[y])):
                if (x, y) in moves:
                    code_matrix[y][x] = moves.index((x, y)) + 1
                else:
                    code_matrix[y][x] = 0
        print(code_matrix)


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


def solve_breach_protocol(code_matrix, sequences, buffer):
    """Solve the breach protocol.

    Args:
        code_matrix (np.array): The matrix of code sequences.
        sequences (dict): The dictionary containing sequence identifiers and their respective code sequences.
        buffer (int): The buffer size.

    Returns:
        List of moves.
    """
    breach_protocol = BreachProtocol(code_matrix, sequences, buffer)
    _, moves = breach_protocol.solve()
    return moves


def main():
    moves = solve_breach_protocol(CODE_MATRIX, SEQUENCES, BUFFER)
    print(moves)
    breach_protocol = BreachProtocol(CODE_MATRIX, SEQUENCES, BUFFER)
    breach_protocol.visualize(moves[::-1])


if __name__ == '__main__':
    main()