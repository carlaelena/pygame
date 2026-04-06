import pygame

pygame.init()
largura_janela, altura_janela = 400, 300
tela = pygame.display.set_mode((largura_janela, altura_janela))
pygame.display.set_caption("Player com Texto e Volume")

# 1. Configuração de Fontes
# O None usa a fonte padrão do sistema. 30 é o tamanho.
fonte_principal = pygame.font.SysFont("Arial", 24, bold=True)
fonte_volume = pygame.font.SysFont("Arial", 18)

pygame.mixer.music.load('elis.mp3')
pygame.mixer.music.play()

volume = 0.5
pygame.mixer.music.set_volume(volume)

# Cores
PRETO = (20, 20, 20)
BRANCO = (255, 255, 255)
VERDE = (50, 205, 50)

rodando = True
while rodando:
    tela.fill(PRETO)
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP:
                volume = min(1.0, volume + 0.05) # Passos menores (5%)
            elif evento.key == pygame.K_DOWN:
                volume = max(0.0, volume - 0.05)
            pygame.mixer.music.set_volume(volume)
          #Parar, pausar ou continuar

        if evento.type==pygame.KEYDOWN:    
            if evento.key ==pygame.K_p:   
                pygame.mixer.music.pause()
            elif evento.key==pygame.K_r:
                pygame.mixer.music.unpause()
            elif evento.key==pygame.K_s:
                pygame.mixer.music.stop()
                tocando=False
                
    # --- Renderização de Texto ---
    # render(texto, suavização_bordas, cor)
    texto_musica = fonte_principal.render("Tocando: Elis Regina", True, BRANCO)
    texto_porcentagem = fonte_volume.render(f"Volume: {int(volume * 100)}%", True, BRANCO)

    # --- Desenho na Tela ---
    # Posicionando o nome da música (Centralizado no topo)
    tela.blit(texto_musica, (largura_janela // 2 - texto_musica.get_width() // 2, 50))
    
    # Barra de Volume
    larg_max = 200
    alt_barra = 20
    x_b, y_b = 100, 150
    pygame.draw.rect(tela, BRANCO, (x_b, y_b, larg_max, alt_barra), 2)
    pygame.draw.rect(tela, VERDE, (x_b, y_b, int(larg_max * volume), alt_barra))

    # Texto da porcentagem (Logo abaixo da barra)
    tela.blit(texto_porcentagem, (x_b, y_b + 30))

    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()