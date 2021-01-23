from pytest import mark

from . import Indenter


def test_indent():
    ind = Indenter()
    with ind:
        assert str(ind) == "  "


def test_usage_without_with():
    ind = Indenter()
    assert str(ind) == ""


def test_inline():
    with Indenter() as ind:
        assert str(ind) == "  "


def test_start():
    ind = Indenter(start=1)
    assert str(ind) == "  "
    with ind:
        assert str(ind) == "    "


def test_nesting():
    ind = Indenter()
    with ind:
        assert str(ind) == "  "
        with ind:
            assert str(ind) == "    "
        assert str(ind) == "  "


def test_nesting_with_start():
    ind = Indenter(start=1)
    with ind:
        assert str(ind) == "    "
        with ind:
            assert str(ind) == "      "


def test_multiple_indenters():
    inda = Indenter(symbol="*")
    indb = Indenter(symbol="$")
    with inda:
        assert str(inda) == "*"
        with indb:
            assert str(inda) == "*"
            assert str(indb) == "$"
            with indb:
                assert str(inda) == "*"
                assert str(indb) == "$$"
                with inda:
                    assert str(inda) == "**"
                    assert str(indb) == "$$"


@mark.xfail(reason="str + ind calls str.__add__, which afaik we can't influence")
def test_add_ind_to_str():
    ind = Indenter()
    assert "some text" + ind == "some text"

    with ind:
        assert "some text" + ind == "  some text"


def test_add_str_to_ind():
    ind = Indenter()
    assert ind + "some text" == "some text"

    with ind:
        assert ind + "some text" == "  some text"


@mark.xfail(reason="str += ind calls str.__add__, which afaik we can't influence")
def test_iadd_ind_to_str():
    ind = Indenter()
    with ind:
        s = "some text"
        s += ind
        assert s == "some text  "


def test_iadd_str_to_ind():
    ind = Indenter()
    with ind:
        s = "some text"
        ind += s
        assert ind == "  some text"
