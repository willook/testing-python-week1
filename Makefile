.PHONY: run stop test

# 서버 실행
run:
	uvicorn app.main:app --reload --host 0.0.0.0 --port 9090

# 서버 종료
stop:
	@echo "서버를 종료합니다..."
	@-pkill -f "uvicorn app.main:app"

# 테스트 실행
test:
	PYTHONPATH=. pytest

