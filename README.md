# 🎭 palja_tools

> **AI가 만들고, 나는 논다. 팔자 좋~다!**

재미있고 창의적인 AI 도구를 개발하여 콘텐츠화하고 SNS에 공유하는 프로젝트입니다.

## 🌟 프로젝트 개요

palja_tools는 일상을 더 재미있게 만들어주는 AI 도구들의 모음집입니다. 각 도구는 창의적이고 유쾌한 경험을 제공하며, 그 결과물을 인스타그램 등 SNS에서 쉽게 공유할 수 있도록 설계되었습니다.

## 🛠️ 도구 목록

### 1. 📜 조선왕조실록체 변환기
현대어를 조선시대 문체로 유쾌하게 변환하는 텍스트 변환 도구입니다.

**특징:**
- 현대 일상어를 고풍스러운 조선시대 문체로 변환
- 재미있는 표현과 어투로 SNS 콘텐츠 제작 가능
- 직관적이고 간편한 사용자 인터페이스

## 🔧 설정 및 설치

### 환경 설정
```bash
# Conda 환경 생성 및 활성화
conda create -n palja python=3.12
conda activate palja

# 의존성 패키지 설치
pip install -r requirements.txt
```

### OpenAI API 키 설정
1. `conf/service.dev.yaml`을 복사하여 `service.yaml` 생성
2. `service.yaml`에서 `openai_api_key` 값을 본인의 API 키로 설정

```yaml
# service.yaml 예시
openai_api_key: "your-openai-api-key-here"
```

## 🚀 실행 방법

### Streamlit 웹 앱 실행
```bash
streamlit run app/streamlit_app.py
```

실행 후 브라우저에서 `http://localhost:8501`로 접속하여 사용할 수 있습니다.

## 📁 프로젝트 구조

```
palja_tools/
├── .streamlit/
│   └── config.toml          # Streamlit 설정 파일
├── app/
│   ├── static/              # 정적 파일 (이미지, 폰트 등)
│   ├── cards.py             # 기능 카드 UI 컴포넌트
│   ├── home.py              # 홈 화면 구성
│   ├── joseon_translator.py # 조선실록체 변환기
│   └── streamlit_app.py     # 앱 메인 진입점
├── conf/
│   ├── service.dev.yaml     # 개발용 설정 템플릿
│   └── service.yaml         # 실제 사용 설정 파일
├── src/
│   ├── tools/
├── requirements.txt         # Python 의존성 목록
└── README.md
```