# Indenter

[![pypi badge](https://img.shields.io/pypi/v/indenter)](https://pypi.org/project/indenter/)

Indenter is a Python package that assists with programmatically indenting text to
arbitrary levels using `with` blocks and `+`/`-` operators. It has zero dependencies.

Use Indenter to get easy structured output, even as your control flow weaves through
multiple functions:

```python
from indenter import Indenter

def validate_email(ind, email):
  print(ind + 'Validating email...')
  # ...

def parse_date(ind, date):
  print(ind + f'Parsing date {date}')
  # ...
  with ind:
    print(ind + 'Checking components')
    y, m, d = date.split('-')
  print(ind + 'Date is valid!')

def get_user_record(ind):
  print(ind + 'Fetching user from database...')
  validate_email(ind + 1, 'ben@twos.dev')
  birthday = parse_date(ind + 1, '1990-08-21')
  print(ind + 'Fetched user!')
  # ...

ind = Indenter(symbol='→ ')
get_user_record(ind)
```
Output:
```plain
Fetching user from database...
→ Validating email...
→ Parsing date 1990-08-21
→ → Checking components
→ Date is valid!
Fetched user!
```

## Getting started

### Requirements

- Python 3.6+

### Installing

```sh
pip install indenter
```

## Usage

```python
from indenter import Indenter
with Indenter() as ind:
  print(ind + "Text to be indented")

# Output:
#   Text to be indented
```

You can nest an arbitrary number of `with` calls:

```python
from indenter import Indenter
ind = Indenter()
with ind:
  print(ind + "I'm one level deep")
  with ind:
    print(ind + "I'm two levels deep")
  print(ind + "I'm one level deep again")

# Output:
#   I'm one level deep
#     I'm two levels deep
#   I'm one level deep again
```

You can manually adjust the indentation level using `+`/`-`. Use this to indent output
by nested function calls correctly:

```python
import logging
from indenter import Indenter

ind = Indenter()

func do_work(ind):
  logging.debug(ind + "Doing some work")

func do_business_logic():
  ind = Indenter()
  logging.debug(ind + "Doing some business logic")
  do_work(ind + 1)
  logging.debug(ind + "Finishing some busines logic")

do_some_business_logic()

# Output:
# Doing some business logic
#   Doing some work
# Finishing some busines logic
```

### Customization

The default indentation symbol is two spaces. You can override this by passing `symbol`:

```python
from indenter import Indenter

# Indent with arrows
with Indenter(symbol="→ ") as ind:
  print(ind + "I'm indented with an arrow")
  with ind:
    print(ind + "I'm indented with two arrows")

# Indent with 4 spaces per level
with Indenter(symbol="    ") as ind:
  print(ind + "I'm indented by four spaces")

# Indent with tabs
with Indenter(symbol="\t") as ind:
  print(ind + "I'm indented by one tab")

# Output:
# → I'm indented by an arrow
# → → I'm indented by two arrows
#     I'm indented by four spaces
# 	I'm indented by one tab
```

When using custom symbols, nested `with`s will inherit the symbol of
their parent. If you need more than one type of indentation at once,
you must make and manage multiple `Indenter`s.

The indenter starts at zero levels of indentation by default, and
increases by one level for each `with` block. This can be overridden
to start at other levels, such as 1:

```python
from indenter import Indenter
ind = Indenter(start=1)
print(ind + "First-level indentation")
with ind:
  print(ind + "Second-level indentation")

# Output:
#   First-level indentation
#     Second-level indentation
```

## Contributing

I welcome contributions and foster an inclusive environment.

### Testing

Testing requires `pytest` (`pip install pytest`).

```sh
pytest
```

### Releasing

_(mostly notes for myself)_

To release, first bump the version number in `setup.cfg`, commit the result, then run:

```sh
rm -rf dist
pip install build twine
python -m build --wheel
twine check dist/* # optional; check for common issues
twine upload dist/*
```

For ease of browsing by users, you should also cut a release on GitHub.
