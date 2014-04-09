/* -*- c++ -*- */
/* 
 * Copyright 2014 Eric de Groot (edegroot@email.arizona.edu).
 * 
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 * 
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */


#ifndef INCLUDED_DSSS_DSSS_DECODER_CC_H
#define INCLUDED_DSSS_DSSS_DECODER_CC_H

#include <dsss/api.h>
#include <gnuradio/block.h>

namespace gr {
  namespace dsss {

    /*!
     * \brief DSSS Decoder
     * \ingroup dsss
     *
     */
    class DSSS_API dsss_decoder_cc : virtual public gr::block
    {
     public:
      typedef boost::shared_ptr<dsss_decoder_cc> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of dsss::dsss_decoder_cc.
       *
       * To avoid accidental use of raw pointers, dsss::dsss_decoder_cc's
       * constructor is in a private implementation
       * class. dsss::dsss_decoder_cc::make is the public interface for
       * creating new instances.
       */
      static sptr make(const std::vector<int> &code, float samples_per_symbol);

      virtual std::vector<int> code() const = 0;
      virtual void set_code(const std::vector<int> &code) = 0;

      virtual std::vector<float> taps() const = 0;
    };

  } // namespace dsss
} // namespace gr

#endif /* INCLUDED_DSSS_DSSS_DECODER_CC_H */
