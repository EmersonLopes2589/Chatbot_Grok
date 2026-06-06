# CHATBOT COM IA - Groq + Streamlit

Chatbot inteligente com integração da API Groq e interface web interativa usando Streamlit.

## 📋 Descrição

Aplicativo web que oferece um chatbot alimentado pela IA Groq (modelo llama-3.3-70b-versatile). Suporta:
- Chat interativo em tempo real
- Upload e análise de arquivos (CSV, Excel, TXT, etc.)
- Histórico de mensagens na sessão
- Interface limpa e intuitiva

## 🚀 Funcionalidades

- 💬 Chat interativo com IA
- 📤 Upload de arquivos para análise
- 📊 Suporte a arquivos CSV e Excel
- 📝 Histórico de mensagens na sessão
- ⚡ Respostas rápidas com modelo Llama 3.3 70B

## 🛠️ Requisitos

- Python 3.x
- Streamlit
- Groq API
- Pandas
- OpenPyXL (para suporte Excel)

## 📦 Instalação

```bash
pip install streamlit groq pandas openpyxl
```

## 🔐 Configuração

1. Obtenha sua chave API em: https://console.groq.com/
2. Crie a pasta `.streamlit` (se não existir)
3. Crie o arquivo `.streamlit/secrets.toml`:

```toml
groq_api_key = "sua_chave_aqui"
```

## 🏃 Como Executar

```bash
py -m streamlit run chatboot_grok.py
```

Ou:
```bash
streamlit run chatboot_grok.py
```

A aplicação abrirá em `http://localhost:8501`

## 📂 Estrutura do Projeto

```
Chatbot_Grok/
├── chatboot_grok.py          # Script principal da aplicação
├── .streamlit/
│   └── secrets.toml          # Configurações e chaves (não versionar!)
└── README.md
```

## 💡 Uso

1. Abra a aplicação no navegador
2. Digite sua pergunta no campo "O que quer saber hoje?"
3. Opcionalmente, anexe um arquivo (CSV, Excel, TXT, etc.)
4. A IA irá processar e responder com base no contexto

## 🤖 Modelo de IA

- **Modelo**: llama-3.3-70b-versatile
- **Provider**: Groq
- **Contexto**: Mantém histórico de mensagens na sessão

## ⚙️ Variáveis de Ambiente

A chave da API deve estar configurada em `.streamlit/secrets.toml`:
- `groq_api_key` - Chave de acesso à API Groq

## 📝 Nota Importante

Nunca compartilhe sua chave API (`groq_api_key`). Mantém sempre em `.streamlit/secrets.toml` que está no `.gitignore`.

## 🔗 Links Úteis

- [Streamlit Docs](https://docs.streamlit.io/)
- [Groq API Docs](https://console.groq.com/docs/speech-text)
- [Groq Console](https://console.groq.com/)
