# Desafio de Automação Digital: Gestão de Peças, Qualidade e Armazenamento

[cite_start]Este projeto é um protótipo em Python desenvolvido para a disciplina de Algoritmos e Lógica de Programação, simulando um sistema de automação industrial. [cite: 5, 24]

[cite_start]O objetivo é automatizar o controle de produção e qualidade de peças em uma linha de montagem, substituindo o processo de inspeção manual que gera atrasos e falhas. [cite: 7, 8]

## 🎯 Funcionalidades

[cite_start]O sistema foi desenvolvido em Python e utiliza um menu interativo para gerenciar o processo.  Ele é capaz de:

* **1. [cite_start]Cadastrar nova peça:** Recebe os dados da peça (peso, cor, comprimento) [cite: 10, 47] e realiza a validação.
* **2. [cite_start]Listar peças (Aprovadas/Reprovadas):** [cite: 48] Mostra o status de todas as peças que passaram pelo sistema.
* **3. [cite_start]Remover peça cadastrada:** [cite: 49] (Funcionalidade para futura implementação).
* **4. [cite_start]Listar caixas fechadas:** [cite: 50] [cite_start]Exibe o histórico de caixas que atingiram a capacidade máxima de 10 peças. 
* **5. [cite_start]Gerar relatório final:**  [cite_start]Consolida os dados totais de produção (aprovadas, reprovadas, motivos e caixas usadas). [cite: 19, 20, 21]

### Regras de Qualidade

[cite_start]Para uma peça ser **APROVADA**, ela deve atender simultaneamente a 3 critérios: 
* **Peso:** Entre 95g e 105g 
* [cite_start]**Cor:** Azul ou Verde 
* [cite_start]**Comprimento:** Entre 10cm e 20cm 

[cite_start]Peças aprovadas são armazenadas em caixas com capacidade para 10 unidades.  [cite_start]Ao atingir o limite, a caixa é fechada e uma nova é iniciada. 

## 🚀 Como Rodar o Programa

Este projeto foi escrito em Python 3.

1.  **Clone o repositório:**
    ```bash
    git clone [URL-DO-SEU-REPOSITORIO-AQUI]
    cd [NOME-DO-SEU-DIRETORIO]
    ```

2.  **Certifique-se de ter o Python 3 instalado.** Você pode verificar com:
    ```bash
    python --version
    # ou
    python3 --version
    ```

3.  [cite_start]**Execute o script principal:** [cite: 54]
    ```bash
    python nome_do_seu_arquivo.py
    # ou
    python3 nome_do_seu_arquivo.py
    ```

## 📋 Exemplos de Entrada e Saída

[cite_start]Ao executar o programa, você verá o menu principal: [cite: 55]
