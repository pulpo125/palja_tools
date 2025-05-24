# ---------------------------
# Streamlit application 실행 파일
# ---------------------------
# 이 파일은 전체 앱의 진입점이며, 페이지를 정의하고 라우팅 처리합니다.
# 새로운 기능 페이지를 추가할 때에는 아래 3단계를 따르세요:
#
# 1. 새로운 페이지 파일을 생성하세요 (예: new_page.py)
# 2. cards.py에 해당 기능을 소개하는 카드 함수를 추가하세요
# 3. 아래 'pages' 리스트에 새 페이지를 등록하세요
#
# 예:
# st.Page("new_page.py", title="새 페이지", icon=":material/bolt:")
# ---------------------------

import streamlit as st


pages = [
    st.Page("home.py", title="PALJA", icon=":material/home:"),
    st.Page("joseon_translator.py", title="조선실록체 변환기", icon=":material/chat:"),
]

page = st.navigation(pages)
page.run()

st.sidebar.caption("© PALJA")
