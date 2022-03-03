#Importando e inicializando o PyGame
import pygame, random
pygame.init()

#Iniciando tela
resolucao = [400,600]
tela = pygame.display.set_mode(resolucao)
pygame.display.set_caption("Flappy Bird")

pontuacao = 0

#Declaração de texto
fonte = pygame.font.Font("freesansbold.ttf", 32)
texto = fonte.render(str(pontuacao), True, [0,255,0])

#Declaração de imagem
fundo = pygame.image.load("./Fundos/Fundo1.png")
fundo = pygame.transform.scale(fundo, (400, 600))

loop = True


#Criando classe de pássaro
class Passaro:
    
    x = 170
    y = 250
    largura = 40
    altura = 40

    pulo = 80
    velocidade = 0
    aceleracao = 0.5

    imagem = pygame.image.load("./Jogadores/bird1.png")
    imagem = pygame.transform.scale(imagem, (largura, altura))

    def Atualizar(self,tela):
        self.rect = pygame.Rect(self.x,self.y,self.largura,self.altura)
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

class Chao:
    x = 0
    y = 510
    largura = 400
    altura = 90

    imagem = pygame.image.load("./Objetos/Choes/Chao1.png")
    imagem = pygame.transform.scale(imagem, (largura, altura))

    def Atualizar(self,tela,passaro):
        self.rect = pygame.Rect(self.x,self.y,self.largura,self.altura)
        self.Colidir(passaro)
        self.Desenhar(tela)

    def Colidir(self,passaro):
        global loop
        
        if self.rect.colliderect(passaro):
            loop = False
            
    def Desenhar(self,tela):
        tela.blit(self.imagem,[self.x,self.y]) #Desenha o chão

class Cano:

    def __init__(self,x):
        self.x = x
        
        self.largura = 100
        self.altura = 1550

        self.velocidade = 5

        self.imagem_cima = pygame.image.load("./Objetos/Canos/Cano1/cima.png")
        self.imagem_cima = pygame.transform.scale(self.imagem_cima, (100, 1550))
        
        self.imagem_baixo = pygame.image.load("./Objetos/Canos/Cano1/baixo.png")
        self.imagem_baixo = pygame.transform.scale(self.imagem_baixo, (100, 1550))

        
        self.Reiniciar()

    def Reiniciar(self):
        y = random.randrange(190,460)
        self.y_baixo = y
        self.y_cima = y - self.altura - 140
        self.ponto = 1

    def Atualizar(self,tela,passaro):
        self.rect_Cima = pygame.Rect(self.x,self.y_cima,self.largura,self.altura)
        self.rect_Baixo = pygame.Rect(self.x,self.y_baixo,self.largura,self.altura)
        self.rect_EntreCanos = pygame.Rect(self.x,self.y_baixo - (self.y_cima + self.altura),self.largura,self.altura)        
        
        self.Colidir(passaro)
        self.Desenhar(tela)
        self.Mover()

    def Colidir(self,passaro):
        global loop
        
        if self.rect_Cima.colliderect(passaro):
            loop = False
        if self.rect_Baixo.colliderect(passaro):
            loop = False
        if self.rect_EntreCanos.colliderect(passaro):
            if self.ponto > 0:
                self.ponto = 1

    def Desenhar(self,tela):
        tela.blit(self.imagem_baixo,[self.x,self.y_baixo]) #Desenha o cano de cima
        tela.blit(self.imagem_cima,[self.x,self.y_cima]) #Desenha o cano de cima

    def Mover(self):
        self.x -= self.velocidade

        if self.x + self.largura <= 0:
            self.x = 450
            self.Reiniciar()

cano1 = Cano(450)
cano2 = Cano(735)
    
def main(): #Função onde o jogo inteiro irá rodar
    global loop
    global pontuacao
    relogio = pygame.time.Clock()
    
    passaro = Passaro()
    chao = Chao()

    while loop: #Criar um loop infinito
        tela.blit(fundo,[0,-85]) #Desenha o fundo
        passaro.Atualizar(tela)
        cano1.Atualizar(tela,passaro.rect)
        cano2.Atualizar(tela,passaro.rect)
        chao.Atualizar(tela,passaro.rect)
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
