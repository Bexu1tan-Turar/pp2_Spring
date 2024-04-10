import pygame
import os

pygame.init()

RES = WIDTH, HEIGHT = 360, 240
screen = pygame.display.set_mode(RES)
pygame.display.set_caption("Music Player")

music_dir = "music"
music_files = [file for file in os.listdir(music_dir) if file.endswith(".mp3")]
current_track = 0

pygame.mixer.music.load(os.path.join(music_dir, music_files[current_track]))

def play_music():
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def next_track():
    global current_track
    current_track = (current_track + 1) % len(music_files)
    pygame.mixer.music.load(os.path.join(music_dir, music_files[current_track]))
    play_music()

def previous_track():
    global current_track
    current_track= (current_track - 1) % len(music_files)
    pygame.mixer.music.load(os.path.join(music_dir, music_files[current_track]))
    play_music()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    stop_music()
                else:
                    play_music()
            elif event.key == pygame.K_UP:
                next_track()
            elif event.key == pygame.K_DOWN:
                previous_track()
    pygame.display.update()
pygame.quit()