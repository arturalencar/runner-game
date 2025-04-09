# Runner Game

Runner Game é um jogo simples desenvolvido em Python usando a biblioteca Pygame. O objetivo do jogo é evitar obstáculos enquanto o jogador corre.

## Requisitos

- Python 3.x
- Pygame

## Instalação

1. Clone o repositório para o seu computador:

    ```bash
    git clone https://github.com/arturalencar/runner-game.git
    cd runner-game
    ```

2. Instale as dependências:

    ```bash
    pip install pygame
    ```

## Como Jogar

1. Execute o jogo:

    ```bash
    python main.py
    ```

2. Use a barra de espaço para pular os obstáculos.

3. O jogo possui as seguintes telas:
   - **Menu Principal**: Clique no botão "Play" para iniciar o jogo ou "Quit" para sair.
   - **Tela do Jogo**: Evite os obstáculos (Fly e Snail) enquanto corre.
   - **Tela de Game Over**: Após uma colisão, clique no botão "Retry" para reiniciar o jogo ou "Back" para voltar ao menu principal.

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
├── modules/
│   ├── __init__.py          # Torna a pasta modules um pacote Python
│   ├── game.py              # Lógica principal do jogo
│   ├── screen.py            # Classe base para telas
│   ├── screenManager.py     # Gerenciador de telas
│   ├── gameScreen.py        # Tela do jogo
│   ├── menuScreen.py        # Tela do menu principal
│   ├── gameOverScreen.py    # Tela de Game Over
│   ├── obstacle.py          # Classe base para obstáculos
│   ├── snail.py             # Classe para o obstáculo Snail
│   └── fly.py               # Classe para o obstáculo Fly
│   ├── player.py            # Classe do jogador
│
├── main.py                  # Arquivo principal para executar o jogo
└── README.md                # Documentação do projeto
```

## Funcionalidades

- **Menu Principal**:
  - Botão "Play" para iniciar o jogo.
  - Botão "Quit" para sair do jogo.

- **Tela do Jogo**:
  - O jogador pode pular obstáculos (Fly e Snail) usando a barra de espaço.
  - A pontuação é exibida no topo da tela.

- **Tela de Game Over**:
  - Exibe a pontuação final.
  - Botão "Retry" para reiniciar o jogo.
  - Botão "Quit" para sair do jogo.

## Controles

- **Barra de Espaço**: Pular obstáculos.
- **Mouse**: Navegar pelos botões nas telas de menu e Game Over.

## Créditos

- **Fontes**: Pixeltype.ttf
- **Música e Sons**:
  - `music.wav`: Música de fundo.
  - `jump.mp3`: Som do pulo.

## Licença

Este projeto é apenas para fins educacionais e não possui uma licença específica.