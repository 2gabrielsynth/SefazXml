import requests
import streamlit as st

st.set_page_config(layout="wide")

def enviar_requisicao(xml_nfe):
    if xml_nfe:
        api_url = "https://ws.meudanfe.com/api/v1/get/nfe/xmltodanfepdf/API"
        headers = {'Content-Type': 'text/plain'}
        response = requests.post(api_url, headers=headers, data=xml_nfe)
        if response.status_code == 200:
            base64_response = response.text.strip('data:application/pdf;base64,').strip('"')
            href = f'<a href="data:application/pdf;base64,{base64_response}" download="DANFE.pdf">Clique aqui para baixar o PDF do DANFE</a>'
            st.markdown(href, unsafe_allow_html=True)
            st.markdown("<span style='font-size: 20px; color: green;'>PDF do DANFE gerado com sucesso.</span>", unsafe_allow_html=True)
        else:
            st.error(f"<span style='font-size: 20px; color: red;'>Falha ao gerar PDF do DANFE! Código de status HTTP: {response.status_code}</span>", unsafe_allow_html=True)
    else:
        st.warning("<span style='font-size: 20px; color: orange;'>Selecione um arquivo XML antes de enviar a requisição.</span>", unsafe_allow_html=True)

def main():
    st.markdown("<h1 style='font-size: 58px;text-align: center; color: #507A99;'>Converter arquivo xml para Danfe(PDF)</h1>", unsafe_allow_html=True)
    #st.markdown("<h1 style='font-size: 20px;text-align: center; color: darkgray;'>Gabriel Machado</h1>", unsafe_allow_html=True)

    # Criando uma linha para as imagens
    st.write('<div style="display: flex;">', unsafe_allow_html=True)

    # Adicionando a primeira imagem
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write('Gabriel Machado')
    with col2:
        st.image("nf.png", width=500, )
    with col3:
        st.write('')

    # Fechando a linha
    st.write('</div>', unsafe_allow_html=True)

    uploaded_file = st.file_uploader("Carregar arquivo XML", type="xml")

    if uploaded_file:
        xml_nfe = uploaded_file.read()

        st.write(f"Arquivo selecionado: {uploaded_file.name}")

        if st.button("Gerar DANFE"):
            enviar_requisicao(xml_nfe)

    st.markdown("LinkedIn: www.linkedin.com/in/gabriel-machado-a47470181")  
    
    st.markdown("Outros projetos no meu GitHub:https://github.com/2gabrielsynth")        
          

if __name__ == "__main__":
    main()
