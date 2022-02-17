#Importando e inicializando o PyGame
import pygame
import random
pygame.init()

#Iniciando tela
resolucao = [400,600]
tela = pygame.display.set_mode(resolucao)
pygame.display.set_caption("Flappy Bird")

#Declaração(cria) de texto
fonte = pygame.font.Font("freesansbold.ttf", 32)
texto = fonte.render("0", True, [0,255,0])

#Declaração(cria) imagem
fundo = pygame.image.load("./Fundos/Fundo1.png")
fundo = pygame.transform.scale(fundo, (400, 600))

#Criando classe de pássaro
class Passaro:
    x = 170
    y = 250
    largura = 40
    altura = 40

    pulo = 80
    velocidade = 4
    aceleracao = 0.5

    imagem = pygame.image.load("./Jogadores/bird1.png")
    imagem = pygame.transform.scale(imagem, (largura, altura))

    def Atualizar(self,tela):
        self.Desenhar(tela)
        self.Cair()

    def Desenhar(self,tela):
        tela.blit(self.imagem,[self.x,self.y]) #Desenha o pássaro

    def Cair(self):
        self.velocidade += self.aceleracao
        self.y += self.velocidade

    def Voar(self):
        self.y -= self.pulo
        self.velocidade = 0

class Cano:
    largura = 100
    altura = 1550
    canoBaixoY = 0
    canoCimaY = 0
    y = 0
    velocidade = 3

    cano_baixo = pygame.image.load("./Objetos/Canos/Cano1/baixo.png")
    cano_baixo = pygame.transform.scale(cano_baixo, (largura, altura))

    cano_cima = pygame.image.load("./Objetos/Canos/Cano1/cima.png")
    cano_cima = pygame.transform.scale(cano_cima, (largura, altura))

    def __init__(self,x):
        self.x = x
        self.Reiniciar()

    def Atualizar(self, tela):
        self.Desenhar(tela)

    def Desenhar(self, tela):
        tela.blit(self.cano_cima,[self.x,self.canoCimaY]) #Desenha o cano em cima[x,y]
        tela.blit(self.cano_baixo,[self.x,self.canoBaixoY]) #Desenha o cano em baixo[x,y]
        self.Mover()
        
    def Reiniciar(self):
        self.y = random.randrange(190, 460) #número aleatório de 190 a 460
        self.canoBaixoY = self.y
        self.canoCimaY = self.canoBaixoY-1690 #espaçamento de 140 entre os canos

    def Mover(self):
        self.x -= self.velocidade
        if self.x<=-95:
            self.x = 450
            self.Reiniciar()
        
class Chao:
    x = 0
    y = 510
    largura = 400
    altura = 90

    imagem = pygame.image.load("./Objetos/Choes/Chao1.png")
    imagem = pygame.transform.scale(imagem, (largura, altura))

    def Atualizar(self, tela):
        self.Desenhar(tela)
    
    def Desenhar(self, tela):
        tela.blit(self.imagem,[self.x,self.y])#posiciona o desenho na tela
    
def main(): #Função onde o jogo inteiro irá¡ rodar
    relogio = pygame.time.Clock()
    loop = True
    
    passaro = Passaro()#Instancia passáro
    chao = Chao() #Instancia chão
    cano1 = Cano(430) #Insatan
    cano2 = Cano(735)
    
    while loop: #Criar um loop infinito
        tela.blit(fundo,[0,-85]) #Desenha o fundo
        
        passaro.Atualizar(tela)
        chao.Atualizar(tela)
        cano1.Atualizar(tela)
        cano2.Atualizar(tela)

        tela.blit(texto, [200,0]) #Desenha o texto
        relogio.tick(30)
        pygame.display.update() #Atualiza a tela
        
        for event in pygame.event.get(): #Pega os eventos que ocorrem no jogo
            if event.type == pygame.QUIT: #Evento para quando o jogador apertar no "X" de nossa tela: sair do jogo
                loop = False

            if event.type == pygame.KEYDOWN: #Verifica se tecla foi pressionada
                if event.key == pygame.K_UP: #Verifica se tecla para cima foi pressionada
                    passaro.Voar()

            if event.type == pygame.MOUSEBUTTONDOWN: #Verifica se mouse foi pressionado
                passaro.Voar()

    pygame.quit()
        
main() #Executa o jogo
