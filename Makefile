
#Makefile
install: # синхронизация окружения .venv с файлами pyproject.toml и uv.lock
	uv sync

brain-games: # запуск проекта
	uv run brain-games

build: # сборка пакета
	uv build

package-install: # установка пакета
	uv tool install dist/*.whl

lint:
	uv run ruff check brain_games
	uv run ruff check brain_even
lint-fix:
	uv run ruff check . --fix
