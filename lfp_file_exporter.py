#!/usr/bin/env python
#
# lfp-reader
# LFP (Light Field Photography) File Reader.
#
# http://behnam.github.com/python-lfp-reader/
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Copyright (C) 2012  Behnam Esfahbod


"""Export LFP file into separate data files
"""


import os.path
import sys

from lfp_reader import LfpGenericFile


def usage(errcode=0, of=sys.stderr):
    print ("Usage: %s file.lfp [file-2.lfp ...]" %
            os.path.basename(sys.argv[0]))
    sys.exit(errcode)

if __name__=='__main__':
    if len(sys.argv) < 2:
        usage()

    for lfp_path in sys.argv[1:]:
        try:
            lfp = LfpGenericFile(lfp_path).load()
            lfp.export()
        except Exception as err:
            print >>sys.stderr, "Error:", err
            exit(1)

