def scramble(seq):
    for i in range(len(seq)):
        yield seq[i:] + seq[:i]

scramble2 = lambda seq: (seq[i:] + seq[i:] for i in range(len(seq)))
