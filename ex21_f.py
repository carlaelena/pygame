import pygame

pygame.init()
largura_janela, altura_janela = 400, 380
tela = pygame.display.set_mode((largura_janela, altura_janela))
pygame.display.set_caption("Meu Player com Playlist")

# 1. Configuração da Playlist
# Certifique-se de que esses arquivos existam na sua pasta!
playlist = ['elis.mp3', 'bruno.mp3', 'melim.mp3']
indice_atual = 0

# Definir um evento para quando a música terminar
MUSICA_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(MUSICA_END)

def tocar_musica(indice):
    pygame.mixer.music.load(playlist[indice])
    pygame.mixer.music.play()

tocar_musica(indice_atual)

# 2. Configurações de Interface
volume = 0.5
pygame.mixer.music.set_volume(volume)
pausado = False
fonte_titulo = pygame.font.SysFont("Arial", 18, bold=True)
BRANCO, VERDE, VERMELHO = (255, 255, 255), (34, 177, 76), (200, 30, 30)

# Botão e Barra
botao_rect = pygame.Rect(150, 180, 100, 40)
x_barra, y_barra = 100, 260

rodando = True
while rodando:
    tela.fill((30, 30, 30)) # Fundo escuro simples para focar na lógica
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        
        # Lógica da Playlist: Se a música acabou, pula para a próxima
        if evento.type == MUSICA_END:
            indice_atual = (indice_atual + 1) % len(playlist)
            tocar_musica(indice_atual)
            print(f"Tocando agora: {playlist[indice_atual]}")

        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1 and botao_rect.collidepoint(evento.pos):
                if pausado:
                    pygame.mixer.music.unpause()
                    pausado = False
                else:
                    pygame.mixer.music.pause()
                    pausado = True

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP:
                volume = min(1.0, volume + 0.05)
            elif evento.key == pygame.K_DOWN:
                volume = max(0.0, volume - 0.05)
            pygame.mixer.music.set_volume(volume)

    # --- DESENHO ---
    # Título dinâmico (mostra qual música da lista está tocando)
    nome_exibicao = f"Tocando [{indice_atual + 1}/{len(playlist)}]: {playlist[indice_atual]}"
    txt_titulo = fonte_titulo.render(nome_exibicao, True, BRANCO)
    tela.blit(txt_titulo, (largura_janela // 2 - txt_titulo.get_width() // 2, 50))

    # Botão Play/Pause
    cor_btn = VERDE if pausado else VERMELHO
    pygame.draw.rect(tela, cor_btn, botao_rect, border_radius=5)
    txt_btn = fonte_titulo.render("PLAY" if pausado else "PAUSE", True, BRANCO)
    tela.blit(txt_btn, (botao_rect.centerx - txt_btn.get_width()//2, botao_rect.centery - txt_btn.get_height()//2))

    # Barra de Volume (abaixo do botão)
    pygame.draw.rect(tela, (100, 100, 100), (x_barra, y_barra, 200, 10))
    pygame.draw.rect(tela, (0, 255, 127), (x_barra, y_barra, int(200 * volume), 10))
    txt_vol = fonte_titulo.render(f"Volume: {int(volume*100)}%", True, BRANCO)
    tela.blit(txt_vol, (x_barra, y_barra + 20))

    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()