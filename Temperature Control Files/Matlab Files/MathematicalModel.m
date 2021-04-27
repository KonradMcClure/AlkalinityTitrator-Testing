clear variables, close all, clc, format compact
time=(0:1:80)';
tau=7.75
tempt=23*exp(-time/tau)+30*(1-exp(-time/tau))
title('Ice point precision test')
ylabel('Temp in C')
xlabel('Time in s')
hold on
plot(time,tempt)
