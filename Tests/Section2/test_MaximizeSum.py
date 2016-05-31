from unittest import TestCase
import sys
import io
from Section2.MaximizeSum import main


class TesMaximizeSum(TestCase):
    def test_initial_case(self):
        input_string = '''1
5 7
3 3 9 9 5
'''

        result = '''6
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())

    def test_case1(self):
        file_input = open('test_MaxSum1.in')
        expected_output = open('test_MaxSum1.out')
        sys.stdin = file_input
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(expected_output.read().strip(), sys.stdout.getvalue().strip())

    def test_case2(self):
        input_string = "1\n" + \
                       "50 1804289384\n" + \
                       "846930887 1681692778 1714636916 1957747794 424238336 719885387 1649760493 596516650 " \
                       "1189641422 1025202363 1350490028 783368691 1102520060 2044897764 1967513927 1365180541 " \
                       "1540383427 304089173 1303455737 35005212 521595369 294702568 1726956430 336465783 861021531 " \
                       "278722863 233665124 2145174068 468703136 1101513930 1801979803 1315634023 635723059 " \
                       "1369133070 1125898168 1059961394 2089018457 628175012 1656478043 1131176230 1653377374 " \
                       "859484422 1914544920 608413785 756898538 1734575199 1973594325 149798316 2038664371 1129566414"

        result = "1802192837"
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result.strip(), sys.stdout.getvalue().strip())

    def test_case3(self):
        input_string = "1\n" + \
                       "50 184803527\n" + \
                       "412776092 1424268981 1911759957 749241874 137806863 42999171 982906997 135497282 511702306 " \
                       "2084420926 1937477085 1827336328 572660337 1159126506 805750847 1632621730 1100661314 " \
                       "1433925858 1141616125 84353896 939819583 2001100546 1998898815 1548233368 610515435 " \
                       "1585990365 1374344044 760313751 1477171088 356426809 945117277 1889947179 1780695789 " \
                       "709393585 491705404 1918502652 752392755 1474612400 2053999933 1264095061 1411549677 " \
                       "1843993369 943947740 1984210013 855636227 1749698587 1469348095 1956297540 1036140796 " \
                       "463480571"


        result = "184770427"
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result.strip(), sys.stdout.getvalue().strip())


    def test_small_case(self):
        input_string = '''1
5 20
1 3 2 4 5
'''

        result = '''15
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())


    def test_dinky_case(self):
        input_string = '''1
5 10
1 3 2 4 5
'''

        result = '''9
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())
