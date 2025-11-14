# Sistema de Controle de Produção e Qualidade

Sistema em Python para controle de produção e qualidade de peças fabricadas em linha de montagem, com validação automática e gerenciamento de caixas.

## Funcionalidades

O sistema oferece as seguintes funcionalidades:

- **Adicionar peça**: Cadastra novas peças com validação automática de qualidade
- **Listar peças**: Exibe todas as peças aprovadas e reprovadas com suas propriedades e caixas
- **Remover peça**: Remove uma peça do sistema pelo ID
- **Gerar relatório**: Gera relatório consolidado com estatísticas e listagem completa
- **Listar caixas fechadas**: Exibe apenas as caixas que já foram fechadas

## Critérios de Qualidade

Uma peça é **aprovada** quando atende a todos os critérios:

- **Peso**: Entre 95g e 105g
- **Cor**: Azul ou Verde
- **Comprimento**: Entre 10cm e 20cm
- **ID**: Deve ser único (não pode estar duplicado)

Se qualquer critério não for atendido, a peça é **reprovada** e o motivo é registrado.

## Gerenciamento de Caixas

- Peças aprovadas são automaticamente armazenadas em caixas
- Cada caixa tem capacidade máxima de **10 peças**
- Quando uma caixa atinge 10 peças, ela é automaticamente fechada e uma nova caixa é iniciada
- O sistema mantém controle de caixas fechadas e caixa atual em uso

## Como Executar o Programa

### Pré-requisitos

- Python 3.6 ou superior instalado no sistema
- Terminal ou prompt de comando

### Passo a Passo

1. **Abra o terminal** (PowerShell no Windows, Terminal no Linux/Mac)

2. **Navegue até o diretório** onde o arquivo `sistema_pecas.py` está localizado:

   ```bash
   cd caminho/para/o/projeto
   ```

3. **Execute o programa** com o comando:

   ```bash
   py sistema_pecas.py
   ```

4. **O menu principal será exibido**. Digite o número da opção desejada e pressione Enter.

5. **Siga as instruções** apresentadas na tela para cada operação.

6. **Para sair**, escolha a opção 6 no menu.

## Exemplos de Entradas e Saídas

### Exemplo 1: Adicionando uma Peça Aprovada

**Entrada:**

```
=== ADICIONAR PEÇA ===
ID da peça: P001
Peso (em gramas): 100
Cor: azul
Comprimento (em cm): 15
```

**Saída:**

```
✓ Peça P001 APROVADA e adicionada à caixa atual.
```

### Exemplo 2: Adicionando uma Peça Reprovada

**Entrada:**

```
=== ADICIONAR PEÇA ===
ID da peça: P002
Peso (em gramas): 90
Cor: azul
Comprimento (em cm): 15
```

**Saída:**

```
✗ Peça P002 REPROVADA.
Motivo: Peso fora da faixa permitida (95g-105g)
```

### Exemplo 3: Adicionando Peça com ID Duplicado

**Entrada:**

```
=== ADICIONAR PEÇA ===
ID da peça: P001
Peso (em gramas): 100
Cor: verde
Comprimento (em cm): 15
```

**Saída:**

```
✗ Peça P001 REPROVADA.
Motivo: ID já existe no sistema
```

### Exemplo 4: Listagem de Peças

**Entrada (opção 2 do menu):**

```
2
```

**Saída:**

```
============================================================
LISTAGEM DE PEÇAS
============================================================

------------------------------------------------------------
PEÇAS APROVADAS
------------------------------------------------------------

📦 Caixa 1 (fechada):
  ID: P001 | Peso: 100g | Cor: azul | Comprimento: 15cm
  ID: P003 | Peso: 98g | Cor: verde | Comprimento: 12cm

📦 Caixa 2 (em uso):
  ID: P005 | Peso: 102g | Cor: azul | Comprimento: 18cm

------------------------------------------------------------
PEÇAS REPROVADAS
------------------------------------------------------------

  ID: P002 | Peso: 90g | Cor: azul | Comprimento: 15cm
  Motivo(s): Peso fora da faixa permitida (95g-105g)

  ID: P004 | Peso: 100g | Cor: vermelho | Comprimento: 15cm
  Motivo(s): Cor não permitida (aceita apenas azul ou verde)

============================================================
```

### Exemplo 5: Removendo uma Peça

**Entrada (opção 3 do menu):**

```
3
ID da peça a ser removida: P002
```

**Saída:**

```
✓ Peça P002 (REPROVADA) removida com sucesso.
```

### Exemplo 6: Gerando Relatório

**Entrada (opção 4 do menu):**

```
4
```

**Saída:**

```
============================================================
RELATÓRIO CONSOLIDADO DE PRODUÇÃO
============================================================

✓ Total de peças APROVADAS: 13

✗ Total de peças REPROVADAS: 1

📦 Quantidade de caixas utilizadas: 2
   - Caixas fechadas: 1
   - Caixa atual em uso: 3/10 peças

============================================================
LISTAGEM DE PEÇAS
============================================================

------------------------------------------------------------
PEÇAS APROVADAS
------------------------------------------------------------

📦 Caixa 1 (fechada):
  ID: P001 | Peso: 100g | Cor: azul | Comprimento: 15cm
  ID: P003 | Peso: 98g | Cor: verde | Comprimento: 12cm
  ID: P006 | Peso: 99g | Cor: azul | Comprimento: 14cm
  ID: P007 | Peso: 101g | Cor: verde | Comprimento: 16cm
  ID: P008 | Peso: 97g | Cor: azul | Comprimento: 13cm
  ID: P009 | Peso: 103g | Cor: verde | Comprimento: 17cm
  ID: P010 | Peso: 100g | Cor: azul | Comprimento: 15cm
  ID: P011 | Peso: 99g | Cor: verde | Comprimento: 11cm
  ID: P012 | Peso: 102g | Cor: azul | Comprimento: 19cm
  ID: P013 | Peso: 98g | Cor: verde | Comprimento: 12cm

📦 Caixa 2 (em uso):
  ID: P015 | Peso: 100g | Cor: azul | Comprimento: 15cm
  ID: P016 | Peso: 99g | Cor: verde | Comprimento: 14cm
  ID: P017 | Peso: 101g | Cor: azul | Comprimento: 16cm

------------------------------------------------------------
PEÇAS REPROVADAS
------------------------------------------------------------

  ID: P004 | Peso: 100g | Cor: vermelho | Comprimento: 15cm
  Motivo(s): Cor não permitida (aceita apenas azul ou verde)

============================================================
```

### Exemplo 7: Listando Caixas Fechadas

**Entrada (opção 5 do menu):**

```
5
```

**Saída:**

```
============================================================
LISTAGEM DE CAIXAS FECHADAS
============================================================

📦 Caixa 1 (fechada) - 10 peças:
  ID: P001 | Peso: 100g | Cor: azul | Comprimento: 15cm
  ID: P003 | Peso: 98g | Cor: verde | Comprimento: 12cm
  ID: P006 | Peso: 99g | Cor: azul | Comprimento: 14cm
  ID: P007 | Peso: 101g | Cor: verde | Comprimento: 16cm
  ID: P008 | Peso: 97g | Cor: azul | Comprimento: 13cm
  ID: P009 | Peso: 103g | Cor: verde | Comprimento: 17cm
  ID: P010 | Peso: 100g | Cor: azul | Comprimento: 15cm
  ID: P011 | Peso: 99g | Cor: verde | Comprimento: 11cm
  ID: P012 | Peso: 102g | Cor: azul | Comprimento: 19cm
  ID: P013 | Peso: 98g | Cor: verde | Comprimento: 12cm

============================================================
```

## Menu Principal

O sistema apresenta um menu interativo com as seguintes opções:

```
============================================================
SISTEMA DE CONTROLE DE PRODUÇÃO E QUALIDADE
============================================================
1. Adicionar peça
2. Listar peças
3. Remover peça
4. Gerar relatório
5. Listar caixas fechadas
6. Sair
============================================================
```

## Observações Importantes

- O sistema valida automaticamente todas as peças cadastradas
- IDs duplicados não são permitidos
- Peças aprovadas são automaticamente organizadas em caixas
- Caixas são fechadas automaticamente ao atingir 10 peças
- Todas as informações são armazenadas em memória durante a execução (dados não persistem após o fechamento do programa)

## Estrutura do Projeto

```
python-logica/
├── sistema_pecas.py    # Arquivo principal com todo o código do sistema
└── README.md          # Este arquivo de documentação
```
