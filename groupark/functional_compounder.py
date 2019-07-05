from typing import List, Callable
from itertools import groupby


class FunctionalCompounder:

    def __init__(self) -> None:
        self.operations = {
            'count': lambda field, values: sum(1 for _ in values),
            'sum': lambda field, values: sum(row[field] for row in values)
        }

    def compound(self, groups: List[str],
                 aggregations: List[str]=None) -> Callable:

        if not aggregations:
            aggregations = [f"count:{next(iter(groups))}"]

        def aggregator(data):
            def key_function(item):
                return tuple(item[group] for group in groups)

            data = sorted(data, key=key_function)

            result = []
            for section, values in groupby(data, key_function):
                row = {}
                if len(aggregations) > 1:
                    values = list(values)

                for index, element in enumerate(section):
                    row[groups[index]] = element

                for aggregation in aggregations:
                    operator, field = aggregation.split(':')
                    composite = self.operations[operator](field, values)
                    row[f"{operator}_{field}"] = composite

                result.append(row)

            return result

        return aggregator
