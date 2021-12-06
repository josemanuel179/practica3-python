run:clean
	./app -h
 
test:clean
	python3 -m unittest -v 

clean:
	find . -path '*/__pycache__*' -delete
