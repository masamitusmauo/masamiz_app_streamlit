import streamlit as st
import pandas as pd
st.title('開発中')
st.caption('これは丸尾将満のサイトです。')
st.write('DataFrame')

with st.container():
    col1, col2, col3 = st.columns(3)
    if col1.button('Button 1'):
        st.write('Button 1 が押されました')
    if col2.button('Button 2'):
        st.write('Button 2 が押されました')
    if col3.button('Button 3'):
        st.write('Button 3 が押されました')
expander1=st.expander('問い合わせ')
expander1.write('回答')
# button=st.button1('右コラムを表示')
# left_column,center_column,right_column=st.columns(3)
#
# if button1:
#     right_column.write('右カラムです')
df=pd.DataFrame({'一列目':[1,2,3,4],'二列目':[10,20,30,40]})
st.dataframe(df,width=200,height=200)
option=st.sidebar.text_input('好きな数字を教えてください。')
'好きな数字は',option
condition=st.sidebar.slider('調子は',0,100,50)
'調子は',condition
