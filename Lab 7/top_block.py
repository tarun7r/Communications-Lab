#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# GNU Radio version: 3.7.13.5
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.filter import pfb
from gnuradio.wxgui import forms
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from math import pi
from math import sqrt
from optparse import OptionParser
import numpy
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")
        _icon_path = "C:\Program Files\GNURadio-3.7\share\icons\hicolor\scalable/apps\gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 4
        self.nfilts = nfilts = 32
        self.ntaps = ntaps = 11*nfilts*sps
        self.excess_bw = excess_bw = 0.4
        self.tx_taps = tx_taps = firdes.root_raised_cosine(nfilts, nfilts, 1.1, 0.4, ntaps)
        self.timing_bw = timing_bw = 2*pi/100
        self.samp_rate_0 = samp_rate_0 = 20000*sps
        self.samp_rate = samp_rate = 32000
        self.rx_taps = rx_taps = firdes.root_raised_cosine(nfilts, nfilts, 1.0, excess_bw, ntaps)
        self.gain_control = gain_control = 0
        self.freq_bw = freq_bw = 2*pi/100
        self.fll_ntaps = fll_ntaps = 55
        self.const_points = const_points = 4
        self.b4 = b4 = 0
        self.b3 = b3 = 0
        self.b2 = b2 = 0
        self.b1 = b1 = 0

        ##################################################
        # Blocks
        ##################################################
        _b4_sizer = wx.BoxSizer(wx.VERTICAL)
        self._b4_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_b4_sizer,
        	value=self.b4,
        	callback=self.set_b4,
        	label='b4',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._b4_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_b4_sizer,
        	value=self.b4,
        	callback=self.set_b4,
        	minimum=-1,
        	maximum=1,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_b4_sizer)
        _b3_sizer = wx.BoxSizer(wx.VERTICAL)
        self._b3_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_b3_sizer,
        	value=self.b3,
        	callback=self.set_b3,
        	label='b3',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._b3_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_b3_sizer,
        	value=self.b3,
        	callback=self.set_b3,
        	minimum=-1,
        	maximum=1,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_b3_sizer)
        _b2_sizer = wx.BoxSizer(wx.VERTICAL)
        self._b2_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_b2_sizer,
        	value=self.b2,
        	callback=self.set_b2,
        	label='b2',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._b2_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_b2_sizer,
        	value=self.b2,
        	callback=self.set_b2,
        	minimum=-1,
        	maximum=1,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_b2_sizer)
        _b1_sizer = wx.BoxSizer(wx.VERTICAL)
        self._b1_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_b1_sizer,
        	value=self.b1,
        	callback=self.set_b1,
        	label='b1',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._b1_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_b1_sizer,
        	value=self.b1,
        	callback=self.set_b1,
        	minimum=-1,
        	maximum=1,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_b1_sizer)
        self.wxgui_scopesink2_0_0 = scopesink2.scope_sink_c(
        	self.GetWin(),
        	title='Scope Plot',
        	sample_rate=samp_rate,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label='Counts',
        )
        self.Add(self.wxgui_scopesink2_0_0.win)
        self.pfb_arb_resampler_xxx_0 = pfb.arb_resampler_ccf(
        	  sps,
                  taps=(tx_taps),
        	  flt_size=32)
        self.pfb_arb_resampler_xxx_0.declare_sample_delay(0)

        self.iir_filter_xxx_0 = filter.iir_filter_ccf(((1, b1, b2, b3, b4)), ((1), ), True)
        _gain_control_sizer = wx.BoxSizer(wx.VERTICAL)
        self._gain_control_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_gain_control_sizer,
        	value=self.gain_control,
        	callback=self.set_gain_control,
        	label='gain_control',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._gain_control_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_gain_control_sizer,
        	value=self.gain_control,
        	callback=self.set_gain_control,
        	minimum=-1,
        	maximum=1,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_gain_control_sizer)
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bc(([1, (1+1j)/sqrt(2), 1j, (-1+1j)/sqrt(2), -1, (-1-1j)/sqrt(2), -1j, (1-1j)/sqrt(2)]), 1)
        self.blocks_throttle_0_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((0.5, ))
        self.blocks_delay_0 = blocks.delay(gr.sizeof_gr_complex*1, 1)
        self.blocks_add_xx_1 = blocks.add_vcc(1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.analog_random_source_x_0 = blocks.vector_source_b(map(int, numpy.random.randint(0, 8, 1000)), True)
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, 0.05, 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_1, 1))
        self.connect((self.analog_random_source_x_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.iir_filter_xxx_0, 0))
        self.connect((self.blocks_add_xx_1, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_add_xx_1, 0), (self.blocks_delay_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_throttle_0_0, 0), (self.wxgui_scopesink2_0_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.pfb_arb_resampler_xxx_0, 0))
        self.connect((self.iir_filter_xxx_0, 0), (self.blocks_throttle_0_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0, 0), (self.blocks_add_xx_1, 0))

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_samp_rate_0(20000*self.sps)
        self.pfb_arb_resampler_xxx_0.set_rate(self.sps)
        self.set_ntaps(11*self.nfilts*self.sps)

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts
        self.set_tx_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.1, 0.4, self.ntaps))
        self.set_rx_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0, self.excess_bw, self.ntaps))
        self.set_ntaps(11*self.nfilts*self.sps)

    def get_ntaps(self):
        return self.ntaps

    def set_ntaps(self, ntaps):
        self.ntaps = ntaps
        self.set_tx_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.1, 0.4, self.ntaps))
        self.set_rx_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0, self.excess_bw, self.ntaps))

    def get_excess_bw(self):
        return self.excess_bw

    def set_excess_bw(self, excess_bw):
        self.excess_bw = excess_bw
        self.set_rx_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0, self.excess_bw, self.ntaps))

    def get_tx_taps(self):
        return self.tx_taps

    def set_tx_taps(self, tx_taps):
        self.tx_taps = tx_taps
        self.pfb_arb_resampler_xxx_0.set_taps((self.tx_taps))

    def get_timing_bw(self):
        return self.timing_bw

    def set_timing_bw(self, timing_bw):
        self.timing_bw = timing_bw

    def get_samp_rate_0(self):
        return self.samp_rate_0

    def set_samp_rate_0(self, samp_rate_0):
        self.samp_rate_0 = samp_rate_0

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_scopesink2_0_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_0.set_sample_rate(self.samp_rate)

    def get_rx_taps(self):
        return self.rx_taps

    def set_rx_taps(self, rx_taps):
        self.rx_taps = rx_taps

    def get_gain_control(self):
        return self.gain_control

    def set_gain_control(self, gain_control):
        self.gain_control = gain_control
        self._gain_control_slider.set_value(self.gain_control)
        self._gain_control_text_box.set_value(self.gain_control)

    def get_freq_bw(self):
        return self.freq_bw

    def set_freq_bw(self, freq_bw):
        self.freq_bw = freq_bw

    def get_fll_ntaps(self):
        return self.fll_ntaps

    def set_fll_ntaps(self, fll_ntaps):
        self.fll_ntaps = fll_ntaps

    def get_const_points(self):
        return self.const_points

    def set_const_points(self, const_points):
        self.const_points = const_points

    def get_b4(self):
        return self.b4

    def set_b4(self, b4):
        self.b4 = b4
        self._b4_slider.set_value(self.b4)
        self._b4_text_box.set_value(self.b4)
        self.iir_filter_xxx_0.set_taps(((1, self.b1, self.b2, self.b3, self.b4)), ((1), ))

    def get_b3(self):
        return self.b3

    def set_b3(self, b3):
        self.b3 = b3
        self._b3_slider.set_value(self.b3)
        self._b3_text_box.set_value(self.b3)
        self.iir_filter_xxx_0.set_taps(((1, self.b1, self.b2, self.b3, self.b4)), ((1), ))

    def get_b2(self):
        return self.b2

    def set_b2(self, b2):
        self.b2 = b2
        self._b2_slider.set_value(self.b2)
        self._b2_text_box.set_value(self.b2)
        self.iir_filter_xxx_0.set_taps(((1, self.b1, self.b2, self.b3, self.b4)), ((1), ))

    def get_b1(self):
        return self.b1

    def set_b1(self, b1):
        self.b1 = b1
        self._b1_slider.set_value(self.b1)
        self._b1_text_box.set_value(self.b1)
        self.iir_filter_xxx_0.set_taps(((1, self.b1, self.b2, self.b3, self.b4)), ((1), ))


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
