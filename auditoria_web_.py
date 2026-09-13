# FAZENDO MUDANÇAS EM MEU SISTEMA WEB DE AUDITORIA
# COM INTERATIVIDADE DO USUÁRIO
import streamlit as st  # Interface web interativa para o sistema de auditoria
import pandas as pd     # Manipulação, agrupamento e saneamento de dados financeiros

st.title("📊 Sistema Web de Auditoria de Erros FP&A")

# Componente Drag & Drop para upload dinâmico de relatórios em CSV
arquivo_carregado = st.file_uploader("Carregue o arquivo CSV de FP&A", type=["csv"])

# Trava de segurança: impede a execução do script se nenhum arquivo foi carregado
if arquivo_carregado is not None:
    df = pd.read_csv(arquivo_carregado)
    
    st.subheader("👀 Visualização Inicial dos Dados (Brutos)")
    st.dataframe(df.head(), hide_index=True)  # Exibe os dados iniciais ocultando índices operacionais
    
    # Saneamento de dados em massa: elimina inconsistências de digitação comuns em ERPs
    df['Centro_Custo'] = df['Centro_Custo'].str.lower().str.strip()
    df['Descricao'] = df['Descricao'].str.lower().str.strip()
    
    # Isolamento estratégico e cálculo de despesas da área de TI Infraestrutura
    df_filtrado = df[df['Centro_Custo'] == 'ti_infra']
    
    # Indicador de alta performance (KPI Card) para rápida tomada de decisão executiva
    st.metric(label="Valor total das despesas de TI Infra", value=f"R$ {df_filtrado['Valor'].sum():,.2f}")
    
    # Tabela Dinâmica: Agrupamento consolidado das despesas por Centro de Custo
    resumo_financeiro = df.groupby('Centro_Custo')['Valor'].sum().reset_index()
    st.subheader("📊 Resumo Financeiro por Centro de Custo")
    st.dataframe(resumo_financeiro, column_config={"Valor": st.column_config.NumberColumn("Valor Total", format="R$ %,.2f")}, hide_index=True)  
    
    # Auditoria Avançada: Filtro por correspondência parcial para identificar licenças ocultas
    df_licencas = df[df['Descricao'].str.contains('licença', na=False)] 
    st.subheader("🔍 Auditoria : Despesas com Licenças")
    st.dataframe(df_licencas, hide_index=True)
    
    # Exportação para Excel: Estrutura os dados tratados diretamente na memória RAM
    import io
    buffer = io.BytesIO()  
    with pd.ExcelWriter(buffer, engine='openpyxl') as writer:  
        df_licencas.to_excel(writer, index=False, sheet_name='Auditoria_Licencas')  
    
    # Botão de download para o usuário salvar o relatório final auditado
    st.download_button(
        label="📥 Baixar Relatório de Auditoria (Excel)",
        data=buffer.getvalue(),
        file_name="auditoria_licencas.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"  
    )

# Configuração estética do Rodapé de Branding Profissional (sempre visível)
st.write("")
st.write("")

col_foto, col_texto = st.columns([1, 10])

with col_foto:
    st.image("imgs/leoperfil.png", width=50)

with col_texto:
    st.caption("🚀 Desenvolvido por **Leonardo Camargo**")
    st.caption("📉📊 Treinamento em FP&A e Analytics | 💻 Conectando Finanças e Tecnologia")
