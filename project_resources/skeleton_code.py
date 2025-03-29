"""
Skeleton code for CS114 project 2025: A QR code generator.

This skeleton code for the project is intended as a starting point for students
to get an idea of how they can begin to code the project. You are not required
to use any of the functions in this skeleton code, however you may find some of
the ideas useful. Your code, however, is required to have the line:

if __name__ == "__main__":

but you are free to and should modify the lines following this.

None of the functions are implemented yet, so if you would like to
use a particular function, you need to implement it yourself. If you decide not
to use any of the functions, you are free to leave them empty or remove them
from this file. You are also free to alter the function signatures (the name of
the function and its arguments), so if you need to pass more arguments to the
function, or do not need a particular argument, you are also free to add and
remove arguments as you see fit. We provide the function signatures only as a
guide for how we think you can start to approach the project.
"""

# imports
import os
import sys
# Your imports go here

# global variables
# Your global variables go here


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
    # TODO: implement this function.
    # remove the following line when you add something to this function:
    pass


def make_alignment_pattern(align_square_size):
    """
    Creates the alignment pattern of size align_square_size and returning it as
    a 2-dimensional array of int.

    Args:
        align_square_size (int): The size of the alignment pattern to generate

    Returns:
        2D array of int: The alignment pattern
    """
    # TODO: implement this function.
    # remove the following line when you add something to this function:
    pass


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
    pass


if __name__ == "__main__":
    """USage: echo 'message' | python3 SUXXXXXXXX.py 'encoding_string' 'size' 'pos_size' 'align_size'"""
    main(sys.argv)