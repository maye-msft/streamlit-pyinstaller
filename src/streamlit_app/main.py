import streamlit as st
import os, sys, datetime
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import my_lib.utils as utils

if __name__ == '__main__':
    st.header("Hello world")
    st.write(utils.get_name() + " is running")
    st.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))