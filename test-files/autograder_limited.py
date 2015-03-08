#!/usr/bin/env python

import autograder_base
import os.path

from autograder_base import file_locations, AbsoluteTestCase, FractionalTestCase, main

tests = [
  ("ALU addu test",AbsoluteTestCase(os.path.join(file_locations,'ALU-addu.circ'),os.path.join(file_locations,'out-files/ALU-addu.out'),1)),
  ("ALU shift test",AbsoluteTestCase(os.path.join(file_locations,'ALU-shift.circ'),os.path.join(file_locations,'out-files/ALU-shift.out'),1)),
  ("RegFile insert test",AbsoluteTestCase(os.path.join(file_locations,'reg-insert.circ'),os.path.join(file_locations,'out-files/reg-insert.out'),1)),
]

if __name__ == '__main__':
  main(tests)
