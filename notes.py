import sys  # importa o modulo sys
import json  # importa o modulo json
import os  # importa o modulo os
import subprocess  # importa o modulo subprocess
import shutil

base_dir = os.environ.get('APPDATA') if os.name == 'nt' else os.path.expanduser('~/.config') # detecta a pasta base de usuario de forma genérica
PASTA_DADOS = os.path.join(base_dir, 'notesCLI') # define a pasta de dados
ARQUIVO_JSON = os.path.join(PASTA_DADOS, 'notas.json') #define o caminho absoluto

def exibir_rodape(): # rodapé com informações
    print("\n © 2026 Desenvolvido por Geovani Rodrigues | notesCLI v0.1.4 \n ")

def abrir_editor(caminho):
    editores = ['vim', 'nano', 'notepad'] #lista de editores por prioridade
    editor_escolhido = None #inicializa a variavel como vazia

    for editor in editores: # inicia um loop para verificar os editores
        if shutil.which(editor): # verifica se o executavel do editor existe no PATH do sistema
            editor_escolhido = editor # se achar algum editor defini como escolhido
            break # interrompe o loop

    exibir_rodape() # exibe o rodapé

    if not editor_escolhido: # se não achar nenhum editor
        print("Erro: Nenhum editor encontrado.") #mensagem de erro
        sys.exit(1) # fecha o programa

    subprocess.run([editor_escolhido, caminho], check=True) #executa o editor

def main(): # funcao principal para o pacote pip
    if not os.path.exists(PASTA_DADOS): # se a pasta de dados nao existir
        os.makedirs(PASTA_DADOS) # cria a pasta de dados

    if len(sys.argv) < 2: # verifica se o numero de argumentos é menor que 2
        print("Uso correto: n [add <nome> | list | delete <id> | <nome_nota>]") # exibe msg caso seja
        sys.exit(1) # fecha o programa

    comando = sys.argv[1] # pega o segundo item digitado, o comando
    print(f" Comando recebido: {comando}")

    try:
        with open(ARQUIVO_JSON, 'r', encoding='utf-8') as arquivo: # abre o arquivo notas.json em modo leitura
            notas = json.load(arquivo) # carrega o arquivo json em notas
    except (FileNotFoundError, json.JSONDecodeError): # caso o arquivo nao exista ou o arquivo nao for json
        notas = [] # cria um array vazio

    # ============ COMANDO LIST
    if comando == 'list': # se o comando for list
        if not notas: # se o array notas estiver vazio
            print("Nenhuma nota encontrada.")
        else:
            print("\n ---MINHAS NOTAS---") # exibe o titulo na tela
            for nota in notas: # percorre o array notas
                print(f"ID: {nota['id']} | Nome: {nota['nome']}")
                print("-" * 20)
        exibir_rodape() #exibe o rodapé
        sys.exit() # fecha o programa

    # ======== COMANDO DELETE
    if comando == 'delete': # se o comando for delete
        if len(sys.argv) < 3:
            print("Uso correto: n delete <id>") # mensagem de instrução caso o numero de argumentos for menor que 3
            sys.exit(1)

        id_apagar = int(sys.argv[2]) # pega o terceiro item digitado
        notas_filtradas = [nota for nota in notas if nota['id'] != id_apagar] # filtra o array notas

        if len(notas_filtradas) == len(notas): # se o tamanho do array não mudou (nada foi apagado)
            print("Nenhuma nota encontrada com o ID fornecido.") # exibe msg
        else:
            with open(ARQUIVO_JSON, 'w', encoding='utf-8') as arquivo: # abre o arquivo notas.json em modo escrita
                json.dump(notas_filtradas, arquivo, ensure_ascii=False, indent=4) # salva o array notas_filtradas no arquivo notas.json
            print(f"Nota com o ID {id_apagar} removida com sucesso!") # mensagem de sucesso
        exibir_rodape()
        sys.exit()

    # =========== COMANDO ADD
    if comando == 'add': # se o comando for add
        if len(sys.argv) < 3: # se o numero de argumentos for menor que 3
            print("Uso correto: n add <nome_da_nota> [texto_opcional]")
            sys.exit(1)

        nome_nota = sys.argv[2] # pega o terceiro item digitado
        caminho_txt = os.path.join(PASTA_DADOS, f"{nome_nota}.txt") # define caminho dentro da pasta de dados

        nova_nota = { # cria um novo dicionario
            "id": len(notas) + 1, # verifica o tamanho do array notas e adiciona 1 para o proximo id
            "nome": nome_nota
        }

        notas.append(nova_nota) #adiciona o dicionario nova_nota ao array notas

        with open(ARQUIVO_JSON, 'w', encoding='utf-8') as arquivo: # abre o notas.json em modo escrita
            json.dump(notas, arquivo, ensure_ascii=False, indent=4) # salva o array notas no arquivo notas.json

        print(f"A nota '{nome_nota}' foi registrada no notasCLI!") # exibe msg de sucesso

        if not os.path.exists(caminho_txt): # se o arquivo não existir, cria um novo com um título dentro
            with open(caminho_txt, 'w', encoding='utf-8') as f:
                f.write(f"--- {nome_nota.upper()} ---\n\n")

        abrir_editor(caminho_txt) # abre o arquivo no vim
        sys.exit() # fecha o programa

    # =========== COMANDO PARA ABRIR PELO NOME
    caminho_txt = os.path.join(PASTA_DADOS, f"{comando}.txt") # define caminho dentro da pasta de dados

    if os.path.exists(caminho_txt):
        abrir_editor(caminho_txt)
    else:
        print(f"Nota '{comando}' não encontrada.")
        sys.exit(1) # fecha o programa

if __name__ == '__main__': #verifica se o script esta sendo executado diretamente
    main() # chama a funcao principal