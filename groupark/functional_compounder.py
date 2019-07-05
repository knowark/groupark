from itertools import groupby


class FunctionalCompounder:

    def compound(self, groups):
        def aggregator(data):

            def key_function(item):
                return tuple(item[group] for group in groups)

            data = sorted(data, key=key_function)

            result = []
            for section, values in groupby(data, key_function):
                row = {}
                operation = 'count'

                for index, element in enumerate(section):
                    row[groups[index]] = element

                composite = sum(1 for _ in values)

                row[f"{operation}_{'_'.join(groups)}"] = composite

                result.append(row)

            return result

        return aggregator
