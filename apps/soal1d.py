import streamlit as st
import numpy as np
import pandas as pd
from sklearn import datasets
from logging import basicConfig
from os import rename
import numpy as np
from pandas.core import indexing
from pandas.core.indexes.base import Index
import streamlit as st
import json
import pandas as pd
import plotly.express as px
import json

def app():

    excel_file = 'produksi_minyak_mentah.csv'

    st.write('# Soal 1 D')

    with open('kode_negara_lengkap.json') as f:
            data = json.load(f)
            names = dict()
            region = dict()
            alpha3 = dict()
            subregion = dict()
            for x in data:
                country = x['name']
                idc = x['alpha-3']
                names[idc] = country
                alpha3[idc] = x['country-code']
                region[idc] = x['region']
                subregion[idc] = x['sub-region']


                


    df2 = pd.read_csv(excel_file)
    df2['produksi'].nlargest(1)


    negaraminyak = df2['kode_negara'].unique()
    minyak_selection = st.selectbox('Pilih :', negaraminyak)


    if minyak_selection in ('WLD','EU28','G20','OECD','OEU'):
        st.write("Negara yang dipilih : ")
        st.write("Kode Negara : ")
        st.write("Region :")
        st.write("Sub Region :")
    else:
        st.write("Negara yang dipilih : ",names[minyak_selection])
        st.write("Kode Negara : ",alpha3[minyak_selection])
        st.write("Region :",region[minyak_selection])
        st.write("Sub Region :",subregion[minyak_selection])

    filterbanyak = df2[df2.kode_negara== minyak_selection]
    filterbanyak = filterbanyak.nlargest(1, columns='produksi')

    filtersedikit = df2[df2.kode_negara== minyak_selection]
    filtersedikit = filtersedikit.nsmallest(44, columns='produksi')
    newfilter = filtersedikit.loc[filtersedikit[filtersedikit.produksi > 0].groupby(by='kode_negara')['produksi'].idxmin()]
    newfilter = newfilter.nsmallest(1, columns='produksi')


    seluruhtahun = df2[df2.kode_negara== minyak_selection]

    st.markdown("<h3 style='text-align: left; color: grey;'>Tahun Terbanyak</h3>", unsafe_allow_html=True)
    if filterbanyak['produksi'].unique() == 0:
        st.write('Tidak ada produksi')
    else:
        st.dataframe(filterbanyak)
    st.markdown("<h3 style='text-align: left; color: grey;'>Tahun Tersedikit</h3>", unsafe_allow_html=True)
    if newfilter.empty:
        st.write('Tidak ada produksi')
    else:
        st.dataframe(newfilter)
    st.markdown("<h3 style='text-align: left; color: grey;'>Produksi Seluruh Tahun</h3>", unsafe_allow_html=True)
    st.dataframe(seluruhtahun)







