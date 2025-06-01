# ---------------------------
# UI 카드 컴포넌트 모음
# ---------------------------
# 이 파일은 홈 화면 등에 표시되는 카드 형태의 UI 컴포넌트를 정의합니다.
# 각 카드 함수는 페이지로 이동 가능한 링크와 간단한 설명을 포함합니다.
#
# 1. 기능에 대응되는 페이지가 있어야 합니다 (예: new_page.py)
# 2. 아래와 같은 형식으로 새로운 카드 함수를 정의하세요:
#
# def new_page_card():
#     st.page_link("new_page.py", label="새 페이지", icon=":material/bolt:")
#
# 3. home.py에서 import하여 적절한 위치에 카드 배치
# ---------------------------

import streamlit as st


def joseon_translator_card():
    st.page_link(
        "joseon_translator.py", label="조선실록체 변환기", icon=":material/chat:"
    )
    st.subheader("조선실록체 변환기")
    inner_cols = st.columns(1, border=True)
    inner_cols[0].markdown(
        "*조선실록체 변환기라 하니, 현대 한국어로 작성된 글을 조선시대 문체로 번역하리라. 번역할 글을 제시하시면, 그에 맞추어 조선실록체로 변환하겠나이다.*"
    )
