# 🌿 Sistema de Geração de Laudos – Palmeira Ambiental

Link de Acesso: https://palmeira-ambiental--laudo-descaracterizacao-hnk.streamlit.app/

Aplicação desenvolvida para automatizar a criação de **laudos técnicos ambientais**, gerando documentos em **Word (.docx)** a partir de dados preenchidos em formulário. Cada laudo segue o modelo institucional da **Palmeira Ambiental**, com identidade visual padronizada, assinatura da responsável técnica e formatação automática.

---

## Sumário
- [Visão Geral](#visão-geral)  
- [Funcionalidades Principais](#funcionalidades-principais)  
- [Arquitetura do Projeto](#arquitetura-do-projeto)  
- [Requisitos](#requisitos)  
- [Instalação e Execução Local](#instalação-e-execução-local)  
- [Uso / Fluxo da Aplicação](#uso--fluxo-da-aplicação)  
- [Estrutura de Pastas](#estrutura-de-pastas)  
- [Configuração e Personalização](#configuração-e-personalização)  
- [Boas Práticas / Segurança](#boas-práticas--segurança)  
- [Testes e Validação](#testes-e-validação)  
- [Deploy / Hospedagem](#deploy--hospedagem)  
- [Contribuição](#contribuição)  
- [Licença e Autor](#licença-e-autor)  
- [Changelog Resumido](#changelog-resumido)  
- [Contato / Suporte](#contato--suporte)

---

## Visão Geral
A aplicação é uma solução leve (Stack baseada em Python + Streamlit) que permite preencher um formulário web, anexar imagens e gerar um arquivo `.docx` formatado conforme o modelo institucional. O documento final contém páginas iniciais com informações gerais, páginas com fotos (cada foto em uma página, com legenda) e página final com assinatura centralizada.

## Funcionalidades Principais
- Interface limpa e responsiva (Streamlit).
- Geração automática de laudos a partir de formulário.
- Inserção de fotos e legendas (cada foto em página separada).
- Modelo Word institucional (`modelo_laudo.docx`) carregado internamente.
- Assinatura centralizada no final do laudo.
- Exportação do laudo final em `.docx`.

## Arquitetura do Projeto
- Linguagem principal: **Python**
- Interface: **Streamlit**
- Geração de documentos: **python-docx**
- Estrutura simples: um único app (`app.py`) que consome o modelo (`modelos/modelo_laudo.docx`) e exporta um arquivo gerado.

## Requisitos
- Python 3.9+  
- Bibliotecas listadas em `requirements.txt`  
- Ambiente virtual recomendado (`venv`, `conda`, etc.)

### Exemplo do `requirements.txt`
```bash
streamlit
python-docx
Pillow
```

## Instalação e Execução Local
```bash
git clone https://github.com/GustavoSantos-BR/PalmeiraAmbientalLaudoDescaracterizacao.git
cd PalmeiraAmbientalLaudoDescaracterizacao

python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

pip install -r requirements.txt
streamlit run app.py
```

Acesse no navegador:  
👉 `http://localhost:8501`

## Uso / Fluxo da Aplicação
1. Abrir a interface Streamlit.
2. Preencher os campos do formulário (informações gerais do laudo).
3. Fazer upload das imagens.
4. Confirmar dados e gerar o laudo.
5. O sistema monta o documento e disponibiliza o download do `.docx`.

## Estrutura de Pastas
```
PalmeiraAmbientalLaudoDescaracterizacao/
├── modelos/
│   └── modelo_laudo.docx
├── app.py
├── requirements.txt
└── README.md
```

## Configuração e Personalização
- Editar `modelos/modelo_laudo.docx` para alterar layout e identidade visual.  
- Adicionar/remover campos do formulário em `app.py`.  
- Substituir imagem de assinatura, se aplicável.  
- Adaptar local de salvamento do arquivo (S3, GDrive, etc.).

## Boas Práticas / Segurança
- Não versionar arquivos sensíveis (assinaturas digitais, chaves).  
- Usar HTTPS/TLS em ambiente de produção.  
- Fazer backup do modelo antes de alterações.  

## Testes e Validação
- Validar geração com diferentes quantidades de imagens.  
- Testar formatação em Word, LibreOffice e Google Docs.  
- Garantir que campos obrigatórios estejam preenchidos.  

## Deploy / Hospedagem
### Exemplo de `Dockerfile`
```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

## Contribuição
1. Abrir issue descrevendo a sugestão/bug.  
2. Criar branch a partir de `main`.  
3. Submeter Pull Request com descrição clara.  

## Licença e Autor
**Autor:** Gustavo Ribeiro dos Santos  
**Licença:** Uso interno da Palmeira Ambiental  
© 2025 – Palmeira Ambiental | Desenvolvido por Gustavo Ribeiro dos Santos

## Changelog Resumido
- v1.0 — Estrutura inicial e modelo funcional do gerador de laudos.

## Contato / Suporte
- Repositório: [PalmeiraAmbientalLaudoDescaracterizacao](https://github.com/GustavoSantos-BR/PalmeiraAmbientalLaudoDescaracterizacao)  


🧑‍💻 Autor

Gustavo Ribeiro dos Santos
Engenheiro Eletricista | Especialista de Dados & IA
📍 Ponta Grossa - PR, Brasil



📜 Licença

Uso interno e autorizado exclusivamente pela equipe técnica da Palmeira Ambiental.
Distribuição, cópia ou modificação não autorizadas são proibidas.


© 2025 – Palmeira Ambiental | Desenvolvido por Gustavo Ribeiro dos Santos
