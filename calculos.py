#  -- CALCULO DE SALARIO MENSAL COM BASE EM DIAS TRABALHADOS --

import os
from dotenv import load_dotenv, set_key

DOTENV_FILE = 'cadastros.env'

USER_KEY = "MEU_USUARIO"
PASS_KEY = "MINHA_SENHA"

# FUNÇÕES DE CADASTRO E CARREGAMENTO DE DADOS

def salvar_credenciais():
    """Pede ao usuário e salva no arquivo .env."""
    print("--- CADASTRO ---")

    novo_usuario = input("Digite seu usuário: ")
    nova_senha = input("Digite sua senha: ")

    try :
        set_key(DOTENV_FILE, USER_KEY, novo_usuario)
        set_key(DOTENV_FILE, PASS_KEY, nova_senha)
        print("\n✔️ Dados salvo com sucesso .env!")
    except Exception as e:
        print(f"\n❌ Erro ao salvar dados: {e}")
        return False

def carregar_credenciais():
    """Carrega e exibe os dados salvos."""
    print("\n--- CARREGANDO DADOS ---")

    load_dotenv(DOTENV_FILE)

    usuario_cadastrado = os.environ.get("MEU_USUARIO")
    senha_cadastrada = os.environ.get("MINHA_SENHA")
    return usuario_cadastrado, senha_cadastrada

# FUNÇÃO DE LOGIN

def realizar_login():
    print("\n--- LOGIN ---")

    usuario_cadastrado, senha_cadastrada = carregar_credenciais()    

    if not usuario_cadastrado or not senha_cadastrada:
        print("❌ Nenhuma conta cadastrada. Por favor, cadastre-se primeiro.")
        return False

    usuario_input = input(f"Usuário: ")
    senha_input = input("Senha: ")

    if usuario_input == usuario_cadastrado and senha_input == senha_cadastrada:
        print("\n✔️ Login bem-sucedido!")
        return True
    else:
        print("\n❌ Usuário ou senha incorretos.")
        return False

# ENTRADA DE VALORES

def calcular_salario():

    print("-" * 30)

    while True:
        try:
            valor_s = float(input("Digite o valor do salario: R$"))
            valor_d = float(input("Digite o valor de dias trabalhados: "))
            if valor_s <= 0 and valor_d <= 0:
                print("VAGABUNDO!")
                continue
            elif valor_s <= 0:
                print("Papo de bola de ferro no pé!")
                print("-" * 30)
                continue
            elif valor_d <= 0:
                print("Essa empresa não te paga pra ficar em casa não né?")
                print("-" * 30)
                continue
        except ValueError:
            print(" E R R O !: Por favor, insira um valor numérico válido. (Lembre-se de usar '.' para decimais)")
            continue
        else:
            break
    
    dias_trabalhados = valor_s / 30 * valor_d

    print("-" * 30)

    calculo = dias_trabalhados

    print("-" * 30)
    print(f"Salario: R$ {valor_s:.2f}")
    print(f"Dias : {valor_d:.2f}")
    print("-" * 30)
    print("Salario completo: R$ {calulo:.2f}".format(calulo=calculo))
    print("Valor por dia: R$ {}".format(valor_s / 30))
    print("-" * 30)

# FUNÇÃO PRINCIPAL

def main():
    while True:
        print("\n" + "=" * 40)
        print("   CALCULADORA DE SALÁRIO PROPORCIONAL")
        print("=" * 40)
        print("1. Cadastrar Credenciais")
        print("2. Fazer Login e Calcular Salário")
        print("3. Sair")
        print("-" * 40)
        
        escolha = input("Selecione uma opção (1, 2 ou 3): ")
        
        if escolha == '1':
            salvar_credenciais()
        
        elif escolha == '2':
            # 1. Tentar carregar as credenciais para ver se existe cadastro
            usuario_cadastrado, _ = carregar_credenciais()
            
            if not usuario_cadastrado:
                print("\n⚠️ Você precisa primeiro Cadastrar as credenciais (Opção 1).")
                continue
                
            # 2. Realizar o login
            if realizar_login():
                # 3. Se o login for bem-sucedido, executa o cálculo
                calcular_salario()
            
        elif escolha == '3':
            print("\n👋 Saindo do programa. Até mais!")
            break
            
        else:
            print("\n❌ Opção inválida. Tente novamente.")

# Chamada da função principal para iniciar o programa
if __name__ == "__main__":
    main()