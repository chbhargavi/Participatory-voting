set term postscript eps enhanced color blacktext "Helvetica" 45
set xlabel 'Total Number of Tasks'
set key autotitle columnheader
set key font "7"
set key left
set xrange [2:28]
set yrange [0:25]
set style fill solid
set boxwidth 4.5
set tics font ", 70"
set term post size 8,6
set output "Data1_rd.eps" 
set ylabel 'Expected Number of Tasks receive GF'
#set title "Probability = 0.2" 
plot "Data1.txt" using 1:2:xtic(1) with boxes lc rgb "#2471A3"lt 4 lw 3.5 notitle, \
