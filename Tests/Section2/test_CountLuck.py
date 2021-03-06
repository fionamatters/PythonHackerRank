from unittest import TestCase
import sys
import io
from Section2.CountLuck import main


class TestCountLuck(TestCase):
    def test_initial_case(self):
        input_string = '''3
2 3
*.M
.X.
1
4 11
.X.X......X
.X*.X.XXX.X
.XX.X.XM...
......XXXX.
3
4 11
.X.X......X
.X*.X.XXX.X
.XX.X.XM...
......XXXX.
4
'''

        result = '''Impressed
Impressed
Oops!
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())



    def test_case1(self):
        input_string = '''7
5
1 1 1 0 1
0 0 1 0 0
1 1 0 1 0
0 1 1 0 0
0 0 0 0 0
0 1 0 0 0
0 0 1 1 0
'''

        result = '''9
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())

    def test_case2(self):
        input_string = '''5
5
0 1 1 1 1
1 0 0 0 1
1 1 0 1 0
0 1 0 1 1
0 1 1 1 0
'''

        result = '''15
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())


