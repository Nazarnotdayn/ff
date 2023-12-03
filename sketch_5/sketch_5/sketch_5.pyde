'''
Изяслав решил сделать красивый проект —
бабочка крутится, всё дальше отдаляясь от центра, и закрашивает собой холст
Должны получиться красивые узоры. Но программа даже не запускается.
Как исправить это?

'''

ugol = 0
x = 30,30
img = loadImage ("butterfly2-a.phg")
def setup():
    global img
    size(700,700)
    img = loadImage('butterfly2-a.png')
    imageMode(CENTER)
    
    
    
def draw():
    global ugol, x,img
    translate(350, 350)
    rotate(radians(ugol))
    image(img,0,0,x,x)
    ugol = ugol - 5
    x = x -1
