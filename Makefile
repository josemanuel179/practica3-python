executable:
	python3 src/application/app.py

all:
	python3 src/application/app.py

clean:
	rm -rf __pycache__

test:clean
	python3 test.py
