.PHONY: build
build:
	pyinstaller --onefile --noconsole --paths lib --hidden-import requests bin/digipy
