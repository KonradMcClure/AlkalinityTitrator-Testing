clear variables, close all, clc, format compact
syms s
k=215.6
t1=102.2
t2=1671
num=k
den=(t1*t2*s^2+(t1+t2)*s+1)
tf=num./den
%sys=tf(num,den);
temp=ilaplace(tf)
%impulse(sys)
C=pid(0.0199, 0, 2.13)
%impulse(feedback(sys, C))
%pidTuner(sys, 'PID')
ezplot(temp)
ezplot(temp*C)