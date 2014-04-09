#!/usr/bin/env python
# 
# Copyright 2013 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import time
import random

from gnuradio import gr, gr_unittest
from gnuradio import blocks
import dsss_swig as dsss

def py_encode(data, code):
    out = []
    for d in data:
        for c in code:
            out.append(d ^ c)
    return out

class qa_dsss_encoder_bb (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_dsss_encoder_bb (self):
        code_length = 21
        code = [random.randint(0, 1) for u in xrange(code_length)]
        data_length = 164
        data = [random.randint(0, 1) for u in xrange(data_length)]
        expected_result = py_encode(data, code)
        src = blocks.vector_source_b (data)
        packer = blocks.unpacked_to_packed_bb(1, gr.GR_MSB_FIRST)
        dsss_encoder = dsss.dsss_encoder_bb(code)
        dst = blocks.vector_sink_b ()

        self.tb.connect (src, packer,  dsss_encoder, dst)
        self.tb.start ()
        time.sleep(0.1)
        self.tb.stop()

        actual_result = list(dst.data ())
        self.assertTrue(len(actual_result) > len(expected_result)/2)
        self.assertEqual(actual_result, expected_result[:len(actual_result)])

if __name__ == '__main__':
    gr_unittest.run(qa_dsss_encoder_bb, "qa_dsss_encoder_bb.xml")
