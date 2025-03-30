import os
import sys
import math
import numpy as np


def draw_qr_grid(qr_grid):
    """
    Draws the given qr data onto the canvas of stddraw in the format specified in
    the project specification.

    Args:
        qr_grid (2D array of int): The data of the QR grid
    """
    # TODO: implement this function.
    # remove the following line when you add something to this function:
    pass


def print_qr_grid(qr_grid):
    """
    Prints the given qr data out to the standard output in the format specified in
    the project specification.

    Args:
        qr_grid (2D array of int): The data of the QR grid
    """
    # TODO: implement this function.
    # remove the following line when you add something to this function:
    pass


def make_position_pattern(pos_square_size):
    """
    Creates the position pattern of size pos_square_size and returning it as a
    2-dimensional array of int.

    Args:
        pos_square_size (int): The size of the position pattern to generate

    Returns:
        2D array of int: The position pattern
    """

    validate_position_square_length(pos_square_size)

    start_with_zeros = not pos_square_size % 4 == 0
    inner_square_length = pos_square_size - 1

    square = make_alternating_square_matrix(
        inner_square_length,
        start_with_ones=not start_with_zeros,
        ignore_center_element=True,
    )

    square.append([int(start_with_zeros)] * inner_square_length)
    for row in square:
        row.append(int(start_with_zeros))

    return square


def validate_position_square_length(length):
    assert (
        length >= 4 and length % 2 == 0
    ), f"position square length must be an even integer greater than or equal to 4"


def make_alignment_pattern(align_square_size):
    """
    Creates the alignment pattern of size align_square_size and returning it as
    a 2-dimensional array of int.

    Args:
        align_square_size (int): The size of the alignment pattern to generate

    Returns:
        2D array of int: The alignment pattern
    """
    validate_alignment_square_length(align_square_size)
    return make_alternating_square_matrix(align_square_size, start_with_ones=True)


def validate_alignment_square_length(length):
    assert (
        length > 0 and (length - 1) % 4 == 0
    ), f"alignment square length must be a positive integer in the series 1, 5, 9, 13, ..."


def make_alternating_square_matrix(
    length, start_with_ones=True, ignore_center_element=False
):
    square = np.ones(
        [length] * 2, dtype=np.uint8
    )  # make_square_matrix(align_square_size, fill_with=1)
    initial_diagonal_idx = int(start_with_ones)
    num_diagonals_to_center = math.ceil(length / 2)
    final_diagonal_idx = num_diagonals_to_center - int(ignore_center_element)

    for min_idx in range(initial_diagonal_idx, final_diagonal_idx, 2):
        max_idx = length - min_idx - 1

        square[min_idx, min_idx:max_idx] = 0
        square[max_idx, min_idx + 1 : max_idx + 1] = 0
        square[min_idx + 1 : max_idx + 1, min_idx] = 0
        square[min_idx:max_idx, max_idx] = 0

    return square.tolist()


def make_square_matrix(length, fill_with=0):
    assert length > 0, f"square matrix length must be greater than 0 (got {length})"
    return [[fill_with] * length for _ in range(length)]


def rotate_pattern_clockwise(data):
    """
    Rotates the values in data clock-wise by 90 degrees

    Args:
        data (2D array of int): The array that should be rotated
    """
    # TODO: implement this function.
    # remove the following line when you add something to this function:
    pass


def add_data_at_anchor(qr_grid, anchor_x, anchor_y, data):
    """
    Places values contained in data to the qr_grid starting as positions given
    by achnor_x and anchor_y.

    Args:
        qr_grid (2D array of int): The QR grid
        anchor_x (int): the x position from where the data should be added
        anchor_y (int): the y position from where the data should be added
        data (2D array of int): The data that should be added to the QR grid
    """
    # TODO: implement this function.
    # remove the following line when you add something to this function:
    pass


def add_data_snake(qr_grid, data):
    """
    Places values contained in data to the qr_grid in the snake layout as
    specified in the project specifications.

    Args:
        qr_grid (2D array of int): The QR grid
        data (array of int): The bit sequence of data that should be added to
        the QR grid
    """
    # TODO: implement this function.
    # remove the following line when you add something to this function:
    pass


def add_data_real(qr_grid, data):
    """
    Places values contained in data to the qr_grid in the real layout as
    specified in the project specifications.

    Args:
        qr_grid (2D array of int): The QR grid
        data (array of int): The bit sequence of data that should be added to
        the QR grid
    """
    # TODO: implement this function.
    # remove the following line when you add something to this function:
    pass


def apply_mask(qr_grid, reserved_positions, mask_id):
    """
    Applies the masking pattern specified by mask_id to the QR grid following
    the masking rules as specified by the project specifications.

    Args:
        qr_grid (2D array of int): The QR grid
        reserved_positions (2D array of int): the reserved positions
        mask_id (str): The mask id to apply to the QR grid
    """
    # TODO: implement this function.
    # remove the following line when you add something to this function:
    pass


def encode_real(size, message, information_bits, pos_square_size, align_square_size):
    """
    Generates the QR code according to the project specifications using the
    real layout.

    Args:
        size (int): The size of the QR grid to be generated
        message (str): The message to be encoded
        information_bits (array of int): the 15-bit information pattern
        pos_square_size (int):  The size of the position pattern to generate
        align_square_size (int):  The size of the alignment pattern to generate

    Returns:
        2D array of int: The completed QR grid
    """
    # TODO: implement this function.
    # remove the following line when you add something to this function:
    pass


def encode_snake(size, message, pos_square_size, align_square_size):
    """
    Generates the QR code according to the project specifications using the
    snake layout.

    Args:
        size (int): The size of the QR grid to be generated
        message (str): The message to be encoded
        pos_square_size (int):  The size of the position pattern to generate
        align_square_size (int):  The size of the alignment pattern to generate

    Returns:
        2D array of int: The completed QR grid
    """
    # TODO: implement this function.
    # remove the following line when you add something to this function:
    pass


def main(args):
    # TODO: put logic here to check if the command-line arguments are correct,
    # and then call the game functions using these arguments.
    print(np.matrix(make_position_pattern(6)))
    # print(make_alignment_pattern(9))


if __name__ == "__main__":
    """USage: echo 'message' | python3 SUXXXXXXXX.py 'encoding_string' 'size' 'pos_size' 'align_size'"""
    main(sys.argv)
