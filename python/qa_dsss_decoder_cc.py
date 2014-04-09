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

from gnuradio import gr, gr_unittest
from gnuradio import blocks
import dsss_swig as dsss

class qa_dsss_decoder_cc (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
        code = ( 157, ) # ( 0b10011100, ) # ( 0b10011100, 0b01000101 ) # code = 01000101 10011100
        expected_result = ( 0, )
        src_data = ( 0, )
        src = blocks.vector_source_c (src_data)
        dsss_decoder = dsss.dsss_decoder_cc(code, 2)
        dst = blocks.vector_sink_c ()

        self.tb.connect (src, dsss_decoder)
        self.tb.connect (dsss_decoder, dst)
        self.tb.run ()

        actual_result = dst.data ()

        self.assertEqual(actual_result, expected_result)

if __name__ == '__main__':
    gr_unittest.run(qa_dsss_decoder_cc, "qa_dsss_decoder_cc.xml")
