import pygame

pygame.init()
# Criamos uma janela um pouco maior para a barra
largura_janela, altura_janela = 400, 300
tela = pygame.display.set_mode((largura_janela, altura_janela))
pygame.display.set_caption('Player com Barra de Volume')

pygame.mixer.music.load('elis.mp3')
pygame.mixer.music.play()

volume = 0.5
pygame.mixer.music.set_volume(volume)

# Cores (RGB)
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERDE = (0, 255, 0)

rodando = True
while rodando:
    tela.fill(PRETO) # Limpa a tela a cada frame
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP:
                volume = min(1.0, volume + 0.1)
            elif evento.key == pygame.K_DOWN:
                volume = max(0.0, volume - 0.1)
            pygame.mixer.music.set_volume(volume)
        #Parar, pausar ou continuar

        if evento.type==pygame.KEYDOWN:    
            if evento.key ==pygame.K_p:   
                pygame.mixer.music.pause()
            elif evento.key==pygame.K_r:
                pygame.mixer.music.unpause()
            elif evento.key==pygame.K_s:
                pygame.mixer.music.stop()
                rodando=False

    # --- Lógica da Barra Visual ---
    largura_maxima = 200
    altura_barra = 20
    x_barra = (largura_janela - largura_maxima) // 2
    y_barra = 240
    
    # 1. Desenha o contorno (fundo da barra)
    pygame.draw.rect(tela, BRANCO, (x_barra, y_barra, 200, altura_barra), 2,border_radius=15 )
    
    # 2. Desenha o preenchimento (proporcional ao volume)
    largura_preenchimento = largura_maxima * volume

    pygame.draw.rect(tela, (0, 0, 255), (100, 240, largura_preenchimento, 20), border_radius=15)
    #pygame.draw.rect(tela, VERDE, (x_barra, y_barra, largura_preenchimento, altura_barra))

    pygame.display.flip() # Atualiza o que aparece na tela
    pygame.time.Clock().tick(30)

pygame.quit()