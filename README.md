# 📊 Sistema Web de Auditoria de Erros FP&A
# Com interatividade do usuário

Este é um sistema web interativo desenvolvido para automatizar a identificação de inconsistências em lançamentos financeiros. O projeto transforma dados brutos extraídos do ERP em relatórios auditados e prontos para tomada de decisão em FP&A.

A aplicação foi migrada de um script de terminal para uma interface visual moderna utilizando **Python**, **Pandas** e **Streamlit**.

## 🚀 Funcionalidades e Impacto no Negócio

*   📂 **Upload Dinâmico (Drag & Drop):** Permite o carregamento de arquivos CSV de qualquer período de forma simples.
*   🧹 **Saneamento de Strings em Massa:** Padronização automatizada de colunas críticas (`Centro_Custo` e `Descricao`), eliminando erros comuns de digitação de usuários e ERPs (como espaços em branco extras e letras maiúsculas/minúsculas misturadas).
*   📉 **Visão Gerencial (KPI Cards):** Destaque financeiro instantâneo com o valor total consolidado de despesas estratégicas (Ex: TI Infraestrutura).
*   🔄 **Tabela Dinâmica Automatizada:** Agrupamento e soma instantânea das despesas por Centro de Custo, eliminando o trabalho manual no Excel.
*   🔍 **Auditoria por Busca Parcial:** Filtro avançado que varre as descrições contábeis buscando palavras-chave específicas (Ex: "licença") para capturar despesas ocultas.
*   📥 **Exportação Direta:** Geração de arquivo Excel (.xlsx) estruturado direto na memória RAM e disponível para download imediato.

## 🛠️ Tecnologias Utilizadas

*   **Python 3**
*   **Pandas:** Engenharia de dados, saneamento e agrupamentos
*   **Streamlit:** Construção da interface do usuário (UI) e experiência web (UX)
*   **OpenPyXL:** Engine para suporte e exportação avançada de arquivos Excel

---
📊 *Desenvolvido com foco em conectar Finanças, Tecnologia e Produtividade.*
