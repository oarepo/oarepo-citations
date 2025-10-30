import pytest
from werkzeug.exceptions import BadRequest

from oarepo_citations.resources.validators import validate_locale, validate_style


def test_validate_style_returns_none_for_empty_input():
    assert validate_style(None) is None


def test_validate_style_accepts_valid_style():
    # "apa" is bundled with citeproc-styles distribution
    assert validate_style("apa") == "apa"


@pytest.mark.parametrize(
    "payload,expected",
    [
        ("bad\x00style", "contains null byte"),
        ("../secret", "path traversal"),
        ("invalid style", "only alphanumeric"),
    ],
)
def test_validate_style_rejects_bad_inputs(payload, expected):
    with pytest.raises(BadRequest, match=expected):
        validate_style(payload)


def test_validate_style_raises_for_unknown_style():
    with pytest.raises(BadRequest, match="style 'missing-style' not found"):
        validate_style("missing-style")


def test_validate_locale_returns_none_for_empty_input():
    assert validate_locale(None) is None


@pytest.mark.parametrize("payload", ["en-US", "en_US", "en"])
def test_validate_locale_accepts_common_inputs(payload):
    assert validate_locale(payload) == payload


@pytest.mark.parametrize(
    "payload,expected",
    [
        ("cs\x00CZ", "contains null byte"),
        ("../cs-CZ", "path traversal"),
        ("czechia", "must be in format"),
    ],
)
def test_validate_locale_rejects_bad_inputs(payload, expected):
    with pytest.raises(BadRequest, match=expected):
        validate_locale(payload)


def test_validate_locale_propagates_unknown_locale():
    with pytest.raises(BadRequest, match="Invalid locale parameter"):
        validate_locale("zz-ZZ")
