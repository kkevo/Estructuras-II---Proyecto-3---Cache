TRACE_FILE=data2 #switch between data and data2 to change input files

a1:
	@echo "Starting tests with 64 bytes block size, 16 ways cache\n"
	@echo "========= 32KB cache ========="
	python3 main.py 32 64 16 $(TRACE_FILE)
	@echo "\n"
	@echo "========= 64KB cache ========="
	python3 main.py 64 64 16 $(TRACE_FILE)
	@echo "\n"
	@echo "========= 128KB cache ========="
	python3 main.py 128 64 16 $(TRACE_FILE)
	@echo "\n"

a2:
	@echo "Starting tests with 64 bytes block size, 32KB cache\n"
	@echo "========= 4 way cache ========="
	python3 main.py 32 64 4 $(TRACE_FILE)
	@echo "\n"
	@echo "========= 8 way cache ========="
	python3 main.py 32 64 8 $(TRACE_FILE)
	@echo "\n"
	@echo "========= 16 way cache ========="
	python3 main.py 32 64 16 $(TRACE_FILE)
	@echo "\n"

a3:
	@echo "Starting tests with 32KB, 8 way cache\n"
	@echo "========= 32 byte block size ========="
	python3 main.py 32 32 8 $(TRACE_FILE)
	@echo "\n"
	@echo "========= 64 byte block size ========="
	python3 main.py 32 64 8 $(TRACE_FILE)
	@echo "\n"
	@echo "========= 128 byte block size ========="
	python3 main.py 32 128 8 $(TRACE_FILE)
	@echo "\n"