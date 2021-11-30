run:clean
	python3 src/application/app.py -h
	rm -f app 
 
test:clean
	python3 -m unittest -v test/test_query.py 

clean:
	py3clean .
