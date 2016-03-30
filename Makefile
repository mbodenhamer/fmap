all: test

#-------------------------------------------------------------------------------

test:
	@coverage erase
	@tox
	@coverage html

show:
	@chromium-browser htmlcov/index.html

.PHONY: test show
#-------------------------------------------------------------------------------


clean: 
	@rm -f *.py[co] */*.py[co] */*/*.py[co]
	@rm -rf */__pycache__ */*/__pycache__

.PHONY: clean
#-------------------------------------------------------------------------------
