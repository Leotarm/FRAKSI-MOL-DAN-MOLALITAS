import streamlit as st

st.write("APLIKASI PENGHITUNG MOLALITAS DAN FRAKSI MOL ZAT")

st.write('Rumus Menghitung Molalitas Suatu Larutan')
st.latex(r'''
    \left(\frac{mol}{massa}\right)''')


st.write('Rumus Menghitung Fraksi Mol Suatu Larutan')
st.latex(r'''
    \left(\frac{mol(A)}{Jumlah mol total}\right)''')

st.write('A = zat terlarut atau zat pelarut')

st.write('1. perhitungan molalitas')


pilihan = st.number_input('Input pilihan penghitungan: ')
num1 = st.number_input('mol zat terlarut : ')
num2 = st.number_input('massa zat pelarut : ')
st.write()

if pilihan == 1:
  st.write('Hasil dari',num1,'/',num2,'=',round(num1/num2,2))

st.write('2. perhitungan fraksi mol')

pilihan = st.number_input('input pilihan penghitungan: ')
num3 = st.number_input('mol zat A : ')
num4 = st.number_input('Jumlah mol total pelarut dan pelarut : ')
st.write()

if pilihan == 2:
  st.write('Hasil dari',num3,'/',num4,'=',round(num3/num4,2))