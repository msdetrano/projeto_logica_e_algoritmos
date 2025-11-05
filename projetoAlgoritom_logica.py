# Lista para armazenar todas as peças reprovadas e o motivo
pecas_reprovadas = [] 

# Lista para armazenar as caixas fechadas (cada caixa será uma lista de peças)
caixas_fechadas = [] 

# Lista para armazenar as peças da caixa que está sendo preenchida no momento
caixa_atual = []

# Constante para a capacidade da caixa
CAPACIDADE_CAIXA = 10 

# Contador para garantir que cada peça tenha um ID único
proximo_id_peca = 1

# --- Funções de Lógica Principal ---

def validar_peca(peso, cor, comprimento):
    """
    Valida uma peça com base nos critérios de qualidade.
    Retorna (True, "Aprovada") se OK, ou (False, "Motivo da Reprovação") se falhar.
    """
    # Lógica de validação (Peso 95-105g, Cor azul/verde, Comprimento 10-20cm)
    # [cite: 12, 14, 15]
    
    if not (95 <= peso <= 105):
        return (False, "Peso fora da especificação (95g-105g)")
        
    if cor.lower() not in ['azul', 'verde']:
        return (False, "Cor fora da especificação (azul ou verde)")
        
    if not (10 <= comprimento <= 20):
        return (False, "Comprimento fora da especificação (10cm-20cm)")
        
    return (True, "Aprovada")

def cadastrar_peca():
    """
    Função para o item 1 do menu: Cadastrar nova peça.
    [cite: 47]
    """
    global proximo_id_peca, caixa_atual, caixas_fechadas, pecas_reprovadas
    
    print("\n--- 1. Cadastrar Nova Peça ---")
    
    # 1. Receber os dados (input do usuário) 
    try:
        # Usamos 'float' para permitir valores decimais como 95.5g
        peso = float(input("Digite o peso (g): "))
        cor = input("Digite a cor: ")
        comprimento = float(input("Digite o comprimento (cm): "))
    except ValueError:
        print("Erro: Entrada inválida. Peso e comprimento devem ser números.")
        return

    # 2. Criar um dicionário para representar a peça
    peca = {
        'id': proximo_id_peca,
        'peso': peso,
        'cor': cor,
        'comprimento': comprimento
    }

    # 3. Avaliar a peça 
    aprovada, motivo = validar_peca(peso, cor, comprimento)

    if aprovada:
        print(f"Status: Peça {peca['id']} APROVADA.")
        
        # 4. Armazenar na caixa atual 
        caixa_atual.append(peca)
        
        # 5. Verificar se a caixa atual está cheia 
        if len(caixa_atual) >= CAPACIDADE_CAIXA:
            print(f"Caixa {len(caixas_fechadas) + 1} está cheia (10 peças). Fechando e abrindo uma nova.")
            caixas_fechadas.append(caixa_atual)
            caixa_atual = [] # Inicia uma nova caixa vazia
            
    else:
        # Armazena a peça reprovada com o motivo 
        peca_rejeitada = peca.copy()
        peca_rejeitada['motivo_reprovacao'] = motivo
        pecas_reprovadas.append(peca_rejeitada)
        print(f"Status: Peça {peca['id']} REPROVADA. Motivo: {motivo}")

    # Incrementa o ID para a próxima peça
    proximo_id_peca += 1

def listar_pecas():
    """
    Função para o item 2 do menu: Listar peças aprovadas/reprovadas.
    [cite: 48]
    """
    print("\n--- 2. Listar Peças ---")

    # Lista peças aprovadas (as que estão em caixas fechadas + as da caixa atual)
    print("\n** Peças Aprovadas **")
    total_aprovadas = 0
    if not caixas_fechadas and not caixa_atual:
        print("Nenhuma peça aprovada cadastrada.")
    
    for i, caixa in enumerate(caixas_fechadas):
        print(f"  Caixa {i+1} (Fechada):")
        for peca in caixa:
            print(f"    - ID: {peca['id']} (Peso: {peca['peso']}g, Cor: {peca['cor']}, Comp: {peca['comprimento']}cm)")
            total_aprovadas += 1

    if caixa_atual:
        print(f"  Caixa {len(caixas_fechadas) + 1} (Em andamento):")
        for peca in caixa_atual:
            print(f"    - ID: {peca['id']} (Peso: {peca['peso']}g, Cor: {peca['cor']}, Comp: {peca['comprimento']}cm)")
            total_aprovadas += 1
    
    print(f"(Total Aprovadas: {total_aprovadas})")


    # Lista peças reprovadas
    print("\n** Peças Reprovadas **")
    if not pecas_reprovadas:
        print("Nenhuma peça reprovada.")
    else:
        for peca in pecas_reprovadas:
            print(f"  - ID: {peca['id']} (Motivo: {peca['motivo_reprovacao']})")
    
    print(f"(Total Reprovadas: {len(pecas_reprovadas)})")


def remover_peca():
    """
    Função para o item 3 do menu: Remover peça cadastrada.
    (Esta é uma função mais complexa, pois teríamos que decidir de onde remover 
    e como isso afeta as caixas. Vamos começar com uma implementação simples
    de "remover última reprovada" ou "remover por ID" se necessário.)
    
    """
    print("\n--- 3. Remover Peça Cadastrada ---")
    print("Funcionalidade de remoção a ser implementada.")
    print("Desafio: A peça deve ser removida de qual lista (aprovadas, reprovadas, caixas)?")
    # Por enquanto, vamos deixar como 'pass'
    pass


def listar_caixas_fechadas():
    """
    Função para o item 4 do menu: Listar caixas fechadas.
    [cite: 50]
    """
    print("\n--- 4. Listar Caixas Fechadas ---")
    
    if not caixas_fechadas:
        print("Nenhuma caixa foi fechada ainda.")
        return

    print(f"Total de caixas fechadas: {len(caixas_fechadas)}")
    for i, caixa in enumerate(caixas_fechadas):
        print(f"\nCaixa {i+1} (Contém {len(caixa)} peças):")
        for peca in caixa:
            print(f"  - ID da Peça: {peca['id']}")


def gerar_relatorio_final():
    """
    Função para o item 5 do menu: Gerar relatório final.
    [cite: 51]
    """
    print("\n--- 5. Relatório Final ---")
    
    # 1. Total de peças aprovadas 
    total_aprovadas = (len(caixas_fechadas) * CAPACIDADE_CAIXA) + len(caixa_atual)
    print(f"Total de peças APROVADAS: {total_aprovadas}")

    # 2. Total de peças reprovadas e o motivo 
    total_reprovadas = len(pecas_reprovadas)
    print(f"Total de peças REPROVADAS: {total_reprovadas}")
    
    if total_reprovadas > 0:
        # Contar os motivos
        motivos = {}
        for peca in pecas_reprovadas:
            motivo = peca['motivo_reprovacao']
            if motivo in motivos:
                motivos[motivo] += 1
            else:
                motivos[motivo] = 1
                
        print("Detalhamento de reprovações:")
        for motivo, contagem in motivos.items():
            print(f"  - {motivo}: {contagem} peça(s)")

    # 3. Quantidade de caixas utilizadas (fechadas + a atual) 
    total_caixas_utilizadas = len(caixas_fechadas)
    if caixa_atual: # Se a caixa atual tiver pelo menos 1 item, ela está em uso
        total_caixas_utilizadas += 1
        
    print(f"Quantidade de caixas utilizadas (fechadas + 1 em uso): {total_caixas_utilizadas}")
    print(f"  - Caixas fechadas: {len(caixas_fechadas)}")
    print(f"  - Peças na caixa atual: {len(caixa_atual)} / {CAPACIDADE_CAIXA}")


# --- Loop Principal (Menu Interativo) ---

def main():
    """
    Função principal que executa o menu interativo.
    """
    while True:
        print("\n--- Sistema de Gestão de Peças (v1.0) ---")
        print("Selecione uma opção:")
        print("1. Cadastrar nova peça")
        print("2. Listar peças aprovadas/reprovadas")
        print("3. Remover peça cadastrada")
        print("4. Listar caixas fechadas")
        print("5. Gerar relatório final")
        print("0. Sair")
        
        opcao = input("Digite o número da opção desejada: ")
        
        if opcao == '1':
            cadastrar_peca()
        elif opcao == '2':
            listar_pecas()
        elif opcao == '3':
            remover_peca()
        elif opcao == '4':
            listar_caixas_fechadas()
        elif opcao == '5':
            gerar_relatorio_final()
        elif opcao == '0':
            print("Saindo do sistema. Obrigado!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# --- Ponto de entrada do script ---
if __name__ == "__main__":
    main()