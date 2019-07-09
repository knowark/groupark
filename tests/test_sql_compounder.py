from pytest import fixture
from groupark.sql_compounder import SqlCompounder


def test_sql_compounder_instantiation():
    compounder = SqlCompounder()
    assert compounder is not None


def test_sql_compounder_compound():
    compounder = SqlCompounder()

    groups = ['type']
    expected = ("COUNT(type)", "type")

    result = compounder.compound(groups=groups)

    assert result == expected


def test_sql_compounder_two_groups():
    compounder = SqlCompounder()

    groups = ['year', 'type']
    expected = ("COUNT(year)", "year, type")

    result = compounder.compound(groups=groups)

    assert result == expected


def test_sql_compounder_double_aggregation():
    compounder = SqlCompounder()

    groups = ['type', 'year']
    aggregations = ['sum:price', 'count:name']
    expected = ("SUM(price), COUNT(name)", "type, year")

    result = compounder.compound(groups=groups, aggregations=aggregations)

    assert result == expected
