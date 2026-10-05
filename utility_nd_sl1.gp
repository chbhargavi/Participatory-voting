set term postscript eps enhanced color blacktext "Helvetica" 45
set xlabel 'Task Number'
set key autotitle columnheader
set key font "7"
set key right
set xrange [1:4]
set yrange [0:25]
set tics font ", 70"
set term post size 8,6
#set object 1 rectangle from screen 0,0 to screen 1,1 fillcolor rgb"#E5E7E9" behind
set output "utility_nd_sl1.eps" 
set ylabel 'Sum of Utility of TEs'
plot "utility_nd_sl1.txt" using 1:2:xtic(1) with lp lc rgb "#145A32" lt 14 lw 11, \
      "utility_nd_sl1.txt" using 1:3:xtic(1) with lp lc rgb "#2471A3" lt 14 lw 11, \
      "utility_nd_sl1.txt" using 1:4:xtic(1) with lp lc rgb "#A32471" lt 14 lw 11, \
       "utility_nd_sl1.txt" using 1:5:xtic(1) with lp lc rgb "#E32636" lt 14 lw 11, \
       "utility_nd_sl1.txt" using 1:6:xtic(1) with lp lc rgb "#6D351A" lt 14 lw 11, \
