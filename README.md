# LFSR
A python script to simulate a Linear feedback shift register (LFSR). This script was created for a course about cryptology in which LFSR's were treated, and then extended to learn some Tikz. The Tikz commands may be buggy as i generally just wanted to learn certain features... The script as is, is not the fastest for large LSFR's.

The script will ask you for the LFSR that you want to analyze. The input has to be given in a very specific format.

Suppose the LFSR that you want to analyze is: S <sub> i+8 </sub> = S <sub> i+1 </sub> + S<sub> i </sub>. The polynomial corresponding to this is X<sup> 8 </sup> = X + 1 or
X<sup> 8 </sup> + X + 1. The program then expects input: **11000000**. The first "1" corresponds to S<sub> i </sub>, the second "1" to S <sub> i+1 </sub> and the "0"'s correspond to S <sub> i+2 </sub> to S <sub> i+7 </sub>.

