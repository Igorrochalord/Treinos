#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import time
import webbrowser
import platform
import subprocess
import shlex

def limpar_tela():
    """Limpa a tela dependendo do Sistema Operacional"""
    sistema = platform.system()
    if sistema == "Windows":
        os.system('cls')
    else:
        # Mac e Linux usam 'clear'
        os.system('clear')

def estilo_digitar(texto, velocidade=0.03):
    """Efeito de digitação para o texto ficar estilo hacker/rpg"""
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(velocidade)
    print()

def tocar_musica():
    """Abre uma playlist de Lofi para codar no navegador padrão"""
    # Link atualizado conforme solicitado
    url_musica = "https://www.youtube.com/watch?v=pFS4zYWxzNA&list=RDpFS4zYWxzNA&start_radio=1"
    
    print("\n🎵 Preparando o ambiente de treino...")
    estilo_digitar("🎧 Abrindo sua trilha sonora de foco...", 0.05)
    time.sleep(1)
    # O webbrowser detecta automaticamente o navegador padrão do sistema
    webbrowser.open(url_musica)

def banner_principal():
    # Códigos de cor ANSI funcionam nativamente no Terminal do Mac e Linux
    vermelho = "\033[91m"
    verde = "\033[92m"
    azul = "\033[94m"
    reset = "\033[0m"
    
    print(f"{verde}")
    print(r"""
  _____           _                   _   _   _  
 |_   _| __ ___  (_)_ __   ___  ___  | \ | | | | 
   | || '__/ _ \ | | '_ \ / _ \/ __| |  \| | | | 
   | || | |  __/ | | | | | (_) \__ \ | |\  | |_| 
   |_||_|  \___| |_|_| |_|\___/|___/ |_| \_| (_) 
    """)
    print(f"{reset}")
    print(f"{azul}Bem-vindo ao Centro de Treinamento Python do Igao!{reset}")
    print("-" * 50)

def menu():
    while True:
        limpar_tela()
        banner_principal()
        
        print("\nEscolha o seu nível de desafio:")
        print("1. 🐣 Iniciante     (Lógica básica, Laços, Listas)")
        print("2. 🦁 Intermediário (Funções, Módulos, Arquivos)")
        print("3. 🐉 Avançado      (Classes, APIs, Automação)")
        print("4. 🤝 Como Contribuir (Pull Request)")
        print("0. ❌ Sair")
        
        opcao = input("\nDigite o número da opção: ")

        if opcao == '1':
            print("\n>>> Carregando treinos de nível INICIANTE...")
            estilo_digitar("Dica: Comece pelos exercícios de variáveis e input.")
            input("\nPressione Enter para voltar ao menu...")
            
        elif opcao == '2':
            print("\n>>> Carregando treinos de nível INTERMEDIÁRIO...")
            estilo_digitar("Dica: O foco agora é organizar seu código em funções.")
            input("\nPressione Enter para voltar ao menu...")
            
        elif opcao == '3':
            print("\n>>> Carregando treinos de nível AVANÇADO...")
            estilo_digitar("Dica: Prepare-se para Orientação a Objetos!")
            input("\nPressione Enter para voltar ao menu...")
            
        elif opcao == '4':
            print("\n>>> GUIA DE CONTRIBUIÇÃO")
            print("1. Faça um Fork deste repositório.")
            print("2. Crie sua branch (git checkout -b feature/novo-treino).")
            print("3. Commit suas mudanças.")
            print("4. Abra um Pull Request.")
            input("\nPressione Enter para voltar ao menu...")

        elif opcao == '0':
            estilo_digitar("Saindo... Bom treino! 🚀")
            break
        else:
            print("Opção inválida!")
            time.sleep(1)

def main():
    limpar_tela()
    banner_principal()
    
    # Input tratamento de string para evitar erros de caixa alta/baixa
    som = input("Deseja ativar o modo música de foco? (S/N): ").strip().upper()
    if som == 'S':
        tocar_musica()
    
    estilo_digitar("\nIniciando sistema de treino...", 0.05)
    time.sleep(1)
    menu()

if __name__ == "__main__":
    # If user passed --new-window, open a new terminal window and run this script there
    def _open_in_new_terminal():
        cwd = os.path.dirname(os.path.abspath(__file__))
        script = os.path.basename(__file__)
        sistema = platform.system()
        # Build platform-specific commands
        if sistema == 'Darwin':
            # macOS Terminal.app
            apple_cmd = f'tell application "Terminal" to do script "cd {shlex.quote(cwd)} && python3 {shlex.quote(script)}"'
            return subprocess.run(['osascript', '-e', apple_cmd])
        elif sistema == 'Linux':
            # Try common terminals: gnome-terminal, x-terminal-emulator, xterm
            cmd = f'cd {shlex.quote(cwd)} && python3 {shlex.quote(script)}; exec $SHELL'
            # prefer gnome-terminal
            for term_cmd in (['gnome-terminal', '--', 'bash', '-lc', cmd],
                             ['x-terminal-emulator', '-e', f"bash -lc '{cmd}'"],
                             ['xterm', '-e', cmd]):
                try:
                    return subprocess.Popen(term_cmd)
                except FileNotFoundError:
                    continue
            # fallback: spawn in background
            return subprocess.Popen(['bash', '-lc', cmd])
        elif sistema == 'Windows':
            # Windows cmd.exe (start keeps window open)
            win_cmd = f'start cmd /k "cd /d {cwd} && python {script}"'
            return subprocess.run(win_cmd, shell=True)
        else:
            raise RuntimeError(f'Unsupported OS: {sistema}')

    if '--new-window' in sys.argv:
        _open_in_new_terminal()
        sys.exit(0)

    main()