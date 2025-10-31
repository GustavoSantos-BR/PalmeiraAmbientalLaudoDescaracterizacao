# 🌿 Sistema de Geração de Laudos – Palmeira Ambiental

Aplicação desenvolvida para automatizar a criação de **laudos técnicos ambientais**, gerando documentos em **Word (.docx)** a partir de dados preenchidos em formulário.  
Cada laudo segue o modelo oficial da **Palmeira Ambiental**, com identidade visual padronizada, assinatura digital e formatação automática.

Objetivos do Documento

Documentar de forma clara e profissional a aplicação PalmeiraAmbientalLaudoDescaracterizacao.

Fornecer instruções de instalação, execução, manutenção e contribuições para desenvolvedores e equipe técnica.

Facilitar a replicação, implantação e personalização do gerador automatizado de laudos técnicos ambientais.

Sumário

Visão Geral

Funcionalidades Principais

Arquitetura do Projeto

Requisitos

Instalação e Execução Local

Uso / Fluxo da Aplicação

Estrutura de Pastas

Configuração e Personalização

Boas Práticas / Segurança

Testes e Validação

Deploy / Hospedagem

Contribuição

Licença e Autor

Changelog Resumido

Contato / Suporte

Visão Geral

A aplicação é uma solução leve (Stack baseada em Python + Streamlit) que permite preencher um formulário web, anexar imagens e gerar um arquivo .docx formatado conforme o modelo institucional. O documento final contém páginas iniciais com informações gerais, páginas com fotos (cada foto em uma página, com legenda) e página final com assinatura centralizada.

Funcionalidades Principais

Interface limpa e responsiva (Streamlit).

Geração automática de laudos a partir de formulário.

Inserção de fotos e legendas (cada foto em página separada).

Modelo Word institucional (modelo_laudo.docx) carregado internamente (sem necessidade de upload manual).

Assinatura centralizada no final do laudo.

Exportação do laudo final em .docx.

Arquitetura do Projeto

Linguagem principal: Python

Interface: Streamlit

Geração de documentos: biblioteca Python para manipulação de .docx (ver requirements.txt).

Estrutura simples: um único app (app.py) que consome o modelo (modelos/modelo_laudo.docx) e exporta um arquivo gerado.

Requisitos

Python 3.9+ (recomenda-se 3.10)

Bibliotecas listadas em requirements.txt (instalar via pip)

Sistema operacional: multiplataforma (Linux / macOS / Windows)

Recomenda-se executar em ambiente virtual (venv, virtualenv, conda)

Exemplo do que esperar em requirements.txt (ver repositório):

streamlit
python-docx
Pillow
# (outras dependências conforme arquivo)

Instalação e Execução Local

Clonar o repositório:

git clone https://github.com/GustavoSantos-BR/PalmeiraAmbientalLaudoDescaracterizacao.git
cd PalmeiraAmbientalLaudoDescaracterizacao


Criar e ativar ambiente virtual:

Linux / macOS:

python -m venv .venv
source .venv/bin/activate


Windows (PowerShell):

python -m venv .venv
.venv\Scripts\Activate.ps1


Instalar dependências:

pip install -r requirements.txt


Executar a aplicação (Streamlit):

streamlit run app.py


Acessar no navegador:

http://localhost:8501

Uso / Fluxo da Aplicação

Abrir a interface Streamlit.

Preencher os campos do formulário (informações gerais do laudo).

Fazer upload das imagens (cada imagem terá sua página e legenda).

Confirmar dados e acionar a geração do laudo.

O sistema monta o documento a partir do modelo_laudo.docx, insere os textos, imagens e assinatura, e disponibiliza um botão para download do .docx gerado.

Estrutura de Pastas (Resumo)
PalmeiraAmbientalLaudoDescaracterizacao/
├── modelos/
│   └── modelo_laudo.docx        # Modelo Word institucional
├── app.py                       # Aplicação principal (Streamlit)
├── requirements.txt             # Dependências
└── README.md                    # Documentação (este arquivo)

Configuração e Personalização

Modelo Word: Para alterar a identidade visual, ajustar o layout ou campos fixos, editar modelos/modelo_laudo.docx diretamente no Word. Atenção ao uso de marcadores/placeholder se a lógica estiver atrelada a tags no .docx.

Campos do Formulário: Editar app.py para adicionar, remover ou modificar campos de entrada (rótulos, validações).

Assinatura: Caso deseje trocar a assinatura (imagem ou texto), substituir o recurso correspondente no repositório e adaptar a posição no .docx se necessário.

Local de Salvamento: Ajustar a lógica em app.py que salva o arquivo temporário/resultado para integrar com storage (S3, Google Drive, rede interna) conforme necessidade.

Boas Práticas / Segurança

Não versionar arquivos sensíveis (assinaturas digitais em alta resolução, chaves, credenciais).

Use ambientes virtuais e arquivos requirements.txt limpos.

Se a aplicação for exposta em rede interna ou internet, aplicar autenticação (ex.: OAuth/SSO ou proteção por proxy) e TLS/HTTPS.

Manter backup do modelo_laudo.docx antes de editar o template.

Testes e Validação

Validar geração de laudo com diferentes volumes de imagens (0..N) para garantir paginação correta.

Verificar formatação (margens, cabeçalho/rodapé) depois de alterar o modelo_laudo.docx.

Testar comportamentos em cenários de dados incompletos (campos obrigatórios ausentes).

Testar compatibilidade do .docx gerado em Word (Windows), LibreOffice e Google Docs.

Deploy / Hospedagem

Opções recomendadas:

Hospedar em um servidor interno com Python e Streamlit (systemd / docker).

Containerizar a aplicação com Docker (recomendado para replicabilidade).

Alternativas: Streamlit Cloud (caso não haja restrição de dados sensíveis) ou VPS com nginx + systemd para servir o app por um domínio com TLS.

Exemplo simples de Dockerfile (modelo):

FROM python:3.10-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

Contribuição

Abrir issue descrevendo a sugestão/bug.

Criar branch a partir de main seguindo convenção feature/<descrição> ou fix/<descrição>.

Submeter Pull Request com descrição clara das mudanças.

Incluir testes automatizados quando aplicável e atualizar a documentação.

Mantener a política de revisão de código (code review) antes do merge.

Licença e Autor

Autor: Gustavo Ribeiro dos Santos — Engenheiro Eletricista | Especialista de Dados & IA (Ponta Grossa - PR, Brasil)

Licença: Uso interno e autorizado exclusivamente pela equipe técnica da Palmeira Ambiental. Distribuição, cópia ou modificação não autorizadas são proibidas.

© 2025 – Palmeira Ambiental | Desenvolvido por Gustavo Ribeiro dos Santos

⚠️ Se for desejar outra licença (MIT, Apache, GPL), adicionar arquivo LICENSE e ajustar o cabeçalho.

Changelog Resumido

Inicial — Estrutura básica com app.py, modelos/modelo_laudo.docx e requirements.txt.

(Registrar aqui futuras versões e mudanças importantes)

Contato / Suporte

Autor / Maintainer: Gustavo Ribeiro dos Santos

Repositório: https://github.com/GustavoSantos-BR/PalmeiraAmbientalLaudoDescaracterizacao

Para suporte técnico: abrir Issue no repositório com descrição detalhada.

Anotações finais e sugestões de melhoria imediata

Incluir um arquivo CONTRIBUTING.md com fluxo de trabalho de git e padrões de commit.

Adicionar LICENSE se necessário para clareza jurídica.

Adicionar Dockerfile e docker-compose.yml de exemplo para facilitar deploy.

Incluir exemplos de entradas (sample inputs) e um laudo gerado de exemplo na pasta examples/ para validação visual.

Possível evolução: adicionar exportação para PDF, integração com assinatura digital certificada (se for requisito legal), e autenticação/controle de acesso.


🧑‍💻 Autor

Gustavo Ribeiro dos Santos
Engenheiro Eletricista | Especialista de Dados & IA
📍 Ponta Grossa - PR, Brasil



📜 Licença

Uso interno e autorizado exclusivamente pela equipe técnica da Palmeira Ambiental.
Distribuição, cópia ou modificação não autorizadas são proibidas.


© 2025 – Palmeira Ambiental | Desenvolvido por Gustavo Ribeiro dos Santos
