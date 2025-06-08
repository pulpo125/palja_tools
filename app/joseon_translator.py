# ---------------------------
# 조선실록체 변환기 페이지
# ---------------------------

import streamlit as st
from PIL import Image
import os
import pyperclip

from src.tools.joseon_translator import run
from src.utils import log_info, log_error, log_warning


# 세션 상태 초기화
if "result_text" not in st.session_state:
    st.session_state.result_text = ""
if "is_converting" not in st.session_state:
    st.session_state.is_converting = False
# 커스텀 CSS
st.markdown(
    """
<style>
    .main-header {
        text-align: center;
        color: #000000;
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .sub-header {
        text-align: center;
        color: #000000;
        font-size: 1.2rem;
        margin-bottom: 30px;
    }
    .result-container {
        background-color: #ECEBE3;
        padding: 5px;
        border-radius: 10px;
        border: 1px solid #DFDED7;
        margin: 5px 0px 20px 0px;
        min-height: 200px;
        max-height: 300px;
        overflow-y: auto;
        font-family: serif;
        line-height: 1.6;
    }
    .spinner-container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100px;
        flex-direction: column;
    }
    .spinner {
        border: 4px solid #f3f3f3;
        border-top: 4px solid #3498db;
        border-radius: 50%;
        width: 40px;
        height: 40px;
        animation: spin 1s linear infinite;
        margin-bottom: 10px;
    }
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    .tiger-container {
        text-align: center;
        margin: 30px 0;
    }
</style>
""",
    unsafe_allow_html=True,
)

# ====================
# 헤더
# ====================
st.markdown(
    '<h1 class="main-header">조선왕조실록체 변환기</h1>', unsafe_allow_html=True
)
st.markdown(
    '<p class="sub-header">현대어를 고풍스러운 조선왕조실록체로 변환해보세요</p>',
    unsafe_allow_html=True,
)


# ===================
# 입력 섹션
# ===================


st.subheader("입력")
input_text = st.text_area(
    label="변환할 현대어를 입력하세요.",
    height=200,
    max_chars=1024,
    key="input_text",
)

# 변환 버튼
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    convert_button = st.button("변환하기", use_container_width=True, type="primary")


# ================
# 결과 섹션
# ================


st.subheader("결과")

# 결과창
if st.session_state.is_converting:
    # 로딩 중일 때 결과창 안에 spinner 표시
    st.markdown(
        """
        <div class="result-container">
            <div class="spinner-container">
                <div class="spinner"></div>
                <p style="color: #666; margin: 0;">변환 중입니다...</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
elif st.session_state.result_text:
    # 결과가 있을 때
    st.markdown(
        f'<div class="result-container">{st.session_state.result_text}</div>',
        unsafe_allow_html=True,
    )
else:
    # 초기 상태
    st.markdown(
        '<div class="result-container"></div>',
        unsafe_allow_html=True,
    )

# 변환 로직
if convert_button:
    if not input_text.strip():
        st.error("❌ 변환할 현대어를 입력해주세요.")
    else:
        # 로딩 상태 시작
        st.session_state.is_converting = True
        st.session_state.result_text = ""
        st.rerun()

# 변환 실행: 로딩 상태 시작 시 변환 실행
if st.session_state.is_converting:
    try:
        log_info("조선왕조실록체 변환 시작")

        # run
        response = run(input_text)
        log_info({"input": input_text, "output": response})

        # 결과 저장 및 로딩 상태 해제
        st.session_state.result_text = response
        st.session_state.is_converting = False
        st.rerun()  # 결과를 즉시 반영하기 위해 페이지 새로고침

    except Exception as e:
        st.error(f"❌ 변환 중 오류가 발생했습니다. 다시 시도해주세요.")
        log_error(f"조선왕조실록체 변환 중 오류 발생: {str(e)}")

        st.session_state.result_text = ""
        st.session_state.is_converting = False
        st.rerun()


# ===================
# 버튼과 호랑이 이미지 섹션
# ===================


st.markdown('<div class="tiger-container">', unsafe_allow_html=True)

# 버튼과 호랑이를 한 줄에 배치
col1, col2, col3 = st.columns([1, 1, 1])

# 복사 버튼 (왼쪽)
with col1:
    if st.button("복사하기", use_container_width=True):
        if st.session_state.result_text:
            try:
                # 클립보드에 복사
                pyperclip.copy(st.session_state.result_text)
                st.success("클립보드에 복사 완료! 🎉")

            except Exception as e:
                # pyperclip이 없는 경우
                st.info("💡 위 텍스트를 드래그해서 복사(Ctrl + C)하세요")
                log_error(f"복사하기 오류: {e}")
        else:
            st.warning("⚠️ 복사할 결과가 없습니다")

# 호랑이 이미지 (가운데)
with col2:
    if os.path.exists("./app/static/img/tiger.png"):
        try:
            tiger_image = Image.open("./app/static/img/tiger.png")
            st.image(tiger_image, width=300)

        except Exception as e:
            st.markdown(
                "<div style='font-size: 150px;'>🐅</div>", unsafe_allow_html=True
            )
            log_error(f"호랑이 이미지 로딩 오류: {str(e)}")

    else:
        st.markdown("<div style='font-size: 150px;'>🐅</div>", unsafe_allow_html=True)

# 새로 시작 버튼 (오른쪽)
with col3:
    if st.button("새로 시작", use_container_width=True):
        if "input_text" in st.session_state:
            del st.session_state.input_text
            st.session_state.input_text = ""

        st.session_state.result_text = ""
        st.session_state.is_converting = False
        st.rerun()

st.markdown("</div>", unsafe_allow_html=True)
