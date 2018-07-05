import unittest

from labels import Label

######################################################################
#  T E S T   C A S E S
######################################################################
class TestImageFeature(unittest.TestCase):
    """ Test Cases for Label class(es) """

    def test_basic_label(self):
        """ Test whether Label class functions well """
        label = Label(name='Test', options=['Test1','Test2'])

        self.assertEqual(label.name, 'Test')

        self.assertEqual(label.id2name(0), 'Test1')
        self.assertEqual(label.id2name(1), 'Test2')
        with self.assertRaises(AssertionError):
            label.id2name(2)
        with self.assertRaises(AssertionError):
            label.id2name(-1)

        self.assertEqual(label.name2id('Test1'), 0)
        self.assertEqual(label.name2id('Test2'), 1)
        with self.assertRaises(AssertionError) as err:
            label.name2id('Test3')
    
######################################################################
#   M A I N
######################################################################
if __name__ == '__main__':
    unittest.main()