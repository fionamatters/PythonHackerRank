import io
import random
import sys
from unittest import TestCase

from Solutions.BlackRock.Done.StockGrants import main


class TestSolution(TestCase):
    def test_initial_case(self):
        input_string = '''12
6 1 1 1 2 2 2 3 3 3 4 5
2 1 2 3 2 1 2 3 2 1 2 3
'''

        result = '''53
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())

    def test_case1(self):
        input_string = '''500
64 72 51 14 38 93 35 88 92 74 96 3 10 32 69 24 87 64 29 97 56 93 41 97 14 7 100 90 52 94 1 1 56 14 96 58 100 15 70 85 48 7 2 11 71 10 57 58 62 42 99 92 72 11 12 15 48 70 5 47 31 41 91 85 100 64 93 77 81 50 35 2 64 34 81 56 89 73 14 25 89 62 5 18 87 4 62 83 5 73 82 42 11 93 16 18 88 33 70 76 79 49 71 99 96 69 78 3 86 86 99 33 7 44 39 11 20 21 93 18 57 92 95 48 46 3 35 55 96 69 77 57 56 96 49 44 56 35 98 41 74 25 95 50 70 29 70 89 27 9 25 99 47 59 50 44 88 22 81 51 94 66 71 99 73 96 13 36 34 24 64 6 42 100 88 42 39 46 85 89 65 65 96 56 70 87 72 33 95 3 60 29 24 63 66 99 64 11 21 66 9 68 70 47 28 8 33 20 35 74 67 9 3 50 50 47 46 57 93 97 20 79 40 24 25 20 52 5 92 29 85 60 74 12 51 52 67 4 27 60 94 99 97 49 86 99 55 84 56 50 40 80 7 58 7 86 6 72 28 98 30 87 99 3 39 92 55 83 26 69 22 72 60 64 87 51 55 84 93 22 2 7 24 52 8 8 49 78 41 96 63 53 91 72 68 25 92 52 97 14 12 81 38 95 45 54 7 67 78 18 36 5 27 22 15 56 8 26 93 43 85 20 63 83 27 53 70 46 92 57 43 6 59 47 62 90 88 75 100 58 86 31 60 88 70 67 96 14 38 65 82 70 58 25 12 72 86 36 75 82 19 35 19 4 46 87 77 39 27 95 31 30 3 62 28 25 8 59 35 20 67 98 74 33 48 15 20 55 13 31 16 89 91 74 67 63 1 16 47 70 95 27 84 74 16 47 20 3 91 24 71 22 22 58 61 1 94 37 95 57 51 17 10 90 6 41 89 81 25 94 40 51 35 99 68 65 31 9 65 27 84 45 22 55 33 76 89 47 30 24 24 24 11 93 23 24 75 63 47 43 3 80 32 63 22 8 22 72 9 96 19 50 37 14 96 3 43 31 14 68 24 65 26 30 73 26 73 67 25 48 61 90 69 82 30 88 40 73 77 15
402 122 652 190 328 462 589 276 743 727 723 432 390 627 313 496 71 348 375 112 645 403 123 212 295 212 650 517 325 653 102 102 456 167 337 37 522 360 558 634 104 334 307 219 177 320 421 176 121 617 323 179 728 618 129 325 703 393 289 684 793 458 44 324 332 685 534 131 623 696 738 137 59 143 780 17 65 284 111 99 478 746 267 282 656 63 746 472 636 153 731 168 123 492 203 729 529 103 71 737 277 613 678 124 304 683 372 352 621 357 292 55 725 648 226 142 34 529 547 143 790 732 702 742 552 461 428 767 528 361 531 138 223 96 452 583 186 48 369 151 524 103 13 88 275 353 601 630 606 53 682 46 185 386 29 726 342 111 97 85 363 243 797 142 172 86 603 263 481 434 377 402 144 221 452 362 315 44 152 721 579 426 139 584 325 330 34 149 641 339 299 732 587 637 313 667 726 422 56 390 169 80 646 289 380 91 489 38 312 99 52 304 160 424 179 569 111 93 655 610 759 628 615 592 690 767 276 261 71 182 382 331 301 264 542 698 40 763 316 715 516 169 234 222 795 314 141 228 797 236 188 216 325 696 668 592 771 294 551 214 112 784 218 755 756 340 352 68 749 72 124 232 330 215 109 744 195 652 455 221 178 13 664 251 582 38 528 516 614 116 775 622 434 758 9 80 373 709 388 13 338 180 601 769 37 108 376 122 776 299 48 497 134 556 457 144 628 56 444 165 249 137 447 500 759 646 179 562 506 758 99 323 789 549 772 151 685 145 228 11 739 194 71 774 152 313 93 709 112 115 455 326 366 501 47 657 405 738 624 21 732 233 253 312 710 537 172 389 684 571 470 633 91 13 189 336 204 416 94 667 511 94 729 697 226 341 97 566 436 387 136 275 483 313 354 272 319 312 399 540 312 120 75 454 787 137 745 444 189 61 450 12 584 727 6 777 383 212 346 74 698 575 386 157 252 575 128 58 800 508 196 773 3 759 275 716 145 162 543 556 568 528 637 379 723 337 663 633 654 242 537 102 113 82 147 340 26 492 515 551 111 252 494 783 698 592 243 411 555 234 340 86 665 308 785 400 300 21 589 234 455 785 131 533 452 717 489 302 660 752 465 86 48 773 788 521 685 610 594 536
'''

        result = '''53
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())

    def test_write_case(self):
       # f = open('test_StockGrants.in','w')
        max_val = 200000
        for i in range(50):
            print("%s %s"%(random.randint(1,1000),random.randint(0,100)))
        #print('100000 5.5 20 15\n')
        #print(" ".join([str(random.randint(1,100)) for a in range(20)])+"\n")
        count =100000
        num1 = 100000
        num2 = 100000
        #f.write(str(count)+"\n")
        #f.write(" ".join([str(random.randint(1,num1)) for a in range(count)])+"\n")
        #f.write(" ".join([str(random.randint(1,num2)) for a in range(count)])+"\n")

    def test_case_file1(self):
        file_input = open('test_StockGrants.in')
        sys.stdin = file_input
        sys.stdout = io.StringIO()
        main()
        self.assertEqual('356', sys.stdout.getvalue().strip())

        #   def test_case1(self):
        #       file_input = open('GridChallenge.in')
        #       expected_output = open('GridChallenge.out')
        #       sys.stdin = file_input
        #       sys.stdout = io.StringIO()
        #       main()
        #       self.assertEqual(expected_output.read().strip(), sys.stdout.getvalue().strip())