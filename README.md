# 🌿 Sistema de Geração de Laudos – Palmeira Ambiental

Aplicação desenvolvida para automatizar a criação de **laudos técnicos ambientais**, gerando documentos em **Word (.docx)** a partir de dados preenchidos em formulário.  
Cada laudo segue o modelo oficial da **Palmeira Ambiental**, com identidade visual padronizada, assinatura digital e formatação automática.

---

## 🧩 Funcionalidades Principais

✅ Interface limpa, responsiva e profissional (tema *light*, layout *wide*)  
✅ Geração automática de laudos a partir de formulário  
✅ Inserção de fotos e legendas fixas  
✅ Cada foto ocupa uma página do relatório  
✅ Modelo Word institucional carregado internamente (sem upload manual)  
✅ Assinatura centralizada ao final do laudo  
✅ Exportação final em formato `.docx`  

---

## 📷 Exemplo de Layout

> *(Adicione aqui um print da interface quando quiser)*  
> Exemplo de estrutura:
> - Página 1: informações gerais  
> - Páginas seguintes: imagens com legendas  
> - Última página: assinatura da responsável técnica  

---

## 🧱 Estrutura do Projeto

📁 laudo_app/
│
├── app.py # Aplicação principal Streamlit
├── modelos/
│ └── modelo_laudo.docx # Modelo Word institucional (não requer upload)
├── requirements.txt # Dependências do projeto
└── README.md # Documentação


---

## ⚙️ Instalação Local

### 1. Clone o repositório

```bash
git clone https://github.com/<seu-usuario>/laudo-palmeira-ambiental.git
cd laudo-palmeira-ambiental

python -m venv .venv
source .venv/bin/activate  # (Linux/Mac)
.venv\Scripts\activate     # (Windows)

pip install -r requirements.txt



streamlit run app.py

http://localhost:8501


🧑‍💻 Autor

Gustavo Ribeiro dos Santos
Engenheiro Eletricista | Especialista de Dados & IA
📍 Ponta Grossa - PR, Brasil



📜 Licença

Uso interno e autorizado exclusivamente pela equipe técnica da Palmeira Ambiental.
Distribuição, cópia ou modificação não autorizadas são proibidas.


© 2025 – Palmeira Ambiental | Desenvolvido por Gustavo Ribeiro dos Santos
