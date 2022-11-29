#from os import XATTR_SIZE_MAX
import streamlit as st
st.write("""
# Addition Of Two Numbers
""")
#Get Input
x=st.number_input("Enter The Number1")
st.write("The number is:",x)
y=st.number_input("Enter The Number2")
st.write("The number is:",y)
sum=st.write(x+y)