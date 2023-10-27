def draw_moai(vert_chars="/|\\", hor_char="_", 
              head_size=(1, 1), eye_size=(1, 1), neck_size=(1, 1)):
    # Define dimensions
    head_width = 8 * head_size[0]
    head_height = 1 * head_size[1]
    neck_width = 8 * neck_size[0]
    neck_height = 1 * neck_size[1]
    eyes_width = 2 * eye_size[0]
    eyes_height = 1 * eye_size[1]

    # Print the top part of the head
    print(" " * 3 + hor_char * head_width + " ")

    # Print the sides of the head
    for i in range(head_height):
        print(" " * 2 + vert_chars[0] + " " * head_width + vert_chars[2])

    # Print the bottom of the head
    print(" " * 2 + vert_chars[1] + hor_char * head_width + vert_chars[1])

    # Print the eyes
    print(" " * 2 + vert_chars[1] + hor_char * eyes_width + vert_chars[1] + " " * 2 + vert_chars[1] + hor_char * eyes_width + vert_chars[1])
    print(" " * 1 + vert_chars[1] + " " * (1 + eyes_width) + vert_chars[1] + " " * 2 + vert_chars[1] + " " * (1 + eyes_width) + vert_chars[1])
    print(" " * 1 + vert_chars[1] + " " * (1 + eyes_width) + vert_chars[1] + hor_char * eyes_width + vert_chars[1] + " " * 3 + vert_chars[1])

    # Print the neck
    print(vert_chars[1] + " " * 3 + hor_char * (6 * neck_size[0]) + " " * 3 + vert_chars[1])
    print(vert_chars[1] + " " * 4 + hor_char * (4 * neck_size[0]) + " " * 4 + vert_chars[1])

    # Print the bottom of the head (upside down)
    print(vert_chars[2] + hor_char * (12 * head_size[0]) + vert_chars[0])

    # Print the body and legs
    print(" " * 2 + vert_chars[0] + " " * neck_width + vert_chars[2])
    print(" " * neck_height + vert_chars[1] + hor_char * (10 * neck_size[0]) + vert_chars[1] * neck_height)


# Test the function without any input (default values will be used)
draw_moai()
