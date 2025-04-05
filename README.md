# Runner Game

Runner Game é um jogo simples desenvolvido em Python usando a biblioteca Pygame. O objetivo do jogo é evitar obstáculos enquanto o jogador corre.

## Requisitos

- Python 3.x
- Pygame

## Instalação

1. Clone o repositório para o seu computador:

    ```bash
    git clone https://github.com/seu-usuario/runner-game.git
    cd runner-game
    ```

2. Instale as dependências:

    ```bash
    pip install pygame
    ```

## Como Jogar

1. Execute o jogo:

    ```bash
    python game.py
    ```

2. Use a barra de espaço para iniciar o jogo e pular os obstáculos.

## Estrutura do Projeto

```plaintext
runner-game/
│
├── audio/
│   ├── jump.mp3
│   └── music.wav
│
├── font/
│   └── Pixeltype.ttf
│
├── images/
│   ├── fly/
│   │   ├── Fly1.png
│   │   └── Fly2.png
│   ├── player/
│   │   ├── jump.png
│   │   ├── player_stand.png
│   │   ├── player_walk_1.png
│   │   └── player_walk_2.png
│   ├── snail/
│   │   ├── snail1.png
│   │   └── snail2.png
│   ├── Sky.png
│   └── ground.png
│
├── [game.py](http://_vscodecontentref_/0)
├── [player.py](http://_vscodecontentref_/1)
├── [obstacle.py](http://_vscodecontentref_/2)
└── README.md