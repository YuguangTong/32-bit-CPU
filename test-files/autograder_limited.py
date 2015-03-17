#!/usr/bin/env python

import autograder_base
import os.path

from autograder_base import file_locations, AbsoluteTestCase, FractionalTestCase, main

tests = [
  ("ALU addu test",AbsoluteTestCase(os.path.join(file_locations,'ALU-addu.circ'),os.path.join(file_locations,'out-files/ALU-addu.out'),1)),
  ("ALU shift test",AbsoluteTestCase(os.path.join(file_locations,'ALU-shift.circ'),os.path.join(file_locations,'out-files/ALU-shift.out'),1)),
  ("ALU add test",AbsoluteTestCase(os.path.join(file_locations,'ALU-add.circ'),os.path.join(file_locations,'out-files/ALU-add.out'),1)),
  ("ALU sub test",AbsoluteTestCase(os.path.join(file_locations,'ALU-sub.circ'),os.path.join(file_locations,'out-files/ALU-sub.out'),1)),
  ("ALU slt test",AbsoluteTestCase(os.path.join(file_locations,'ALU-slt.circ'),os.path.join(file_locations,'out-files/ALU-slt.out'),1)),
  ("ALU bitpal/lfsr test",AbsoluteTestCase(os.path.join(file_locations,'ALU-bitpal-lfsr.circ'),os.path.join(file_locations,'out-files/ALU-bitpal-lfsr.out'),1)),
  ("RegFile insert test",AbsoluteTestCase(os.path.join(file_locations,'reg-insert.circ'),os.path.join(file_locations,'out-files/reg-insert.out'),1)),
]

if __name__ == '__main__':
  main(tests)
