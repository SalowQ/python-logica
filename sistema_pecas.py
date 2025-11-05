"""
Sistema de Controle de Produção e Qualidade
Aplicação Python para controle de produção de peças com validação automática
"""

def exibir_menu():
    """
    Exibe o menu principal do sistema.
    """
    print("\n" + "="*60)
    print("SISTEMA DE CONTROLE DE PRODUÇÃO E QUALIDADE")
    print("="*60)
    print("1. Adicionar peça")
    print("2. Gerar relatório")
    print("3. Sair")
    print("="*60)


def main():
    """
    Função principal do sistema.
    Gerencia o loop do menu e as operações.
    """
    pecas_aprovadas = []
    pecas_reprovadas = []
    caixa_atual = []
    caixas_fechadas = []
    
    print("Bem-vindo ao Sistema de Controle de Produção e Qualidade!")
    
    while True:
        exibir_menu()
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == "1":
            print("Adicionando peça...")
        elif opcao == "2":
            print("Gerando relatório...")
        elif opcao == "3":
            print("\nSaindo do sistema. Até logo!")
            break
        else:
            print("\n✗ Opção inválida! Por favor, escolha uma opção entre 1 e 3.")


if __name__ == "__main__":
    main()
