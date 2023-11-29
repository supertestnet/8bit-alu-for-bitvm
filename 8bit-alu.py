import circuit
from circuit import *
import bfcl
from bfcl import gate, operation
from pprint import pprint
c = circuit()

#run alu
run_alu = c.gate(op.id_, is_input=True)
#add_or_subtract
add_or_subtract = c.gate(op.id_, is_input=True)
#initial_carry_out
initial_carry_out = c.gate(op.id_, is_input=True)
A8 = c.gate(op.id_, is_input=True)
A7 = c.gate(op.id_, is_input=True)
A6 = c.gate(op.id_, is_input=True)
A5 = c.gate(op.id_, is_input=True)
A4 = c.gate(op.id_, is_input=True)
A3 = c.gate(op.id_, is_input=True)
A2 = c.gate(op.id_, is_input=True)
A1 = c.gate(op.id_, is_input=True)
pre_B8 = c.gate(op.id_, is_input=True)
pre_B7 = c.gate(op.id_, is_input=True)
pre_B6 = c.gate(op.id_, is_input=True)
pre_B5 = c.gate(op.id_, is_input=True)
pre_B4 = c.gate(op.id_, is_input=True)
pre_B3 = c.gate(op.id_, is_input=True)
pre_B2 = c.gate(op.id_, is_input=True)
pre_B1 = c.gate(op.id_, is_input=True)

inverted_B1 = c.gate(op.not_, [pre_B1])
inverted_B2 = c.gate(op.not_, [pre_B2])
inverted_B3 = c.gate(op.not_, [pre_B3])
inverted_B4 = c.gate(op.not_, [pre_B4])
inverted_B5 = c.gate(op.not_, [pre_B5])
inverted_B6 = c.gate(op.not_, [pre_B6])
inverted_B7 = c.gate(op.not_, [pre_B7])
inverted_B8 = c.gate(op.not_, [pre_B8])

inverted_add_or_subtract = c.gate(op.not_, [add_or_subtract])

#B1_inverter
first_B1_and = c.gate(op.and_, [inverted_B1, add_or_subtract])
second_B1_and = c.gate(op.and_, [inverted_add_or_subtract, pre_B1])
B1 = c.gate(op.or_, [first_B1_and, second_B1_and])
#B2_inverter
first_B2_and = c.gate(op.and_, [inverted_B2, add_or_subtract])
second_B2_and = c.gate(op.and_, [inverted_add_or_subtract, pre_B2])
B2 = c.gate(op.or_, [first_B2_and, second_B2_and])
#B3_inverter
first_B3_and = c.gate(op.and_, [inverted_B3, add_or_subtract])
second_B3_and = c.gate(op.and_, [inverted_add_or_subtract, pre_B3])
B3 = c.gate(op.or_, [first_B3_and, second_B3_and])
#B4_inverter
first_B4_and = c.gate(op.and_, [inverted_B4, add_or_subtract])
second_B4_and = c.gate(op.and_, [inverted_add_or_subtract, pre_B4])
B4 = c.gate(op.or_, [first_B4_and, second_B4_and])
#B5_inverter
first_B5_and = c.gate(op.and_, [inverted_B5, add_or_subtract])
second_B5_and = c.gate(op.and_, [inverted_add_or_subtract, pre_B5])
B5 = c.gate(op.or_, [first_B5_and, second_B5_and])
#B6_inverter
first_B6_and = c.gate(op.and_, [inverted_B6, add_or_subtract])
second_B6_and = c.gate(op.and_, [inverted_add_or_subtract, pre_B6])
B6 = c.gate(op.or_, [first_B6_and, second_B6_and])
#B7_inverter
first_B7_and = c.gate(op.and_, [inverted_B7, add_or_subtract])
second_B7_and = c.gate(op.and_, [inverted_add_or_subtract, pre_B7])
B7 = c.gate(op.or_, [first_B7_and, second_B7_and])
#B8_inverter
first_B8_and = c.gate(op.and_, [inverted_B8, add_or_subtract])
second_B8_and = c.gate(op.and_, [inverted_add_or_subtract, pre_B8])
B8 = c.gate(op.or_, [first_B8_and, second_B8_and])

#only pass A and B into the alu if the run_alu bit is set
g0 = c.gate(op.and_, [A1, run_alu])
g1 = c.gate(op.and_, [A2, run_alu])
g2 = c.gate(op.and_, [A3, run_alu])
g3 = c.gate(op.and_, [A4, run_alu])
g4 = c.gate(op.and_, [A5, run_alu])
g5 = c.gate(op.and_, [A6, run_alu])
g6 = c.gate(op.and_, [A7, run_alu])
g7 = c.gate(op.and_, [A8, run_alu])
g8 = c.gate(op.and_, [B1, run_alu])
g9 = c.gate(op.and_, [B2, run_alu])
g10 = c.gate(op.and_, [B3, run_alu])
g11 = c.gate(op.and_, [B4, run_alu])
g12 = c.gate(op.and_, [B5, run_alu])
g13 = c.gate(op.and_, [B6, run_alu])
g14 = c.gate(op.and_, [B7, run_alu])
g15 = c.gate(op.and_, [B8, run_alu])

#first_4bit_adder
#set1
g16 = c.gate(op.and_, [add_or_subtract, g0])
g17 = c.gate(op.xor_, [add_or_subtract, g0])
g18 = c.gate(op.and_, [g17, g8])
#1s place
g19 = c.gate(op.xor_, [g17, g8])
#adder-1-to-adder-2
g20 = c.gate(op.or_, [g16, g18])
#set2
g21 = c.gate(op.and_, [g20, g1])
g22 = c.gate(op.xor_, [g20, g1])
g23 = c.gate(op.and_, [g22, g9])
#2s place
g24 = c.gate(op.xor_, [g22, g9])
#adder-2-to-adder-3
g25 = c.gate(op.or_, [g21, g23])
#set3
g26 = c.gate(op.and_, [g25, g2])
g27 = c.gate(op.xor_, [g25, g2])
g28 = c.gate(op.and_, [g27, g10])
#4s place
g29 = c.gate(op.xor_, [g27, g10])
#adder-3-to-adder-4
g30 = c.gate(op.or_, [g26, g28])
#set4
g31 = c.gate(op.and_, [g30, g3])
g32 = c.gate(op.xor_, [g30, g3])
g33 = c.gate(op.and_, [g32, g11])
#8s place
g34 = c.gate(op.xor_, [g32, g11])
#carry out to second 4bit adder
g35 = c.gate(op.or_, [g31, g33])

#second_4bit_adder
#set5
g36 = c.gate(op.and_, [g35, g4])
g37 = c.gate(op.xor_, [g35, g4])
g38 = c.gate(op.and_, [g37, g12])
#16s place
g39 = c.gate(op.xor_, [g37, g12])
#adder-5-to-adder-6
g40 = c.gate(op.or_, [g36, g38])
#set2
g41 = c.gate(op.and_, [g40, g5])
g42 = c.gate(op.xor_, [g40, g5])
g43 = c.gate(op.and_, [g42, g13])
#32s place
g44 = c.gate(op.xor_, [g42, g13])
#adder-6-to-adder-7
g45 = c.gate(op.or_, [g41, g43])
#set3
g46 = c.gate(op.and_, [g45, g6])
g47 = c.gate(op.xor_, [g45, g6])
g48 = c.gate(op.and_, [g47, g14])
#64s place
g49 = c.gate(op.xor_, [g47, g14])
#adder-7-to-adder-8
g50 = c.gate(op.or_, [g46, g48])
#set4
g51 = c.gate(op.and_, [g50, g7])
g52 = c.gate(op.xor_, [g50, g7])
g53 = c.gate(op.and_, [g52, g15])
#128s place
g54 = c.gate(op.xor_, [g52, g15])
#carry out to inverter
g55 = c.gate(op.or_, [g51, g53])

#set the run_alu bit to 0
inverted_run_alu = c.gate(op.not_, [run_alu])
run_alu_out = c.gate(op.and_, [run_alu, inverted_run_alu])

#set the operation bit to 0
add_or_subtract_out = c.gate(op.and_, [add_or_subtract, inverted_add_or_subtract])

#set the carry_out bit to 0 if necessary
inverted_carry_out = c.gate(op.not_, [g55])
zeroed_carry_out = c.gate(op.and_, [inverted_carry_out, g55])
first_carry_out_and = c.gate(op.and_, [zeroed_carry_out, add_or_subtract])
second_carry_out_and = c.gate(op.and_, [inverted_add_or_subtract, g55])
carry_out = c.gate(op.or_, [first_carry_out_and, second_carry_out_and])

#if run_alu is set, pass the alu's result to A_output,
#otherwise pass A_input to A_output unchanged
#A1_selector
first_A1_and = c.gate(op.and_, [g19, run_alu])
second_A1_and = c.gate(op.and_, [inverted_run_alu, A1])
A1_out = c.gate(op.or_, [first_A1_and, second_A1_and])
#A2_inverter
first_A2_and = c.gate(op.and_, [g24, run_alu])
second_A2_and = c.gate(op.and_, [inverted_run_alu, A2])
A2_out = c.gate(op.or_, [first_A2_and, second_A2_and])
#B3_inverter
first_A3_and = c.gate(op.and_, [g29, run_alu])
second_A3_and = c.gate(op.and_, [inverted_run_alu, A3])
A3_out = c.gate(op.or_, [first_A3_and, second_A3_and])
#B4_inverter
first_A4_and = c.gate(op.and_, [g34, run_alu])
second_A4_and = c.gate(op.and_, [inverted_run_alu, A4])
A4_out = c.gate(op.or_, [first_A4_and, second_A4_and])
#B5_inverter
first_A5_and = c.gate(op.and_, [g39, run_alu])
second_A5_and = c.gate(op.and_, [inverted_run_alu, A5])
A5_out = c.gate(op.or_, [first_A5_and, second_A5_and])
#B6_inverter
first_A6_and = c.gate(op.and_, [g44, run_alu])
second_A6_and = c.gate(op.and_, [inverted_run_alu, A6])
A6_out = c.gate(op.or_, [first_A6_and, second_A6_and])
#B7_inverter
first_A7_and = c.gate(op.and_, [g49, run_alu])
second_A7_and = c.gate(op.and_, [inverted_run_alu, A7])
A7_out = c.gate(op.or_, [first_A7_and, second_A7_and])
#B8_inverter
first_A8_and = c.gate(op.and_, [g54, run_alu])
second_A8_and = c.gate(op.and_, [inverted_run_alu, A8])
A8_out = c.gate(op.or_, [first_A8_and, second_A8_and])

run_alu_final = c.gate(op.id_, [run_alu_out], is_output=True)
add_or_subtract_final = c.gate(op.id_, [add_or_subtract_out], is_output=True)
carry_out_final = c.gate(op.id_, [carry_out], is_output=True)
one_two_eights_place = c.gate(op.id_, [A8_out], is_output=True)
sixty_fours_place = c.gate(op.id_, [A7_out], is_output=True)
thirty_twos_place = c.gate(op.id_, [A6_out], is_output=True)
sixteens_place = c.gate(op.id_, [A5_out], is_output=True)
eights_place = c.gate(op.id_, [A4_out], is_output=True)
fours_place = c.gate(op.id_, [A3_out], is_output=True)
twos_place = c.gate(op.id_, [A2_out], is_output=True)
ones_place = c.gate(op.id_, [A1_out], is_output=True)
B8_out = c.gate(op.id_, [B8], is_output=True)
B7_out = c.gate(op.id_, [B7], is_output=True)
B6_out = c.gate(op.id_, [B6], is_output=True)
B5_out = c.gate(op.id_, [B5], is_output=True)
B4_out = c.gate(op.id_, [B4], is_output=True)
B3_out = c.gate(op.id_, [B3], is_output=True)
B2_out = c.gate(op.id_, [B2], is_output=True)
B1_out = c.gate(op.id_, [B1], is_output=True)
#flags: run alu, add_or_subtract, initial_carry
# print(c.evaluate([0, 0, 0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0]))

for line in bfcl.circuit(c).emit().split('\n'):
	print(line)