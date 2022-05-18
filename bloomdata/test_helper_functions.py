import bloomdata.helper_functions as hf

adjectives = ['blue', 'large', 'grainy', 'substantial', 'potent', 'thermonuclear']
nouns = ['food', 'house', 'tree', 'bicycle', 'toupee', 'phone']

def test_random_phrase():
    assert type(hf.random_phrase(adjectives, nouns)) == str
    assert type(hf.random_phrase(adjectives, nouns).split(' ')[0]) == str
    assert type(hf.random_phrase(adjectives, nouns).split(' ')[1]) == str
    assert hf.random_phrase(adjectives, nouns).split(' ')[0] in adjectives
    assert hf.random_phrase(adjectives, nouns).split(' ')[1] in nouns
    assert hf.random_phrase(['Ryan'], ['Allred']) == 'Ryan Allred'
    assert hf.random_phrase([3], [4]) == '3 4'