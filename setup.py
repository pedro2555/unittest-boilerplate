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
from setuptools import setup, find_packages

setup(
    name='unittest boilerplate',
    version='0.1',
    description = 'unittest boilerplate',
    author = 'Pedro Rodrigues',
    author_email = 'prodrigues1990@gmail.com',
    packages = find_packages(),
    install_requires = [],
    test_requires = ['lint'],
    test_suite = 'tests'                      
)
