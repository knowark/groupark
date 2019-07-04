from itertools import groupby


class FunctionalCompounder:

    def compound(self, groups):
        def aggregator(data):

            def key_function(item):
                return tuple(item[group] for group in groups)

            data = sorted(data, key=key_function)

            result = []
            for group, values in groupby(data, key_function):
                row = {}
                operation = 'count'

                composite = sum(1 for _ in values)

                row[f"{groups[0]}"] = group[0]
                row[f"{operation}_{groups[0]}"] = composite

                result.append(row)

            return result

        return aggregator
