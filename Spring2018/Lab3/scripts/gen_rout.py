#!/usr/bin/python
import common

TABLES_DIR = "tables/"
PREC = 2

I = 1e-6 # Amperes
V_tn = 1.4

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
	# Common Drain Amplifier
	g_m_cda = ( 2 * I_D_cda ) / ( V_GS_cda - V_tn )
	g_m_sim_cda = 2.828e-3
	common.write_csv_from_matrix( TABLES_DIR + "common_drain_amp_gm.csv" , [ [ "gm from Op Point Listing [mA / V]" , "Calculated gm [mA / V]" , "Error from Listing" ] , [ common.set_precision_str( 1e3 * g_m_sim_cda , PREC ) , common.set_precision_str( 1e3 * g_m_cda , PREC ) , common.fmt_perc_err( g_m_cda , g_m_sim_cda , PREC ) ] ] )
	# Common Source Amplifier
	g_m_csa = ( 2 * I_D_csa ) / ( V_GS_csa - V_tn )
	g_m_sim_csa = 3.405e-3
	common.write_csv_from_matrix( TABLES_DIR + "common_source_amp_gm.csv" , [ [ "gm from Op Point Listing [mA / V]" , "Calculated gm [mA / V]" , "Error from Listing" ] , [ common.set_precision_str( 1e3 * g_m_sim_csa , PREC ) , common.set_precision_str( 1e3 * g_m_csa , PREC ) , common.fmt_perc_err( g_m_csa , g_m_sim_csa , PREC ) ] ] )

	# Common-Drain Amp r_out
	v_x_high_cda = 1.638615
	v_x_low_cda = 1.63796
	v_x_cda = ( v_x_high_cda - v_x_low_cda ) / 2.0
	r_out_sim_cda = v_x_cda / I
	r_out_theory_cda = 1.0 / ( ( 1.0 / R_S ) + g_m_cda )
	common.write_csv_from_matrix( TABLES_DIR + "common_drain_amp_rout.csv" , [ [ "rout from Simulation [Ohms]" , "rout from Theory [Ohms]" , "Error from Theory" ] , [ common.set_precision_str( r_out_sim_cda , PREC ) , common.set_precision_str( r_out_theory_cda , PREC ) , common.fmt_perc_err( r_out_sim_cda , r_out_theory_cda , PREC ) ] ] )

	# Common-Source Amp r_out
	v_x_high_csa = 2.6217311
	v_x_low_csa = 2.6118918
	v_x_csa = ( v_x_high_csa - v_x_low_csa ) / 2.0
	r_out_sim_csa = v_x_csa / I
	r_out_theory_csa = R_D
	common.write_csv_from_matrix( TABLES_DIR + "common_source_amp_rout.csv" , [ [ "rout from Simulation [Ohms]" , "rout from Theory [Ohms]" , "Error from Theory" ] , [ common.set_precision_str( r_out_sim_csa , PREC ) , common.set_precision_str( r_out_theory_csa , PREC ) , common.fmt_perc_err( r_out_sim_csa , r_out_theory_csa , PREC ) ] ] )
