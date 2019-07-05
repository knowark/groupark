from pytest import fixture
from groupark.functional_compounder import FunctionalCompounder


@fixture
def dataset():
    return [
        {'name': 'Mazda 3', 'type': 'sedan', 'year': '2018', 'price': 21000},
        {'name': 'Corolla', 'type': 'sedan', 'year': '2019', 'price': 25000},
        {'name': 'Tesla M3', 'type': 'sedan', 'year': '2020', 'price': 51000},
        {'name': 'GMC', 'type': 'truck', 'year': '2019', 'price': 60000},
        {'name': 'Mercedes', 'type': 'sedan', 'year': '2020', 'price': 70000},
        {'name': 'Wolkswagen', 'type': 'van', 'year': '2020', 'price': 30000},
        {'name': 'BMW', 'type': 'sedan', 'year': '2019', 'price': 65000},
        {'name': 'Ford F150', 'type': 'truck', 'year': '2019', 'price': 70000},
        {'name': 'Chrysler', 'type': 'van', 'year': '2018', 'price': 45000},
        {'name': 'Kia', 'type': 'suv', 'year': '2020', 'price': 47000},
        {'name': 'Jeep', 'type': 'truck', 'year': '2020', 'price': 43000},
        {'name': 'Audi Q8', 'type': 'suv', 'year': '2019', 'price': 67000}
    ]


def test_functional_compounder_instantiation():
    compounder = FunctionalCompounder()
    assert compounder is not None


def test_functional_compounder_compound(dataset):
    compounder = FunctionalCompounder()

    groups = ['type']
    aggregator = compounder.compound(groups=groups)

    result = aggregator(dataset)

    assert result == [
        {'type': 'sedan', 'count_type': 5},
        {'type': 'suv', 'count_type': 2},
        {'type': 'truck', 'count_type': 3},
        {'type': 'van', 'count_type': 2}
    ]


def test_functional_compounder_other_key(dataset):
    compounder = FunctionalCompounder()

    groups = ['year']
    aggregator = compounder.compound(groups=groups)

    result = aggregator(dataset)

    assert result == [
        {'year': '2018', 'count_year': 2},
        {'year': '2019', 'count_year': 5},
        {'year': '2020', 'count_year': 5}
    ]


def test_functional_compounder_two_groups(dataset):
    compounder = FunctionalCompounder()

    groups = ['year', 'type']
    aggregator = compounder.compound(groups=groups)

    result = aggregator(dataset)

    assert result == [
        {'year': '2018', 'type': 'sedan', 'count_year': 1},
        {'year': '2018', 'type': 'van', 'count_year': 1},
        {'year': '2019', 'type': 'sedan', 'count_year': 2},
        {'year': '2019', 'type': 'suv', 'count_year': 1},
        {'year': '2019', 'type': 'truck', 'count_year': 2},
        {'year': '2020', 'type': 'sedan', 'count_year': 2},
        {'year': '2020', 'type': 'suv', 'count_year': 1},
        {'year': '2020', 'type': 'truck', 'count_year': 1},
        {'year': '2020', 'type': 'van', 'count_year': 1}
    ]


def test_functional_compounder_two_groups_inverted(dataset):
    compounder = FunctionalCompounder()

    groups = ['type', 'year']
    aggregator = compounder.compound(groups=groups)

    result = aggregator(dataset)

    assert result == [
        {'type': 'sedan', 'year': '2018', 'count_type': 1},
        {'type': 'sedan', 'year': '2019', 'count_type': 2},
        {'type': 'sedan', 'year': '2020', 'count_type': 2},
        {'type': 'suv', 'year': '2019', 'count_type': 1},
        {'type': 'suv', 'year': '2020', 'count_type': 1},
        {'type': 'truck', 'year': '2019', 'count_type': 2},
        {'type': 'truck', 'year': '2020', 'count_type': 1},
        {'type': 'van', 'year': '2018', 'count_type': 1},
        {'type': 'van', 'year': '2020', 'count_type': 1}
    ]


def test_functional_compounder_single_aggregation(dataset):
    compounder = FunctionalCompounder()

    groups = ['year']
    aggregations = ['sum:price']

    aggregator = compounder.compound(groups=groups, aggregations=aggregations)

    result = aggregator(dataset)

    assert result == [
        {'year': '2018', 'sum_price': 66000},
        {'year': '2019', 'sum_price': 287000},
        {'year': '2020', 'sum_price': 241000}
    ]
