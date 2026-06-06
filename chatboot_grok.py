# COMANDO PARA RODAR: py -m streamlit run chatboot_grok.py
import pandas as pd
import streamlit as st
from groq import Groq
import io
import traceback

try:
    import PyPDF2
    HAS_PYPDF = True
except ImportError:
    HAS_PYPDF = False

groq_api_key = st.secrets.get("groq_api_key")
if not groq_api_key:
    st.error("Configure a chave groq_api_key no arquivo .streamlit/secrets.toml.")
    st.stop()

modelo_ia = Groq(api_key=groq_api_key)

st.write("# CHATBOT COM IA")

if "list_mensagens" not in st.session_state:
    st.session_state["list_mensagens"] = []

for mensagem in st.session_state["list_mensagens"]:
    st.chat_message(mensagem["role"]).write(mensagem["content"])

texto_usuario = st.chat_input("O que quer saber hoje?")
arquivo_anexo = st.file_uploader("Envie um arquivo para a IA analisar", type=None)

conteudo_arquivo = ""

def ler_csv(arquivo):
    """Lê arquivo CSV e converte para string formatada"""
    try:
        df = pd.read_csv(arquivo)
        st.write("**Preview do CSV:**")
        st.dataframe(df)
        
        resumo = f"Arquivo '{arquivo.name}' (CSV)\n"
        resumo += f"Linhas: {len(df)}\n"
        resumo += f"Colunas: {', '.join(df.columns.tolist())}\n\n"
        resumo += "Dados:\n"
        resumo += df.to_string()
        
        return resumo
    except Exception as e:
        st.error(f"Erro ao ler CSV: {str(e)}")
        return ""

def ler_excel(arquivo):
    """Lê arquivo Excel (XLSX/XLS) e converte para string formatada"""
    try:
        excel_file = pd.ExcelFile(arquivo)
        conteudo = f"Arquivo '{arquivo.name}' (Excel)\n"
        conteudo += f"Abas: {', '.join(excel_file.sheet_names)}\n\n"
        
        for sheet_name in excel_file.sheet_names:
            df = pd.read_excel(arquivo, sheet_name=sheet_name)
            st.write(f"**Preview da aba '{sheet_name}':**")
            st.dataframe(df)
            
            conteudo += f"--- Aba: {sheet_name} ---\n"
            conteudo += f"Linhas: {len(df)}\n"
            conteudo += f"Colunas: {', '.join(df.columns.tolist())}\n"
            conteudo += df.to_string()
            conteudo += "\n\n"
        
        return conteudo
    except Exception as e:
        st.error(f"Erro ao ler Excel: {str(e)}")
        return ""

def ler_pdf(arquivo):
    """Lê arquivo PDF e extrai texto"""
    try:
        if not HAS_PYPDF:
            st.warning("PyPDF2 não está instalado. Execute: pip install PyPDF2")
            return ""
        
        pdf_reader = PyPDF2.PdfReader(arquivo)
        conteudo = f"Arquivo '{arquivo.name}' (PDF)\n"
        conteudo += f"Total de páginas: {len(pdf_reader.pages)}\n\n"
        
        st.write(f"**PDF com {len(pdf_reader.pages)} página(s) detectada**")
        
        for page_num, page in enumerate(pdf_reader.pages, 1):
            texto_pagina = page.extract_text()
            conteudo += f"--- Página {page_num} ---\n"
            conteudo += texto_pagina + "\n\n"
        
        return conteudo
    except Exception as e:
        st.error(f"Erro ao ler PDF: {str(e)}")
        return ""

def ler_arquivo_texto(arquivo):
    """Lê arquivo de texto genérico"""
    try:
        conteudo = arquivo.read().decode("utf-8", errors="ignore")
        st.text_area("Preview do arquivo:", conteudo[:2000], height=200, disabled=True)
        return f"Arquivo '{arquivo.name}':\n{conteudo}"
    except Exception as e:
        st.error(f"Erro ao ler arquivo: {str(e)}")
        return ""

if arquivo_anexo:
    nome = arquivo_anexo.name
    extensao = nome.split(".")[-1].lower()
    
    with st.spinner(f"Processando {extensao.upper()}..."):
        if extensao == "csv":
            conteudo_arquivo = ler_csv(arquivo_anexo)
        
        elif extensao in ["xlsx", "xls"]:
            conteudo_arquivo = ler_excel(arquivo_anexo)
        
        elif extensao == "pdf":
            conteudo_arquivo = ler_pdf(arquivo_anexo)
        
        else:
            conteudo_arquivo = ler_arquivo_texto(arquivo_anexo)
        
        if conteudo_arquivo:
            st.success(f"✅ Arquivo '{nome}' processado com sucesso!")
        else:
            st.error(f"❌ Não foi possível processar o arquivo '{nome}'")

if texto_usuario:
    conteudo_final = f"{texto_usuario}\n\n{conteudo_arquivo}" if conteudo_arquivo else texto_usuario
    
    st.chat_message("user").write(texto_usuario)
    st.session_state["list_mensagens"].append({"role": "user", "content": conteudo_final})
    
    with st.spinner("IA pensando..."):
        try:
            resposta_ia = modelo_ia.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=st.session_state["list_mensagens"],
            )
            
            texto_resposta_ia = resposta_ia.choices[0].message.content
            st.chat_message("assistant").write(texto_resposta_ia)
            st.session_state["list_mensagens"].append({"role": "assistant", "content": texto_resposta_ia})
        except Exception as e:
            st.error(f"Erro ao chamar IA: {str(e)}")
            st.info("Verifique sua chave API do Groq em .streamlit/secrets.toml")
