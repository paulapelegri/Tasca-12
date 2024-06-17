import pygame
import random
import time

def principal():
    # Inicializar pygame
    pygame.init()
    # Configuración de la pantalla
    screen_width = 370 #ancho
    screen_height = 600 #alto
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("¡cuidado con las bombas!")

    # Colores
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)

    # FPS (frames per second)
    clock = pygame.time.Clock()
    fps = 60

    # Cargar la imagen de fondo
    fondo = pygame.image.load('fondo.png') # Cargar una imagen de fondo
    fondo = pygame.transform.scale(fondo, (screen_width, screen_height))  # Redimensionar la imagen al tamaño de la pantalla

    # Clase Cesta
    class Cesta:
        def __init__(self):
            self.image = pygame.image.load('cesta.png')  # Cargar la imagen de la cesta
            self.image = pygame.transform.scale(self.image, (75, 80))  # Redimensionar la imagen
            self.width = self.image.get_width() #tamaño de la imagen
            self.height = self.image.get_height()
            self.x = screen_width // 2 - self.width // 2
            self.y = screen_height - self.height - 10
            self.speed = 13 # Velocidad en la que se desplaza la cesta

        def draw(self):
            screen.blit(self.image, (self.x, self.y))  # Dibujar la imagen de la cesta

        def move(self, direction): # para que se mueva la imagen horizontalmente
            if direction == "left" and self.x > 0:
                self.x -= self.speed
            if direction == "right" and self.x < screen_width - self.width:
                self.x += self.speed

    # Clase Objeto
    class Objeto:
        def __init__(self, image_path, width, height, speed, is_bomba=False):
            self.image = pygame.image.load(image_path)
            self.image = pygame.transform.scale(self.image, (width, height))  # Redimensionar la imagen
            self.width = width
            self.height = height
            self.x = random.randint(0, screen_width - self.width)
            self.y = -self.height
            self.speed = speed  # usar velocidad constante
            self.is_bomba = is_bomba

        def fall(self):
            self.y += self.speed

        def draw(self): # dibujar la imagen en la pantalla
            screen.blit(self.image, (self.x, self.y))

    # función para mostrar texto en pantalla
    def mostrar_texto(texto, tamaño, color, x, y):
        fuente = pygame.font.Font(None, tamaño)
        superficie_texto = fuente.render(texto, True, color)
        rect_texto = superficie_texto.get_rect(center=(x, y))
        screen.blit(superficie_texto, rect_texto)

    # función para que los objetos no se superpongan entre ellos
    def crear_objeto(image_path, width, height, speed, is_bomba=False, objetos=[]):
        while True:
            nuevo_objeto = Objeto(image_path, width, height, speed, is_bomba)
            # verificar superposición
            superpuesto = False
            for obj in objetos:
                if (nuevo_objeto.x + nuevo_objeto.width > obj.x and nuevo_objeto.x < obj.x + obj.width and
                        nuevo_objeto.y + nuevo_objeto.height > obj.y and nuevo_objeto.y < obj.y + obj.height):
                    superpuesto = True
                    break
            if not superpuesto:
                return nuevo_objeto

    # función principal del juego
    def game_loop():
        cesta = Cesta()
        objeto_imagenes = ['uva.png', 'piña.png', 'poma.png','coco.png', 'platano.png', 'fresa.png', 'naranja.png', 'sandia.png']  # cargar lista de imágenes de objetos
        bomba_imagen = 'bomba.png'  # cargar imagen de la bomba
        velocidad_objetos = 4  # Velocidad constante para todos los objetos
        objetos = [crear_objeto(random.choice(objeto_imagenes), 40, 40, velocidad_objetos)]  # ajustar tamaño y velocidad de los objetos
        score = 0
        running = True
        game_over = False
        tiempo_ultima_bomba = time.time()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed() 
            if keys[pygame.K_LEFT]: # las teclas que hay que apretar para desplazar la cesta
                cesta.move("left")
            if keys[pygame.K_RIGHT]: # las teclas que hay que apretar para desplazar la cesta
                cesta.move("right")

            # Controlar la generación de bombas cada 4 segundos
            tiempo_actual = time.time()
            if tiempo_actual - tiempo_ultima_bomba >= 4:
                objetos.append(crear_objeto(bomba_imagen, 45, 45, velocidad_objetos, is_bomba=True, objetos=objetos))
                tiempo_ultima_bomba = tiempo_actual

            if not game_over:
                for objeto in objetos:
                    objeto.fall()
                    if objeto.y > screen_height:
                        if not objeto.is_bomba:  # Si un objeto (a parte de la bomba) cae sin ser recogida por la cesta, se acaba el juego
                            game_over = True
                        objetos.remove(objeto)
                        if not game_over:  # Solo agregar nuevos objetos si el juego no ha terminado
                            objetos.append(crear_objeto(random.choice(objeto_imagenes), 50, 50, velocidad_objetos, objetos=objetos))
                    if (objeto.x + objeto.width > cesta.x and objeto.x < cesta.x + cesta.width and
                            objeto.y + objeto.height > cesta.y and objeto.y < cesta.y + cesta.height):
                        if objeto.is_bomba:
                            game_over = True
                        else:
                            objetos.remove(objeto)
                            objetos.append(crear_objeto(random.choice(objeto_imagenes), 45, 45, velocidad_objetos, objetos=objetos))  # Ajustar tamaño y velocidad de los objetos
                            score += 1

            screen.blit(fondo, (0, 0))  # Dibujar la imagen de fondo
            cesta.draw()
            for objeto in objetos:
                objeto.draw()

            if game_over:
                mostrar_texto("GAME OVER!", 65, red, screen_width // 2, screen_height // 2) # cuando te comes una bomba o se te cae una fruta, sale "game over" en la pantalla.

            pygame.display.flip()
            clock.tick(fps)

        pygame.quit()

    game_loop()

def pex3():
    principal()