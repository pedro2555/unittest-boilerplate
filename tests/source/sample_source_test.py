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
from src.source.sample_source import SampleSource

class SampleSource_test(unittest.TestCase):

	def setUp(self):
		self.s = SampleSource()

	def test___init__(self):
		self.assertTrue(self.s.text == 'It Works!')

	def test_IsEven(self):
		self.assertTrue(self.s.IsEven(0))
		self.assertFalse(self.s.IsEven(1))
		self.assertTrue(self.s.IsEven(2))

if __name__ == '__main__':
    unittest.main()