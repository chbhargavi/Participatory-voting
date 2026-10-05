set term postscript eps enhanced color blacktext "Helvetica" 45
set xlabel 'Slot Number'
set key autotitle columnheader
set key font "7"
set key left
set xrange [1:4]
set yrange [5:40]
set tics font ", 70"
set term post size 8,6
#set object 1 rectangle from screen 0,0 to screen 1,1 fillcolor rgb"#E5E7E9" behind
set output "budget_rd.eps" 
set ylabel 'Budget Utilized'
plot "budget_rd.txt" using 1:2:xtic(1) with lp lc rgb "#145A32" lt 14 lw 11, \
      "budget_rd.txt" using 1:3:xtic(1) with lp lc rgb "#2471A3" lt 14 lw 11, \
      "budget_rd.txt" using 1:4:xtic(1) with lp lc rgb "#A32471" lt 14 lw 11, \
       "budget_rd.txt" using 1:5:xtic(1) with lp lc rgb "#E32636" lt 14 lw 11, \
       "budget_rd.txt" using 1:6:xtic(1) with lp lc rgb "#6D351A" dt 14 lw 11, \
