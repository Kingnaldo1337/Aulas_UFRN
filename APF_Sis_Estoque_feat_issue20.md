# 📊 Análise de Pontos de Função (APF)

A Análise de Pontos de Função (APF) permite medir o tamanho funcional do sistema, considerando as funcionalidades implementadas na branch `feat/issue20` do projeto Sis Estoque.

## 🔍 Visão Geral do Sistema

O Sis Estoque é um sistema de gerenciamento de estoques, desenvolvido com:

- **Backend**: NestJS (TypeScript)
- **Frontend**: Angular (TypeScript)

A estrutura do repositório indica uma separação clara entre o frontend e o backend, com pastas dedicadas para cada um.

## 📁 Contagem Indicativa

Na contagem indicativa, consideramos apenas as Funções de Dados:

- **ALI (Arquivo Lógico Interno)**: 35 PF cada
- **AIE (Arquivo de Interface Externa)**: 15 PF cada

### Modelo de Dados

```mermaid
erDiagram
    Produto {
        int id
        string nome
        string descricao
        int quantidade
        float preco
    }
    Categoria {
        int id
        string nome
    }
    Fornecedor {
        int id
        string nome
        string contato
    }
    Produto }o--|| Categoria : pertence_a
    Produto }o--|| Fornecedor : fornecido_por
```

### Tabela de Contagem Indicativa

| Função de Dado  | Entidades Relacionadas       | Tamanho em PF |
|-----------------|------------------------------|---------------|
| ALI Produto     | Produto, Categoria, Fornecedor | 35 PF        |
| AIE Categoria   | Categoria                    | 15 PF         |
| AIE Fornecedor  | Fornecedor                   | 15 PF         |
| **Total**       |                              | **65 PF**     |

## 📋 Contagem Detalhada

A contagem detalhada considera as Funções de Dados e as Funções de Transação:

- **ALI (Arquivo Lógico Interno)**
- **AIE (Arquivo de Interface Externa)**
- **EE (Entrada Externa)**
- **CE (Consulta Externa)**
- **SE (Saída Externa)**

### Tabela de Contagem Detalhada

| Descrição            | Tipo | ALR | DER | Complexidade | Tamanho em PF |
|----------------------|------|-----|-----|--------------|---------------|
| ALI Produto          | ALI  | 3   | 5   | Média        | 7 PF          |
| AIE Categoria        | AIE  | 1   | 2   | Baixa        | 5 PF          |
| AIE Fornecedor       | AIE  | 1   | 2   | Baixa        | 5 PF          |
| Inserir Produto      | EE   | 3   | 4   | Média        | 4 PF          |
| Atualizar Produto    | EE   | 3   | 4   | Média        | 4 PF          |
| Consultar Produto    | CE   | 3   | 4   | Média        | 4 PF          |
| Detalhar Produto     | CE   | 3   | 4   | Média        | 4 PF          |
| Inserir Categoria    | EE   | 1   | 2   | Baixa        | 3 PF          |
| Atualizar Categoria  | EE   | 1   | 2   | Baixa        | 3 PF          |
| Consultar Categoria  | CE   | 1   | 2   | Baixa        | 3 PF          |
| Inserir Fornecedor   | EE   | 1   | 2   | Baixa        | 3 PF          |
| Atualizar Fornecedor | EE   | 1   | 2   | Baixa        | 3 PF          |
| Consultar Fornecedor | CE   | 1   | 2   | Baixa        | 3 PF          |
| **Total**            |      |     |     |              | **56 PF**     |

---

**Observações**:

- As estimativas de ALR (Arquivos Lógicos Referenciados) e DER (Dados Elementares Referenciados) foram feitas com base nas entidades e relacionamentos identificados no modelo de dados.
- A complexidade foi determinada conforme as diretrizes da APF, considerando a quantidade de ALR e DER.