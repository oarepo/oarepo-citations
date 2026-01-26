import pytest
from werkzeug.exceptions import BadRequest

from oarepo_citations.resources import csl_url_args_retriever


def test_csl_url_args_retriever_uses_query_parameters(create_app):
    app = create_app()

    with app.test_request_context("/?style=apa&locale=en-US"):
        style, locale = csl_url_args_retriever()

    assert style == "apa"
    assert locale == "en-US"

    
@pytest.mark.parametrize(
    "query,expected_style,expected_locale",
    [
        ("/?style=apa&locale=en", "apa", "en"),
        ("/?style=apa&locale=cs", "apa", "cs"),
        ("/?locale=cs", "apa", "cs"),
        ("/?style=iso690-author-date-cs", "iso690-author-date-cs", "en_US"),
        ("/", "apa", "en_US"),
    ],
)
def test_csl_url_args_retriever_fixes_style_or_locale(create_app, query, expected_style, expected_locale):
    app = create_app()

    with app.test_request_context(query):
        style, locale = csl_url_args_retriever()

    assert style == expected_style
    assert locale == expected_locale


@pytest.mark.parametrize(
    "query,expected",
    [
        ("/?style=../evil", "only alphanumeric characters, hyphens, and underscores allowed"),
        ("/?style=missing-style", "style 'missing-style' not found"),
    ],
)
def test_csl_url_args_retriever_rejects_invalid_style(create_app, query, expected):
    app = create_app()

    with app.test_request_context(query):
        with pytest.raises(BadRequest, match=expected):
            csl_url_args_retriever()


@pytest.mark.parametrize(
    "query,expected",
    [
        ("/?locale=../cs-CZ", "Invalid locale parameter"),
        ("/?locale=zz-ZZ", "Invalid locale parameter"),
    ],
)
def test_csl_url_args_retriever_rejects_invalid_locale(create_app, query, expected):
    app = create_app()

    with app.test_request_context(query):
        with pytest.raises(BadRequest, match=expected):
            csl_url_args_retriever()
