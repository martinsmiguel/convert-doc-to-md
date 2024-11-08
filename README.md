# Conversor de Arquivos .doc para .md

Este script converte arquivos `.doc` para `.txt` e, em seguida, transforma esses arquivos `.txt` (contendo HTML) em arquivos `.md` (Markdown). As tags HTML de tabelas são substituídas por `<div>` com classes CSS, para uma formatação mais amigável ao Markdown.

## Pré-requisitos

Para rodar este script, você precisa:

- **Python 3** instalado.

## Instalação do Python

### Windows
1. Acesse o [site do Python](https://www.python.org/downloads/) e baixe a versão mais recente para Windows.
2. Durante a instalação, **selecione a opção "Add Python to PATH"**.
3. Verifique a instalação abrindo o **Prompt de Comando** e executando:
   ```bash
   python --version
   ```

### Linux/macOS
1. A maioria das distribuições Linux e o macOS já vêm com o Python 3 instalado. Verifique a instalação com:
   ```bash
   python3 --version
   ```
2. Se o Python 3 não estiver instalado, instale-o executando:
   - **Linux (Debian/Ubuntu):**
     ```bash
     sudo apt update
     sudo apt install python3
     ```
   - **macOS:** Instale usando o [Homebrew](https://brew.sh/):
     ```bash
     brew install python
     ```

## Configurando o Ambiente Virtual

1. No diretório onde o script `conversor.py` está localizado, crie um ambiente virtual (`venv`):
   ```bash
   python -m venv venv
   ```

   - Em algumas distribuições Linux/macOS, use `python3`:
     ```bash
     python3 -m venv venv
     ```

2. Ative o ambiente virtual:

   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```

   - **Linux/macOS:**
     ```bash
     source venv/bin/activate
     ```

3. Instale as dependências do projeto usando o arquivo `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

   > **Nota**: O `requirements.txt` deve incluir o seguinte:
   > ```txt
   > markdownify
   > ```

## Estrutura do Projeto

- Coloque os arquivos `.doc` que deseja converter em uma pasta.
- O script converterá esses arquivos para `.md` e salvará os resultados em uma subpasta `mdfiles`.

## Uso

### 1. Baixando o Script

Salve o script em um arquivo chamado `conversor.py`.

### 2. Executando o Script

#### Windows

1. Abra o **Prompt de Comando**.
2. Navegue até o diretório onde o script `conversor.py` está localizado:
   ```bash
   cd caminho\para\o\diretorio\do\script
   ```
3. Ative o ambiente virtual:
   ```bash
   venv\Scripts\activate
   ```
4. Execute o script com:
   ```bash
   python conversor.py
   ```

#### Linux/macOS

1. Abra o **Terminal**.
2. Navegue até o diretório onde o script `conversor.py` está localizado:
   ```bash
   cd /caminho/para/o/diretorio/do/script
   ```
3. Ative o ambiente virtual:
   ```bash
   source venv/bin/activate
   ```
4. Execute o script com:
   ```bash
   python3 conversor.py
   ```

### 3. Fornecendo o Caminho do Diretório

Após rodar o script:
- Informe se está rodando em **Linux/macOS** (digite `0`) ou **Windows** (digite `1`).
- Cole o caminho da pasta onde estão os arquivos `.doc` que deseja converter.

### 4. Resultado

- O script irá:
  - Converter arquivos `.doc` para `.txt`.
  - Converter arquivos `.txt` contendo HTML para `.md`, substituindo tags de tabela.
  - Salvar os arquivos `.md` em uma pasta `mdfiles` dentro do diretório especificado.
  - Excluir os arquivos `.txt` após a conversão.

## Exemplo de Uso

```
Você está usando um dispositivo Linux/macOS ou Windows? (digite '0' para Linux/macOS ou '1' para Windows): 0
Cole o caminho do diretório onde os arquivos estão localizados (Ex.: /Users/seu-usuario/Documents/sua-pasta): /Users/seu-usuario/Documents/conversao
🚀 Iniciando a conversão dos arquivos...

✅ Arquivo "exemplo.doc" convertido para "/Users/seu-usuario/Documents/conversao/exemplo.txt" com sucesso.

✅ Arquivo "exemplo.txt" convertido para Markdown: "/Users/seu-usuario/Documents/conversao/mdfiles/exemplo.md".

🗑️ Todos os arquivos .txt foram excluídos com sucesso após a conversão.

🎉 Conversão concluída!
```

## Problemas Comuns

1. **Erro de Permissão**: Se você receber um erro de permissão, execute o terminal como **Administrador** (Windows) ou com `sudo` (Linux/macOS).

2. **Pacote `markdownify` não encontrado**: Verifique se instalou as dependências corretamente com `pip install -r requirements.txt`.

3. **Diretório não encontrado**: Verifique se o caminho do diretório está correto e tente novamente.

## Desativando o Ambiente Virtual

Para sair do ambiente virtual após terminar, use:

- **Windows**:
  ```bash
  venv\Scripts\deactivate.bat
  ```

- **Linux/macOS**:
  ```bash
  deactivate
  ```

## Contribuição

Sinta-se à vontade para contribuir para melhorias no script ou em sua documentação.
