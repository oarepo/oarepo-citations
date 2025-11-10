import pytest

from oarepo_citations.resources.csl.csl_to_bibtex import (
    create_bibtex_entry,
    get_bibtex_type,
    map_resource_type_to_bibtex,
)


@pytest.mark.parametrize(
    "resource_type,expected",
    [
        ("report", "techreport"),
        ("article", "article"),
        ("paper-conference", "inproceedings"),
        ("unknown-type", "misc"),
    ],
)
def test_map_resource_type_to_bibtex(resource_type, expected):
    assert map_resource_type_to_bibtex(resource_type) == expected


def test_create_bibtex_entry_with_full_metadata():
    csl_data = {
        "type": "article",
        "author": [
            {"family": "Doe", "given": "John"},
            {"family": "Roe", "given": "Jane"},
        ],
        "title": "A Sample Article",
        "issued": {"date-parts": [[2023, 5, 17]]},
        "DOI": "10.1234/example",
        "publisher": "Test Publisher",
    }

    bibtex = create_bibtex_entry(csl_data, "record-id")

    assert bibtex == (
        "@article{record-id,\n"
        "author = {Doe, John and Roe, Jane},\n"
        "title = {A Sample Article},\n"
        "year = {2023},\n"
        "month = {5},\n"
        "day = {17},\n"
        "publisher = \"Test Publisher\",\n"
        "doi = {10.1234/example}\n"
        "}\n"
    )


def test_create_bibtex_entry_without_optional_fields():
    csl_data = {
        "type": "dataset",
        "title": "Open Dataset",
        "issued": {"date-parts": [[2022]]},
    }

    bibtex = create_bibtex_entry(csl_data, "dataset-id")

    assert "@misc{dataset-id" in bibtex
    assert "year = {2022}" in bibtex
    assert "month" not in bibtex
    assert "author" not in bibtex


def test_get_bibtex_type_returns_dataset():
    assert get_bibtex_type("any-type") == "dataset"
