width_free_space = int(input())
length_free_space = int(input())
height_free_space = int(input())

volume_free_space = width_free_space * length_free_space * height_free_space

while True:
    box = input()
    if box == "Done" and volume_free_space > 0:
        print(f"{volume_free_space} Cubic meters left.")
        break

    if box != "Done":
        new_box = int(box)
        volume_new_box = 1 * 1 * 1
        volume_free_space -= new_box * volume_new_box
        if volume_free_space < 0:
            print(f"No more free space! You need {abs(volume_free_space)} Cubic meters more.")
            break

#    if volume_free_space < 0:
#        print(f"No more free space! You need {abs(volume_free_space)} Cubic meters more.")
#        break

