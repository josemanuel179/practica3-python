executable:
	python3 src/application/app.py

all:
	python3 src/application/app.py

clean:
	py3clean .

test:clean
	python3 -m unittest -v 
