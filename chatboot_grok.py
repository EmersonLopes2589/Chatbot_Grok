# COMANDO PARA RODAR: py -m streamlit run chatboot_grok.py
import pandas as pd
import streamlit as st
from groq import Groq

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

if arquivo_anexo:
    nome = arquivo_anexo.name
    extensao = nome.split(".")[-1].lower()

    if extensao == "csv":
        df = pd.read_csv(arquivo_anexo)
        st.write(df.head())
        conteudo_arquivo = f"Arquivo '{nome}':\n{df.to_string()}"

    elif extensao in ["xlsx", "xls"]:
        df = pd.read_excel(arquivo_anexo)
        st.write(df.head())
        conteudo_arquivo = f"Arquivo '{nome}':\n{df.to_string()}"

    else:
        try:
            conteudo = arquivo_anexo.read().decode("utf-8", errors="ignore")
            st.text_area("Previa", conteudo[:3000], height=200)
            conteudo_arquivo = f"Arquivo '{nome}':\n{conteudo}"
        except Exception:
            st.warning("Nao foi possivel ler o conteudo deste arquivo.")

if texto_usuario:
    conteudo_final = f"{texto_usuario}\n\n{conteudo_arquivo}" if conteudo_arquivo else texto_usuario

    st.chat_message("user").write(texto_usuario)
    st.session_state["list_mensagens"].append({"role": "user", "content": conteudo_final})

    resposta_ia = modelo_ia.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=st.session_state["list_mensagens"],
    )

    texto_resposta_ia = resposta_ia.choices[0].message.content
    st.chat_message("assistant").write(texto_resposta_ia)
    st.session_state["list_mensagens"].append({"role": "assistant", "content": texto_resposta_ia})
