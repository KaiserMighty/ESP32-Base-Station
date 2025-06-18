import os
import pygame

def ring_bell():
    try:
        pygame.mixer.init()
        sound_path = os.path.join(os.path.dirname(__file__), "resources", "doorbell.wav")
        pygame.mixer.music.load(sound_path)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        print("Played doorbell sound.")

    except Exception as e:
        print(f"Failed to play sound: {e}")