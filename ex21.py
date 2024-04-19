# Faça um programa que abra e reproduza o áudio de um arquivo MP3

# instalar o pygame via pip install
import pygame
pygame.init()

# inserir o arquivo mp3 na mesma pasta que este exercício
pygame.mixer.music.load('STARSET PERFECT MACHINE.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()