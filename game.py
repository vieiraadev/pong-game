import pygame
import random

pygame.init()
largura_tela = 800
altura_tela = 600
branco = (255, 255, 255)
preto = (0, 0, 0)
azul = (0, 0, 255)
vermelho = (255, 0, 0)

tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('GAME')
clock = pygame.time.Clock()
largura_raquete = 15
altura_raquete = 90
velocidade_raquete = 10
largura_bola = 15
altura_bola = 15
velocidade_bola_x = 4  
velocidade_bola_y = 4
raquete_esquerda_y = (altura_tela - altura_raquete) // 2
raquete_direita_y = (altura_tela - altura_raquete) // 2
bola_x = largura_tela // 2
bola_y = altura_tela // 2
pontuacao_esquerda = 0
pontuacao_direita = 0
pontos_vitoria = 5

def desenha_raquete(x, y, cor):
    pygame.draw.rect(tela, cor, (x, y, largura_raquete, altura_raquete))
def desenha_bola(x, y):
    pygame.draw.rect(tela, branco, (x, y, largura_bola, altura_bola))
def exibir_mensagem_vitoria(vencedor):
    fonte = pygame.font.SysFont(None, 75)
    mensagem = fonte.render(f"Jogador {vencedor} Venceu!", True, branco)
    tela.blit(mensagem, (largura_tela // 2 - mensagem.get_width() // 2, altura_tela // 2 - mensagem.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(3000)
def jogo():
    global raquete_esquerda_y, raquete_direita_y, bola_x, bola_y, velocidade_bola_x, velocidade_bola_y, pontuacao_esquerda, pontuacao_direita
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_w] and raquete_esquerda_y > 0:
            raquete_esquerda_y -= velocidade_raquete
        if teclas[pygame.K_s] and raquete_esquerda_y < altura_tela - altura_raquete:
            raquete_esquerda_y += velocidade_raquete
        if teclas[pygame.K_UP] and raquete_direita_y > 0:
            raquete_direita_y -= velocidade_raquete
        if teclas[pygame.K_DOWN] and raquete_direita_y < altura_tela - altura_raquete:
            raquete_direita_y += velocidade_raquete
        bola_x += velocidade_bola_x
        bola_y += velocidade_bola_y
        if bola_y <= 0 or bola_y >= altura_tela - altura_bola:
            velocidade_bola_y = -velocidade_bola_y
        if (bola_x <= largura_raquete and raquete_esquerda_y < bola_y < raquete_esquerda_y + altura_raquete) or \
           (bola_x >= largura_tela - largura_raquete - largura_bola and raquete_direita_y < bola_y < raquete_direita_y + altura_raquete):
            velocidade_bola_x = -velocidade_bola_x
        if bola_x <= 0:
            pontuacao_direita += 1
            bola_x = largura_tela // 2
            bola_y = altura_tela // 2
            velocidade_bola_x = random.choice([-4, 4])
            velocidade_bola_y = random.choice([-4, 4])
        elif bola_x >= largura_tela - largura_bola:
            pontuacao_esquerda += 1
            bola_x = largura_tela // 2
            bola_y = altura_tela // 2
            velocidade_bola_x = random.choice([-4, 4])
            velocidade_bola_y = random.choice([-4, 4])
        if pontuacao_esquerda == pontos_vitoria:
            exibir_mensagem_vitoria("1")
            pygame.quit()
            return
        elif pontuacao_direita == pontos_vitoria:
            exibir_mensagem_vitoria("2")
            pygame.quit()
            return
        tela.fill(preto)
        desenha_raquete(0, raquete_esquerda_y, azul)
        desenha_raquete(largura_tela - largura_raquete, raquete_direita_y, vermelho)
        desenha_bola(bola_x, bola_y)
        fonte = pygame.font.SysFont(None, 75)
        texto_pontuacao = fonte.render(f"{pontuacao_esquerda}   {pontuacao_direita}", True, branco)
        tela.blit(texto_pontuacao, (largura_tela // 2 - texto_pontuacao.get_width() // 2, 20))
        pygame.display.flip()
        clock.tick(60)

jogo()