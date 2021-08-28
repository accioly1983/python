'''Exercício 18:
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet 
(em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).'''

tamanho_download = float(input('Tamanho em MB do arquivo de download: '))
velocidade_link = float(input('Velocidade do link em Mbps: '))

print(f'Download Size: {tamanho_download} | link speed {velocidade_link} - Time: {tamanho_download/(velocidade_link/8)} segundos')