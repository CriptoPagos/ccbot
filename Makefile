all: install dist

install:
	sudo pip install -e .

dist:
	sudo python setup.py sdist

upload: dist
	twine upload dist/*

clean:
	sudo rm -rf dist ccbot.egg-info ccbot/__pycache__ ccbot/*.pyc
