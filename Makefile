.PHONY: install test serve dashboard web generate-images all

install:
	bash install.sh

test:
	python3 safeplate_platform/hydrology.py
	python3 safeplate_platform/washing.py
	python3 safeplate_platform/gemini_agent.py

generate-images:
	python3 generate_assets.py

all: test generate-images

serve:
	uvicorn safeplate_platform.api:app --reload --host 0.0.0.0 --port 8000

dashboard:
	streamlit run safeplate_platform/dashboard.py

web:
	python3 -m http.server 8080
