clear variables, close all, clc, format compact
time=(0:1:80)';

tau=7.75
Ti=23
Tf=30
tempt=Ti*exp(-time/tau)+Tf*(1-exp(-time/tau))
SYS1=tf([690 30],[30 1 0])
SYS2=tf([184 30],[8 1 0])

step(feedback(SYS1,1))
title('Ice point precision test')
ylabel('Amplitude')
xlabel('Time in s')
hold on
%plot(time,tempt)
