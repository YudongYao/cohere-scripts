#F /net/s34data/export/34idc-data/2020/Staff20-1//Staff20-1a.spec
#E 1580609738
#D Sat Feb 01 20:15:38 2020
#C sixc  User = cxduser

#O0 Delta  Theta  Chi  Phi  Mu  Gamma  z-sample  rbverpos
#O1 Monochr  Tweak  chi_mono  WhitePos  WhiteGap  Mirror  horiz_gap  horiz_pos
#O2 vert_gap  detectorX  Piezo_X  Piezo_Y  Piezo_Z  Lab_X  Lab_Y  Lab_Z
#O3 Clab_X  Clab_Y  Clab_Z  Sample_X  Sample_Y  camdist  LanlTension  IDEnergy
#O4 Energy  hub_chi  hub_phi  kb_hpos  kb_vpos  detectorY  hxp_chi  hxp_phi
#O5 dacx  Tension  LinkamTemp  tipx  tipy  tipz  ctipx  ctipy
#O6 ctipz  
#o0 del th chi phi mu gam z vp
#o1 mcr twe chimono wbsp wbsg mth hg hp
#o2 vg detx px py pz labx laby labz
#o3 clabx claby clabz x y cam lanl iden
#o4 en hub_chi hub_phi condx condyy dety hxp_chi hxp_phi
#o5 dacx ten linkt tipx tipy tipz ctipx ctipy
#o6 ctipz 
#J0 Seconds  Monitor  Detector  pm detector  PIN  ImageTot  ImageMax  ROI1Tot
#J1 ROI2Tot  ROI3Tot  ROI4Tot  IMSCA1  IMSCA2  IMSCA3  IMSCA4  MantaROI
#J2 Current  Temperature  SECCM Voltage  SECCM Current  
#j0 sec mon det det2 pin imtot immax imroi1
#j1 imroi2 imroi3 imroi4 imsca1 imsca2 imsca3 imsca4 mroi
#j2 cur temp vol sbad019 




#S 299  ascan  labz -1.2 2.8  20 0.2
#D Wed Feb 05 12:05:29 2020
#T 0.2  (Seconds)
#G0 0 0 0 0 0 1 0 0 0 0 0 0 600 0 0 0 143.6 0 0
#G1 1.54 1.54 1.54 90 90 90 4.079990459 4.079990459 4.079990459 90 90 90 1 0 0 0 1 0 60 30 0 0 0 0 60 30 0 90 0 0 1.54 1.54 0 0
#G3 4.079990459 -6.561125068e-16 -6.561125068e-16 0 4.079990459 -2.498273628e-16 0 0 4.079990459
#G4 -0.2017139255 -0.1575099938 0.532607014 1.54 0.00999635 32.16995989 -16.40550365 34.36931693 49.97093241 0 0 0 0 0 0 0 0 0 0 0 0 -180 -180 -180 -180 -180 -180 0
#Q -0.201714 -0.15751 0.532607
#P0 32.831 0.00999635 90 -5 0 10.7905 10.142 -0.0335
#P1 12.690528 -1.3369048 -0.8246601 2.6258 0.1106 0.926866 0.03 0.1485
#P2 0.07 6.1 -2.5 0 0 -0.55 0.003 0.8
#P3 0 0 0 -0.978 2.01 500 0 9.198
#P4 9 90 -5 -659.03887 4971.6398 0 90 0
#P5 12 0 0 0 0 0 8.0950225 -1.24899
#P6 -6.34731 
#UIMDET 34idcTIM2:
#UIM Image header information from areaDetector
#UIM UIMR: ROI information, UIMC: image counter setup
#UIMR Name minX sizeX minY sizeY BgdWidth
#Readout 0 512 0 512
#UIMR1  300 120 15 60 1
#UIMR2  64 128 64 128 0
#UIMR3  210 40 210 40 1
#UIMR4  265 40 210 40 1
#UIMR5  0 256 0 256 1
#UIMC counter STATS# Value-PV
#UIMC1 imtot 5 Total
#UIMC2 immax 5 MaxValue
#UIMC3 imroi1 1 Net
#UIMC4 imroi2 2 Net
#UIMC5 imroi3 3 Net
#UIMC6 imroi4 4 Net
#UIMC7 imsca1 1 MaxValue
#UIMC8 imsca2 2 MaxValue
#UIMC9 imsca3 3 MaxValue
#UIMC10 imsca4 4 MaxValue
#N 25
#L Lab_Z  H  K  L  Epoch  Seconds  pm detector  PIN  ImageTot  ImageMax  ROI1Tot  ROI2Tot  ROI3Tot  ROI4Tot  IMSCA1  IMSCA2  IMSCA3  IMSCA4  MantaROI  Current  Temperature  SECCM Voltage  SECCM Current  Monitor  Detector
-1.2 -0.201714 -0.15751 0.532607 316192.622 0.2 0 0 470 8 4 398 3 2 1 8 1 1 0 0 0 -0.095238095 -0.12454212 832 0
-1 -0.201714 -0.15751 0.532607 316192.954 0.2 2 0 405 10 -16 334 3 -8 1 10 1 1 0 0 0 -0.10500611 -0.12454212 818 0
-0.8 -0.201714 -0.15751 0.532607 316193.278 0.2 3 0 654 11 2 578 1 2 1 11 1 1 0 0 0 -0.10500611 -0.12454212 832 0
-0.6 -0.201714 -0.15751 0.532607 316193.623 0.2 1 0 791 17 -17 711 3 0 1 17 1 0 0 0 0 -0.095238095 -0.11965812 832 0
-0.4 -0.201714 -0.15751 0.532607 316193.947 0.2 2 0 917 15 3 861 -17 0 1 15 1 0 0 0 0 -0.10500611 -0.11965812 818 0
-0.2 -0.201714 -0.15751 0.532607 316194.271 0.2 1 0 1176 17 3 1105 -8 2 1 17 1 1 0 0 0 -0.10500611 -0.11965812 804 0
0 -0.201714 -0.15751 0.532607 316194.604 0.2 1 0 1646 27 4 1572 -8 3 1 27 1 1 0 0 0 -0.095238095 -0.11965812 836 0
0.2 -0.201714 -0.15751 0.532607 316194.929 0.2 4 0 1559 29 5 1483 1 0 1 29 1 0 0 0 0 -0.10500611 -0.11965812 842 0
0.4 -0.201714 -0.15751 0.532607 316195.252 0.2 1 0 5605 86 -14 5521 4 1 1 86 1 1 0 0 0 -0.10500611 -0.11965812 804 0
0.6 -0.201714 -0.15751 0.532607 316195.578 0.2 2 0 13917 211 2 13815 -8 1 1 211 1 1 0 0 0 -0.10500611 -0.11965812 836 0
0.8 -0.201714 -0.15751 0.532607 316195.901 0.2 1 0 21809 351 6 21723 -8 2 1 351 1 1 0 0 0 -0.10500611 -0.11965812 830 0
1 -0.201714 -0.15751 0.532607 316196.225 0.2 3 0 12318 194 7 12239 2 0 1 194 1 0 0 0 0 -0.10500611 -0.11965812 808 0
1.2 -0.201714 -0.15751 0.532607 316196.549 0.2 3 0 5800 102 5 5735 3 1 1 102 1 1 0 0 0 -0.10500611 -0.11965812 832 0
1.4 -0.201714 -0.15751 0.532607 316196.872 0.2 4 0 5511 106 -34 5429 1 1 1 106 1 1 0 0 0 -0.10500611 -0.11965812 830 0
1.6 -0.201714 -0.15751 0.532607 316197.206 0.2 1 0 6342 116 2 6268 1 0 1 116 1 0 0 0 0 -0.10500611 -0.11965812 812 0
1.8 -0.201714 -0.15751 0.532607 316197.530 0.2 4 0 3673 65 4 3592 -17 2 1 65 1 1 0 0 0 -0.10500611 -0.11965812 834 0
2 -0.201714 -0.15751 0.532607 316197.853 0.2 3 0 2041 36 4 1976 5 1 1 36 1 1 0 0 0 -0.10500611 -0.11965812 826 0
2.2 -0.201714 -0.15751 0.532607 316198.177 0.2 4 0 1074 19 5 997 1 0 1 19 1 0 0 0 0 -0.10989011 -0.11965812 824 0
2.4 -0.201714 -0.15751 0.532607 316198.501 0.2 1 0 720 17 8 631 2 0 1 17 1 0 0 0 0 -0.10989011 -0.11965812 826 0
2.6 -0.201714 -0.15751 0.532607 316198.824 0.2 3 0 884 16 -17 825 -8 2 1 16 1 1 0 0 0 -0.10500611 -0.11965812 820 0
2.8 -0.201714 -0.15751 0.532607 316199.148 0.2 3 0 603 13 2 534 0 2 1 13 0 1 0 0 0 -0.10989011 -0.11965812 828 0

#S 300  ascan  th -0.390004 0.409996  80 1
#D Wed Feb 05 12:06:04 2020
#T 1  (Seconds)
#G0 0 0 0 0 0 1 0 0 0 0 0 0 600 0 0 0 143.6 0 0
#G1 1.54 1.54 1.54 90 90 90 4.079990459 4.079990459 4.079990459 90 90 90 1 0 0 0 1 0 60 30 0 0 0 0 60 30 0 90 0 0 1.54 1.54 0 0
#G3 4.079990459 -6.561125068e-16 -6.561125068e-16 0 4.079990459 -2.498273628e-16 0 0 4.079990459
#G4 -0.2017139255 -0.1575099938 0.532607014 1.54 0.00999635 32.16995989 -16.40550365 34.36931693 49.97093241 0 0 0 0 0 0 0 0 0 0 0 0 -180 -180 -180 -180 -180 -180 0
#Q -0.201714 -0.15751 0.532607
#P0 32.831 0.00999635 90 -5 0 10.7905 10.142 -0.0335
#P1 12.690528 -1.3369048 -0.8246601 2.6258 0.1106 0.926866 0.03 0.1485
#P2 0.07 6.1 -2.5 0 0 -0.55 0.003 0.8
#P3 0 0 0 -0.978 2.01 500 0 9.198
#P4 9 90 -5 -659.03887 4971.6398 0 90 0
#P5 12 0 0 0 0 0 8.0950225 -1.24899
#P6 -6.34731 
#UIMDET 34idcTIM2:
#UIM Image header information from areaDetector
#UIM UIMR: ROI information, UIMC: image counter setup
#UIMR Name minX sizeX minY sizeY BgdWidth
#Readout 0 512 0 512
#UIMR1  300 120 15 60 1
#UIMR2  64 128 64 128 0
#UIMR3  210 40 210 40 1
#UIMR4  265 40 210 40 1
#UIMR5  0 256 0 256 1
#UIMC counter STATS# Value-PV
#UIMC1 imtot 5 Total
#UIMC2 immax 5 MaxValue
#UIMC3 imroi1 1 Net
#UIMC4 imroi2 2 Net
#UIMC5 imroi3 3 Net
#UIMC6 imroi4 4 Net
#UIMC7 imsca1 1 MaxValue
#UIMC8 imsca2 2 MaxValue
#UIMC9 imsca3 3 MaxValue
#UIMC10 imsca4 4 MaxValue
#N 25
#L Theta  H  K  L  Epoch  Seconds  pm detector  PIN  ImageTot  ImageMax  ROI1Tot  ROI2Tot  ROI3Tot  ROI4Tot  IMSCA1  IMSCA2  IMSCA3  IMSCA4  MantaROI  Current  Temperature  SECCM Voltage  SECCM Current  Monitor  Detector
-0.3900013 -0.202038 -0.16121 0.531376 316232.903 1 14 0 4351 12 20 494 -4 -5 1 3 1 1 0 0 0 -0.11477411 -0.12454212 4090 0
-0.38000495 -0.20203 -0.161117 0.531407 316238.208 1 18 0 4683 18 14 465 -1 -6 1 3 1 1 0 0 0 -0.10500611 -0.12454212 4080 0
-0.37000015 -0.202021 -0.161025 0.531438 316243.505 1 17 0 4746 9 8 606 -4 -7 1 4 1 1 0 0 0 -0.10500611 -0.12454212 4072 0
-0.3600038 -0.202013 -0.160933 0.531469 316248.802 1 8 0 4911 8 1 614 4 9 2 4 1 1 0 0 0 -0.10500611 -0.12454212 4072 0
-0.35000745 -0.202005 -0.16084 0.5315 316254.107 1 17 0 5156 15 8 610 2 3 1 5 1 1 0 0 0 -0.10500611 -0.11965812 4066 0
-0.34000265 -0.201997 -0.160748 0.531531 316259.403 1 12 0 5213 12 -8 597 8 5 1 3 1 1 0 0 0 -0.10989011 -0.11965812 4060 0
-0.3300063 -0.201989 -0.160655 0.531562 316264.707 1 19 0 5416 11 -14 630 -18 -13 1 5 2 1 0 0 0 -0.11477411 -0.12454212 4046 0
-0.3200015 -0.201981 -0.160563 0.531593 316270.003 1 15 0 5801 12 4 769 9 6 1 5 2 1 0 0 0 -0.11477411 -0.12454212 4032 0
-0.31000515 -0.201973 -0.160471 0.531624 316275.309 1 8 0 6178 14 15 795 -1 4 1 7 2 1 0 0 0 -0.11477411 -0.12454212 4028 0
-0.30000035 -0.201965 -0.160378 0.531655 316280.606 1 14 0 6419 16 1 782 15 4 1 5 1 1 0 0 0 -0.095238095 -0.12454212 4020 0
-0.290004 -0.201957 -0.160286 0.531686 316285.902 1 7 0 6581 13 -10 916 0 -4 1 5 1 1 0 0 0 -0.10500611 -0.12454212 4016 0
-0.28000765 -0.201949 -0.160193 0.531717 316291.209 1 12 0 6783 16 -56 895 -19 -7 1 5 1 1 0 0 0 -0.10500611 -0.12454212 4020 0
-0.27000285 -0.201941 -0.160101 0.531748 316296.506 1 8 0 7456 19 22 1030 6 5 1 6 1 1 0 0 0 -0.10989011 -0.11965812 4016 0
-0.2600065 -0.201933 -0.160008 0.531779 316301.802 1 12 0 7506 15 -35 916 0 3 1 5 1 1 0 0 0 -0.11477411 -0.12454212 4012 0
-0.2500017 -0.201924 -0.159916 0.53181 316307.109 1 19 0 8416 33 19 1090 -5 -5 1 6 1 1 0 0 0 -0.11477411 -0.12454212 4006 0
-0.24000535 -0.201916 -0.159823 0.531841 316312.407 1 11 0 10663 69 -4 1178 -12 -6 2 9 1 1 0 0 0 -0.11477411 -0.12454212 4032 0
-0.23000055 -0.201908 -0.159731 0.531871 316317.704 1 16 0 12813 81 1 1538 12 8 1 9 1 1 0 0 0 -0.10989011 -0.12454212 4030 0
-0.2200042 -0.2019 -0.159638 0.531902 316323.000 1 14 0 17971 304 -4 1742 9 4 1 9 1 1 0 0 0 -0.10500611 -0.12454212 4030 0
-0.21000785 -0.201892 -0.159546 0.531933 316328.306 1 10 0 22527 350 21 1977 11 5 1 9 2 1 0 0 0 -0.10500611 -0.12454212 4030 0
-0.20000305 -0.201884 -0.159453 0.531964 316333.603 1 13 0 22051 245 18 2124 10 -3 1 13 1 1 0 0 0 -0.095238095 -0.12454212 4024 0
-0.1900067 -0.201876 -0.159361 0.531995 316338.899 1 11 0 19422 131 20 2102 -9 1 2 12 1 1 0 0 0 -0.10500611 -0.12454212 4030 0
-0.1800019 -0.201868 -0.159268 0.532025 316344.205 1 8 0 16698 44 23 1967 3 -6 1 9 2 1 0 0 0 -0.10500611 -0.11965812 4032 0
-0.17000555 -0.20186 -0.159176 0.532056 316349.500 1 11 0 17235 77 -3 2300 9 7 1 17 1 1 0 0 0 -0.10989011 -0.11965812 4028 0
-0.16000075 -0.201852 -0.159083 0.532087 316354.805 1 13 0 19630 125 -7 2746 11 3 1 28 1 1 0 0 0 -0.10989011 -0.12454212 4030 0
-0.1500044 -0.201843 -0.158991 0.532118 316360.103 1 9 0 23672 183 -56 3860 11 8 1 44 1 1 0 0 0 -0.11477411 -0.12454212 4030 0
-0.1399996 -0.201835 -0.158898 0.532148 316365.399 1 10 0 28690 222 0 4536 -9 -1 1 53 1 1 0 0 0 -0.11477411 -0.12454212 4022 0
-0.13000325 -0.201827 -0.158806 0.532179 316370.705 1 20 0 32401 242 -15 5819 11 5 1 54 2 1 0 0 0 -0.11477411 -0.12454212 4022 0
-0.1200069 -0.201819 -0.158713 0.53221 316376.001 1 15 0 34334 227 5 6111 -22 -4 1 43 1 1 0 0 0 -0.11477411 -0.12454212 4030 0
-0.1100021 -0.201811 -0.158621 0.53224 316381.309 1 15 0 33755 203 3 5914 -2 -10 1 43 1 1 0 0 0 -0.11477411 -0.12454212 4034 0
-0.10000575 -0.201803 -0.158528 0.532271 316386.606 1 13 0 32374 172 2 6002 -1 -6 1 37 1 1 0 0 0 -0.1001221 -0.12454212 4032 0
-0.09000095 -0.201795 -0.158436 0.532302 316391.902 1 8 0 34526 139 -4 6765 3 -4 1 32 1 1 0 0 0 -0.10989011 -0.12454212 4038 0
-0.0800046 -0.201787 -0.158343 0.532332 316397.209 1 9 0 47108 424 -18 8776 -10 4 2 88 1 1 0 0 0 -0.10989011 -0.12454212 4018 0
-0.0699998 -0.201779 -0.158251 0.532363 316402.515 1 14 0 77172 1110 -1 15164 -4 -4 1 239 1 1 0 0 0 -0.10500611 -0.12454212 4010 0
-0.06000345 -0.201771 -0.158158 0.532393 316407.824 1 11 0 119709 1850 -6 22361 -5 -5 1 344 1 1 0 0 0 -0.10500611 -0.12454212 4024 0
-0.0500071 -0.201763 -0.158066 0.532424 316413.119 1 7 0 188777 3143 21 39709 -9 6 1 654 1 2 0 0 0 -0.10500611 -0.12454212 4038 0
-0.0400023 -0.201754 -0.157973 0.532455 316418.432 1 9 0 276786 4647 -53 54967 1 -6 1 912 1 1 0 0 0 -0.10500611 -0.12454212 4044 0
-0.03000595 -0.201746 -0.15788 0.532485 316423.738 1 13 0 316028 5208 -44 56500 -2 -11 1 942 1 1 0 0 0 -0.10500611 -0.12454212 4052 0
-0.02000115 -0.201738 -0.157788 0.532516 316429.045 1 11 0 356279 5835 -3 73167 1 4 1 1182 1 1 0 0 0 -0.10500611 -0.11965812 4048 0
-0.0100048 -0.20173 -0.157695 0.532546 316434.348 1 8 0 404800 6460 -2 86632 -13 4 1 1436 1 1 0 0 0 -0.10989011 -0.11965812 4072 0
0 -0.201722 -0.157603 0.532577 316439.662 1 16 0 430251 6475 10 89859 -7 -2 1 1376 1 1 0 0 0 -0.1001221 -0.12454212 4074 0
0.00999635 -0.201714 -0.15751 0.532607 316444.967 1 9 0 446550 6588 21 88016 -25 10 1 1286 1 1 0 0 0 -0.11477411 -0.12454212 4082 0
0.0199927 -0.201706 -0.157417 0.532637 316450.270 1 12 0 402516 6015 1 81039 2 3 1 1246 1 1 0 0 0 -0.10989011 -0.12454212 4086 0
0.0299975 -0.201698 -0.157325 0.532668 316455.586 1 16 0 326159 4904 21 62094 4 -5 1 944 1 1 0 0 0 -0.09035409 -0.12454212 4084 0
0.03999385 -0.20169 -0.157232 0.532698 316460.879 1 11 0 268259 4179 -22 53856 -8 -20 1 806 1 1 0 0 0 -0.10500611 -0.12454212 4082 0
0.04999865 -0.201682 -0.15714 0.532729 316466.184 1 10 0 198312 3036 5 38667 0 -2 1 620 1 1 0 0 0 -0.10500611 -0.11965812 4078 0
0.059995 -0.201673 -0.157047 0.532759 316471.480 1 7 0 143306 2037 -25 26597 7 -11 1 386 1 1 0 0 0 -0.11477411 -0.12454212 4076 0
0.0699998 -0.201665 -0.156954 0.532789 316476.786 1 17 0 92851 1209 24 18634 -29 -16 1 259 1 1 0 0 0 -0.11477411 -0.12454212 4084 0
0.07999615 -0.201657 -0.156862 0.53282 316482.081 1 9 0 58168 548 22 10659 -1 -5 1 110 1 1 0 0 0 -0.11477411 -0.12454212 4094 0
0.0899925 -0.201649 -0.156769 0.53285 316487.378 1 10 0 43815 234 17 8441 5 -2 1 55 1 1 0 0 0 -0.10500611 -0.12454212 4102 0
0.0999973 -0.201641 -0.156676 0.53288 316492.683 1 17 0 34390 127 5 6008 -1 -11 1 32 2 1 0 0 0 -0.09035409 -0.12454212 4110 0
0.10999365 -0.201633 -0.156584 0.532911 316497.996 1 15 0 30988 167 2 5564 4 -7 1 33 1 1 0 0 0 -0.10500611 -0.12454212 4114 0
0.11999845 -0.201625 -0.156491 0.532941 316503.303 1 11 0 28159 147 -23 5404 -2 4 1 37 1 1 0 0 0 -0.11477411 -0.10500611 4102 0
0.1299948 -0.201617 -0.156398 0.532971 316508.618 1 12 0 25275 134 -17 4763 5 2 1 37 1 1 0 0 0 -0.1001221 -0.12454212 4098 0
0.1399996 -0.201609 -0.156306 0.533002 316513.914 1 14 0 21077 114 15 3470 9 -15 1 25 1 1 0 0 0 -0.10989011 -0.12454212 4090 0
0.14999595 -0.2016 -0.156213 0.533032 316519.210 1 9 0 18432 75 0 2881 8 4 1 15 1 1 0 0 0 -0.10500611 -0.12454212 4076 0
0.1599923 -0.201592 -0.15612 0.533062 316524.516 1 9 0 16136 62 -13 2805 4 7 1 13 1 1 0 0 0 -0.10500611 -0.11965812 4070 0
0.1699971 -0.201584 -0.156028 0.533092 316529.809 1 11 0 13505 50 15 2146 -9 5 1 10 1 1 0 0 0 -0.11477411 -0.12454212 4064 0
0.17999345 -0.201576 -0.155935 0.533122 316535.115 1 17 0 11963 28 -36 1807 8 5 1 8 1 1 0 0 0 -0.11477411 -0.12454212 4056 0
0.18999825 -0.201568 -0.155842 0.533153 316540.420 1 12 0 10761 22 -3 1577 10 -10 1 7 1 1 0 0 0 -0.10989011 -0.12454212 4056 0
0.1999946 -0.20156 -0.15575 0.533183 316545.714 1 10 0 10240 28 14 1404 7 11 1 7 1 1 0 0 0 -0.095238095 -0.12454212 4062 0
0.2099994 -0.201552 -0.155657 0.533213 316551.012 1 7 0 10635 77 -20 1270 -5 7 1 7 1 1 0 0 0 -0.10500611 -0.12454212 4068 0
0.21999575 -0.201544 -0.155564 0.533243 316556.319 1 13 0 11017 146 -7 1118 7 -14 1 8 1 1 0 0 0 -0.10500611 -0.11965812 4066 0
0.23000055 -0.201536 -0.155471 0.533273 316561.617 1 9 0 9729 90 -8 1121 10 -3 1 6 1 1 0 0 0 -0.1001221 -0.12454212 4058 0
0.2399969 -0.201527 -0.155379 0.533303 316566.914 1 11 0 7902 38 19 942 20 -1 1 4 1 1 0 0 0 -0.11477411 -0.12454212 4050 0
0.24999325 -0.201519 -0.155286 0.533333 316572.208 1 15 0 7044 25 -1 790 -6 15 1 4 1 1 0 0 0 -0.11477411 -0.12454212 4038 0
0.25999805 -0.201511 -0.155193 0.533363 316577.514 1 15 0 6868 15 8 790 0 7 1 4 1 1 0 0 0 -0.10989011 -0.12454212 4030 0
0.2699944 -0.201503 -0.155101 0.533393 316582.810 1 8 0 6627 14 -37 748 13 7 1 6 1 1 0 0 0 -0.10500611 -0.12454212 4016 0
0.2799992 -0.201495 -0.155008 0.533423 316588.115 1 15 0 6915 16 22 740 2 10 1 7 1 1 0 0 0 -0.10500611 -0.12454212 4018 0
0.28999555 -0.201487 -0.154915 0.533453 316593.412 1 11 0 7306 29 12 700 -6 -13 1 5 1 1 0 0 0 -0.10500611 -0.11965812 4024 0
0.30000035 -0.201479 -0.154822 0.533483 316598.719 1 7 0 7763 72 7 669 -5 0 1 6 1 1 0 0 0 -0.095238095 -0.11965812 4026 0
0.3099967 -0.201471 -0.15473 0.533513 316604.014 1 14 0 9049 174 -14 589 4 5 1 3 1 1 0 0 0 -0.11477411 -0.12454212 4018 0
0.31999305 -0.201463 -0.154637 0.533543 316609.309 1 9 0 12241 221 -19 506 10 -15 1 3 1 1 0 0 0 -0.10989011 -0.12454212 4024 0
0.32999785 -0.201454 -0.154544 0.533573 316614.616 1 8 0 13079 204 22 506 -9 -9 1 3 1 1 0 0 0 -0.1001221 -0.12454212 4032 0
0.3399942 -0.201446 -0.154451 0.533603 316619.910 1 12 0 10955 127 22 466 -4 -4 1 3 1 1 0 0 0 -0.11477411 -0.12454212 4030 0
0.349999 -0.201438 -0.154358 0.533633 316625.216 1 6 0 9233 100 -5 462 -6 -4 1 2 1 1 0 0 0 -0.10989011 -0.12454212 4028 0
0.35999535 -0.20143 -0.154266 0.533663 316630.511 1 21 0 8282 70 4 454 5 6 1 4 1 1 0 0 0 -0.10989011 -0.12454212 4040 0
0.37000015 -0.201422 -0.154173 0.533693 316635.807 1 16 0 7156 51 17 397 3 -3 1 3 1 1 0 0 0 -0.10989011 -0.12454212 4048 0
0.3799965 -0.201414 -0.15408 0.533723 316641.112 1 11 0 6386 33 -4 402 7 5 1 4 1 1 0 0 0 -0.10989011 -0.12454212 4050 0
0.38999285 -0.201406 -0.153987 0.533753 316646.419 1 9 0 5860 37 -1 368 18 6 1 4 2 1 0 0 0 -0.10989011 -0.12454212 4048 0
0.39999765 -0.201398 -0.153894 0.533782 316651.725 1 7 0 5638 27 19 421 16 -20 1 4 1 1 0 0 0 -0.10989011 -0.12454212 4042 0
0.409994 -0.201389 -0.153802 0.533812 316657.030 1 8 0 5270 23 2 496 -17 6 1 5 1 1 0 0 0 -0.10989011 -0.12454212 4044 0
#C Wed Feb 05 12:13:34 2020.  do align.mac.

#S 301  ascan  labx -2.55 1.45  20 0.2
#D Wed Feb 05 12:13:34 2020
#T 0.2  (Seconds)
#G0 0 0 0 0 0 1 0 0 0 0 0 0 600 0 0 0 143.6 0 0
#G1 1.54 1.54 1.54 90 90 90 4.079990459 4.079990459 4.079990459 90 90 90 1 0 0 0 1 0 60 30 0 0 0 0 60 30 0 90 0 0 1.54 1.54 0 0
#G3 4.079990459 -6.561125068e-16 -6.561125068e-16 0 4.079990459 -2.498273628e-16 0 0 4.079990459
#G4 -0.2017139255 -0.1575099938 0.532607014 1.54 0.00999635 32.16995989 -16.40550365 34.36931693 49.97093241 0 0 0 0 0 0 0 0 0 0 0 0 -180 -180 -180 -180 -180 -180 0
#Q -0.201714 -0.15751 0.532607
#P0 32.831 0.00999635 90 -5 0 10.7905 10.142 -0.0335
#P1 12.690528 -1.3369048 -0.8246601 2.6258 0.1106 0.926866 0.03 0.1485
#P2 0.07 6.1 -2.5 0 0 -0.55 0.003 0.8
#P3 0 0 0 -0.978 2.01 500 0 9.198
#P4 9 90 -5 -659.03887 4971.6398 0 90 0
#P5 12 0 0 0 0 0 8.0950225 -1.24899
#P6 -6.34731 
#UIMDET 34idcTIM2:
#UIM Image header information from areaDetector
#UIM UIMR: ROI information, UIMC: image counter setup
#UIMR Name minX sizeX minY sizeY BgdWidth
#Readout 0 512 0 512
#UIMR1  300 120 15 60 1
#UIMR2  64 128 64 128 0
#UIMR3  210 40 210 40 1
#UIMR4  265 40 210 40 1
#UIMR5  0 256 0 256 1
#UIMC counter STATS# Value-PV
#UIMC1 imtot 5 Total
#UIMC2 immax 5 MaxValue
#UIMC3 imroi1 1 Net
#UIMC4 imroi2 2 Net
#UIMC5 imroi3 3 Net
#UIMC6 imroi4 4 Net
#UIMC7 imsca1 1 MaxValue
#UIMC8 imsca2 2 MaxValue
#UIMC9 imsca3 3 MaxValue
#UIMC10 imsca4 4 MaxValue
#N 25
#L Lab_X  H  K  L  Epoch  Seconds  pm detector  PIN  ImageTot  ImageMax  ROI1Tot  ROI2Tot  ROI3Tot  ROI4Tot  IMSCA1  IMSCA2  IMSCA3  IMSCA4  MantaROI  Current  Temperature  SECCM Voltage  SECCM Current  Monitor  Detector
-2.55 -0.201714 -0.15751 0.532607 316677.963 0.2 3 0 1267 23 6 1197 1 -9 1 23 1 1 0 0 0 -0.10500611 -0.12454212 800 0
-2.35 -0.201714 -0.15751 0.532607 316678.294 0.2 2 0 1187 25 2 1142 0 0 1 25 0 0 0 0 0 -0.10500611 -0.12454212 824 0
-2.15 -0.201714 -0.15751 0.532607 316678.628 0.2 2 0 758 14 6 697 1 1 1 14 1 1 0 0 0 -0.095238095 -0.12454212 812 0
-1.95 -0.201714 -0.15751 0.532607 316678.952 0.2 5 0 386 9 2 341 2 2 1 9 1 1 0 0 0 -0.10500611 -0.12454212 808 0
-1.75 -0.201714 -0.15751 0.532607 316679.277 0.2 4 0 385 8 4 329 2 1 1 8 1 1 0 0 0 -0.10500611 -0.12454212 822 0
-1.55 -0.201714 -0.15751 0.532607 316679.612 0.2 1 0 587 10 3 523 2 -18 1 10 1 1 0 0 0 -0.09035409 -0.12454212 810 0
-1.35 -0.201714 -0.15751 0.532607 316679.935 0.2 1 0 1564 30 1 1493 1 0 1 30 1 0 0 0 0 -0.10500611 -0.12454212 822 0
-1.15 -0.201714 -0.15751 0.532607 316680.258 0.2 3 0 4339 73 2 4273 0 1 1 73 0 1 0 0 0 -0.10500611 -0.12454212 824 0
-0.95 -0.201714 -0.15751 0.532607 316680.582 0.2 1 0 7962 138 6 7893 2 2 1 138 1 1 0 0 0 -0.10500611 -0.11965812 806 0
-0.75 -0.201714 -0.15751 0.532607 316680.906 0.2 3 0 12190 181 4 12096 1 0 1 181 1 0 0 0 0 -0.10500611 -0.11965812 826 0
-0.55 -0.201714 -0.15751 0.532607 316681.241 0.2 4 0 18441 293 6 18339 1 1 1 293 1 1 0 0 0 -0.10500611 -0.11965812 828 0
-0.35 -0.201714 -0.15751 0.532607 316681.565 0.2 3 0 19673 292 4 19586 1 1 1 292 1 1 0 0 0 -0.10500611 -0.11965812 802 0
-0.15 -0.201714 -0.15751 0.532607 316681.889 0.2 3 0 16135 237 3 16045 -7 2 1 237 1 1 0 0 0 -0.10500611 -0.11965812 812 0
0.05 -0.201714 -0.15751 0.532607 316682.223 0.2 3 0 11472 179 5 11378 5 0 1 179 1 0 0 0 0 -0.10500611 -0.11965812 826 0
0.25 -0.201714 -0.15751 0.532607 316682.547 0.2 2 0 7738 127 2 7654 -9 1 1 127 1 1 0 0 0 -0.10500611 -0.12454212 798 0
0.45 -0.201714 -0.15751 0.532607 316682.871 0.2 2 0 4482 74 3 4398 -7 0 1 74 1 0 0 0 0 -0.10500611 -0.12454212 804 0
0.65 -0.201714 -0.15751 0.532607 316683.195 0.2 3 0 3205 58 5 3134 2 0 1 58 1 0 0 0 0 -0.10500611 -0.12454212 824 0
0.85 -0.201714 -0.15751 0.532607 316683.519 0.2 4 0 2570 40 4 2482 2 2 1 40 1 1 0 0 0 -0.10500611 -0.12454212 794 0
1.05 -0.201714 -0.15751 0.532607 316683.854 0.2 0 0 2164 38 4 2072 3 0 1 38 1 0 0 0 0 -0.10500611 -0.11965812 808 0
1.25 -0.201714 -0.15751 0.532607 316684.177 0.2 3 0 1667 32 0 1606 1 1 0 32 1 1 0 0 0 -0.10500611 -0.11965812 820 0
1.45 -0.201714 -0.15751 0.532607 316684.503 0.2 3 0 1215 19 2 1127 1 0 1 19 1 0 0 0 0 -0.10500611 -0.11965812 804 0

