#Importando e inicializando o PyGame
import pygame, random
pygame.init()

#Iniciando tela
resolucao = [400,600]
tela = pygame.display.set_mode(resolucao)
pygame.display.set_caption("Flappy Bird")

#Declaração de fonte
fonte = pygame.font.Font("freesansbold.ttf", 32)

#Declaração de imagem
fundo = pygame.image.load("./Fundos/Fundo1.png")
fundo = pygame.transform.scale(fundo, (400, 600))

#Efeito sonoro quando o jogo iniciar
som_iniciar = pygame.mixer.Sound("./Sons/iniciar.wav")
som_iniciar.play()

#Tocar música
pygame.mixer.music.load("./Sons/musica.wav")
pygame.mixer.music.play(-1)

loop = True
pontuacao = 0

#Criando classe de pássaro
class Passaro:
    x = 170
    y = 250
    largura = 40
    altura = 40

    pulo = 40
    velocidade = 0
    aceleracao = 0.5

    som_voar = pygame.mixer.Sound("./Sons/voar.wav")

    imagens = [pygame.image.load("./Jogadores/bird1.png"),
               pygame.image.load("./Jogadores/bird2.png"),
               pygame.image.load("./Jogadores/bird3.png")]
    
    for i in range(len(imagens)):
        imagens[i] = pygame.transform.scale(imagens[i], (largura, altura))

    sprite_atual = 0

    def Atualizar(self,tela):
        self.rect = pygame.Rect(self.x,self.y,self.largura,self.altura)
        self.Desenhar(tela)
        self.Cair()

    def Desenhar(self,tela):
        tela.blit(self.imagens[self.sprite_atual],[self.x,self.y]) #Desenha o pássaro

    def Cair(self):
        self.velocidade += self.aceleracao
        self.y += self.velocidade

    def Voar(self):
        self.y -= self.pulo
        self.velocidade = 0
        self.som_voar.play()

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

        self.som_ponto = pygame.mixer.Sound("./Sons/ponto.wav")
        self.Reiniciar()

    def Reiniciar(self):
        y = random.randrange(190,460)
        self.y_baixo = y
        self.y_cima = y - self.altura - 140
        self.ponto = 1

    def Atualizar(self,tela,passaro):
        self.rect_cima = pygame.Rect(self.x,self.y_cima,self.largura,self.altura)
        self.rect_baixo = pygame.Rect(self.x,self.y_baixo,self.largura,self.altura)
        self.rect_ponto = pygame.Rect(self.x,self.y_cima + self.altura,self.largura,self.y_baixo-(self.y_cima + self.altura))
        
        self.Desenhar(tela)
        self.Mover()
        self.Colidir(passaro)

    def Colidir(self,passaro):
        global loop, pontuacao
        
        if self.rect_cima.colliderect(passaro):
            loop = False

        if self.rect_baixo.colliderect(passaro):
            loop = False

        if self.rect_ponto.colliderect(passaro):
            if self.ponto > 0:
                pontuacao += self.ponto
                self.som_ponto.play(0)
                self.ponto = 0
                

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
    relogio = pygame.time.Clock()
    
    passaro = Passaro()
    chao = Chao()

    contador = 0
    while loop: #Criar um loop infinito
        tela.blit(fundo,[0,-85]) #Desenha o fundo
        passaro.Atualizar(tela)
        cano1.Atualizar(tela,passaro.rect)
        cano2.Atualizar(tela,passaro.rect)
        chao.Atualizar(tela,passaro.rect)
        texto = fonte.render(str(pontuacao), True, [0,255,0]) #Define texto
        tela.blit(texto, [200,0]) #Desenha o texto

        contador = 0
        if contador > 30:
            contador = contador + 1
        else:
            contador = 0
        print(contador)
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
