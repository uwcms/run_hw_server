rpm:
	python3 setup.py bdist --format=rpm

clean:
	rm -rf build dist *.egg-info
