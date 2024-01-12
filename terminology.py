import json

class Term:
    def __init__(self, term, keywords=[]):
        self._term = term

    @property
    def acronym(self):
        words = self._term.split()
        letters = [word[0] for word in words]
        return ''.join(letters)
    
    def matches(self, keyword):
        for k in self._keywords:
            if keyword in k:
                return True
        return False