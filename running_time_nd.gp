set term postscript eps enhanced color blacktext "Helvetica" 45
set xlabel 'Number of Agents'
set key autotitle columnheader
set key font "7"
set key left
set xrange [100:600]
set yrange [5:55]
set ytics 5
set tics font ", 70"
set term post size 8,6
#set object 1 rectangle from screen 0,0 to screen 1,1 fillcolor rgb"#E5E7E9" behind
set output "running_time_nd.eps" 
set ylabel 'running time (in millisecond)'
plot "running_time_nd.txt" using 1:2:xtic(1) with lp lc rgb "#145A32" lt 14 lw 11, \
      "running_time_nd.txt" using 1:3:xtic(1) with lp lc rgb "#2471A3" lt 14 lw 11, \
      "running_time_nd.txt" using 1:4:xtic(1) with lp lc rgb "#A32471" lt 14 lw 11, \
       "running_time_nd.txt" using 1:5:xtic(1) with lp lc rgb "#E32636" lt 14 lw 11, \
      # "running_time_nd.txt" using 1:6:xtic(1) with lp lc rgb "#6D351A" dt 14 lw 11, \
