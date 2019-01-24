# LFSR
A python script to simulate a Linear feedback shift register (LFSR). 

The script will ask you for the LFSR that you want to analyze. The input has to be given in a very specific format.

Suppose the LFSR that you want to analyze is: S <sub> i+8 </sub> = S <sub> i+1 </sub> + S<sub> i </sub>. The polynomial corresponding to this is X<sup> 8 </sup> = X + 1 or
X<sup> 8 </sup> + X + 1. The program then expects input: **11000000**. 

