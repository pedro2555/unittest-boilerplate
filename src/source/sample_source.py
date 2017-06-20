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
class SampleSource(object):

	def __init__(self):
		self.text = "It Works!"

	def IsEven(self, n):
	    return n % 2 == 0