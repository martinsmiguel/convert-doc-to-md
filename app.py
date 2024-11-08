import os
import re
from markdownify import markdownify as md

def replace_table_tags(content):
    """
    Substitui tags de tabela (<table>, <tr>, <th>, <td>) por <div> com classes específicas.

    Args:
        content (str): Conteúdo HTML com tags de tabela.

    Returns:
        str: Conteúdo com as tags de tabela substituídas por <div> e classes CSS.
    """
    content = re.sub(r'<table.*?>', '<div class="table">', content, flags=re.DOTALL)
    content = re.sub(r'</table>', '</div>', content, flags=re.DOTALL)
    content = re.sub(r'<tr.*?>', '<div class="row">', content, flags=re.DOTALL)
    content = re.sub(r'</tr>', '</div>', content, flags=re.DOTALL)
    content = re.sub(r'<th.*?>', '<div class="header">', content, flags=re.DOTALL)
    content = re.sub(r'</th>', '</div>', content, flags=re.DOTALL)
    content = re.sub(r'<td.*?>', '<div class="cell">', content, flags=re.DOTALL)
    content = re.sub(r'</td>', '</div>', content, flags=re.DOTALL)
    return content

def convert_doc_to_txt(directory):
    """
    Converte arquivos .doc para .txt em um diretório especificado.

    Args:
        directory (str): Caminho do diretório contendo os arquivos .doc.
    """
    for filename in os.listdir(directory):
        if filename.endswith('.doc'):
            doc_path = os.path.join(directory, filename)
            txt_path = os.path.join(directory, filename.replace('.doc', '.txt'))

            try:
                with open(doc_path, 'r', encoding='utf-8', errors='ignore') as doc_file:
                    content = doc_file.read()

                with open(txt_path, 'w', encoding='utf-8') as txt_file:
                    txt_file.write(content)

                print(f'✅ Arquivo "{filename}" convertido para "{txt_path}" com sucesso.\n')
            except Exception as e:
                print(f'❌ Erro ao converter "{filename}": {e}\n')

def convert_txt_to_md(directory):
    """
    Converte arquivos .txt com HTML para .md, substitui tags de tabela por <div> e apaga os arquivos .txt após a conversão.

    Args:
        directory (str): Caminho do diretório contendo os arquivos .txt.
    """
    mdfiles_dir = os.path.join(directory, 'mdfiles')
    os.makedirs(mdfiles_dir, exist_ok=True)
    errors_occurred = False

    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            txt_path = os.path.join(directory, filename)
            md_path = os.path.join(mdfiles_dir, filename.replace('.txt', '.md'))

            try:
                with open(txt_path, 'r', encoding='utf-8', errors='ignore') as txt_file:
                    content = txt_file.read()

                content = replace_table_tags(content)
                markdown_content = md(content)

                with open(md_path, 'w', encoding='utf-8') as md_file:
                    md_file.write(markdown_content)

                print(f'✅ Arquivo "{filename}" convertido para Markdown: "{md_path}".\n')

                os.remove(txt_path)
            except Exception as e:
                print(f'❌ Erro ao converter "{filename}": {e}\n')
                errors_occurred = True

    if errors_occurred:
        print("❌ Alguns arquivos .txt não puderam ser excluídos após a conversão.\n")
    else:
        print("🗑️ Todos os arquivos .txt foram excluídos com sucesso após a conversão.\n")

def main():
    """
    Função principal para gerenciar a conversão de arquivos .doc para .txt e .txt para .md.
    """
    os_type = input("Você está usando um dispositivo Linux/macOS ou Windows? (digite '0' para Linux/macOS ou '1' para Windows): ").strip()

    if os_type == '1':
        directory_path = input(r"Cole o caminho do diretório onde os arquivos estão localizados (Ex.: C:\\Users\\<nome-do-usuario>\\Documents\\<pasta-com-arquivos>): ").strip().strip('"')
        directory_path = directory_path.replace('/', '\\')
    elif os_type == '0':
        directory_path = input(r"Cole o caminho do diretório onde os arquivos estão localizados (Ex.: /Users/<nome-do-usuario>/Documents/<pasta-com-arquivos>): ").strip().strip('"')
        directory_path = directory_path.replace('\\', '/')
    else:
        print("❌ Tipo de sistema operacional não reconhecido. Use '0' para Linux/macOS ou '1' para Windows.\n")
        return

    if not os.path.isdir(directory_path):
        print(f'❌ Diretório "{directory_path}" não encontrado. Verifique o caminho e tente novamente.\n')
        return

    print("🚀 Iniciando a conversão dos arquivos...\n")
    convert_doc_to_txt(directory_path)
    convert_txt_to_md(directory_path)
    print("🎉 Conversão concluída!\n")

if __name__ == "__main__":
    main()
