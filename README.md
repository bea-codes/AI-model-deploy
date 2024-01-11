# Projeto: deploy de modelo treinado para classificação de imagens

## Sobre

O projeto consiste em uma aplicação web com a funcionalidade de "deployar" um modelo deep learning treinado para a classificação de imagens. O projeto possuí um arquivo `Dockerfile` para o possibilitar que o deployment seja feito em um container.
O front-end recebe uma imagem a ser classificada, o back alimenta essa imagem ao modelo `MobileNetV3` e retorna as preduções do modelo ao front.

Modelo usando os pelos do dataset `IMAGENET1K_V1`. Possuí 1000 classes para a tarefa de classificação de imagens, disponiveis no arquivo `imagenet_classes.txt`

## Tecnologias usadas

- Python
- PyTorch (biblioteca de machine learning)
- Flask (web framework)
- Docker (container)

Comando para rodar a aplicação
`python3 app.py` ou `python app.py`

Dependências:
- Flask==2.2.2
- Werkzeug==2.2.2
- torchvision
