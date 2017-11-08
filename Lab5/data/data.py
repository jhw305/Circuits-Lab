#!/usr/bin/python

# 20Vpp square wave - 10kHz

pn_junction_vp_over_resistor = 8.375 #V
pn_junction_vn_over_resistor = -9.8125 #V
R_L = 300 #ohms
pn_junction_ts = 2.97e-6 #s

# t_s increases when you decreases Vpp and make the offset positive

schottky_vp_over_resistor = 8.275 #V
schottky_vn_over_resistor = 0 #V

switching_vp_over_resistor = 7.95 #V
switching_vn_over_resistor = 0 #V

# full-wave rectifier

# 20 Vpp

rectified_amplitude_pos = 8.906 #V
rectified_amplitude_neg = 8.593 #V

input_amplitude_pos = 9.375 #V
input_amplitude_neg = 8.75 #V

# After dropping frequency to 500Hz

rectified_amplitude_both = 7.5 #V

# Period can't go below 2ts

other_pn_junction_ts = 4.52e-6 #s
last_pn_junction_ts = 4.52e-6 #s
yet_another_pn_junction_ts = 4.02e-6 #s
