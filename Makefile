run:clean
	python3 src/application/app.py -h
	rm -f app 
 
test:clean
	python3 -m unittest -v 

clean:
	find . -path '*/__pycache__*' -delete
