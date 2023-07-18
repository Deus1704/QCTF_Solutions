# mess = []
# with open('textfile.txt', "r") as file_object:
#     lines = file_object.readlines()
#     for line in lines:
#         sub = "key press"
#         if sub in line:
#             mess.append(line[12:14])
# print(*mess, sep=",")

# def map_scan_code_to_character(scan_code):
#     # Hypothetical mapping for a keyboard layout (not real-world data)
#     scan_to_char_mapping = {
#         50: 'A',
#         54: 'B',
#         28: 'C',
#         # Add more mappings for other scan codes as needed
#     }

#     return scan_to_char_mapping.get(scan_code, '')  # Return the mapped character or an empty string if not found

# def find_possible_words(scan_codes):
#     characters = [map_scan_code_to_character(int(code)) for code in scan_codes.split(',')]
#     return ''.join(characters)

# # Provided scan codes as a comma-separated string
# scan_codes = '50,54,28,41,50,34,25,12,10,27,40,50,20,41,46,38,42,50,35'
# possible_words = find_possible_words(scan_codes)
# print("Possible words:", possible_words)


import keyboard

# Define the scan codes of the keys that were pressed.
scan_codes = [50, 54, 28, 41, 50, 34, 25, 12, 10, 27, 40, 50, 20, 41, 46, 38, 42, 50, 35]

# Simulate the key presses.
for scan_code in scan_codes:
    keyboard.press(scan_code)

# '32'M, '36', '1c', '29'~, '32'M, '22'G, '19'P, 'c'_/-, 'a'(, '1b'}, '28'", '32'M, '14'T, '29'~, '2e'C, '26'L, '2a', '32'M, '23'H
# M~MGP_(}"MT~CLMH