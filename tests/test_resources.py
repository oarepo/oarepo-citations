from oarepo_citations.resources import csl_url_args_retriever


def test_csl_url_args_retriever_uses_query_parameters(create_app):
    app = create_app()

    with app.test_request_context("/?style=apa&locale=en-US"):
        style, locale = csl_url_args_retriever()

    assert style == "apa"
    assert locale == "en-US"


def test_csl_url_args_retriever_builds_locale_when_missing(create_app):
    app = create_app()

    with app.test_request_context("/?style=iso690-author-date-cs"):
        style, locale = csl_url_args_retriever()

    assert style == "iso690-author-date-cs"
    # Locale is derived from Babel territory lookup = most popular locale for the app's current language
    assert locale == "en-AG"
