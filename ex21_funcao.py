import pygame

# --- CONFIGURAÇÕES TÉCNICAS ---
pygame.init()
LARGURA, ALTURA = 400, 300
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Player Pro - Elis Regina")
relogio = pygame.time.Clock()

# Cores
PRETO = (20, 20, 20)
BRANCO = (255, 255, 255)
VERDE  = (0, 255, 127)
CINZA  = (100, 100, 100)

# --- FUNÇÕES DE LÓGICA ---

def inicializar_musica(arquivo):
    """Carrega e inicia a música."""
    pygame.mixer.music.load(arquivo)
    pygame.mixer.music.play()

def ajustar_volume(valor_atual, alteracao):
    """Calcula o novo volume respeitando os limites de 0.0 e 1.0."""
    novo_vol = valor_atual + alteracao
    return max(0.0, min(1.0, novo_vol))

# --- FUNÇÕES DE DESENHO ---

def desenhar_interface(vol):
    """Desenha todos os elementos visuais na tela."""
    tela.fill(PRETO)
    
    # 1. Título
    fonte = pygame.font.SysFont("Arial", 20, bold=True)
    texto = fonte.render("Tocando: Elis Regina", True, BRANCO)
    tela.blit(texto, (LARGURA // 2 - texto.get_width() // 2, 50))
    
    # 2. Barra de Volume (Fundo)
    larg_barra, alt_barra = 200, 15
    x_b, y_b = (LARGURA - larg_barra) // 2, 150
    pygame.draw.rect(tela, CINZA, (x_b, y_b, larg_barra, alt_barra), border_radius=5)
    
    # 3. Preenchimento da Barra (Proporcional ao volume)
    larg_preenchimento = int(larg_barra * vol)
    pygame.draw.rect(tela, VERDE, (x_b, y_b, larg_preenchimento, alt_barra), border_radius=5)
    
    # 4. Texto de Porcentagem
    fonte_vol = pygame.font.SysFont("Arial", 16)
    txt_vol = fonte_vol.render(f"Volume: {int(vol * 100)}%", True, BRANCO)
    tela.blit(txt_vol, (x_b, y_b + 25))

# --- LOOP PRINCIPAL ---

def main():
    volume = 0.5
    inicializar_musica('elis.mp3')
    pygame.mixer.music.set_volume(volume)
    
    executando = True
    while executando:
        # 1. Gerenciamento de Eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                executando = False
            
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    volume = ajustar_volume(volume, 0.05)
                elif evento.key == pygame.K_DOWN:
                    volume = ajustar_volume(volume, -0.05)
                elif evento.key == pygame.K_p:
                    pygame.mixer.music.pause()
                elif evento.key == pygame.K_r:
                    pygame.mixer.music.unpause()
                elif evento.key == pygame.K_s:
                    pygame.mixer.music.stop()
                    executando = False
                
                pygame.mixer.music.set_volume(volume)

        # 2. Desenho
        desenhar_interface(volume)
        
        # 3. Atualização da Tela
        pygame.display.flip()
        relogio.tick(30)

    pygame.quit()

# Iniciar o programa
if __name__ == "__main__":
    main()