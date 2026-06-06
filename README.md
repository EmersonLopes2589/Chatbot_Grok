# CHATBOT COM IA - Groq + Streamlit

Chatbot inteligente com integração da API Groq e interface web interativa usando Streamlit.

## 📋 Descrição

Aplicativo web que oferece um chatbot alimentado pela IA Groq (modelo llama-3.3-70b-versatile). Suporta:
- Chat interativo em tempo real
- Upload e análise de múltiplos formatos de arquivo
- **CSV** - Análise de dados tabulares
- **Excel (XLSX/XLS)** - Leitura de múltiplas abas
- **PDF** - Extração de texto de documentos
- **TXT e outros** - Processamento de arquivos de texto
- Histórico de mensagens na sessão
- Interface limpa e intuitiva

## 🚀 Funcionalidades

- 💬 Chat interativo com IA
- 📤 Upload de múltiplos formatos de arquivo
- 📊 **Suporte aprimorado para CSV e Excel**
  - Visualização de dados em tabelas
  - Leitura completa de dados para análise
  - Suporte a múltiplas abas no Excel
- 📄 **Suporte para PDF**
  - Extração de texto de todas as páginas
  - Análise de documentos PDF
- 📝 Histórico de mensagens na sessão
- ⚡ Respostas rápidas com modelo Llama 3.3 70B
- ✅ Tratamento robusto de erros

## 🛠️ Requisitos

- Python 3.8+
- Streamlit >= 1.28.0
- Groq API
- Pandas >= 2.0.0
- OpenPyXL >= 3.10.0 (Excel)
- PyPDF2 >= 3.0.0 (PDF)

## 📦 Instalação

### 1. Clonar o repositório
```bash
git clone https://github.com/EmersonLopes2589/Chatbot_Grok.git
cd Chatbot_Grok
```

### 2. Instalar dependências
```bash
pip install -r requirements.txt
```

Ou instalar manualmente:
```bash
pip install streamlit groq pandas openpyxl PyPDF2
```

## 🔐 Configuração

1. Obtenha sua chave API em: https://console.groq.com/
2. Crie a pasta `.streamlit` (se não existir)
3. Crie o arquivo `.streamlit/secrets.toml`:

```toml
groq_api_key = "sua_chave_aqui"
```

**IMPORTANTE**: Adicione `.streamlit/secrets.toml` ao `.gitignore` para não expor sua chave!

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
├── requirements.txt          # Dependências do projeto
├── .streamlit/
│   ├── config.toml          # Configurações do Streamlit
│   └── secrets.toml         # Chaves (NÃO versionar!)
└── README.md
```

## 💡 Como Usar

### Conversa Básica
1. Abra a aplicação no navegador
2. Digite sua pergunta no campo "O que quer saber hoje?"
3. A IA responde com base no contexto

### Com Análise de Arquivo

#### CSV
1. Clique em "Envie um arquivo para a IA analisar"
2. Selecione um arquivo `.csv`
3. O arquivo será lido completamente e exibido como tabela
4. Faça sua pergunta sobre os dados

#### Excel (XLSX/XLS)
1. Selecione um arquivo `.xlsx` ou `.xls`
2. Todas as abas serão lidas automaticamente
3. Visualize os dados na tela
4. Pergunte à IA sobre qualquer aspecto dos dados

#### PDF
1. Selecione um arquivo `.pdf`
2. O texto será extraído de todas as páginas
3. Pergunte sobre o conteúdo do PDF

#### Outros Formatos
- Arquivo `.txt`, `.json`, `.html`, etc.
- Será tentada leitura como texto

## 🤖 Modelo de IA

- **Modelo**: llama-3.3-70b-versatile
- **Provider**: Groq
- **Contexto**: Mantém histórico completo de mensagens na sessão

## ⚙️ Variáveis de Ambiente

A chave da API deve estar configurada em `.streamlit/secrets.toml`:
- `groq_api_key` - Chave de acesso à API Groq

## 🔍 Troubleshooting

### "Erro ao ler PDF"
- Certifique-se de que `PyPDF2` está instalado: `pip install PyPDF2`

### "Erro ao ler Excel"
- Certifique-se de que `openpyxl` está instalado: `pip install openpyxl`

### "Configure a chave groq_api_key"
- Verifique se o arquivo `.streamlit/secrets.toml` existe
- Verifique se a chave está configurada corretamente

### IA não consegue processar arquivo
- Arquivo muito grande? Tente com arquivo menor
- Formato diferente? Experimente converter para CSV/Excel/PDF

## 📝 Notas Importantes

- **Nunca compartilhe sua chave API** (`groq_api_key`)
- Mantenha sempre em `.streamlit/secrets.toml` (listado em `.gitignore`)
- Arquivos muito grandes podem demorar mais para processar
- O contexto do chat é resetado ao recarregar a página

## 🔗 Links Úteis

- [Streamlit Docs](https://docs.streamlit.io/)
- [Groq API Docs](https://console.groq.com/docs)
- [Groq Console](https://console.groq.com/)
- [PyPDF2 Docs](https://pypdf2.readthedocs.io/)
- [Pandas Docs](https://pandas.pydata.org/docs/)

## 📄 Licença

MIT License - Sinta-se livre para usar e modificar!
