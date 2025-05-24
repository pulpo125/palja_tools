# ---------------------------
# PALJA Home Page
# ---------------------------
# 이 파일은 PALJA 앱의 홈 화면을 구성합니다.
# 주요 기능들을 카드 형태로 시각화하여 배치합니다.
#
# 1. cards.py에 새로운 카드 함수 정의 (예: new_page_card)
# 2. 아래 `cols`에 원하는 위치에 해당 카드 함수 호출
#
# 예:
# from app.cards import new_page_card
# ...
# with cols[1].container(height=310):
#     new_page_card()
# ---------------------------

import streamlit as st
from app.cards import joseon_translator_card


st.title("PALJA")

st.markdown("AI가 만들고, 나는 논다. 팔자 좋~다!")

cols = st.columns(2)
with cols[0].container(height=310):
    joseon_translator_card()
