lint:
	flake8 .

run_raw:
	@echo $(RAW)
	python3 main.py --raw "$(RAW)"

clean:
	rm -rf __pycache__

run:
	python3 main.py --file "$(FILE)"
