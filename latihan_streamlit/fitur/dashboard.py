import streamlit as st

st.title("Halaman Dashboard")
st.image("CIRENG ISI.png", caption="Ini Cireng Tyassss, jgn lupa beli ya😍")

# fungsi menghitung dan menyimpan total
def total():
    total_nabung = sum(t['Jumlah']
                       for t in st.session_state['total_semua']
                       if t ['Tipe'] == 'Menabung')
    
    return total_nabung

total_semua = st.session_state['total_semua']
total_nabung = total()

st.metric("Total Menabung", f"Rp {total_nabung}")