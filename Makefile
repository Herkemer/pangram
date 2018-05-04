PYLINT = pylint
PYLINTFLAGS = --reports n --disable=duplicate-code
PYCODESTYLE = pycodestyle
PYCODESTYLEFLAGS = --max-line-length=100

PYTHONDIRS = .

check: lint check-style

lint:
	$(PYLINT) $(PYLINTFLAGS) $(PYTHONDIRS) | tee pylint.out

%.pylint:
	$(PYLINT) $(PYLINTFLAGS) $* || true

check-style:
	$(PYCODESTYLE) $(PYCODESTYLEFLAGS) $(PYTHONDIRS) || true

%.style:
	$(PYCODESTYLE) $(PYCODESTYLEFLAGS) $* || true

test:
	python -m unittest discover -v

.PHONY: check lint check-style
