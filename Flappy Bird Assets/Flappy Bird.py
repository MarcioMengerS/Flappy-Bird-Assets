#Importa biblioteca e inicializa o Pygame
import pygame
pygame.init()

#Declara (cria) tela principal do jogo e seu tamanho
resolucao = [400,600] #variavel para tamanho da tela
tela = pygame.display.set_mode(resolucao)

#Modifica o nome na barra do aplicativo
pygame.display.set_caption("Flappy Bird")

#Declara (Cria) uma superfície com tamanho de x,y
#superficie = pygame.Surface([100,400])

#Declaração(criação) do retângulo
#rect = pygame.Rect(20,20,35,45) #(x,y,largura,altura)

#Declaração (criação) de texto
fonte = pygame.font.Font("freesansbold.ttf", 32)
texto = fonte.render("0", True, [0,255,0])#texto, borda suave, cor

#Declaração (criação) de Imagem de fundo
fundo = pygame.image.load("./Fundos/Fundo1.png")
fundo = pygame.transform.scale(fundo,(400,600))#Redimensionamento da imagem

#passaro = pygame.image.load("./Jogadores/bird1.png")
#passaro = pygame.transform.scale(passaro,(40,40))#Define o tamanho da imagem

canoCima = pygame.image.load("./Objetos/Canos/Cano1/cima.png")
canoCima = pygame.transform.scale(canoCima,(100,1550))

canoBaixo = pygame.image.load("./Objetos/Canos/Cano1/baixo.png")
canoBaixo = pygame.transform.scale(canoBaixo,(100,1550))

chao = pygame.image.load("./Objetos/Choes/chao1.png")
chao = pygame.transform.scale(chao,(400,90))

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
        self.Desenhar(tela)
        self.Cair()
        
    def Desenhar(self,tela):#Desenha o passaro
        tela.blit(self.imagem,[self.x,self.y])

    def Cair(self):
        self.velocidade += self.aceleracao # Aumenta a velocidade de queda do passaro
        self.y += self.velocidade #Alterar a posião do passaro com base na velocidade 

    def Voar(self):
        self.y -= self.pulo #passar salta
        self.velocidade = 0 #reseta a velocidade de queda

class Cano:
    def __init__(self,x,y):
        self.x = x
        self.y = y

cano = Cano(2,3)
print(cano.x,cano.y)
        
#Pintando Tela
#tela.fill([0,100,220]) # principal AZUL
#superficie.fill([0,255,0]) #superfície VERDE


#Imprimir retângulo em cima da superficie verde
#pygame.draw.rect(superficie,[255,0,0],rect)

#Imprimir na tela principal
#tela.blit(superficie,[300,200])#superficie verde na posição x,y
#tela.blit(fundo,[0,-85])
#tela.blit(texto, [0,0])#texto na posição x,y
#tela.blit(passaro, [170,250])#imagem n posição x,y
#tela.blit(canoBaixo, [300,310])
#tela.blit(canoCima, [300,-1380])
#tela.blit(chao,[0,510])

#atualiza a tela
#pygame.display.update()

#Função onde o jogo inteiro irá rodar
def main():
    relogio = pygame.time.Clock() #Cria um console de frame rate
    loop = True
    posX = 300
    
    passaro = Passaro() #Cria instancia da classe passaro
    #posY = 250
    
    #Criar loop infinito
    while loop:
        posX -=4 #Atualiza posição canoCima em pixel
        #posY +=5 #Atualiza posição passaro
        
        tela.blit(fundo,[0,-85])# Desenha fundo posição x,y
        passaro.Atualizar(tela)
        #tela.blit(passaro,[170,posY])#Desenha passaro
        tela.blit(canoBaixo,[posX,310])#Desenha cano em baixo
        tela.blit(canoCima,[posX,-1380])#Desenha cano em cima
        tela.blit(chao,[0,510])#Desenha chão
        tela.blit(texto,[200,0])#Desenha texto
        relogio.tick(30)#Define a taxa de atualização da tela(framerate)
        pygame.display.update()#Atualiza a tela
        
        #percorra todos eventos que ocorrem no jogo
        for event in pygame.event.get():
            #Evento para quando o jogador aperta no "x" da tela: sair do jogo
            if event.type == pygame.QUIT:
                loop = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:#Verifica teclado pressionado
                if event.key == pygame.K_UP:#Verifica tecla para cima pressionada
                    passaro.Voar()
                    #posY -=80 # Atualiza posição do pássaro conforme salto

            if event.type == pygame.MOUSEBUTTONDOWN:#Verifica mouse pressionado
                passaro.Voar()
                #posY -=80

#Executa o jogo
main()
