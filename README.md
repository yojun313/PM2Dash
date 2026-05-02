# PM2DASH

FastAPI 기반의 실시간 PM2 프로세스 모니터링 및 관리 대시보드입니다. 웹 브라우저에서 서버의 프로세스 상태를 한눈에 파악하고 제어할 수 있습니다.

## 주요 기능
* **실시간 모니터링**: CPU 사용량, 메모리 점유율, 업타입 실시간 업데이트
* **프로세스 제어**: 웹UI에서 즉시 Restart, Stop, Watch 모드 전환 가능
* **실시간 로그 스트리밍**: 실시간 프로세스 로그 확인

## 시작하기

### 1. 가상환경 구축 및 활성화
```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# Windows의 경우: venv\Scripts\activate
```

### 2. 의존성 패키지 설치
```bash
pip install -r requirements.txt
```

### 3. 대시보드 실행
```bash
python3 run.py
```
실행 후 브라우저에서 `http://localhost:8000` (또는 지정된 포트)으로 접속하세요.

## 프로젝트 구조
```text
PM2DASH/
├── app/
│   ├── routes/          # API 및 페이지 라우팅 (pm2_routes.py)
│   ├── services/        # PM2 명령 실행 로직 (pm2_service.py)
│   ├── templates/       # HTML 템플릿 (process.html)
│   └── main.py          # FastAPI 앱 설정
├── venv/                # 파이썬 가상환경
├── README.md            # 프로젝트 문서
├── requirements.txt     # 설치 필요 패키지 목록
└── run.py               # 서버 실행 엔트리포인트
```
---