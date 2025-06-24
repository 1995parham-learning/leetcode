from typing import Generator


def palindrome_numbers() -> Generator[int]:
    """
    A generator function that yields palindrome numbers by constructing them
    in ascending order. This method is significantly more efficient for
    generating large palindromes as it avoids checking every number.

    The construction process follows these steps:
    1. Yields single-digit palindromes (0-9).
    2. Iteratively generates palindromes of increasing lengths (2-digit, 3-digit, etc.).
       For each length:
       a. For even-length palindromes, it takes a 'half' number (e.g., 12 for 1221),
          converts it to a string, reverses it, and concatenates them (s_half + s_reversed_half).
       b. For odd-length palindromes, it takes a 'half' number (e.g., 12 for 12321),
          converts it to a string, inserts each possible middle digit (0-9),
          and then concatenates with the reversed 'half' (s_half + mid_digit + s_reversed_half).
    This ensures that palindromes are generated in strictly numerical ascending order.
    """
    # Step 1: Yield single-digit palindromes (0-9)
    for i in range(10):
        yield i

    # Step 2: Generate multi-digit palindromes based on length
    current_length = 2  # Start with palindromes of length 2

    while True:
        # Determine the range for the 'first half' number based on the current_length
        # For a palindrome of length `L`, its first half (excluding the middle digit for odd lengths)
        # will have `L // 2` digits if L is even, or `(L - 1) // 2` digits if L is odd.

        # Calculate the length of the 'half' string
        if current_length % 2 == 0:  # Even length palindromes (e.g., 11, 1001)
            half_string_len = current_length // 2
        else:  # Odd length palindromes (e.g., 101, 10001)
            half_string_len = (current_length - 1) // 2

        # Determine the start and end values for the 'half' number
        # Example: For half_string_len = 1 (palindromes like 11, 101), half goes from 1 to 9.
        # Example: For half_string_len = 2 (palindromes like 1001, 10001), half goes from 10 to 99.
        start_half_num = 10 ** (half_string_len - 1) if half_string_len > 0 else 1
        end_half_num = (10**half_string_len) - 1 if half_string_len > 0 else 9

        # Iterate through all possible 'first half' numbers for the current length
        for half in range(start_half_num, end_half_num + 1):
            s_half = str(half)
            s_reversed_half = s_half[::-1]  # Reverse the 'first half' string

            if current_length % 2 == 0:
                # Construct even length palindrome: first_half + reversed(first_half)
                # Example: half=1, s_half='1', s_reversed_half='1' -> '11'
                # Example: half=10, s_half='10', s_reversed_half='01' -> '1001'
                yield int(s_half + s_reversed_half)
            else:
                # Construct odd length palindromes: first_half + middle_digit + reversed(first_half)
                # Iterate through all possible middle digits (0-9)
                # Example: half=1, s_half='1', s_reversed_half='1'
                #   mid=0 -> '101'
                #   mid=1 -> '111'
                #   ...
                #   mid=9 -> '191'
                # Example: half=10, s_half='10', s_reversed_half='01'
                #   mid=0 -> '10001'
                #   mid=1 -> '10101'
                #   ...
                #   mid=9 -> '10901'
                for mid_digit in range(10):
                    yield int(s_half + str(mid_digit) + s_reversed_half)

        current_length += 1  # Move to the next palindrome length


if __name__ == "__main__":
    for i in palindrome_numbers():
        print(i)
