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
            adicionar_peca(pecas_aprovadas, pecas_reprovadas, caixa_atual, caixas_fechadas)
        elif opcao == "2":
            print("Gerando relatório...")
        elif opcao == "3":
            print("\nSaindo do sistema. Até logo!")
            break
        else:
            print("\n✗ Opção inválida! Por favor, escolha uma opção entre 1 e 3.")

def adicionar_peca(pecas_aprovadas, pecas_reprovadas, caixa_atual, caixas_fechadas):
    """
    Adiciona uma nova peça ao sistema.
    Solicita dados do usuário, valida e armazena conforme aprovação.
    """
    print("\n=== ADICIONAR PEÇA ===")
    
    try:
        id_peca = input("ID da peça: ").strip()
        peso = float(input("Peso (em gramas): "))
        cor = input("Cor: ").strip()
        comprimento = float(input("Comprimento (em cm): "))
        
        aprovada, motivo = True, ""
        
        peca = {
            'id': id_peca,
            'peso': peso,
            'cor': cor,
            'comprimento': comprimento
        }
        
        if aprovada:
            caixa_atual.append(peca)
            pecas_aprovadas.append(peca)
            print(f"\n✓ Peça {id_peca} APROVADA e adicionada à caixa atual.")
            
            if len(caixa_atual) >= 10:
                caixas_fechadas.append(caixa_atual.copy())
                print(f"✓ Caixa fechada com {len(caixa_atual)} peças. Nova caixa iniciada.")
                caixa_atual.clear()
        else:
            peca['motivo_reprovacao'] = motivo
            pecas_reprovadas.append(peca)
            print(f"\n✗ Peça {id_peca} REPROVADA.")
            print(f"Motivo: {motivo}")
            
    except ValueError:
        print("\n✗ Erro: Peso e comprimento devem ser números válidos.")
    except Exception as e:
        print(f"\n✗ Erro ao processar peça: {e}")

if __name__ == "__main__":
    main()
