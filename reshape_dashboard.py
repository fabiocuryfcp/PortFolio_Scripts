import streamlit as st
import pandas as pd

# ---------- Dados completos com SQL ----------
data = [
    {
        "Conceito": "Transpor dados",
        "Python": "df.T",
        "Excel": "TRANSPOSE(array)",
        "Power BI": "Transpose (Power Query)",
        "SQL": "N/A (não aplicável em SQL puro)",
        "Uso": "Utilizado para inverter linhas e colunas, comum para preparar dados para análise.",
        "Palavras-chave": "transpor, rotacionar, T"
    },
    {
        "Conceito": "Pivotar (Wider)",
        "Python": "df.pivot(index, columns, values)",
        "Excel": "Tabela dinâmica (linhas → colunas)",
        "Power BI": "Pivot Column (Power Query)",
        "SQL": "SELECT col1, SUM(valor) FROM tabela GROUP BY col1 PIVOT(valor)",
        "Uso": "Transforma dados longos em formato largo, útil para análises cruzadas.",
        "Palavras-chave": "pivot, wide, reorganizar"
    },
    {
        "Conceito": "Unpivot (Longer)",
        "Python": "df.melt(id_vars, var_name, value_name)",
        "Excel": "Tabela dinâmica reversa (manual)",
        "Power BI": "Unpivot Columns (Power Query)",
        "SQL": "UNPIVOT (valor FOR coluna IN (...))",
        "Uso": "Transforma dados largos em formato longo, ideal para análises por categoria ou tempo.",
        "Palavras-chave": "melt, unpivot, reshape"
    },
    {
        "Conceito": "Concatenar dados (empilhar)",
        "Python": "pd.concat([df1, df2], axis=0)",
        "Excel": "APPEND (Power Query) ou colar linhas",
        "Power BI": "Append Queries",
        "SQL": "SELECT * FROM tabela1 UNION ALL SELECT * FROM tabela2",
        "Uso": "Empilha dois ou mais datasets com mesmas colunas.",
        "Palavras-chave": "concatenar, empilhar, append, juntar"
    },
    {
        "Conceito": "Mesclar dados (juntar colunas)",
        "Python": "pd.merge(df1, df2, on='coluna', how='tipo')",
        "Excel": "VLOOKUP/XLOOKUP ou MERGE no Power Query",
        "Power BI": "Merge Queries",
        "SQL": "SELECT * FROM tabela1 JOIN tabela2 ON tabela1.col = tabela2.col",
        "Uso": "Une datasets com base em colunas-chave.",
        "Palavras-chave": "merge, join, lookup, relacionar"
    },
    {
        "Conceito": "Separar colunas",
        "Python": "df[['col1', 'col2']] = df['col'].str.split('-', expand=True)",
        "Excel": "Texto para colunas / SPLIT",
        "Power BI": "Split Column (Power Query)",
        "SQL": "SUBSTRING(col, ...) ou SPLIT_PART (PostgreSQL)",
        "Uso": "Divide strings em múltiplas colunas.",
        "Palavras-chave": "split, separar, string, texto"
    },
    {
        "Conceito": "Unir colunas (colapsar)",
        "Python": "df['nova_col'] = df['col1'] + '-' + df['col2']",
        "Excel": "CONCAT ou TEXTJOIN",
        "Power BI": "Column From Examples ou custom column",
        "SQL": "CONCAT(col1, '-', col2)",
        "Uso": "Combina múltiplas colunas em uma só.",
        "Palavras-chave": "colapsar, unir, concatenar colunas"
    },
    {
        "Conceito": "Alterar tipo de dados",
        "Python": "df['col'] = df['col'].astype(int)",
        "Excel": "Alterar tipo de célula (número, texto etc)",
        "Power BI": "Transform > Data Type",
        "SQL": "CAST(col AS INT) ou CONVERT(INT, col)",
        "Uso": "Essencial para cálculos e agrupamentos.",
        "Palavras-chave": "tipo, cast, converter, transformar"
    },
    {
        "Conceito": "Preencher valores ausentes",
        "Python": "df.fillna(valor) ou df.ffill()/bfill()",
        "Excel": "Preenchimento manual ou fórmulas (IF, LAG)",
        "Power BI": "Fill Down / Fill Up",
        "SQL": "COALESCE(col, valor)",
        "Uso": "Evita erros e mantém consistência.",
        "Palavras-chave": "fill, preencher, missing, NaN"
    },
    {
        "Conceito": "Remover duplicatas",
        "Python": "df.drop_duplicates()",
        "Excel": "Remover duplicatas",
        "Power BI": "Remove Duplicates",
        "SQL": "SELECT DISTINCT * FROM tabela",
        "Uso": "Garante integridade dos dados.",
        "Palavras-chave": "duplicatas, únicos, limpar, deduplicar"
    },
    {
        "Conceito": "Filtrar linhas",
        "Python": "df[df['coluna'] == 'valor']",
        "Excel": "Filtro automático ou fórmulas (FILTER)",
        "Power BI": "Filtros em visual ou etapa no Power Query",
        "SQL": "SELECT * FROM tabela WHERE coluna = 'valor'",
        "Uso": "Seleciona subconjuntos relevantes de dados.",
        "Palavras-chave": "filtrar, condicional, subset, query"
    },
]

df = pd.DataFrame(data)

# ---------- Layout ----------
st.set_page_config(page_title="Guia de Transformações de Dados", layout="wide")
st.title("🔄 Guia de Transformações de Dados")

st.markdown("""
Este guia apresenta **equivalências entre ferramentas (Python, Excel, Power BI, SQL)** para as principais transformações em dados.  
Ideal para quem transita entre ferramentas ou quer aprender a traduzir manipulações entre linguagens.

💡 Dica: use o campo de busca abaixo para encontrar rapidamente um conceito ou função.
""")

# ---------- Campo de busca ----------
search = st.text_input("🔍 Buscar por conceito, palavra-chave ou ferramenta...")

if search:
    filtered_df = df[df.apply(lambda row: row.astype(str).str.contains(search, case=False).any(), axis=1)]
else:
    filtered_df = df

# ---------- Exibição dos cards ----------
for _, row in filtered_df.iterrows():
    with st.expander(row["Conceito"]):
        st.markdown(f"**Python:** `{row['Python']}`")
        st.markdown(f"**Excel:** `{row['Excel']}`")
        st.markdown(f"**Power BI:** `{row['Power BI']}`")
        st.markdown(f"**SQL:** `{row['SQL']}`")
        st.markdown(f"**Uso:** {row['Uso']}")
        st.markdown(f"**Palavras-chave:** _{row['Palavras-chave']}_")

# ---------- Rodapé opcional ----------
st.markdown("---")
st.caption("Criado com ❤️ por Fabio Cury")
