# CG UFU-2019.1
# Grupo: Bruno Borges e Rafael Morais de Assis

import pygame, sys
from pygame.locals import *
from math import sqrt

# ----------- Funções para Processos Gráficos ----------
def bresenham(first_click, second_click, surface):
        # first_click second_click
        second_x, second_y = second_click
        enable = False

        if(second_x > WIDTH_TO_DRAW):
            enable = True

        x0, y0 = first_click
        x1, y1 = second_click
        dx = x1 - x0
        dy = y1 - y0

        if dy < 0:
            dy = -dy
            stepy = -1
        else:
            stepy = 1

        if dx < 0:
            dx = -dx
            stepx = -1
        else:
            stepx = 1

        dx <<= 2
        dy <<= 2

        if(enable):
            surface.set_at((x0, y0), brush_color)
            # screen.set_at((x0, y0), brush_color)

        if dx > dy:
            fraction = dy - (dx >> 1)
            while x0 != x1:
                if fraction >= 0:
                    y0 += stepy
                    fraction -= dx
                x0 += stepx
                fraction += dy
                if(enable):
                    surface.set_at((x0, y0), brush_color)
                    # screen.set_at((x0, y0), brush_color)
        else:
            fraction = dx - (dy >> 1)
            while y0 != y1:
                if fraction >= 0:
                    x0 += stepx
                    fraction -= dy
                y0 += stepy
                fraction += dx
                if(enable):
                    surface.set_at((x0, y0), brush_color)
                    # screen.set_at((x0, y0), brush_color)

        pygame.display.flip()

## Auxliar do criculo : printar o octeto
def plotaOcteto(x, y, center_x, center_y, surface):
    dict = {
        '1': ( center_x + x, center_y + y),
        '2': ( center_x - x, center_y + y),
        '3': ( center_x - y, center_y + x),
        '4': ( center_x - y, center_y - x),
        '5': ( center_x - x, center_y - y),
        '6': ( center_x + x, center_y - y),
        '7': ( center_x + y, center_y - x),
        '8': ( center_x + y, center_y + x),
    }
    for point in dict.values():
        if(point[X] > WIDTH_TO_DRAW):
            surface.set_at(point, brush_color)

# Processamento co círculo
def mindPointCircle( raio, second_click, surface):
    point_x, point_y = second_click
    x = 0
    y = raio
    d = 1 - raio

    plotaOcteto(x, y, point_x, point_y, surface)

    while(x < y):
        if(d < 0):
            d += (2 * x) + 3
        else:
            d += 2 * (x - y) + 5
            y -= 1
        x += 1
        plotaOcteto(x, y, point_x, point_y, surface)

    pygame.display.flip() # permite atualiza a cada movimento do mouse



## Bezier
# LINK: https://www.pygame.org/wiki/BezierCurve
def compute_bezier_points(vertices, numPoints = 30):
    result = []

    b0x = vertices[0][0]
    b0y = vertices[0][1]
    b1x = vertices[1][0]
    b1y = vertices[1][1]
    b2x = vertices[2][0]
    b2y = vertices[2][1]
    b3x = vertices[3][0]
    b3y = vertices[3][1]

    # Compute polynomial coefficients from Bezier points
    ax = -b0x + 3 * b1x + -3 * b2x + b3x
    ay = -b0y + 3 * b1y + -3 * b2y + b3y

    bx = 3 * b0x + -6 * b1x + 3 * b2x
    by = 3 * b0y + -6 * b1y + 3 * b2y

    cx = -3 * b0x + 3 * b1x
    cy = -3 * b0y + 3 * b1y

    dx = b0x
    dy = b0y

    # Set up the number of steps and step size
    numSteps = numPoints - 1 # arbitrary choice
    h = 1.0 / numSteps # compute our step size

    # Compute forward differences from Bezier points and "h"
    pointX = dx
    pointY = dy

    firstFDX = ax * (h * h * h) + bx * (h * h) + cx * h
    firstFDY = ay * (h * h * h) + by * (h * h) + cy * h


    secondFDX = 6 * ax * (h * h * h) + 2 * bx * (h * h)
    secondFDY = 6 * ay * (h * h * h) + 2 * by * (h * h)

    thirdFDX = 6 * ax * (h * h * h)
    thirdFDY = 6 * ay * (h * h * h)

    # Compute points at each step
    result.append((int(pointX), int(pointY)))

    for i in range(numSteps):
        pointX += firstFDX
        pointY += firstFDY

        firstFDX += secondFDX
        firstFDY += secondFDY

        secondFDX += thirdFDX
        secondFDY += thirdFDY

        result.append((int(pointX), int(pointY)))

    return result

#  Auxiliar do Bezier
def makeSurfaceBezier(control_points):
    bez_surface = makeSurface()
    if(len(control_points) >= 4):
        b_points = compute_bezier_points(control_points)
        pygame.draw.lines(bez_surface, brush_color, False, b_points)
    return bez_surface

# ----------- Funções para Auílio da Execução (util) ----------

# Cria uma Surface: todas as formas chamam ela
def makeSurface():
    s = pygame.Surface(DIMENSION, pygame.SRCALPHA, 32)
    s.convert_alpha()
    return s

# Atualiza menu
def att_menu():
    pygame.draw.rect(screen, GRAY, menu_screen)
    for (color, rect) in rect_colors.items():
        pygame.draw.rect(screen, color, rect) # coloca a cor no retangulo
        if brush_color == color:
            border = 3
        else:
            border = 1
        pygame.draw.rect(screen, BLACK, rect, border) # coloca a borda

    pygame.draw.rect(screen, BLACK, clear_rect, 1)

    # coloca a imagem
    screen.blit(line, (13, 253))
    screen.blit(rectangle, (13, 293))
    screen.blit(square, (13, 333))
    screen.blit(circle, (13, 373))
    screen.blit(polyline, (13, 413))
    screen.blit(curve, (13, 453))
    screen.blit(clear, (13, 523))

    for(img, rect) in rect_shapes.items():
        if shape == img:
            border = 3
        else:
            border = 1
        pygame.draw.rect(screen, BLACK, rect, border) # coloca o retangulo da imagem

# Printa todas as Surfaces que estao na lista (para atualizar a tela)
def print_all_with_new_surface(listImages, new_surface):
    screen.fill(WHITE)
    att_menu()
    screen.blit(new_surface, DEFAULT_POSITON)
    for i in listImages:
        screen.blit(i, DEFAULT_POSITON )

# Atualiza todas as Surface ja colocadas
def print_all_images(listImages):
    screen.fill(WHITE)
    att_menu()
    for i in listImages:
        screen.blit(i, DEFAULT_POSITON)

# Detecca qual botao do mouse_pos
# sequence of booleans representing the state of all the mouse buttons
def button_mouse(tripla):
    if(tripla[0]):
        return ESQUERDO
    elif(tripla[1]):
        return MEIO
    elif(tripla[2]):
        return DIREITO
    else:
        return -1

# ----------------------------------------------

# ----------- Color List ----------

GREEN = (0, 255, 0)
GRAY = (197, 197, 197)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
DARK_GRAY = (107, 104, 99)
PINK = (249, 57, 255)
LIGHT_BLUE = (54, 207, 241)
YELLOW = (255, 241, 73)
ORANGE = (252, 155, 64)
PURPLE = (167, 0, 238)
DARK_GREEN = (58, 158, 73)
WHITE = (255, 255, 255)
BROWN = (85, 46, 46)
PRETTY_BLUE = (0, 238, 195)
VIOLET = (238,130,238)

# ---------------------------------

# ----------- Constantes ----------

LINE = "line"
RECTANGLE = "rectangle"
SQUARE = "square"
CIRCLE = "circle"
POLYLINE = "polyline"
CURVE = "curve"

WIDTH = 1024

HEIGHT = 680

DIMENSION = (WIDTH, HEIGHT)

LINHA = (20, 20, 20 ,20)

WIDTH_TO_DRAW = 60

# Mapea tuplas
X = 0
Y = 1
Z = 2

DEFAULT_POSITON = (0,0)

# Botoẽs do Mouse
ESQUERDO = 1
MEIO = 2
DIREITO = 3


# ----------- Variáveis ----------

click_position = False

ListSurfaces = []

# ----------- Execução do programa ----------

# Cria a tela
screen = pygame.display.set_mode(DIMENSION)
screen.fill(WHITE)

pygame.init()

# cria a parte do menu mas não coloca na tela
menu_screen = pygame.Rect(0, 0, 60, 680)
pygame.draw.rect(screen, GRAY, menu_screen)

green_rect = pygame.Rect(5, 5, 20, 20)
red_rect = pygame.Rect(30, 5, 20, 20)
blue_rect = pygame.Rect(5, 30, 20, 20)
pink_rect = pygame.Rect(30, 30, 20, 20)
light_blue_rect = pygame.Rect(5, 55, 20, 20)
yellow_rect = pygame.Rect(30, 55, 20, 20)
orange_rect = pygame.Rect(5, 80, 20, 20)
purple_rect = pygame.Rect(30, 80, 20, 20)
dark_green_rect = pygame.Rect(5, 105, 20, 20)
brown_rect = pygame.Rect(30, 105, 20, 20)
white_rect = pygame.Rect(5, 130, 20, 20)
pretty_blue_rect = pygame.Rect(30, 130, 20, 20)
gray_rect = pygame.Rect(5, 155, 20, 20)
dark_gray_rect = pygame.Rect(30, 155, 20, 20)
black_rect = pygame.Rect(5, 180, 20, 20)
violet_rect = pygame.Rect(30, 180, 20, 20)



line = pygame.image.load("images/substract.png")
line_rect = pygame.Rect(5, 250, 45, 30)

rectangle = pygame.image.load("images/rectangle.png")
rectangle_rect = pygame.Rect(5, 290, 45, 30)

square = pygame.image.load("images/perfect-square.png")
square_rect = pygame.Rect(5, 330, 45, 30)

circle = pygame.image.load("images/empty.png")
circle_rect = pygame.Rect(5, 370, 45, 30)

polyline = pygame.image.load("images/icon.png")
polyline_rect = pygame.Rect(5, 410, 45, 30)

curve = pygame.image.load("images/scribble.png")
curve_rect = pygame.Rect(5, 450, 45, 30)

# dicionario: rgb -> rect, função: automatizar a criação do menu
rect_colors = {GREEN: green_rect,
               RED: red_rect,
               BLUE: blue_rect,
               PINK: pink_rect,
               LIGHT_BLUE: light_blue_rect,
               YELLOW: yellow_rect,
               ORANGE: orange_rect,
               PURPLE: purple_rect,
               DARK_GREEN: dark_green_rect,
               BROWN: brown_rect,
               WHITE: white_rect,
               PRETTY_BLUE: pretty_blue_rect,
               GRAY: gray_rect,
               DARK_GRAY: dark_gray_rect,
               BLACK: black_rect,
               VIOLET: violet_rect
               }

# dicionario: shape(imagem) -> rect, função: automatizar a criação do menu
rect_shapes = {line: line_rect,
               rectangle: rectangle_rect,
               square: square_rect,
               circle: circle_rect,
               polyline: polyline_rect,
               curve: curve_rect
               }


brush_color = GREEN
shape = line

clear_rect = pygame.Rect(5, 520, 45, 20)
font = pygame.font.SysFont('Arial', 10)
clear = font.render("Clear", True, BLACK)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                syst.exit()

        # clicou
        if event.type == MOUSEBUTTONDOWN:
            click_position = True

        # "desclicou"
        if event.type == MOUSEBUTTONUP:
            click_position = False

    # pega a posição do mouse na area de
    mouse_pos = pygame.mouse.get_pos()

    running = False
    if click_position == True and mouse_pos[0] > WIDTH_TO_DRAW:
        if(shape == line):
            running = True
            first_click = mouse_pos
            while(running):
                event = pygame.event.wait()
                second_click = pygame.mouse.get_pos()
                line_surface = makeSurface()

                bresenham(first_click, second_click, line_surface)

                print_all_with_new_surface(ListSurfaces, line_surface)
                if event.type == MOUSEBUTTONUP:
                    click_position = False
                    running = False
                    ListSurfaces.append(line_surface)

        elif(shape == rectangle):
            running = True
            first_click = mouse_pos
            while(running):
                event = pygame.event.wait()
                second_click = pygame.mouse.get_pos()
                rectangle_surface = makeSurface()

                xFirst, yFirst = first_click
                xSecond, ySecond = second_click

                p1 = (xFirst, ySecond)
                p2 = (xSecond, yFirst)

                if second_click[0] > WIDTH_TO_DRAW:
                    bresenham(first_click, p1, rectangle_surface)
                    bresenham(first_click, p2, rectangle_surface)
                    bresenham(second_click, p1, rectangle_surface)
                    bresenham(second_click, p2, rectangle_surface)

                print_all_with_new_surface(ListSurfaces, rectangle_surface)
                if event.type == MOUSEBUTTONUP:
                    click_position = False
                    running = False
                    ListSurfaces.append(rectangle_surface)

        elif(shape == square):
            running = True
            first_click = mouse_pos
            while(running):
                event = pygame.event.wait()
                second_click = pygame.mouse.get_pos()
                square_surface = makeSurface()

                xFirst, yFirst = first_click
                xSecond, ySecond = second_click

                xMirror = abs(xFirst - xSecond)
                yMirror = abs(yFirst - ySecond)

                if xSecond > xFirst:
                    if(ySecond > yFirst):
                        p3 = (xSecond - xMirror, ySecond - xMirror)
                        p2 = (xSecond, ySecond - xMirror)
                        p1 = (xSecond - xMirror, ySecond)
                    else:
                        p3 = (xSecond - xMirror, ySecond + xMirror)
                        p2 = (xSecond - xMirror, ySecond)
                        p1 = (xSecond, ySecond + xMirror)

                elif xSecond < xFirst:
                    if(ySecond < yFirst):
                        p3 = (xSecond + xMirror, ySecond + xMirror)
                        p2 = (xSecond + xMirror, ySecond)
                        p1 = (xSecond, ySecond + xMirror)
                    else:
                        p3 = (xSecond + xMirror, ySecond - xMirror)
                        p2 = (xSecond + xMirror, ySecond)
                        p1 = (xSecond, ySecond - xMirror)
                else:
                    p1 = p2 = p3 = second_click

                if second_click[0] > WIDTH_TO_DRAW:
                    bresenham(second_click, p1, square_surface)
                    bresenham(second_click, p2, square_surface)
                    bresenham(p3, p2, square_surface)
                    bresenham(p3, p1, square_surface)

                print_all_with_new_surface(ListSurfaces, square_surface)
                if event.type == MOUSEBUTTONUP:
                    click_position = False
                    running = False
                    ListSurfaces.append(square_surface)

        elif(shape == circle):
            running = True
            first_click = mouse_pos
            while(running):
                event = pygame.event.wait()
                second_click = pygame.mouse.get_pos()
                circle_suface = makeSurface()

                # Valor do raio da circuferencia: Distancia entre dois pontos
                raio = int(sqrt(
                    ( (first_click[X] - second_click[X]) ** 2) + ( (first_click[Y] - second_click[Y]) ** 2)
                ))

                mindPointCircle(raio, second_click, circle_suface)

                print_all_with_new_surface(ListSurfaces, circle_suface)
                if event.type == MOUSEBUTTONUP:
                    click_position = False
                    running = False
                    ListSurfaces.append(circle_suface)

        elif(shape == polyline):
            running = True
            first_click = mouse_pos
            while(running):
                event = pygame.event.wait()
                button_pressed = pygame.mouse.get_pressed()
                second_click = pygame.mouse.get_pos()
                polyline_surface = makeSurface()
                bresenham(first_click, second_click, polyline_surface)
                print_all_with_new_surface(ListSurfaces, polyline_surface)

                # clicou no esquerdo: cria uma polyline e continua
                if(ESQUERDO == button_mouse(button_pressed)):
                    if event.type == MOUSEBUTTONDOWN:
                        ListSurfaces.append(polyline_surface)
                        first_click = second_click

                # clicou no dirretio, para de fazer uma polyline
                if(DIREITO == button_mouse(button_pressed)):
                    if event.type == MOUSEBUTTONDOWN:
                        click_position = False
                        running = False
                        ListSurfaces.append(polyline_surface)

        elif(shape == curve):
            running = True
            first_click = mouse_pos
            selected = None
            control_points = []
            while(running):

                curve_surface = makeSurfaceBezier(control_points)

                for event in pygame.event.get():
                    if event.type in (QUIT, KEYDOWN):
                        running = False

                    elif event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:

                            # Verifica qual botao foi selecionado.
                            # Passa por todo e no final fica o que estiver mais perto do ponto do click
                            i = 0
                            for p in control_points:
                                if(abs(p[X] - event.pos[0]) < 10 and abs(p[Y] - event.pos[1]) < 10):
                                    selected = p
                                    j = i
                                i += 1

                        # Adiciona ponto a lista de controle (nao pega o primero botao)
                        elif event.button == 3 and len(control_points) < 4:
                            if pygame.mouse.get_pos()[0] > WIDTH_TO_DRAW:
                                control_points.append(pygame.mouse.get_pos())

                    # Se tirou o botao , entao o que estava selecionado
                    elif event.type == MOUSEBUTTONUP and event.button == 1:
                        selected = None

                # Quando tiver um selecionado, vai arrastar a image, trocando sua posicao
                # pela posicao do ponto de controle
                if selected is not None:
                    selected = pygame.mouse.get_pos()
                    control_points[j] = selected

                # Bolinhas colocadas
                for p in control_points:
                    pygame.draw.circle(curve_surface, BLUE, (int(p[X]), int(p[Y])), 7)

                ### Draw control "lines"
                if(len(control_points) >= 2):
                    pygame.draw.lines(curve_surface, LIGHT_BLUE, False, [(ponto[X], ponto[Y]) for ponto in control_points])

                pygame.display.flip()
                print_all_with_new_surface(ListSurfaces, curve_surface)

            # Quando sair da curva
            click_position = False
            running = False
            ListSurfaces.append( makeSurfaceBezier(control_points) )
            shape = ""
            screen.fill(WHITE)

    # verifica se houve um click_position
    if(click_position == True and click_position <= WIDTH_TO_DRAW):
        if green_rect.collidepoint(mouse_pos):
            brush_color = GREEN
        elif red_rect.collidepoint(mouse_pos):
            brush_color = RED
        elif blue_rect.collidepoint(mouse_pos):
            brush_color = BLUE
        elif pink_rect.collidepoint(mouse_pos):
            brush_color = PINK
        elif light_blue_rect.collidepoint(mouse_pos):
            brush_color = LIGHT_BLUE
        elif yellow_rect.collidepoint(mouse_pos):
            brush_color = YELLOW
        elif orange_rect.collidepoint(mouse_pos):
            brush_color = ORANGE
        elif purple_rect.collidepoint(mouse_pos):
            brush_color = PURPLE
        elif dark_green_rect.collidepoint(mouse_pos):
            brush_color = DARK_GREEN
        elif white_rect.collidepoint(mouse_pos):
            brush_color = WHITE
        elif brown_rect.collidepoint(mouse_pos):
            brush_color = BROWN
        elif pretty_blue_rect.collidepoint(mouse_pos):
            brush_color = PRETTY_BLUE
        elif gray_rect.collidepoint(mouse_pos):
            brush_color = GRAY
        elif dark_gray_rect.collidepoint(mouse_pos):
            brush_color = DARK_GRAY
        elif black_rect.collidepoint(mouse_pos):
            brush_color = BLACK
        elif violet_rect.collidepoint(mouse_pos):
            brush_color = VIOLET

        # verifica qual forma de desenho foi clicada
        if line_rect.collidepoint(mouse_pos):
            shape = line
        elif rectangle_rect.collidepoint(mouse_pos):
            shape = rectangle
        elif square_rect.collidepoint(mouse_pos):
            shape = square
        elif circle_rect.collidepoint(mouse_pos):
            shape = circle
        elif polyline_rect.collidepoint(mouse_pos):
            shape = polyline
        elif curve_rect.collidepoint(mouse_pos):
            shape = curve

        if clear_rect.collidepoint(mouse_pos):
            screen.fill(WHITE)
            ListSurfaces = []


    att_menu()
    for i in ListSurfaces:
        screen.blit(i, (0,0))
    pygame.display.update()

# ------------- EOF --------------------
