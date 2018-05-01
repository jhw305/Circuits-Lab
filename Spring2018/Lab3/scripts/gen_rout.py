#!/usr/bin/python
import common

TABLES_DIR = "tables/"
PREC = 2

I = 1e-6 # Amperes
V_tn = 1.4 # Volts
R_L = 500 # Ohms
LAMBDA = 0.005 # Volts^-1

# Common Source Amplifier
R_D = 5e3 # Ohms
I_D_csa = 476.6e-6 # Amperes
V_GS_csa = 1.68 # Volts

# Common Drain Amplifier
R_S = 5e3 # Ohms
I_D_cda = 327.7e-6 # Amperes
V_GS_cda = 1.632 # Volts

if __name__ == "__main__" :

	# g_m calculations
	# Common Drain Amplifier (CDA)
	g_m_cda = ( 2 * I_D_cda ) / ( V_GS_cda - V_tn )
	g_m_sim_cda = 2.828e-3
	common.write_csv_from_matrix( TABLES_DIR + "common_drain_amp_gm.csv" , [ [ "gm from Op Point Listing [mA / V]" , "Calculated gm [mA / V]" , "Error from Listing" ] , [ common.set_precision_str( 1e3 * g_m_sim_cda , PREC ) , common.set_precision_str( 1e3 * g_m_cda , PREC ) , common.fmt_perc_err( g_m_cda , g_m_sim_cda , PREC ) ] ] )
	# Common Source Amplifier (CSA)
	g_m_csa = ( 2 * I_D_csa ) / ( V_GS_csa - V_tn )
	g_m_sim_csa = 3.405e-3
	common.write_csv_from_matrix( TABLES_DIR + "common_source_amp_gm.csv" , [ [ "gm from Op Point Listing [mA / V]" , "Calculated gm [mA / V]" , "Error from Listing" ] , [ common.set_precision_str( 1e3 * g_m_sim_csa , PREC ) , common.set_precision_str( 1e3 * g_m_csa , PREC ) , common.fmt_perc_err( g_m_csa , g_m_sim_csa , PREC ) ] ] )

	# ro calculations
	# CDA
	ro_cda = 1.0 / ( LAMBDA * I_D_cda )
	ro_sim_cda = 1.0 / ( 1.666e-6 )
	common.write_csv_from_matrix( TABLES_DIR + "common_drain_amp_ro.csv" , [ [ "ro from Op Point Listing [ kiloohms ]" , "Calculated ro [ kiloohms ]" , "Error from Listing" ] , [ common.set_precision_str( 1e-3 * ro_sim_cda , PREC ) , common.set_precision_str( 1e-3 * ro_cda , PREC ) , common.fmt_perc_err( ro_cda , ro_sim_cda , PREC ) ] ] )
	# CSA
	ro_csa = 1.0 / ( LAMBDA * I_D_csa )
	ro_sim_csa = 1.0 / ( 2.415e-6 )
	common.write_csv_from_matrix( TABLES_DIR + "common_source_amp_ro.csv" , [ [ "ro from Op Point Listing [ kiloohms ]" , "Calculated ro [ kiloohms ]" , "Error from Listing" ] , [ common.set_precision_str( 1e-3 * ro_sim_cda , PREC ) , common.set_precision_str( 1e-3 * ro_cda , PREC ) , common.fmt_perc_err( ro_cda , ro_sim_cda , PREC ) ] ] )

	# CSA Gain
	gain_theory = -1 * g_m_csa * ( 1.0 / ( ( 1.0 / R_D ) + ( 1 / ro_sim_csa ) ) )
	gain_result = -16.79
	common.write_csv_from_matrix( TABLES_DIR + "common_source_amp_gain_1.csv" , [ [ "Gain from Graph [V/V]" , "Gain from Theory [V/V]" , "Error from Theory" ] , [ common.set_precision_str( gain_result , PREC ) , common.set_precision_str( gain_theory , PREC ) , common.fmt_perc_err( gain_result , gain_theory , PREC ) ] ] )

	# Common-Drain Amp r_out
	v_x_high_cda = 1.638615
	v_x_low_cda = 1.63796
	v_x_cda = ( v_x_high_cda - v_x_low_cda ) / 2.0
	r_out_sim_cda = v_x_cda / I
	r_out_theory_cda = 1.0 / ( ( 1.0 / R_S ) + g_m_cda + ( 1.0 / ro_cda ) )
	common.write_csv_from_matrix( TABLES_DIR + "common_drain_amp_rout.csv" , [ [ "rout from Simulation [Ohms]" , "rout from Theory [Ohms]" , "Error from Theory" ] , [ common.set_precision_str( r_out_sim_cda , PREC ) , common.set_precision_str( r_out_theory_cda , PREC ) , common.fmt_perc_err( r_out_sim_cda , r_out_theory_cda , PREC ) ] ] )

	# Common-Source Amp r_out
	v_x_high_csa = 2.6217311
	v_x_low_csa = 2.6118918
	v_x_csa = ( v_x_high_csa - v_x_low_csa ) / 2.0
	r_out_sim_csa = v_x_csa / I
	r_out_theory_csa = 1.0 / ( ( 1.0 / R_D ) + ( 1.0 / ro_sim_csa ) )
	common.write_csv_from_matrix( TABLES_DIR + "common_source_amp_rout.csv" , [ [ "rout from Simulation [Ohms]" , "rout from Theory [Ohms]" , "Error from Theory" ] , [ common.set_precision_str( r_out_sim_csa , PREC ) , common.set_precision_str( r_out_theory_csa , PREC ) , common.fmt_perc_err( r_out_sim_csa , r_out_theory_csa , PREC ) ] ] )

	# Circuit 5 Gain
	vin_amplitude = ( 1.68099716 - 1.67900126 ) / 2.0
	vout_amplitude = ( 1.536e-3 - ( -1.5443e-3 ) ) / 2.0
	gain = - ( vout_amplitude / vin_amplitude )
	gain_theory = -1 * g_m_csa * ( 1.0 / ( ( 1.0 / R_D ) + ( 1.0 / R_L ) + ( 1.0 / ro_sim_csa ) ) )
	common.write_csv_from_matrix( TABLES_DIR + "common_source_amp_gain.csv" , [ [ "Measured Gain [V/V]" , "Theoretical Gain [V/V]" , "Error from Theoretical" ] , [ common.set_precision_str( gain , PREC ) , common.set_precision_str( gain_theory , PREC ) , common.fmt_perc_err( gain , gain_theory , PREC ) ] ] )

	# Circuit 6 Gain
	vout_amplitude_6 = ( 8.56e-3 - ( -8.397e-3 ) ) / 2.0
	gain_6 = - ( vout_amplitude_6 / vin_amplitude )
	R_S_parallel_ro_cda = 1.0 / ( ( 1.0 / R_S ) + ( 1.0 / ro_cda ) )
	cda_gain = 1.0 / ( 1.0 + ( 1.0 / ( g_m_cda * R_S_parallel_ro_cda ) ) )
	csa_gain = -1 * g_m_csa * ( 1.0 / ( ( 1.0 / R_D ) + ( 1.0 / ro_sim_csa ) ) )
	gain_theory_6 = ( csa_gain * cda_gain * R_L ) / ( r_out_theory_cda + R_L )
	common.write_csv_from_matrix( TABLES_DIR + "cascade_gain.csv" , [ [ "Measured Gain [V/V]" , "Theoretical Gain [V/V]" , "Error from Theoretical" ] , [ common.set_precision_str( gain_6 , PREC ) , common.set_precision_str( gain_theory_6 , PREC ) , common.fmt_perc_err( gain_6 , gain_theory_6 , PREC ) ] ] )
