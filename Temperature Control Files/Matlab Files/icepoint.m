clear variables, close all, clc, format compact
%%
temp=[24.415158090843303
24.448978412442557
24.448978412442557
24.313699168877676
23.806450513975243
23.16404546157896
22.42036141238116
21.57546557131715
20.73078199080814
19.818761950533588
18.97451936002966
18.09673170790678
17.219172925665852
16.40932164933912
15.59966509338257
14.891375228106504
14.149516956944927
13.44153184331163
12.801102008220484
12.160793819955249
11.554298211468842
10.981596942416889
10.476353037288606
9.971184794173354
9.499762667903664
9.062072516385205
8.624439124025733
8.220520197631163
7.850303635830607
7.513778352060772
7.177286607407962
6.874472704879821
6.571685953610841
6.268926346298286
5.999829476973348
5.7307540438336675
5.495330620181387
5.259923601257436
5.024532983632921
4.856406867900189
4.6210443588153245
4.41931811213634
4.25122210460557
4.083134457594493
3.9486703587210754
3.7805977575013907
3.6125335133090477
3.511698977648467
3.3436481021078484
3.2428215866814254
3.108390910434597
2.973965579495974
2.8731500887666694
2.805941431690415
2.6715281253634227
2.6043234759531053
2.5035190063057855
2.402717541780396
2.301919082108842
2.2347217782247535
2.1675258096320453
2.1003311762514905
2.0331378780027363
1.965945914807307
1.8651604730631883
1.831565993255388
1.7643780347396938
1.6971914109592918
1.6300061218338295
1.5964139777414497
1.5292306904485795
1.4620487376123947
1.4284582615903083
1.3948681191525425
1.3612783102885837
1.3276888349894205
1.2940996932445392
1.2605108850434268
1.1933342692364612
1.1933342692364612
1.1261589874874198
1.1261589874874198
1.0925718468602146
1.0589850397174518
1.0253985660501201
0.9582266190996958
0.9246411457978291
0.9582266190996958
0.8910560059300905
0.8910560059300905
0.8574711994882194
0.8574711994882194
0.7903025868400256
0.7903025868400256
0.7567187806141781
0.7231353077743969
0.7231353077743969
0.7231353077743969
0.6895521683094179
0.6895521683094179
0.6559693622102293
0.6559693622102293
0.6223868894670685
0.6223868894670685
0.6223868894670685
0.5888047500694225
0.5552229440075283
0.5552229440075283
0.5552229440075283
0.5552229440075283
0.5216414712723745
0.5216414712723745
0.5216414712723745
0.48806033185269676
0.48806033185269676
0.48806033185269676
0.48806033185269676
0.4544795257394834
0.4544795257394834
0.4544795257394834
0.4208990529222211
0.4208990529222211
0.4208990529222211
0.4208990529222211
0.4208990529222211
0.4208990529222211
0.4208990529222211
0.4208990529222211
0.38731891339039615
0.38731891339039615
0.3537391071357482
0.3537391071357482
0.38731891339039615
0.3537391071357482
0.3537391071357482
0.3537391071357482
0.3537391071357482
0.3537391071357482
0.3537391071357482
0.32015963414776366
0.3537391071357482
0.32015963414776366
0.32015963414776366
0.32015963414776366
0.32015963414776366
0.32015963414776366
0.32015963414776366
0.32015963414776366
0.28658049441592903
0.28658049441592903
0.32015963414776366
0.28658049441592903
0.32015963414776366
0.32015963414776366
0.28658049441592903
0.28658049441592903
0.28658049441592903
0.28658049441592903
0.28658049441592903
0.28658049441592903
0.28658049441592903
0.25300168793123284
0.28658049441592903
0.28658049441592903
0.28658049441592903
0.28658049441592903
0.28658049441592903
0.25300168793123284
0.25300168793123284
0.25300168793123284
0.25300168793123284
0.25300168793123284
0.28658049441592903
0.28658049441592903
0.25300168793123284
0.25300168793123284
0.25300168793123284
0.25300168793123284
0.25300168793123284
0.25300168793123284
0.25300168793123284
0.25300168793123284
0.25300168793123284
0.25300168793123284
0.25300168793123284
0.25300168793123284
0.25300168793123284
0.25300168793123284
0.25300168793123284
0.25300168793123284
0.25300168793123284
0.25300168793123284
0.25300168793123284
0.25300168793123284
0.25300168793123284
0.25300168793123284
0.25300168793123284
0.2194232146824106
0.25300168793123284
0.25300168793123284
0.25300168793123284
0.2194232146824106
0.25300168793123284
0.25300168793123284
0.2194232146824106
0.2194232146824106
0.2194232146824106
0.2194232146824106
0.2194232146824106
0.25300168793123284
0.2194232146824106
0.2194232146824106
0.2194232146824106
0.2194232146824106
0.2194232146824106
0.2194232146824106
0.2194232146824106
0.25300168793123284
0.2194232146824106
0.2194232146824106
0.2194232146824106
0.2194232146824106
0.2194232146824106
0.2194232146824106
0.2194232146824106
0.2194232146824106
0.25300168793123284
0.2194232146824106
0.2194232146824106
0.2194232146824106
0.2194232146824106
0.2194232146824106
0.2194232146824106
0.18584507466045078
0.2194232146824106
0.2194232146824106
0.18584507466045078
0.2194232146824106
0.2194232146824106
0.2194232146824106
0.2194232146824106
0.2194232146824106
0.2194232146824106
0.2194232146824106
0.2194232146824106
0.2194232146824106
0.18584507466045078
0.2194232146824106
0.2194232146824106
0.2194232146824106
0.2194232146824106
0.2194232146824106
0.2194232146824106
0.2194232146824106
0.2194232146824106
0.18584507466045078
0.2194232146824106
0.2194232146824106
0.18584507466045078
0.2194232146824106
0.2194232146824106
0.2194232146824106
0.18584507466045078
0.2194232146824106
0.2194232146824106
0.2194232146824106
0.18584507466045078
0.2194232146824106
0.2194232146824106
0.2194232146824106
0.2194232146824106
0.2194232146824106
0.2194232146824106
0.2194232146824106
0.2194232146824106
0.18584507466045078
0.2194232146824106
0.2194232146824106
0.2194232146824106
0.2194232146824106
0.18584507466045078
0.18584507466045078
0.2194232146824106
0.2194232146824106
0.2194232146824106
0.2194232146824106
0.2194232146824106
0.2194232146824106
0.2194232146824106
0.2194232146824106
0.18584507466045078
0.2194232146824106
0.2194232146824106
0.2194232146824106
0.18584507466045078
0.2194232146824106
0.18584507466045078
0.2194232146824106
0.2194232146824106
0.18584507466045078
0.18584507466045078
0.18584507466045078
0.18584507466045078
0.18584507466045078
0.18584507466045078
0.18584507466045078
0.2194232146824106
0.18584507466045078
0.18584507466045078
0.2194232146824106
0.2194232146824106
0.2194232146824106
0.2194232146824106
0.18584507466045078
0.2194232146824106
0.2194232146824106
0.18584507466045078
0.2194232146824106
0.18584507466045078
0.2194232146824106
0.2194232146824106
0.2194232146824106
0.2194232146824106
0.2194232146824106
0.2194232146824106
0.2194232146824106
0.2194232146824106
0.2194232146824106
0.18584507466045078
0.2194232146824106
0.2194232146824106
0.18584507466045078
0.2194232146824106
0.2194232146824106
0.2194232146824106
0.2194232146824106
0.18584507466045078
0.2194232146824106
0.18584507466045078
0.2194232146824106
0.2194232146824106
0.2194232146824106
0.2194232146824106
0.18584507466045078
0.2194232146824106
0.2194232146824106
0.2194232146824106
0.18584507466045078
0.2194232146824106
0.18584507466045078
0.18584507466045078
0.18584507466045078
0.18584507466045078
0.2194232146824106
0.18584507466045078
0.2194232146824106
0.2194232146824106
0.2194232146824106
0.2194232146824106
0.2194232146824106
]

%%
time=(0:0.5:359/2)';
hold on
plot(time,temp)

responsetemp=max(temp)-max(temp)*.632;
plot(12.575,responsetemp,'x')
yline(responsetemp)
xline(12.575)
title('Ice Point Cell Time Constant Test')
ylabel('Temp in C')
xlabel('Time in s')
legend('Probe Response', 'Time Constant (\tau=12.575)')
%risetime=20
stepinfo(temp,time)