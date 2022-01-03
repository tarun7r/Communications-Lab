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

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.filter import pfb
from math import pi
from math import sqrt
from optparse import OptionParser
import numpy
import sip
import sys
from gnuradio import qtgui


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 4
        self.nfilts = nfilts = 32
        self.ntaps = ntaps = 11*nfilts*sps
        self.excess_bw = excess_bw = 0.4
        self.tx_taps = tx_taps = firdes.root_raised_cosine(nfilts, nfilts, 1.0, excess_bw, ntaps)
        self.timing_bw = timing_bw = 2*pi/100
        self.samp_rate_2 = samp_rate_2 = 20000
        self.samp_rate = samp_rate = 320000
        self.rx_taps = rx_taps = firdes.root_raised_cosine(nfilts, nfilts, 1.0, excess_bw, ntaps)
        self.const_points = const_points = 4

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_sink_x_0 = qtgui.sink_c(
        	1024, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate/4, #bw
        	"", #name
        	True, #plotfreq
        	True, #plotwaterfall
        	True, #plottime
        	True, #plotconst
        )
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_sink_x_0_win)

        self.qtgui_sink_x_0.enable_rf_freq(False)



        self.pfb_arb_resampler_xxx_0 = pfb.arb_resampler_ccf(
        	  sps,
                  taps=(tx_taps),
        	  flt_size=32)
        self.pfb_arb_resampler_xxx_0.declare_sample_delay(0)

        self.iir_filter_xxx_1 = filter.iir_filter_ffd(([1.0001,-1]), ([-1,1]), True)
        self.iir_filter_xxx_0 = filter.iir_filter_ffd(([0.01]), ([-1,0.99]), True)
        self.digital_pfb_clock_sync_xxx_0_0 = digital.pfb_clock_sync_ccf(sps, timing_bw, (rx_taps), nfilts, 16, 1.5, 1)
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bc(([1+1j,-1+1j,-1-1j,1-1j]), 1)
        self.blocks_vco_c_0 = blocks.vco_c(samp_rate/4, -5, 1)
        self.blocks_udp_source_0 = blocks.udp_source(gr.sizeof_float*1, '127.0.0.1', 12345, 1472, True)
        self.blocks_udp_sink_0 = blocks.udp_sink(gr.sizeof_float*1, '127.0.0.1', 12345, 1472, True)
        self.blocks_throttle_1 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate/4,True)
        self.blocks_threshold_ff_0_0 = blocks.threshold_ff(-0.001, 0.001, 0)
        self.blocks_threshold_ff_0 = blocks.threshold_ff(-0.001, 0.001, 0)
        self.blocks_sub_xx_0 = blocks.sub_ff(1)
        self.blocks_multiply_xx_2 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_1_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_1 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vff((sqrt(2), ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((sqrt(2), ))
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, 10)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.blocks_add_const_vxx_0_0 = blocks.add_const_vff((-0.5, ))
        self.blocks_add_const_vxx_0 = blocks.add_const_vff((-0.5, ))
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_SIN_WAVE, 10, 1, 0)
        self.analog_random_source_x_0 = blocks.vector_source_b(map(int, numpy.random.randint(0, 4, 1000)), True)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_random_source_x_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_add_const_vxx_0_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_multiply_xx_1, 1))
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_multiply_xx_1_0, 0))
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_threshold_ff_0, 0))
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_threshold_ff_0_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.iir_filter_xxx_1, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_multiply_xx_1, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_multiply_xx_1_0, 1))
        self.connect((self.blocks_multiply_xx_0, 0), (self.digital_pfb_clock_sync_xxx_0_0, 0))
        self.connect((self.blocks_multiply_xx_1, 0), (self.blocks_sub_xx_0, 0))
        self.connect((self.blocks_multiply_xx_1_0, 0), (self.blocks_sub_xx_0, 1))
        self.connect((self.blocks_multiply_xx_2, 0), (self.blocks_complex_to_float_0, 0))
        self.connect((self.blocks_multiply_xx_2, 0), (self.blocks_throttle_1, 0))
        self.connect((self.blocks_sub_xx_0, 0), (self.iir_filter_xxx_0, 0))
        self.connect((self.blocks_threshold_ff_0, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.blocks_threshold_ff_0_0, 0), (self.blocks_add_const_vxx_0_0, 0))
        self.connect((self.blocks_throttle_1, 0), (self.qtgui_sink_x_0, 0))
        self.connect((self.blocks_udp_source_0, 0), (self.blocks_delay_0, 0))
        self.connect((self.blocks_vco_c_0, 0), (self.blocks_multiply_xx_2, 1))
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.pfb_arb_resampler_xxx_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0_0, 0), (self.blocks_multiply_xx_2, 0))
        self.connect((self.iir_filter_xxx_0, 0), (self.blocks_udp_sink_0, 0))
        self.connect((self.iir_filter_xxx_1, 0), (self.blocks_vco_c_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0, 0), (self.blocks_multiply_xx_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.pfb_arb_resampler_xxx_0.set_rate(self.sps)
        self.set_ntaps(11*self.nfilts*self.sps)

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts
        self.set_tx_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0, self.excess_bw, self.ntaps))
        self.set_rx_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0, self.excess_bw, self.ntaps))
        self.set_ntaps(11*self.nfilts*self.sps)

    def get_ntaps(self):
        return self.ntaps

    def set_ntaps(self, ntaps):
        self.ntaps = ntaps
        self.set_tx_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0, self.excess_bw, self.ntaps))
        self.set_rx_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0, self.excess_bw, self.ntaps))

    def get_excess_bw(self):
        return self.excess_bw

    def set_excess_bw(self, excess_bw):
        self.excess_bw = excess_bw
        self.set_tx_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0, self.excess_bw, self.ntaps))
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
        self.digital_pfb_clock_sync_xxx_0_0.set_loop_bandwidth(self.timing_bw)

    def get_samp_rate_2(self):
        return self.samp_rate_2

    def set_samp_rate_2(self, samp_rate_2):
        self.samp_rate_2 = samp_rate_2

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_sink_x_0.set_frequency_range(0, self.samp_rate/4)
        self.blocks_throttle_1.set_sample_rate(self.samp_rate/4)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_rx_taps(self):
        return self.rx_taps

    def set_rx_taps(self, rx_taps):
        self.rx_taps = rx_taps
        self.digital_pfb_clock_sync_xxx_0_0.update_taps((self.rx_taps))

    def get_const_points(self):
        return self.const_points

    def set_const_points(self, const_points):
        self.const_points = const_points


def main(top_block_cls=top_block, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
