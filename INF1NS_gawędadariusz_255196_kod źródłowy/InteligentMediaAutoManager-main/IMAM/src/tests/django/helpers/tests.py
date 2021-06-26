import unittest

from form_to_python.helpers.commentService import toJsonFormatedDict


class MyTestCase(unittest.TestCase):
    def test_toJsonFormatedDictFunction(self):
        setting = {
            'author_name': "Patrick",
            'description': "Test case",
            'commentsSet': [{
                'mandatory_words': ["words", "are", "ducks"],
                'comments': ["My favorite place is Zalesie"]
            }]}
        result = toJsonFormatedDict(setting)
        expected = {'author_name': 'Patrick',
                    'commentsSet': [{'comments': ['My favorite place is Zalesie'],
                                     'mandatory_words': ['words', 'are', 'ducks']}],
                    'description': 'Test case'}
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
