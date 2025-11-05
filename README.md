# 🏭 Desafio de Automação Digital: Gestão de Peças

![Status](https://img.shields.io/badge/Status-Concluído-brightgreen)
![Python Version](https://img.shields.io/badge/Python-3.x-blue.svg)

Este projeto é um protótipo de software em Python desenvolvido para a disciplina de **Algoritmos e Lógica de Programação** da UniFECAF.

O objetivo é simular uma solução de automação digital para uma indústria, substituindo um processo manual de inspeção de peças que gera atrasos, falhas de conferência e aumento de custo.

---

## 📚 Sumário

* [1. O Desafio](#1--o-desafio)
* [2. Lógica de Negócio e Regras de Qualidade](#2--lógica-de-negócio-e-regras-de-qualidade)
* [3. Funcionalidades do Sistema (Menu)](#3--funcionalidades-do-sistema-menu)
* [4. Como Executar o Programa](#4--como-executar-o-programa)
* [5. Exemplos de Uso](#5--exemplos-de-uso)
* [6. Tecnologias Utilizadas](#6--tecnologias-utilizadas)

---

## 1. 📝 O Desafio

A missão do projeto foi desenvolver um sistema lógico em Python capaz de gerenciar o controle de produção e qualidade de uma linha de montagem.

O sistema precisa ser capaz de:
* Receber os dados de cada peça produzida (peso, cor e comprimento).
* Avaliar automaticamente se a peça está **aprovada** ou **reprovada** com base em critérios pré-definidos.
* Armazenar peças aprovadas em caixas com capacidade limitada (10 peças).
* Fechar uma caixa ao atingir a capacidade e iniciar uma nova.
* Gerar relatórios consolidados de produção.

## 2. ⚙️ Lógica de Negócio e Regras de Qualidade

O núcleo do sistema é a sua capacidade de tomar decisões. Toda a lógica de automação se baseia nas seguintes regras:

### Critérios de Aprovação
Para uma peça ser considerada **APROVADA**, ela deve atender **SIMULTANEAMENTE** aos três critérios de qualidade:
1.  **Peso:** Deve estar entre 95g e 105g (inclusive).
2.  **Cor:** Deve ser "azul" OU "verde".
3.  **Comprimento:** Deve estar entre 10cm e 20cm (inclusive).

Se **qualquer um** desses critérios falhar, a peça é automaticamente **REPROVADA** e o sistema armazena o motivo da falha.

### Lógica de Armazenamento
* **Caixas:** Peças aprovadas são armazenadas em caixas.
* **Capacidade:** Cada caixa pode conter no máximo 10 peças aprovadas.
* **Automação:** Assim que a 10ª peça é adicionada, a caixa é considerada "fechada" e uma nova caixa vazia é iniciada para as próximas peças.

## 3. 🚀 Funcionalidades do Sistema (Menu)

O programa é controlado por um menu interativo que permite ao operador gerenciar todo o processo:

#### 1. Cadastrar nova peça
* **O que faz:** Solicita ao usuário os dados da peça (peso, cor, comprimento).
* **Lógica:** O sistema imediatamente aplica as `Regras de Qualidade`.
    * Se **aprovada**, a peça é adicionada à `caixa_atual`. O sistema verifica se essa peça encheu a caixa.
    * Se **reprovada**, a peça é adicionada à lista de `pecas_reprovadas`, registrando o motivo.
* **Feedback:** O usuário recebe uma mensagem imediata do status (Aprovada ou Reprovada + Motivo).

#### 2. Listar peças aprovadas/reprovadas
* **O que faz:** Exibe um relatório detalhado de todas as peças processadas.
* **Exibição:**
    * Mostra todas as peças **aprovadas**, organizadas por caixa (incluindo as caixas fechadas e a caixa atual).
    * Mostra todas as peças **reprovadas**, listando o motivo específico da falha para cada uma.

#### 3. Remover peça cadastrada
* **O que faz:** (Funcionalidade de gerenciamento). Esta opção foi incluída como parte do requisito do menu.
* **Nota:** No contexto do protótipo atual, a remoção é uma operação complexa (ex: remover de uma caixa fechada?). Sua implementação principal foca no fluxo de entrada.

#### 4. Listar caixas fechadas
* **O que faz:** Mostra um resumo de todas as caixas que já atingiram sua capacidade máxima (10 peças) e foram "fechadas".
* **Utilidade:** Permite ao gestor saber quantas caixas completas foram enviadas para o estoque.

#### 5. Gerar relatório final
* **O que faz:** Exibe o painel consolidado (Dashboard) da produção, atendendo aos requisitos de relatório.
* **Indicadores:**
    * **Total de peças aprovadas**.
    * **Total de peças reprovadas**.
    * **Detalhamento de Reprovações:** Um resumo de *quantas* peças falharam por *cada* motivo (ex: 5 por Peso, 2 por Cor).
    * **Quantidade de caixas utilizadas** (soma das caixas fechadas + a caixa atual em uso).

## 4. 🛠️ Como Executar o Programa

O projeto foi desenvolvido inteiramente em Python e não requer nenhuma biblioteca externa.

**Pré-requisitos:**
* Python 3.x instalado em seu sistema.

**Passo a passo para executar**:

1.  **Clone o repositório**:
    ```bash
    git clone [https://github.com/msdetrano/projeto_logica_e_algoritmos.git](https://github.com/msdetrano/projeto_logica_e_algoritmos.git)
    ```

2.  **Navegue até o diretório** do projeto:
    ```bash
    cd projeto_logica_e_algoritmos
    ```

3.  **Execute o script Python** (substitua `seu_script.py` pelo nome do seu arquivo `.py`):
    ```bash
    python seu_script.py
    ```
    *(Pode ser `python3` dependendo do seu sistema operacional)*

4.  O menu interativo será exibido no seu terminal.

## 5. 📋 Exemplos de Uso

Exemplos de entradas e saídas do sistema.

### Exemplo de Menu Principal
```
--- Sistema de Gestão de Peças (v1.0) ---
Selecione uma opção:
1. Cadastrar nova peça
2. Listar peças aprovadas/reprovadas
3. Remover peça cadastrada
4. Listar caixas fechadas
5. Gerar relatório final
0. Sair
Digite o número da opção desejada:
```

### Exemplo: Cadastrando Peças
```
Digite o número da opção desejada: 1
--- 1. Cadastrar Nova Peça ---
Digite o peso (g): 102
Digite a cor: verde
Digite o comprimento (cm): 11
Status: Peça 1 APROVADA.

Digite o número da opção desejada: 1
--- 1. Cadastrar Nova Peça ---
Digite o peso (g): 110
Digite a cor: azul
Digite o comprimento (cm): 15
Status: Peça 2 REPROVADA. Motivo: Peso fora da especificação (95g-105g)
```

### Exemplo: Gerando Relatório Final
```
Digite o número da opção desejada: 5
--- 5. Relatório Final ---
Total de peças APROVADAS: 1
Total de peças REPROVADAS: 1
Detalhamento de reprovações:
  - Peso fora da especificação (95g-105g): 1 peça(s)
Quantidade de caixas utilizadas (fechadas + 1 em uso): 1
  - Caixas fechadas: 0
  - Peças na caixa atual: 1 / 10
```

## 6. 💻 Tecnologias Utilizadas

* **[Python 3](https://www.python.org/)**: Linguagem principal utilizada para toda a lógica do programa.
* **Lógica de Programação:**
    * Funções (para modularização).
    * Estruturas Condicionais (If/Elif/Else) para validação.
    * Loops (While/For) para o menu e para iterar listas.
    * Estruturas de Dados (Listas e Dicionários) para armazenar peças e caixas.

---
*Autor: Marcos Detrano*
*Curso: Algoritmos e Lógica de Programação - UniFECAF*
