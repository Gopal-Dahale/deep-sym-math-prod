# For deployment
from math import exp
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

# use streamlit run app.py to run the app

# creating a basic flask server
import numpy as np

from flask import Flask

app = Flask(__name__)


def main():
    st.title('Deep Sym Math - Integration')

    st.sidebar.header("About")
    st.sidebar.markdown(
        'Deep Sym Math - Integration is a free online tool that allows you to calculate integrals and functions. The tool is trained on a transformer model and has been heavily inspired by the original work of [Deep Learning for Symbolic Mathematics](https://github.com/facebookresearch/SymbolicMathematics). The tool is open source and is available on [Github](https://github.com/Gopal-Dahale/deep-sym-math). As of now, the tool offers only definite integration. The tool is still in development and will be updated soon. So now, good luck with your integration!'
    )
    st.sidebar.header("How to use")
    st.sidebar.markdown(
        'Type the function whose integral you want to find and press enter when done. Latex view is shown below. Use parantheses to show preferences.'
    )

    expr = ''
    expr = st.text_input("Calulate", value=expr)
    disp = '\int dx'
    if expr != '':
        try:
            expr = str(sp.latex(sp.simplify(expr)))
        except:
            st.error('Invalid Expression')
        else:
            disp = '\int ' + expr + ' dx'
    st.latex(disp)
    st.subheader('Prediction')
    if st.button('Get prediction'):
        # API call
        # End API call
        st.latex(expr)


if __name__ == '__main__':
    main()