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
    print("2. Listar peças")
    print("3. Gerar relatório")
    print("4. Sair")
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
            listar_pecas(pecas_aprovadas, pecas_reprovadas, caixas_fechadas, caixa_atual)
        elif opcao == "3":
            gerar_relatorio(pecas_aprovadas, pecas_reprovadas, caixas_fechadas, caixa_atual)
        elif opcao == "4":
            print("\nSaindo do sistema. Até logo!")
            break
        else:
            print("\n✗ Opção inválida! Por favor, escolha uma opção entre 1 e 4.")

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
        
        aprovada, motivo = validar_peca(peso, cor, comprimento)
        
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

def validar_peca(peso, cor, comprimento):
    """
    Valida uma peça de acordo com os critérios de qualidade:
    - Peso entre 95g e 105g
    - Cor azul ou verde
    - Comprimento entre 10cm e 20cm
    
    Retorna: (aprovada: bool, motivo_reprovacao: str)
    """
    motivos = []
    
    if peso < 95 or peso > 105:
        motivos.append("Peso fora da faixa permitida (95g-105g)")
    
    cor_lower = cor.lower().strip()
    if cor_lower not in ['azul', 'verde']:
        motivos.append("Cor não permitida (aceita apenas azul ou verde)")
    
    if comprimento < 10 or comprimento > 20:
        motivos.append("Comprimento fora da faixa permitida (10cm-20cm)")
    
    if motivos:
        return False, "; ".join(motivos)
    else:
        return True, ""

def listar_pecas(pecas_aprovadas, pecas_reprovadas, caixas_fechadas, caixa_atual):
    """
    Lista todas as peças aprovadas e reprovadas com suas propriedades e caixas.
    """
    print("\n" + "="*60)
    print("LISTAGEM DE PEÇAS")
    print("="*60)
    
    total_aprovadas = len(pecas_aprovadas)
    total_reprovadas = len(pecas_reprovadas)
    
    print("\n" + "-"*60)
    print("PEÇAS APROVADAS")
    print("-"*60)
    
    if total_aprovadas == 0:
        print("Nenhuma peça aprovada ainda.")
    else:
        numero_caixa = 1
        for caixa in caixas_fechadas:
            print(f"\n📦 Caixa {numero_caixa} (fechada):")
            for peca in caixa:
                print(f"  ID: {peca['id']} | Peso: {peca['peso']}g | Cor: {peca['cor']} | Comprimento: {peca['comprimento']}cm")
            numero_caixa += 1
        
        if len(caixa_atual) > 0:
            print(f"\n📦 Caixa {numero_caixa} (em uso):")
            for peca in caixa_atual:
                print(f"  ID: {peca['id']} | Peso: {peca['peso']}g | Cor: {peca['cor']} | Comprimento: {peca['comprimento']}cm")
    
    print("\n" + "-"*60)
    print("PEÇAS REPROVADAS")
    print("-"*60)
    
    if total_reprovadas == 0:
        print("Nenhuma peça reprovada.")
    else:
        for peca in pecas_reprovadas:
            print(f"\n  ID: {peca['id']} | Peso: {peca['peso']}g | Cor: {peca['cor']} | Comprimento: {peca['comprimento']}cm")
            print(f"  Motivo(s): {peca['motivo_reprovacao']}")
    
    print("\n" + "="*60)


def gerar_relatorio(pecas_aprovadas, pecas_reprovadas, caixas_fechadas, caixa_atual):
    """
    Gera relatório consolidado com estatísticas do sistema.
    """
    print("\n" + "="*60)
    print("RELATÓRIO CONSOLIDADO DE PRODUÇÃO")
    print("="*60)
    
    total_aprovadas = len(pecas_aprovadas)
    print(f"\n✓ Total de peças APROVADAS: {total_aprovadas}")
    
    total_reprovadas = len(pecas_reprovadas)
    print(f"\n✗ Total de peças REPROVADAS: {total_reprovadas}")
    
    caixas_completas = len(caixas_fechadas)
    caixa_em_uso = 1 if len(caixa_atual) > 0 else 0
    total_caixas = caixas_completas + caixa_em_uso
    
    print(f"\n📦 Quantidade de caixas utilizadas: {total_caixas}")
    print(f"   - Caixas fechadas: {caixas_completas}")
    if caixa_em_uso > 0:
        print(f"   - Caixa atual em uso: {len(caixa_atual)}/10 peças")
    
    listar_pecas(pecas_aprovadas, pecas_reprovadas, caixas_fechadas, caixa_atual)
    
if __name__ == "__main__":
    main()
