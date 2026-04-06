import pygame

pygame.init()
largura_janela, altura_janela = 400, 350
tela = pygame.display.set_mode((largura_janela, altura_janela))
pygame.display.set_caption("Player: Elis Regina")

# 1. Carregar Imagem de Fundo
try:
    imagem_original = pygame.image.load('images.webp')
    fundo = pygame.transform.smoothscale(imagem_original, (largura_janela, altura_janela))
except:
    fundo = pygame.Surface((largura_janela, altura_janela))
    fundo.fill((40, 40, 40))

# 2. Configuração de Áudio
pygame.mixer.music.load('elis.mp3')
pygame.mixer.music.play()
pausado = False
volume = 0.5
pygame.mixer.music.set_volume(volume)

# 3. Fontes e Cores
fonte_titulo = pygame.font.SysFont("Arial", 22, bold=True)
fonte_label = pygame.font.SysFont("Arial", 14, bold=True)
BRANCO = (255, 255, 255)

# --- NOVO POSICIONAMENTO ---

# BOTÃO (Fica em cima agora)
larg_botao, alt_botao = 100, 40
x_botao = (largura_janela - larg_botao) // 2
y_botao = 180 
botao_rect = pygame.Rect(x_botao, y_botao, larg_botao, alt_botao)

# BARRA DE VOLUME (Fica embaixo do botão)
larg_barra = 200
x_barra = (largura_janela - larg_barra) // 2
y_barra = 250 # 30 pixels abaixo do final do botão (180 + 40 + 30)

rodando = True
while rodando:
    tela.blit(fundo, (0, 0))
    
    # Overlay superior
    overlay = pygame.Surface((largura_janela, 70), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 180)) 
    tela.blit(overlay, (0, 0))

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP:
                volume = min(1.0, volume + 0.05)
            elif evento.key == pygame.K_DOWN:
                volume = max(0.0, volume - 0.05)
            pygame.mixer.music.set_volume(volume)

        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1 and botao_rect.collidepoint(evento.pos):
                if pausado:
                    pygame.mixer.music.unpause()
                    pausado = False
                else:
                    pygame.mixer.music.pause()
                    pausado = True

    # --- DESENHO ---
    
    # Título
    texto_musica = fonte_titulo.render("Elis Regina - Águas de Março", True, BRANCO)
    tela.blit(texto_musica, (largura_janela // 2 - texto_musica.get_width() // 2, 20))

    # 1. Desenhar o BOTÃO (Superior)
    cor_btn = (34, 177, 76) if pausado else (200, 30, 30)
    txt_btn = "PLAY" if pausado else "PAUSE"
    pygame.draw.rect(tela, cor_btn, botao_rect, border_radius=5)
    
    img_txt = fonte_label.render(txt_btn, True, BRANCO)
    tela.blit(img_txt, (botao_rect.centerx - img_txt.get_width() // 2, 
                        botao_rect.centery - img_txt.get_height() // 2))

    # 2. Desenhar a BARRA (Inferior)
    # Rótulo "Volume"
    txt_vol = fonte_label.render(f"VOLUME: {int(volume*100)}%", True, BRANCO)
    tela.blit(txt_vol, (x_barra, y_barra - 20))
    
    # Fundo e preenchimento da barra
    pygame.draw.rect(tela, (100, 100, 100), (x_barra, y_barra, larg_barra, 10))
    pygame.draw.rect(tela, (0, 255, 127), (x_barra, y_barra, int(larg_barra * volume), 10))

    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()