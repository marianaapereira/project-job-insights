from src.pre_built.counter import count_ocurrences

PATH = 'data/jobs.csv'
WORD_PY = 'Python'
WORD_JS = 'Javascript'

def test_counter():
    'Returns the correct number of ocurrences of "Python"'
    assert count_ocurrences(PATH, WORD_PY) is 1639

    'Returns the correct number of ocurrences of "Javascript"'
    assert count_ocurrences(PATH, WORD_JS) is 122
