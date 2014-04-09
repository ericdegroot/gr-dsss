/* -*- c++ -*- */

#define DSSS_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "dsss_swig_doc.i"

%{
#include "dsss/dsss_encoder_bb.h"
#include "dsss/dsss_decoder_cc.h"
%}


%include "dsss/dsss_encoder_bb.h"
GR_SWIG_BLOCK_MAGIC2(dsss, dsss_encoder_bb);
%include "dsss/dsss_decoder_cc.h"
GR_SWIG_BLOCK_MAGIC2(dsss, dsss_decoder_cc);
