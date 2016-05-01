from nltk.corpus import wordnet

def get_synonyms(word):
    '''Return a list of synonyms for a given word.'''
    synonyms = []
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.append(lemma.name())
    return synonyms

def thesaurus_distance(src, target):
    '''Return an ordered list of synonyms that describe the path required
    to transform src into target. Returns None if no route exists.
    '''
    if src == target: return []

    reverse_syn = []  # format: [depth][synonym] = word
    src_set = set([src])
    tried = set()
    while(True):
        reverse_syn.append({})

        next_src = set()
        for w in src_set:
            syns = get_synonyms(w)
            for s in syns: reverse_syn[-1][s] = w

            if target in syns:
                path = []  # path from src -> target
                syn = target
                for depth in list(reversed(range(len(reverse_syn)))):
                    path.append(reverse_syn[depth][syn])
                    syn = path[-1]
                return list(reversed(path[:-1]))  # list does not include src or target

            tried.add(w)
            next_src.update(syns)

        src_set = next_src - tried
        # XXX should this be an exception?
        if not src_set: return None


if __name__ == '__main__':
    import csv
    import sys

    if not len(sys.argv) == 3:
        print "usage: {} <src> <target>".format(sys.argv[0])
        sys.exit(2)

    path = thesaurus_distance(*sys.argv[1:])
    if path:
        csv.writer(sys.stdout).writerow(path)
    else:
        print "no route found."
