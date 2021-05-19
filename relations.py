from dataclasses import dataclass


@dataclass(frozen=True, order=False)
class Relation:
    r: tuple

    def inverse(self):
        return Relation((self.r[1], self.r[0]))


class Graph:
    def __init__(self, state_set, sequence):
        self.set = state_set
        self.permutations = 2**(len(self.set)**2)

        if type(sequence) == int:
            if sequence >= self.permutations:
                raise Exception("Sequence out of bounds (seq > permutations)")

            sequence = list(map(int, list(bin(sequence)[:1:-1])))
            sequence += [0] * (len(self.set)**2 - len(sequence))

        self.sequence = sequence
        self.relations = self.create_graph()

    def __repr__(self):
        string = ''
        for relation in sorted(self.relations):
            string += f'{(self.relations[relation])}\n'
        return string[:-1]

    def create_graph(self):
        rel = {}
        i = 0
        for x in self.set:
            for y in self.set:
                if self.sequence[i]:
                    rel[hash(Relation((x, y)))] = Relation((x, y))
        return rel


if __name__ == '__main__':

    print(Graph(['a', 'b', 'c'], 23))
