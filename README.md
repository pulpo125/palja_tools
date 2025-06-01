# palja_tools

## Settings

- OpenAI Key 설정
    - conf/service.dev.yaml 을 복사하여 service.yaml 을 만드세요.
    - service.yaml 에서 openai_api_key 를 입력하세요.

- ENV 설정
    ```
    conda create -n palja python=3.12
    conda activate palja
    pip install -r requirements.txt
    ```


## Streamlit APP
### 🔧 구조
- `.streamlit/`: Streamlit 설정 파일 디렉토리 (`config.toml`)
- `app/`
    - `static/`: 정적 파일 (이미지, 폰트 등) 저장 폴더
    - `cards.py`: 각 기능 페이지에 대응하는 카드 UI 컴포넌트 정의
    - `home.py`: 홈 화면 구성. 기능 카드들을 배치
    - `joseon_translator.py`: 조선실록체 변환기 기능 페이지
    - `streamlit_app.py`: 전체 앱 실행 진입점이며, 페이지 라우팅 설정 포함

### 🚀 실행
```bash
streamlit run app/streamlit_app.py
```