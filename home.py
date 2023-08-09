import streamlit as st
import base64
import os

st.markdown(
    f"""
        <div style="text-align: center;">
            <h2 style="text-align: center;">AI 콘텐츠 생성기</h2>
        </div>
        """,
    unsafe_allow_html=True
)

def get_image_string(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

img_path = os.path.join('img', 'Content-AI-Working.jpg')
st.write('')
st.markdown(
    f"""
        <div style="text-align: center;">
            <h6 style="text-align: center;">디지털 마케팅 콘텐츠 제작을 위한 생성형AI 활용 및 프롬프트 작성 도구입니다.</h6>
            <br> <!-- line break tag to add space -->
            <br> <!-- add as many as you need to get the desired spacing -->
            <img src='data:image/png;base64,{get_image_string(img_path)}' style='width: 600px; margin: auto;' /> <!-- increased image size -->
        </div>
        """,
    unsafe_allow_html=True
)
