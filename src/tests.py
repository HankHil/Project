import unittest

from utils import parse_command


class MyTestCase(unittest.TestCase):
    def test_parse_command(self):
        self.assertEqual(parse_command('add ivan_ivanov 123-1345-2323-2'),
                         ('add', 'ivan_ivanov 123-1345-2323-2'))

    def test_parse_command_two(self):
        self.assertEqual(parse_command('add "Иванов Иван Иванович" "+9 1223 222 22 22"'),
        ('add', '"Иванов Иван Иванович" "+9 1223 222 22 22"'))
    # add assertion here


if __name__ == '__main__':
    unittest.main()
