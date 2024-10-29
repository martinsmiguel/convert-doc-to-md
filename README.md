# Conversor de Arquivos DOC para Markdown

Este script Python converte arquivos `.doc` para `.txt`, substitui tags de tabela HTML por `<div>`, e depois converte o conteúdo para arquivos Markdown (`.md`). Os arquivos `.txt` são excluídos após a conversão, e os arquivos Markdown gerados são movidos para uma subpasta chamada `mdfiles`.

## Funcionalidades

- Converte arquivos `.doc` para `.txt`.
- Substitui as tags de tabela HTML por `<div>`.
- Converte o conteúdo de HTML para Markdown.
- Exclui os arquivos `.txt` após a conversão.
- Armazena os arquivos Markdown gerados em uma subpasta `mdfiles`.

## Pré-requisitos

Certifique-se de ter o Python 3 instalado em sua máquina. Além disso, você precisará instalar a biblioteca `markdownify` para a conversão de HTML para Markdown.

### Instalação da Biblioteca

Para instalar a biblioteca necessária, execute o seguinte comando:

```bash
pip install markdownify
```