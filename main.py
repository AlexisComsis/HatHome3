from init import *
from entity import *
from player import *
from copy import *
# Main loop
run = True
while run:
    clock.tick(120)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # Exit Control
    if keys[pygame.K_ESCAPE]:
        run = False
    if keys[pygame.QUIT]:
        run = False

    #Controlkeys
    pygame.Surface.fill(window, (0, 0, 0))

    #be
    background.be(window)


    listt = []
    temporary = []
    for object in Entity.list_object_phys:
        listt.append(int(object.y))

    listt.append(home.y)
    listt.sort()

    for object in Entity.list_object_phys:
        temporary.append(copy(object))

    for yobj in listt:
        if yobj == home.y:
            home.be(window, keys, mouse, click)

        for object in temporary:
            if int(object.y) == yobj:
                object.be(window)


    #Update Display
    pygame.display.update()
