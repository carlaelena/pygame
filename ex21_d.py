import pygame

pygame.init()
largura_janela, altura_janela = 400, 300
tela = pygame.display.set_mode((largura_janela, altura_janela))
pygame.display.set_caption("Player com Capa de Álbum")

# 1. Carregar e Ajustar a Imagem de Fundo
# Substitua 'capa.jpg' pelo nome do seu arquivo de imagem
try:
    imagem_original = pygame.image.load('images.webp')
    # Ajusta a imagem para preencher toda a janela
    fundo = pygame.transform.smoothscale(imagem_original, (largura_janela, altura_janela))
except:
    # Caso não encontre a imagem, cria um fundo cinza para não dar erro
    fundo = pygame.Surface((largura_janela, altura_janela))
    fundo.fill((50, 50, 50))

# Configuração de Fontes e Áudio
fonte_principal = pygame.font.SysFont("Arial", 24, bold=True)
pygame.mixer.music.load('elis.mp3')
pygame.mixer.music.play()

volume = 0.5
pygame.mixer.music.set_volume(volume)

# Cores
BRANCO = (255, 255, 255)
VERDE = (0, 255, 127)
SOMBRA = (0, 0, 0, 150) # Cor com transparência (RGBA)

rodando = True
while rodando:
    # 2. Desenhar o Fundo
    tela.blit(fundo, (0, 0))
    
    # Opcional: Criar uma "camada escura" por cima da imagem para o texto aparecer melhor
    overlay = pygame.Surface((largura_janela, 100), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 180)) # Preto com transparência
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

    # Renderizar Textos
    texto_musica = fonte_principal.render("Elis Regina - Águas de Março", True, BRANCO)
    tela.blit(texto_musica, (largura_janela // 2 - texto_musica.get_width() // 2, 30))

    # Desenhar Barra de Volume (mais estilizada)
    x_b, y_b, larg_max = 100, 250, 200
    pygame.draw.rect(tela, (200, 200, 200), (x_b, y_b, larg_max, 10)) # Fundo da barra
    pygame.draw.rect(tela, VERDE, (x_b, y_b, int(larg_max * volume), 10)) # Volume atual

    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()