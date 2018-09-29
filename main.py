from init import *
from entity import *
from player import *
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
    for object in Entity.list_object_phys:
        listt.append(object.y)

    listt.append(home.y)
    listt.sort()


    for yobj in (listt):
        if yobj == home.y and :
            home.be(window, keys, mouse, click)


        for object in Entity.list_object_phys:
            if object.y == yobj:
                object.be(window)


    #Update Display
    pygame.display.update()
