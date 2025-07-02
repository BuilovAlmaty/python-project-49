
#Makefile
install: # синхронизация окружения .venv с файлами pyproject.toml и uv.lock
	uv sync
reinstall:
	uv tool install -e .

brain-games: # запуск проекта
	uv run brain-games

build: # сборка пакета
	uv build

package-install: # установка пакета
	uv tool install dist/*.whl

lint:
	uv run ruff check .

lint-fix:
	uv run ruff check . --fix

