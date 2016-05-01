from types import ListType
from unittest import TestCase, main
import ThesaurusDistance

thesaurus_distance = ThesaurusDistance.thesaurus_distance

class ThesaurusDistanceTestCase(TestCase):
    def test_src_target_same(self):
        self.assertEqual(thesaurus_distance('dog', 'dog'), [])

    def test_no_path(self):
        self.assertEqual(thesaurus_distance('xyz', 'abc'), None)

    def test_return_type(self):
        self.assertTrue(isinstance(
            thesaurus_distance('dog', 'diaper'),
            ListType))

    def test_route(self):
        orig_get_synonyms = ThesaurusDistance.get_synonyms
        def _mock_get_synonyms(word):
            if word == 'abc':
                return ['def']
            elif word == 'def':
                return ['hij']
            elif word == 'hij':
                return ['klm']

            return orig_get_synonyms(word)
        ThesaurusDistance.get_synonyms = _mock_get_synonyms

        self.assertEqual(thesaurus_distance('abc', 'klm'), ['def', 'hij'])

        ThesaurusDistance.get_synonyms = orig_get_synonyms

if __name__ == '__main__':
    main()
