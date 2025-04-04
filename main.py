import stdio
import sys
import math

ENCODING_INFO = [0, 1, 0, 0]
TERMINATOR_PATTERN = [0] * 4
PADDING_BITS = [1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1]
REMAINDER_BITS = [0] * 7
NUM_ERROR_CORRECTION_WORDS = 16
NUM_MESSAGE_LENGTH_BITS = 8


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
    for row in qr_grid:  # could remove the loop by doing 2 joins :)
        line = ""
        for col in row:
            line += f"{col} "

        stdio.writeln(line.rstrip())


def make_position_pattern(pos_square_size):
    """
    Creates the position pattern of size pos_square_size and returning it as a
    2-dimensional array of int.

    Args:
        pos_square_size (int): The size of the position pattern to generate

    Returns:
        2D array of int: The position pattern
    """

    start_with_zeros = not pos_square_size % 4 == 0
    inner_square_length = pos_square_size - 1

    square = make_alternating_square_matrix(
        inner_square_length,
        start_with_ones=not start_with_zeros,
        ignore_center_element=True,
    )

    outer_vals = int(start_with_zeros)
    square.append([outer_vals] * inner_square_length)  # bottom row of zeros/ones

    for row in square:  # right column of zeros/ones
        row.append(outer_vals)

    return square


def make_alignment_pattern(align_square_size):
    """
    Creates the alignment pattern of size align_square_size and returning it as
    a 2-dimensional array of int.

    Args:
        align_square_size (int): The size of the alignment pattern to generate

    Returns:
        2D array of int: The alignment pattern
    """
    return make_alternating_square_matrix(align_square_size, start_with_ones=True)


def make_alternating_square_matrix(length, start_with_ones=True, ignore_center_element=False):
    square = make_square_matrix(length, fill_with=1)
    initial_diagonal_idx = int(start_with_ones)
    num_diagonals_to_center = math.ceil(length / 2)
    final_diagonal_idx = num_diagonals_to_center - int(ignore_center_element)

    for min_idx in range(initial_diagonal_idx, final_diagonal_idx, 2):
        max_idx = length - min_idx - 1
        zeros = [0] * (max_idx - min_idx)

        square[min_idx][min_idx:max_idx] = zeros  # top row of zeros
        square[max_idx][min_idx + 1 : max_idx + 1] = zeros  # bottom row of zeros

        for row in square[min_idx + 1 : max_idx + 1]:  # left column of zeros
            row[min_idx] = 0

        for row in square[min_idx:max_idx]:  # right column of zeros
            row[max_idx] = 0

    return square


def make_square_matrix(length, fill_with=0):
    return [[fill_with] * length for _ in range(length)]


def rotate_position_pattern_clockwise(position_pattern):
    """
    Rotates the values in position_pattern clock-wise by 90 degrees.

    Args:
        position_pattern (2D array of int): The position pattern that should be rotated
    """
    return rotate_square_matrix_clockwise(position_pattern, first_layer_only=True)


def rotate_square_matrix_clockwise(data, first_layer_only=False):
    """
    Rotates the values in data clock-wise by 90 degrees

    Args:
        data (2D array of int): The array that should be rotated
    """
    length = len(data)
    final_diagonal_idx = 1 if first_layer_only else length // 2

    for min_idx in range(final_diagonal_idx):

        max_idx = length - min_idx - 1

        for idx in range(min_idx, max_idx):
            opposite_idx = length - idx - 1

            temp = data[min_idx][idx]  # store top element
            data[min_idx][idx] = data[opposite_idx][min_idx]  # replace top with left
            data[opposite_idx][min_idx] = data[max_idx][opposite_idx]  # replace left with bottom
            data[max_idx][opposite_idx] = data[idx][max_idx]  # replace bottom with right
            data[idx][max_idx] = temp  # replace right with top

    return data


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
    data_len = len(data)

    for row_idx in range(data_len):
        qr_grid[anchor_x + row_idx][anchor_y : anchor_y + data_len] = data[row_idx]


def add_data_snake(qr_grid, data):
    """
    Places values contained in data to the qr_grid in the snake layout as
    specified in the project specifications.

    Args:
        qr_grid (2D array of int): The QR grid
        data (array of int): The bit sequence of data that should be added to
        the QR grid
    """
    rng = range(len(qr_grid))

    for row in qr_grid:
        for col_idx in rng:
            if row[col_idx] is None:
                row[col_idx] = data.pop(0)

        rng = rng[::-1]


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


def parse_program_inputs(args):
    """returns a tuple of the validated & parsed input arguments. Otherwise throws an error"""

    if len(args) < 6:
        raise ValueError("Too few arguments")

    if len(args) > 6:
        raise ValueError("Too many arguments")

    encoding_param = parse_encoding_param(args[1])
    use_gui, use_real_layout, masking_pattern = get_encoding_param_parts(encoding_param)

    grid_size = parse_grid_size_param(args[2], use_real_layout)
    position_pattern_size = parse_position_pattern_param(args[3], use_real_layout)
    alignment_pattern_size = parse_alignment_pattern_param(args[4], use_real_layout)

    ensure_sizes_are_within_bounds(grid_size, position_pattern_size, alignment_pattern_size)

    num_unreserved_bits = get_num_unreserved_bits(
        grid_size, position_pattern_size, alignment_pattern_size, use_real_layout
    )

    information_bits = parse_payload_param(args[5], use_real_layout, num_unreserved_bits)

    return (
        use_gui,
        use_real_layout,
        masking_pattern,
        grid_size,
        position_pattern_size,
        alignment_pattern_size,
        information_bits,
    )


def parse_encoding_param(encoding_param):
    """returns the 3 parts of the encoding_param as ints if it's valid, otherwise raises an error"""

    if not encoding_param.isdigit():
        raise TypeError(f"Invalid encoding argument: {encoding_param}")

    encoding_param = int(encoding_param)

    if 0 <= encoding_param < 32:
        return encoding_param

    raise ValueError(f"Invalid encoding argument: {encoding_param}")


def get_encoding_param_parts(encoding_param):
    USE_GUI_BITMASK = 0b10000
    USE_REAL_LAYOUT_BITMASK = 0b01000
    MASKING_PATTERN_BITMASK = 0b00111

    use_gui = (USE_GUI_BITMASK & encoding_param) > 0  # convert bits to bool
    use_real_layout = (USE_REAL_LAYOUT_BITMASK & encoding_param) > 0  # convert bits to bool
    masking_pattern = MASKING_PATTERN_BITMASK & encoding_param

    return use_gui, use_real_layout, masking_pattern


def parse_grid_size_param(grid_size, use_real_layout):
    """returns the value of grid_size as an int if it's valid, otherwise raises an error"""

    if not grid_size.isdigit():
        raise TypeError(f"Invalid size argument: {grid_size}")

    grid_size = int(grid_size)

    if 10 <= grid_size <= 48 and (not use_real_layout or grid_size == 25):
        return grid_size

    raise ValueError(f"Invalid size argument: {grid_size}")


def parse_position_pattern_param(position_pattern_size, use_real_layout):
    """returns the value of position_pattern_size as an int if it's valid, otherwise raises an error"""

    if not position_pattern_size.isdigit():
        raise TypeError(f"Invalid position pattern size argument: {position_pattern_size}")

    position_pattern_size = int(position_pattern_size)

    if (
        position_pattern_size > 3
        and position_pattern_size % 2 == 0
        and (not use_real_layout or position_pattern_size == 8)
    ):
        return position_pattern_size

    raise ValueError(f"Invalid position pattern size argument: {position_pattern_size}")


def parse_alignment_pattern_param(alignment_pattern_size, use_real_layout):
    """returns the value of alignment_pattern_size as an int if it's valid, otherwise raises an error"""

    if not alignment_pattern_size.isdigit():
        raise TypeError(f"Invalid alignment pattern size argument: {alignment_pattern_size}")

    alignment_pattern_size = int(alignment_pattern_size)

    if (
        alignment_pattern_size > 0
        and (alignment_pattern_size - 1) % 4 == 0
        and (not use_real_layout or alignment_pattern_size == 5)
    ):
        return alignment_pattern_size

    raise ValueError(f"Invalid alignment pattern size argument: {alignment_pattern_size}")


def ensure_sizes_are_within_bounds(grid_size, position_pattern_size, alignment_pattern_size):
    if (
        position_pattern_size * 2 > grid_size  # pos patterns overlap
        or position_pattern_size + alignment_pattern_size > grid_size  # both patterns overlap
        or alignment_pattern_size > position_pattern_size + 1  # align pattern placement is OOB
    ):
        raise ValueError(f"Alignment/position pattern out of bounds")


def get_num_unreserved_bits(
    grid_size, position_pattern_size, alignment_pattern_size, use_real_layout
):
    num_bits = grid_size**2 - 3 * position_pattern_size**2 - alignment_pattern_size**2

    if use_real_layout:
        num_bits -= 15 * 2 + 9 * 2 + 1  # format info region, timing strips & dark cell

    return num_bits


def parse_payload_param(payload, use_real_layout, num_unreserved_bits_in_qr_grid):
    num_payload_chars = len(payload)

    min_bit_sequence_len = (
        len(ENCODING_INFO)
        + NUM_MESSAGE_LENGTH_BITS
        + num_payload_chars * 8  # assuming each char is ascii
        + len(TERMINATOR_PATTERN)
        + 0  # min number of padding bits
        + NUM_ERROR_CORRECTION_WORDS * 8 * use_real_layout  # 0 when use_real_layout is False
        # + len(REMAINDER_BITS) # hand in 3 only
    )

    num_padding_bits = num_unreserved_bits_in_qr_grid - min_bit_sequence_len

    if (
        payload.isascii()
        and num_payload_chars < NUM_MESSAGE_LENGTH_BITS - 1
        and num_padding_bits >= 0
    ):
        payload_ascii_codes = [ord(char) for char in payload]
        payload_bits = [bit for i in payload_ascii_codes for bit in int_to_8_bits(i)]
        padding_bits = make_padding_bits(num_padding_bits)
        return (
            ENCODING_INFO
            + int_to_8_bits(len(payload_ascii_codes))  # message length byte
            + payload_bits
            + TERMINATOR_PATTERN
            + padding_bits
            # below is for hand in 3 only
            # + get_error_codewords(payload_ascii_codes, NUM_ERROR_CORRECTION_WORDS)
            # + REMAINDER_BITS
        )

    raise ValueError(f"ERROR: Payload too large")


def make_padding_bits(num_padding_bits):
    quotient = num_padding_bits // len(PADDING_BITS)
    remainder = num_padding_bits % len(PADDING_BITS)
    return PADDING_BITS * quotient + PADDING_BITS[:remainder]


def int_to_8_bits(integer):
    return [int(char) for char in f"{integer:08b}"]  # convert int to byte string


def main(args):
    try:
        (
            use_gui,
            use_real_layout,
            masking_pattern,
            grid_size,
            position_pattern_size,
            alignment_pattern_size,
            information_bits,
        ) = parse_program_inputs(args)

        grid = make_square_matrix(grid_size, fill_with=None)

        data = make_position_pattern(position_pattern_size)
        add_data_at_anchor(grid, 0, 0, data)

        data = rotate_position_pattern_clockwise(data)
        add_data_at_anchor(grid, 0, grid_size - position_pattern_size, data)

        data = rotate_position_pattern_clockwise(data)
        data = rotate_position_pattern_clockwise(data)
        add_data_at_anchor(grid, grid_size - position_pattern_size, 0, data)

        data = make_alignment_pattern(alignment_pattern_size)
        alignment_pattern_pos = grid_size - position_pattern_size - 1
        add_data_at_anchor(grid, alignment_pattern_pos, alignment_pattern_pos, data)

        if use_real_layout:
            add_data_real(grid, information_bits)
        else:
            add_data_snake(grid, information_bits)

        # apply_mask(grid, reserved_positions, mask_pattern)

        if use_gui:
            draw_qr_grid(grid)
        else:
            print_qr_grid(grid)

    except (TypeError, ValueError) as e:
        # see https://docs.python.org/3/library/exceptions.html#TypeError
        stdio.writeln(f"ERROR: {e}")


if __name__ == "__main__":
    """USage: echo 'message' | python3 SUXXXXXXXX.py 'encoding_string' 'size' 'pos_size' 'align_size'"""

    main(sys.argv)
