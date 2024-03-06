import streamlit as st
import matplotlib.pyplot as plt
import yfinance as yf   

st.title('Meu primeiro programa de web')
st.text('Nome')
nome = st.text_input('Digite seu nome')
st.write('Olá', nome)


def inverte_texto(texto):
    return texto[::-1]


# Botão para inverter o texto
b1 = st.button("Inverter")
# st.write(b1)
if b1:
    texto_invertido = inverte_texto(nome)
    st.write(f"Texto Invertido: {texto_invertido}")

b2 = st.button("Gráfico")
if b2:
    fig, ax = plt.subplots()
    ax.scatter([1, 2, 3], [1, 2, 3])
    st.pyplot(fig)

# pegar ticker de uma ação da ibovespa e baixar os dados e plotar o gráfico
    
ticker = st.text_input('Digite o ticker da ação')
data_inicio = str(st.date_input('Data Início'))
data_fim = str(st.date_input('Data Fim'))
st.write(data_inicio)
b3 = st.button('Buscar')
if b3:
    # loading
    st.write('Carregando...')
    acao = yf.download(ticker + '.SA', start=data_inicio, end=data_fim)
    st.line_chart(acao['Close'])
    st.write(acao)
    st.write(acao.describe())