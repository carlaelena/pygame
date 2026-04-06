import pygame
pygame.init()
pygame.display.set_mode((200,100))
pygame.mixer.music.load('elis.mp3')
pygame.mixer.music.play()


volume = 0.5
pygame.mixer.music.set_volume(volume)
print(f"Volume Atual: {int(volume * 100)}%")
print("Comandos: [Seta Cima] Aumentar | [Seta Baixo] Diminuir | [S] Sair")

print("Comandos: [P] Pausar | [R] Retomar | [S] Sair")
tocando=True
while tocando:
    for evento in pygame.event.get():
        if evento.type== pygame.QUIT:
            tocando=False

        #Teclas p/ Volume, pausar, retomar ou sair
        if evento.type == pygame.KEYDOWN:
            # Aumentar Volume
            if evento.key == pygame.K_UP:
                volume = min(1.0, volume + 0.1) # Aumenta 10%, limite max 1.0
                pygame.mixer.music.set_volume(volume)
                print(f"Volume: {int(volume * 100)}%")
                
            # Diminuir Volume
            elif evento.key == pygame.K_DOWN:
                volume = max(0.0, volume - 0.1) # Diminui 10%, limite min 0.0
                pygame.mixer.music.set_volume(volume)
                print(f"Volume: {int(volume * 100)}%") 
 
            elif evento.key ==pygame.K_p:   
                pygame.mixer.music.pause()
            elif evento.key==pygame.K_r:
                pygame.mixer.music.unpause()
            elif evento.key==pygame.K_s:
                pygame.mixer.music.stop()
                tocando=False
    pygame.time.Clock().tick(30)

pygame.quit()    
