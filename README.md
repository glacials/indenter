# Indenter

Indenter is a Python package that assists with programmatically indenting
text to arbitrary levels using `with` blocks.

## Installation

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

You can nest an arbitrary amount of calls:

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

The default indentation symbol is two spaces. You can override this by
passing `symbol`:

```python
from indenter import Indenter
# Indent with 4 spaces per level
with Indenter(symbol="    ") as ind:
  print(ind + "I'm indented by four spaces")

# Indent with tabs
with Indenter(symbol="\t") as ind:
  print(ind + "I'm indented by one tab")

# Output:
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
print(ind + "First-level indentation)
with ind:
  print(ind + "Second-level indentation")

# Output:
#   First-level indentation
#     Second-level indentation
```

## Contributing

I welcome contributions and foster an inclusive environment.

### Releasing

_(mostly notes for myself)_

To release, first bump the version number in `setup.py`, commit the result,
then run:

```sh
pip install twine
python setup.py sdist bdist_wheel
twine check dist/* # optional; check for common issues
twine upload dist/*
```

For ease of browsing by users, you should also cut a release on GitHub.
