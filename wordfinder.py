from random import choice

"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    """Machine for finding random words from dictionary.
    
    >>> wf = WordFinder("simple.txt")
    3 words read

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True
    """

    def __init__(self, path):
        dict_file = open(path);
        self.words = self.parse(dict_file);
        print (F"{len(self.words)} words read")

    def parse (self, file):
        """reads the file and returns the array of words withougt '/n line"""
        return [word.strip() for word in file]

    def random(self):
        return choice (self.words)



class SpecialWordFinder (WordFinder):
    """Specialized WordFinder that excludes blank lines/comments.
    
    >>> swf = SpecialWordFinder("groceries.txt")
    4 words read

    >>> swf.random() in ["carrot", "kale", "pear", "mango"]
    True

    >>> swf.random() in ["carrot", "kale", "pear", "mango"]
    True

    >>> swf.random() in ["carrot", "kale", "pear", "mango"]
    True

    >>> swf.random() in ["carrot", "kale", "pear", "mango"]
    True

    """
    
    def parse (self, file):
        """Parse dict_file -> list of words, skipping blanks/comments."""
        return [w.strip() for w in file if w.strip() and not w.startswith ("#")]
