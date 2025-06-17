start-server-prod:
	python mcp-client.py

run-server-dev:
	uvicorn mcp-client:app --reload --port 5000 --host "127.0.0.1"