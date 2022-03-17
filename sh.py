from time import sleep
import turtle
turtle.title("Sutherland-Hodgman Polygon Clipping")
t = turtle.Turtle()
t.speed("fastest")
def clip(subjectPolygon, clipPolygon):
    def inside(p):
        return(cp2[0]-cp1[0])*(p[1]-cp1[1]) > (cp2[1]-cp1[1])*(p[0]-cp1[0])
    def computeIntersection():
        dc = [ cp1[0] - cp2[0], cp1[1] - cp2[1] ]
        dp = [ s[0] - e[0], s[1] - e[1] ]
        n1 = cp1[0] * cp2[1] - cp1[1] * cp2[0]
        n2 = s[0] * e[1] - s[1] * e[0]
        n3 = 1.0 / (dc[0] * dp[1] - dc[1] * dp[0])
        return [(n1*dp[0] - n2*dc[0]) * n3, (n1*dp[1] - n2*dc[1]) * n3]
    outputList = subjectPolygon
    cp1 = clipPolygon[-1]
    for clipVertex in clipPolygon:
        cp2 = clipVertex
        inputList = outputList
        outputList = []
        s = inputList[-1]
        for subjectVertex in inputList:
            e = subjectVertex
            if inside(e):
                if not inside(s):
                    outputList.append(computeIntersection())
                outputList.append(e)
            elif inside(s):
                outputList.append(computeIntersection())
            s=e
        cp1 = cp2
    return(outputList)
def goto(p):
    t.penup()
    t.goto(p)
    t.pendown()
def write(text):
    t.color("black")
    t.penup()
    t.goto(0,180)
    t.write(text,align="center",font=("Verdana",20,"normal"))
def draw(points,col):
    t.color(col)
    goto(points[0])
    for point in points:
        t.goto(point)
    t.goto(points[0])
polygon = [ (-150,0), (0,-120), (150,0), (50,150), (0,50), (-50,150)]
clipWindow = [ (-100,-100), (100,-100), (100,100), (-100,100) ]
write("Before Clipping")
t.begin_fill()
draw(polygon,"black")
t.end_fill()
draw(clipWindow,"black")
clippedPoints = clip(polygon,clipWindow)
clippedResult = [tuple(p) for p in clippedPoints]
sleep(1)
t.clear()
write("After Clipping")
t.begin_fill()
draw(clippedResult,"black")
t.end_fill()
draw(clipWindow,"black")
t.ht()
 
 
