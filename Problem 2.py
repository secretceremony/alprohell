def draw_moai(vert_chars, hor_char, head_size, eye_size, neck_size):
    # Define dimensions based on input
    head_width = head_size[1]
    head_height = head_size[0]
    neck_width = neck_size[1]
    neck_height = neck_size[0]
    eyes_width = eye_size[1]
    eyes_height = eye_size[0]

    # Print the top part of the head
    print(" " * 3 + hor_char * head_width + " ")

    # Print the sides of the head
    print(" " * 2 + vert_chars[0] + " " * head_width + vert_chars[2])
    print(" " * 2 + vert_chars[1] + hor_char * head_width + vert_chars[1])

    # Print the eyes
    print(" " * 2 + vert_chars[1] + hor_char * eyes_width + vert_chars[1] + " " * eyes_width + vert_chars[1] + hor_char * eyes_width + vert_chars[1])
    print(" " * 1 + vert_chars[1] + " " * (1 + eyes_width) + vert_chars[1] + " " * eyes_width + vert_chars[1] + " " * (1 + eyes_width) + vert_chars[1])
    print(" " * 1 + vert_chars[1] + " " * (1 + eyes_width) + vert_chars[1] + hor_char * eyes_width + vert_chars[1] + " " * (1 + eyes_width) + vert_chars[1])

    # Print the neck
    print(vert_chars[1] + " " * 3 + hor_char * (neck_size[1] - 2) + " " * 3 + vert_chars[1])
    print(vert_chars[1] + " " * 4 + hor_char * (neck_size[1] - 4) + " " * 4 + vert_chars[1])

    # Print the bottom of the head (upside down)
    print(vert_chars[2] + hor_char * (head_size[1] + 4) + vert_chars[0])

    # Print the body and legs
    print(" " * 2 + vert_chars[0] + " " * neck_width + vert_chars[2])
    print(" " * neck_height + vert_chars[1] + hor_char * (neck_size[1] + 2) + vert_chars[1])


# Get user input
vert_chars = input("Masukkan karakter ASCII untuk vertikal (format: /|\\): ")
hor_char = input("Masukkan karakter ASCII untuk horizontal (contoh: _): ")
head_size = tuple(map(int, input("Masukkan ukuran kepala (tinggi lebar): ").split()))
eye_size = tuple(map(int, input("Masukkan ukuran mata (tinggi lebar): ").split()))
neck_size = tuple(map(int, input("Masukkan ukuran leher (tinggi lebar): ").split()))

draw_moai(vert_chars, hor_char, head_size, eye_size, neck_size)