import streamlit as st
from docxtpl import DocxTemplate, InlineImage
from docx.shared import Mm
from datetime import datetime
import tempfile
import os

# --------------------------
# Configuração inicial
# --------------------------
st.set_page_config(
    page_title="Gerador de Laudos Técnicos",
    page_icon="📄",
    layout="wide",  # modo WIDE
    initial_sidebar_state="collapsed"
)

# Forçar tema claro e tons de verde
st.markdown(
    """
    <style>
    :root {
        color-scheme: light !important;
    }
    .stApp {
        background-color: #ffffff;
        color: #1a1a1a;
    }
    h1, h2, h3, h4, h5 {
        color: #016241;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --------------------------
# Cabeçalho
# --------------------------
st.title("📄 Gerador de Laudo Técnico")
st.markdown("Preencha o formulário e exporte o laudo em Word (.docx) com o modelo padrão da empresa.")

# --------------------------
# Caminho do modelo interno
# --------------------------
modelo_path = os.path.join("modelos", "modelo_laudo.docx")
if not os.path.exists(modelo_path):
    st.error("❌ O modelo Word não foi encontrado. Verifique se o arquivo 'modelo_laudo.docx' está na pasta 'modelos'.")
    st.stop()

# --------------------------
# Formulário (1 coluna)
# --------------------------
st.markdown("### 🧾 Informações do Laudo")

data = st.date_input("Data", datetime.today())
nf = st.text_input("Nº Nota Fiscal")

produto = st.selectbox(
    "Produto",
    [
        "904961 - CERV HEINEKEN 0,0% 0,350LTSLEEKDES12UNPB",
        "904504 - AMSTEL LATA 473ML 12PACK PURO MALTE",
        "903940 - HEINEKEN LT12 PACK 473ML NV EMBALAGEM",
        "904721 - CERV HEINEKEN PIL 0,269LT DESC 8UN PBR",
        "903478 - HEINEKEN LN 330ML 4X6 - K2",
        "904895 - CERV HEINEKEN 0,0% 0,269LT DESC 8UN PBR",
        "903996 - HEINEKEN 0,0% LN 330ML 4X6 - K2",
        "904932 - CERV HEINEKEN PIL 0,350LT SLEEKDES12UNPB",
    ],
)

quantidade_pack = st.number_input("Quantidade Pack", min_value=0, step=1)
unidade_pack = st.number_input("Unidade Pack", min_value=0, step=1)
transportadora = st.text_input("Transportadora")
observacoes = st.text_area("Observações", height=120)

st.markdown("### 📸 Envie as imagens")
foto_etiqueta = st.file_uploader("Foto | Etiqueta", type=["jpg", "jpeg", "png"])
foto_produto = st.file_uploader("Foto | Produto Recebido", type=["jpg", "jpeg", "png"])
foto_embalagem = st.file_uploader("Foto | Embalagem", type=["jpg", "jpeg", "png"])
foto_descaracterizado = st.file_uploader("Foto | Produto Descaracterizado", type=["jpg", "jpeg", "png"])

# --------------------------
# Função auxiliar para imagens
# --------------------------
def criar_inline_image(doc, img_bytes, tamanho_mm=150):
    if img_bytes:
        tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")
        tmp.write(img_bytes)
        tmp.close()
        return InlineImage(doc, tmp.name, width=Mm(tamanho_mm))
    return ""

# --------------------------
# Geração do laudo
# --------------------------
if st.button("🚀 Gerar Laudo"):
    if not nf:
        st.error("⚠️ Preencha o número da nota fiscal antes de gerar.")
    else:
        doc = DocxTemplate(modelo_path)

        # Dicionário de dados (placeholders)
        dados = {
            "data": data.strftime("%d/%m/%Y"),
            "nota_fiscal": nf,
            "produto": produto,
            "quantidade_pack": quantidade_pack,
            "unidade_pack": unidade_pack,
            "transportadora": transportadora,
            "observacoes": observacoes or "Sem observações.",
            "foto_etiqueta": criar_inline_image(doc, foto_etiqueta.read() if foto_etiqueta else None),
            "foto_produto": criar_inline_image(doc, foto_produto.read() if foto_produto else None),
            "foto_embalagem": criar_inline_image(doc, foto_embalagem.read() if foto_embalagem else None),
            "foto_descaracterizado": criar_inline_image(doc, foto_descaracterizado.read() if foto_descaracterizado else None),
            "assinatura": f"Ponta Grossa, {data.strftime('%d/%m/%Y')}\nPreenchido por:\n______________________________\nHemellin Nathali Mendes\nAnalista de Meio Ambiente",
            "responsavel_geracao": "Sistema de Laudos - Beleza S/A",
            "data_geracao": datetime.now().strftime("%d/%m/%Y %H:%M"),
        }

        doc.render(dados)

        # Nome automático
        nome_docx = f"Laudo_{nf}_{data.strftime('%Y-%m-%d')}.docx"
        doc.save(nome_docx)
        st.success(f"✅ Laudo gerado com sucesso: {nome_docx}")

        with open(nome_docx, "rb") as fdocx:
            st.download_button("📘 Baixar Laudo em Word (.docx)", fdocx, file_name=nome_docx)
