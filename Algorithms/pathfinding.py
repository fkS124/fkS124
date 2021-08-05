from copy import copy
import pygame as pg


pg.init()

grid = [
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
]

screen = pg.display.set_mode((64*len(grid[0]), 64*len(grid)))


first_pos = [0, 0]
second_pos = [len(grid[0])-1, len(grid)-1]


def find_direction():
    found = path_found(first_pos)
    if found[0]:
        print("done")
        return found[1]
    return False
    

def path_found(pos):

    points = [pos]
    paths = [[pos]]
    while len(points) > 0:
        
        added = False

        new_paths = []
        for l_pts in paths:

            pt = l_pts[-1]
            pts = [
                [pt[0]+1, pt[1]],
                [pt[0]-1, pt[1]],
                [pt[0], pt[1]+1],
                [pt[0], pt[1]-1]
            ]
            for pt_ in pts:
                if pt_available(pt_) and pt_ not in points:
                    
                    added = True
                    new = copy(l_pts)
                    points.append(pt_)
                    new.append(pt_)
                    new_paths.append(new)

        paths = new_paths
            
        for pts in paths:
            if second_pos in pts:
                return True, pts
            for pt in pts:
                pg.draw.rect(screen, (255, 255, 0), [pt[0]*64, pt[1]*64, 64, 64])
                pg.display.update()

        if not added:
            break
            
    return False, None

def pt_available(pos):
    if pos[0] > len(grid[0])-1 or pos[1] > len(grid)-1 or pos[0] < 0 or pos[1] < 0:
        return False
    if grid[pos[1]][pos[0]] == 1:
        return False
    return True


found = None
while True:

    for event in pg.event.get():

        if event.type == pg.QUIT:
            pg.quit()
            raise SystemExit

    for y, row in enumerate(grid):
        for x, cel in enumerate(row):
            color = (255, 255, 255) if cel == 0 else (0, 0, 0)
            pg.draw.rect(screen, color, [x*64, y*64, 64, 64])

    pg.draw.rect(screen, (255, 0, 0), [first_pos[0]*64, first_pos[1]*64, 64, 64])
    pg.draw.rect(screen, (0, 255, 0), [second_pos[0]*64, second_pos[1]*64, 64, 64])

    if found is None:
        path = find_direction()
        found = path
    elif not found:
        print("NO PATHS SORRY DUMBASS")
    else:
        if type(path) is list:
            for i in path:
                pg.draw.rect(screen, (0, 255, 0), [i[0]*64, i[1]*64, 64, 64])


    pg.display.update()