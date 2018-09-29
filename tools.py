'''
Tools for the developpement
'''
import json
import pygame

class tools:

    # take the height and width needed
    with open("Assets\Data\Options.txt", "r+") as openfile:
        openfile = json.loads(openfile.read())
        w0 = openfile["Width"]
        h0 = openfile["Height"]

    # Convert resolution depending on the screen
    def convert_coord(nx, ny, w=w0, h=h0):
        return [int(nx / 1600 * w), int(ny / 900 * h)]

    # Possibly usefull find the width and height of an image
    def get_width(img_path):
        img = pygame.image.load(img_path).convert_alpha()
        return img.get_width()
    def get_height(img_path):
        img = pygame.image.load(img_path).convert_alpha()
        return img.get_height()

    def load_convert(img_path, w=w0, h=h0):
        img = pygame.image.load(img_path).convert_alpha()
        wc = int(img.get_width() / 1600 * w)
        hc = int(img.get_height() / 900 * h)
        return pygame.transform.scale(img, (wc, hc))

    def convert(img, w=w0, h=h0):
        '''
        convert an image in the format of the options
        '''
        wc = int(img.get_width() / 1600 * w)
        hc = int(img.get_height() / 900 * h)
        return pygame.transform.scale(img, (wc, hc))


    def give(file, key, cat, value):
        with open("Data"+file, "r") as options:
            data = options.read()
            options = json.loads(data)

            (options[key][cat]) = value
            data = json.dumps(options)

        with open("Data"+file, "w") as file:
            file.write(data)



    def separate(img_path, w1, mult=1):
        '''
        separate different sprites
        '''
        img = pygame.image.load(img_path).convert_alpha()
        w2 = img.get_width()
        h2 = img.get_height()
        timer = int(w2/w1)
        img_list = []
        for i in range(timer):
            img_list.append(img.subsurface(i*w1, 0, w1, h2))
            img_list[i] = pygame.transform.scale(img_list[i], (int(mult*w1), int(mult*h2)))
            img_list[i] = tools.convert(img_list[i])
        return img_list
