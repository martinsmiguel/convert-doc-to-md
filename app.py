import os
import re
from markdownify import markdownify as md

# Função para substituir tags de tabela por <div>
def replace_table_tags(content):
    content = re.sub(r'<table.*?>', '<div class="table">', content, flags=re.DOTALL)
    content = re.sub(r'</table>', '</div>', content, flags=re.DOTALL)
    content = re.sub(r'<tr.*?>', '<div class="row">', content, flags=re.DOTALL)
    content = re.sub(r'</tr>', '</div>', content, flags=re.DOTALL)
    content = re.sub(r'<th.*?>', '<div class="header">', content, flags=re.DOTALL)
    content = re.sub(r'</th>', '</div>', content, flags=re.DOTALL)
    content = re.sub(r'<td.*?>', '<div class="cell">', content, flags=re.DOTALL)
    content = re.sub(r'</td>', '</div>', content, flags=re.DOTALL)
    return content

# Função para converter arquivos .doc para .txt
def convert_doc_to_txt(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.doc'):
            doc_path = os.path.join(directory, filename)
            txt_path = os.path.join(directory, filename.replace('.doc', '.txt'))

            with open(doc_path, 'r', encoding='utf-8', errors='ignore') as doc_file:
                content = doc_file.read()

            with open(txt_path, 'w', encoding='utf-8') as txt_file:
                txt_file.write(content)

            print(f'Converted {filename} to {txt_path}')

# Função para converter arquivos .txt com HTML para .md
def convert_txt_to_md(directory):
    mdfiles_dir = os.path.join(directory, 'mdfiles')

    # Cria a subpasta mdfiles se não existir
    os.makedirs(mdfiles_dir, exist_ok=True)

    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            txt_path = os.path.join(directory, filename)
            md_path = os.path.join(mdfiles_dir, filename.replace('.txt', '.md'))

            with open(txt_path, 'r', encoding='utf-8', errors='ignore') as txt_file:
                content = txt_file.read()

            content = replace_table_tags(content)
            markdown_content = md(content)

            with open(md_path, 'w', encoding='utf-8') as md_file:
                md_file.write(markdown_content)

            print(f'Converted {filename} to {md_path}')

            # Apaga o arquivo .txt após a conversão
            os.remove(txt_path)
            print(f'Deleted {txt_path}')

# Função principal
def main():
    # Pergunta ao usuário se o diretório é de um dispositivo Linux/macOS ou Windows
    os_type = input("Você está usando um dispositivo Linux/macOS ou Windows? (digite 'linux' ou 'windows'): ").strip().lower()

    # Input do caminho do diretório
    directory_path = input("Cole o caminho do diretório onde os arquivos estão localizados: ").strip().strip('"')

    # Verifica o tipo de sistema operacional e ajusta o caminho, se necessário
    if os_type == 'windows':
        directory_path = directory_path.replace('/', '\\')
    elif os_type == 'linux':
        directory_path = directory_path.replace('\\', '/')
    else:
        print("Tipo de sistema operacional não reconhecido. Use 'linux' ou 'windows'.")
        return

    # Chama as funções
    convert_doc_to_txt(directory_path)
    convert_txt_to_md(directory_path)

# Executa a função principal
if __name__ == "__main__":
    main()
