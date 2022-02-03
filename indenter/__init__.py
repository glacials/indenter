from copy import deepcopy

class Indenter:
    def __init__(self, start=0, symbol="  "):
        """
        Assists with programmatically indenting text to arbitrary levels
        using `with` blocks. Use like:

          with Indenter() as ind:
            print(ind + "Text to be indented")

        You can indent further by passing the same `Indenter` object to more
        `with` blocks:

          ind = Indenter()
          with ind: # ind is two spaces
            print(ind + "First-level indentation")
            with ind: # ind is four spaces
              print(ind + "Second-level indentation")
            # ind is two spaces again
            print(ind + "First-level indentation")

        Outputs:

            First-level indentation
              Second-level indentation
            First-level indentation

        The default indentation symbol is two spaces. You can override this
        by passing `symbol`:

          # Indent with 4 spaces per level
          with Indenter(symbol="    ") as ind:

          # Indent with tabs
          with Indenter(symbol="\t") as ind:

        When using custom symbols, nested `with`s will inherit the symbol of
        their parent. If you need more than one type of indentation at once,
        you must make and manage multiple `Indenter`s.

        The indenter starts at zero levels of indentation by default, and
        increases by one level for each `with` block. This can be overridden
        to start at other levels, such as 1:

          # Start with one level of indentation
          ind = Indenter(start=1)
          print(ind + "First-level indentation)
          with ind:
            print(ind + "Second-level indentation")
        """
        self.level = start
        self.symbol = symbol

    def __enter__(self) -> "Indent":
        """
        By definition, `with` calls this at its start. Adds one indentation
        level and returns the `Indenter` object itself, which allows uses of
        `with...as` like so:

          with Indenter() as ind:
            print(ind + "Indented text)

        This method's return value is assigned to the variable after `as`.
        """
        self.level += 1
        return self

    def __exit__(self, type, value, traceback) -> None:
        """
        By definition, `with` calls this at its end. Subtracts one
        indentation level.
        """
        self.level -= 1

    def __str__(self):
        """
        Returns the current indentation as a string.
        """
        return self.level * self.symbol

    def __add__(self, other):
        """
        Indent the given text, or increase the indentation level by the given amount.

        If `other` is an `Indenter`, the returned `Indenter` has an indentation level of
        `self.level + other.level`.

        If `other` is an integer, the returned `Indenter` has an indentation level of
        `self.level + other`.

        Otherwise, `other` is indented.

        Examples:

        ```python
        ind = Indenter()
        str(ind)             # ""
        str(ind + "abc")     # "abc"

        with ind:
            str(ind + "abc") # "  abc"

        str(ind + 1)         # "  "
        str(ind + 1 + "abc") # "  abc"
        str(ind + 2)         # "    "

        ind_b = ind + 1
        str(ind + ind_b)     # "  abc"
        ```
        """

        if isinstance(other, Indenter):
            new = deepcopy(self)
            new.level += other.level
            return new
        elif isinstance(other, int):
            new = deepcopy(self)
            new.level += other
            return new

        return self.__str__() + other


    def __sub__(self, other):
        """
        Return a new `Indenter` whose indentation level is `other` less than this one's.

        If `other` is an `Indenter`, the returned `Indenter` has an indentation level of
        `self.level - other.level`.

        If `other` is any other type, the returned `Indenter` has an indentation level
        of `self.level - other`.
        """
        new = deepcopy(self)

        if isinstance(other, Indenter):
            new.level -= other.level
        else:
            new.level -= other

        return new
