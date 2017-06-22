#!/usr/bin/env python
"""
unittest boilerplate.
Copyright (C) 2017  Pedro Rodrigues <prodrigues1990@gmail.com>

unittest boilerplate is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 2 of the License.

unittest boilerplate is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with unittest boilerplate.  If not, see <http://www.gnu.org/licenses/>.
"""
import unittest
from src import sample

class Sample_test(unittest.TestCase):

	def test_merge_sort(self):

		# base case test
		case = [3]
		self.assertEqual(sample.merge_sort(case), case)

		# even sized sort
		case = [1, 5, 2, 7]
		self.assertEqual(sample.merge_sort(case), [1, 2, 5, 7])

		# odd sized sort
		case = [7, 1, 2]
		self.assertEqual(sample.merge_sort(case), [1, 2, 7])

	def test_merge(self):

		# even sized sort
		case1 = [1, 3]
		case2 = [2, 4]
		self.assertEqual(sample.merge(case1, case2), [1, 2, 3, 4])

		# odd sized sort
		case1 = [1, 3]
		case2 = [4]
		self.assertEqual(sample.merge(case1, case2), [1, 3, 4])

if __name__ == '__main__':
    unittest.main()
