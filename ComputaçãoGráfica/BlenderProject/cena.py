import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import pywavefront
from pywavefront import visualization

# VARIÁVEIS GLOBAIS
obj = []

mouseX = 0
mouseY = 0

cameraX = 0.0
cameraY = 0.0

mouseRightDown = False

transX = 0
transY = 0

zoom = -15

reset = False

LIGHT_POSITION_LEFT = [-20.0,2.0,-2.0,1.0]
LIGHT_POSITION_RIGHT = [20.0,-2.0,2.0,-1.0]

# FIM VARIÁVEIS GLOBAIS

def onMouse(button, state, x, y):
  global mouseX, mouseY, mouseRightDown
  mouseX = x
  mouseY = y

  if button == GLUT_RIGHT_BUTTON:
    if state == GLUT_DOWN:
      mouseRightDown = True
    elif state == GLUT_UP:
      mouseRightDown = False

def onWheel(wheel, direction, x, y):
  global zoom

  if direction == -1:
    zoom = zoom - 5.0
  elif direction == +1:
    zoom = zoom + 5.0


  glutPostRedisplay()


def onMotion(x, y):
  global mouseX, mouseY, cameraX, cameraY, mouseRightDown, transX, transY

  if mouseRightDown:
    if cameraX >= 0 and cameraX <= 90:
      cameraX = cameraX + (y - mouseY)
      cameraY = cameraY + (x - mouseX)

      mouseX = x
      mouseY = y
    elif cameraX < 0:
      cameraX = 0
    else:
      cameraX = 90

    glutPostRedisplay()


def keyboard(key, x, y):
  global transY, transX, cameraX, cameraY, zoom

  if ord(key) == 49:#'1'
    transX = 0
    transY = 0
    cameraX = 0
    cameraY = 0
    zoom = -15

  if ord(key) == ord('a'):
    transX = transX + 0.1

  if ord(key) == ord('d'):
    transX = transX - 0.1

  if ord(key) == ord('w'):
    transY = transY - 0.1

  temp = transY + 0.1
  if ord(key) == ord('s') and transY < 0.0:
    transY = temp

  # Iluminação
  if ord(key) == ord('i'):
    glDisable(GL_LIGHT2)
    glDisable(GL_LIGHT1)

  if ord(key) == ord('o'):  # Luz a esquerda
    glEnable(GL_LIGHT2)
    glEnable(GL_LIGHT1)
    glLightfv(GL_LIGHT0, GL_POSITION, [20.,2.,-2.,1.])
    glLightfv(GL_LIGHT1, GL_POSITION, [-20.,2.,-2.,1.])

  if ord(key) == ord('p'):  # luz a direita
    glEnable(GL_LIGHT2)
    glEnable(GL_LIGHT1)
    glLightfv(GL_LIGHT0, GL_POSITION, [-20.,2.,-2.,1.])
    glLightfv(GL_LIGHT1, GL_POSITION, [20.,2.,-2.,1.])

  glutPostRedisplay()

def main():
    global obj
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(900, 600)
    glutCreateWindow('Floresta')

    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutMouseFunc(onMouse);
    glutMotionFunc(onMotion)
    glutMouseWheelFunc(onWheel);
    glClearColor(0.3,0.3,0.3,0)

    glEnable(GL_LIGHTING)
    glEnable(GL_NORMALIZE)
    glMaterialfv(GL_FRONT, GL_SPECULAR, [ 1.0, 1.0, 1.0, 1.0 ]);
    glMaterialfv(GL_FRONT, GL_SHININESS, [100.0]);

    lightZeroColor = [0.2,0.2,0.2,0.0]


    # Iluminação config
    lightMainPosition = [-20.0,2.0,-2.0,1.0]
    glLightfv(GL_LIGHT2, GL_POSITION, lightMainPosition)
    glLightfv(GL_LIGHT2, GL_DIFFUSE, lightZeroColor)
    glLightfv(GL_LIGHT2, GL_CONSTANT_ATTENUATION, 0.89)
    glLightfv(GL_LIGHT2, GL_LINEAR_ATTENUATION, 0.1)
    glEnable(GL_LIGHT2)


    lightSecondPosition = [20.0,-2.0,2.0,-1.0]
    lightZeroColor2 = [2.0,2.0,2.0,0.0]
    glLightfv(GL_LIGHT1, GL_POSITION, lightSecondPosition)
    glLightfv(GL_LIGHT1, GL_DIFFUSE, lightZeroColor2)
    glLightfv(GL_LIGHT1, GL_CONSTANT_ATTENUATION, 0.89)
    glLightfv(GL_LIGHT1, GL_LINEAR_ATTENUATION, 0.09)
    glEnable(GL_LIGHT1)

    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, lightZeroColor)

    glutDisplayFunc(display)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(30.,1.,0.1,80.)
    glMatrixMode(GL_MODELVIEW)
    glEnable(GL_DEPTH_TEST)

    obj = pywavefront.Wavefront('cena.obj')

    glutMainLoop()
    return

def display():
    global obj, cameraX, cameraY, transX, transY, zoom

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT);

    glLoadIdentity();

    glTranslatef(transX, transY, zoom);

    glRotatef(cameraX, 1, 0, 0);
    glRotatef(cameraY, 0, 1, 0);
    visualization.draw(obj)

    glFlush()
    glutSwapBuffers()
    return

if __name__ == '__main__': main()
