import csv
from pathlib import Path


def read_csv(path):
    with Path(path).open() as f:
        f.readline()  # skip the first line with indexes
        reader = csv.reader(f, delimiter=',', quotechar='"')
        __, ___, *people = next(reader)
        traits = []
        for idx, line in enumerate(reader, start=1):
            _id_, trait, *matches = line
            matched = set()
            for mid, maybe_match in enumerate(matches):
                if maybe_match == 'x':
                    matched.add(people[mid])
            traits.append((idx, trait, matched))
        return traits
