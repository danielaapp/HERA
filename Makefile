.DEFAULT_GOAL := run

PIP = ./venv/bin/pip3

install_argus:
	sudo apt install argus-server -y
	sudo apt install argus-client -y

venv/bin/activate: requirements.txt install_argus
	sudo apt update && sudo apt upgrade -y
	sudo apt install build-essential -y
	sudo add-apt-repository ppa:deadsnakes/ppa -y
	sudo apt update
	sudo apt install python3.11 python3-pip -y
	python3.11 --version

	sudo apt install python3-venv -y

	python3 -m venv venv
	chmod +x venv/bin/activate
	. ./venv/bin/activate
	$(PIP) install -r requirements.txt

run: venv/bin/activate
	@echo "Starting Jupyter Notebook..."
	. ./venv/bin/activate && jupyter notebook

clean:
	rm -rf __pycache__
	rm -rf venv