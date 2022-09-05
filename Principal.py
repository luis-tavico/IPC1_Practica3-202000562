import random


class Principal:

    tablero = []
    filas = 15
    columnas = 40
    x = 7
    y = 20
    pacman = "C"
    juegoTerminado = False
    puntos = 0
    movimientos = 0
    ultimaFruta = 0

    def crearTablero(self):
        for i in range(self.filas):
            self.tablero.append([])
            for j in range(self.columnas):
                self.tablero[i].append([])

        for i in range(self.filas):
            for j in range(self.columnas):
                self.tablero[i][j] = " "

        ######################################
        # Creando los muros del tablero
        ####################LADO IZQUIERDO####################
        # Primer linea horizontal al lado izquierdo
        self.tablero[3][0] = "="
        self.tablero[3][1] = "="
        self.tablero[3][2] = "="
        # Segunda linea horizontal al lado izquierdo
        self.tablero[8][0] = "="
        self.tablero[8][1] = "="
        self.tablero[8][2] = "="
        self.tablero[8][3] = "="
        self.tablero[8][4] = "="
        self.tablero[8][5] = "="
        # Tercer linea horizontal al lado izquierdo
        self.tablero[11][0] = "="
        self.tablero[11][1] = "="
        self.tablero[11][2] = "="
        self.tablero[11][3] = "="
        self.tablero[11][4] = "="
        self.tablero[11][5] = "="
        self.tablero[11][6] = "="
        ####################LADO DERECHO####################
        # Primer linea horizontal al lado derecho
        self.tablero[3][30] = "="
        self.tablero[3][31] = "="
        self.tablero[3][32] = "="
        self.tablero[3][33] = "="
        self.tablero[3][34] = "="
        self.tablero[3][35] = "="
        self.tablero[3][36] = "="
        self.tablero[3][37] = "="
        self.tablero[3][38] = "="
        self.tablero[3][39] = "="
        self.tablero[1][35] = "|"  # linea vertical
        self.tablero[2][35] = "|"  # linea vertical
        # Segunda linea horizontal al lado derecho
        self.tablero[8][35] = "="
        self.tablero[8][36] = "="
        self.tablero[8][37] = "="
        self.tablero[8][38] = "="
        self.tablero[8][39] = "="
        # Tercer linea horizontal al lado derecho
        self.tablero[11][35] = "="
        self.tablero[11][36] = "="
        self.tablero[11][37] = "="
        self.tablero[11][38] = "="
        self.tablero[11][39] = "="
        ####################LADO INFERIOR####################
        # Primer linea vertical al lado inferior
        self.tablero[13][7] = "|"
        self.tablero[14][7] = "|"
        # Segunda linea vertical al lado inferior
        self.tablero[10][14] = "|"
        self.tablero[11][14] = "|"
        self.tablero[12][14] = "|"
        self.tablero[13][14] = "|"
        self.tablero[14][14] = "|"
        self.tablero[10][12] = "="  # linea horizontal lado izquierdo
        self.tablero[10][13] = "="  # linea horizontal lado izquierdo
        self.tablero[10][15] = "="  # linea horizontal lado derecho
        self.tablero[10][16] = "="  # linea horizontal lado derecho
        self.tablero[10][17] = "="  # linea horizontal lado derecho
        self.tablero[10][18] = "="  # linea horizontal lado derecho
        self.tablero[10][19] = "="  # linea horizontal lado derecho
        self.tablero[10][20] = "="  # linea horizontal lado derecho
        # Tercer linea vertical al lado inferior
        self.tablero[12][24] = "|"
        self.tablero[13][24] = "|"
        self.tablero[14][24] = "|"
        self.tablero[12][20] = "="  # linea horizontal izquierdo
        self.tablero[12][21] = "="  # linea horizontal izquierdo
        self.tablero[12][22] = "="  # linea horizontal izquierdo
        self.tablero[12][23] = "="  # linea horizontal izquierdo
        # Cuarta linea vertical al lado inferior
        self.tablero[10][30] = "|"
        self.tablero[11][30] = "|"
        self.tablero[12][30] = "|"
        self.tablero[13][30] = "|"
        self.tablero[14][30] = "|"
        self.tablero[13][31] = "="  # linea horizontal derecho
        self.tablero[13][32] = "="  # linea horizontal derecho
        self.tablero[13][33] = "="  # linea horizontal derecho
        self.tablero[13][34] = "="  # linea horizontal derecho
        self.tablero[13][35] = "="  # linea horizontal derecho
        ####################LADO SUPERIOR####################
        # Primer linea vertical al lado superior
        self.tablero[0][7] = "|"
        self.tablero[1][7] = "|"
        # segunda linea vertical de lado superior
        self.tablero[0][14] = "|"
        self.tablero[1][14] = "|"
        self.tablero[2][14] = "|"
        self.tablero[3][14] = "|"
        self.tablero[4][14] = "|"
        self.tablero[4][15] = "="  # linea horizontal derecho
        self.tablero[4][16] = "="  # linea horizontal derecho
        self.tablero[4][17] = "="  # linea horizontal derecho
        self.tablero[4][18] = "="  # linea horizontal derecho
        # Tercer linea vertical al lado superior
        self.tablero[0][24] = "|"
        self.tablero[1][24] = "|"
        self.tablero[2][24] = "|"
        self.tablero[3][24] = "|"
        self.tablero[4][24] = "|"
        self.tablero[5][24] = "|"
        self.tablero[6][24] = "|"
        self.tablero[7][24] = "|"
        self.tablero[2][18] = "="  # linea horizontal izquierda
        self.tablero[2][19] = "="  # linea horizontal izquierda
        self.tablero[2][20] = "="  # linea horizontal izquierda
        self.tablero[2][21] = "="  # linea horizontal izquierda
        self.tablero[2][22] = "="  # linea horizontal izquierda
        self.tablero[2][23] = "="  # linea horizontal izquierda
        self.tablero[6][25] = "="  # linea horizontal derecho
        self.tablero[6][26] = "="  # linea horizontal derecho
        self.tablero[6][27] = "="  # linea horizontal derecho
        self.tablero[6][28] = "="  # linea horizontal derecho
        self.tablero[6][29] = "="  # linea horizontal derecho
        self.tablero[6][30] = "="  # linea horizontal derecho
        self.tablero[6][31] = "="  # linea horizontal derecho
        self.tablero[6][32] = "="  # linea horizontal derecho
        self.tablero[6][33] = "="  # linea horizontal derecho
        self.tablero[5][33] = "|"  # linea vertical
        # Cuarta linea vertical al lado superior
        self.tablero[0][30] = "|"
        ####################CENTRO####################
        # Primer linea horizontal al centro
        self.tablero[5][3] = "="
        self.tablero[5][4] = "="
        self.tablero[5][5] = "="
        self.tablero[5][6] = "="
        self.tablero[5][7] = "="
        self.tablero[5][8] = "="
        self.tablero[5][9] = "="
        self.tablero[5][10] = "|"  # linea vertical superior
        self.tablero[6][10] = "|"  # linea vertical superior
        self.tablero[7][10] = "|"  # linea vertical superior
        self.tablero[7][10] = "="
        self.tablero[7][11] = "="
        self.tablero[7][12] = "="
        self.tablero[7][13] = "="
        self.tablero[7][14] = "="
        self.tablero[7][15] = "="
        self.tablero[7][16] = "="
        self.tablero[7][17] = "="
        # Poniendo comida en el tablero
        self.tablero[0][19] = "#"
        self.tablero[1][5] = "#"
        self.tablero[9][32] = "#"
        self.tablero[10][5] = "#"
        self.tablero[13][22] = "#"
        # Posicion de pacman en el tablero
        self.x = 7
        self.y = 20
        self.tablero[self.x][self.y] = self.pacman
        ####################Tablero Puntuaciones####################
        self.puntos = 0
        self.movimientos = 0
        self.ultimaFruta = 0

    def imprimirTablero(self):
        print(" ________________________________________ ")
        for i in range(self.filas):
            print("|", end="")
            for j in range(self.columnas):
                print(self.tablero[i][j], end="")
            print("|")
        print("|________________________________________|")
        print(" ________________________________________ ")
        print("|>Puntos: ", self.puntos, (28-len(str(self.puntos)))*(" "), "|")
        print("|>Movimientos: ", self.movimientos,
              (23-len(str(self.movimientos)))*(" "), "|")
        print("|>Ultima fruta: ", self.ultimaFruta,
              (22-len(str(self.ultimaFruta)))*(" "), "|")
        print("|________________________________________|")

    def posicionComida(self):
        numeroX = random.randint(0, 14)
        numeroY = random.randint(0, 39)
        while (self.tablero[numeroX][numeroY] != " "):
            numeroX = random.randint(0, 14)
            numeroY = random.randint(0, 39)
        self.tablero[numeroX][numeroY] = "#"

    def iniciar(self):
        self.juegoTerminado = False
        self.crearTablero()
        while(self.juegoTerminado == False):
            self.imprimirTablero()
            self.tablero[self.x][self.y] = " "
            if (self.puntos < 30):
                letra = input(
                    "Ingrese una tecla (W: arriba, S: abajo, A: izquierda, D: derecha, M: salir): ")
            else:
                letra = "m"
            if(letra == "w"):
                self.x -= 1
                if (self.x == -1):
                    self.x = 14
                if (self.tablero[self.x][self.y] == " "):
                    self.tablero[self.x][self.y] = self.pacman
                    self.movimientos += 1
                elif(self.tablero[self.x][self.y] == "#"):
                    self.posicionComida()
                    self.ultimaFruta = random.randint(1, 5)
                    self.puntos += self.ultimaFruta
                    self.tablero[self.x][self.y] = self.pacman
                    self.movimientos += 1
                else:
                    self.x += 1
                    self.tablero[self.x][self.y] = self.pacman
            elif(letra == "s"):
                self.x += 1
                if (self.x == 15):
                    self.x = 0
                if (self.tablero[self.x][self.y] == " "):
                    self.tablero[self.x][self.y] = self.pacman
                    self.movimientos += 1
                elif(self.tablero[self.x][self.y] == "#"):
                    self.posicionComida()
                    self.ultimaFruta = random.randint(1, 5)
                    self.puntos += self.ultimaFruta
                    self.tablero[self.x][self.y] = self.pacman
                    self.movimientos += 1
                else:
                    self.x -= 1
                    self.tablero[self.x][self.y] = self.pacman
            elif(letra == "a"):
                self.y -= 1
                if (self.y == -1):
                    self.y = 39
                if (self.tablero[self.x][self.y] == " "):
                    self.tablero[self.x][self.y] = self.pacman
                    self.movimientos += 1
                elif(self.tablero[self.x][self.y] == "#"):
                    self.posicionComida()
                    self.ultimaFruta = random.randint(1, 5)
                    self.puntos += self.ultimaFruta
                    self.tablero[self.x][self.y] = self.pacman
                    self.movimientos += 1
                else:
                    self.y += 1
                    self.tablero[self.x][self.y] = self.pacman
            elif(letra == "d"):
                self.y += 1
                if (self.y == 40):
                    self.y = 0
                if (self.tablero[self.x][self.y] == " "):
                    self.tablero[self.x][self.y] = self.pacman
                    self.movimientos += 1
                elif(self.tablero[self.x][self.y] == "#"):
                    self.posicionComida()
                    self.ultimaFruta = random.randint(1, 5)
                    self.puntos += self.ultimaFruta
                    self.tablero[self.x][self.y] = self.pacman
                    self.movimientos += 1
                else:
                    self.y -= 1
                    self.tablero[self.x][self.y] = self.pacman
            elif(letra == "m"):
                respuesta = "l"
                if (self.puntos >= 30):
                    while (respuesta != "s" and respuesta != "n"):
                        respuesta = input(
                            ("¡Juego Finalizado! ¿Desea Jugar de Nuevo? (S/N) "))
                        if (respuesta == "s"):
                            self.juegoTerminado = False
                            self.crearTablero()
                        elif(respuesta == "n"):
                            self.juegoTerminado = True
                            print("¡Ejecucion Finalizada!")
                        else:
                            print("¡Ingrese una letra valida!")
                else:
                    while (respuesta != "s" and respuesta != "n"):
                        respuesta = input("¿Seguro que Desea Salir? (S/N) ")
                        if (respuesta == "s"):
                            self.juegoTerminado = True
                            print("¡Ejecucion Finalizada!")
                        elif(respuesta == "n"):
                            self.tablero[self.x][self.y] = self.pacman
                            self.juegoTerminado = False
                        else:
                            print("¡Ingrese una letra valida!")
            else:
                self.tablero[self.x][self.y] = self.pacman
                print("¡Ingrese una tecla valida!")


if __name__ == "__main__":
    nuevoJuego = Principal()
    nuevoJuego.iniciar()
