import ROOT
import numpy as np
import math
from ROOT import gPad

etamx=14
depmx=7
nfile=35
nphi=72
per = (2*nfile)-3


xval=[2.9,4.9,6.4,8.1,10.8,13.1,15.1,16.9,18.9,21.1,22.8,25.0,27.1,29.1,30.7,32.6,34.46,35.61,37.0,39.0,41.,43.,45.,47.0,48.9,50.8, 52.8, 54.5, 56.5, 59.0, 61.1, 63.1, 65.1, 66.9]
xerr=[0]
colcode= [1,2,3,4,6,7,'kGreen+3',11,'kCyan+2,8', 'kBlue-7', 'kMagenta-9', 'kRed-5', 'kYellow-6', 'kGreen-6', 'kRed-7']
            

def heatmap(period):
    index = (period-5)/2+2
    c1 = ROOT.TCanvas("c1", "", 1200, 600)
    c1.Divide(2,1)
    
    latex = ROOT.TLatex()  	
    latex.SetTextSize(0.025)      
    latex.SetTextFont(42)
    latex.SetTextAlign(1)

    ytitle = ROOT.TLatex()
    ytitle.SetTextSize(0.035)
    ytitle.SetTextFont(42)
    ytitle.SetTextAngle(90.)
    
    xtitle = ROOT.TLatex()
    xtitle.SetTextSize(0.035)
    xtitle.SetTextFont(42)
    
    y2title = ROOT.TLatex()
    y2title.SetTextSize(0.035)
    y2title.SetTextFont(42)
    y2title.SetTextAngle(90.)
    
    x2title = ROOT.TLatex()
    x2title.SetTextSize(0.035)
    x2title.SetTextFont(42)
    
    lumitex = ROOT.TLatex()
    lumitex.SetTextSize(0.04);
    lumitex.SetTextFont(42);
    
    ROOT.gStyle.SetPadLeftMargin(0.15);
    ROOT.gStyle.SetPadRightMargin(0.2);
    ROOT.gStyle.SetOptStat(0);
    ROOT.gStyle.SetPalette(53);
    ROOT.gStyle.SetPaintTextFormat("1.2f");
    ROOT.gStyle.SetNumberContours(999);
    
    slip = -1e-11
    x = np.zeros((14,7))
    y = np.zeros((14,7))
    y1 = np.zeros((14,7))

    
    hist = list()    
    for ii in range(2):
        hist.append([])
        for jj in range(14):
            hist[ii].append([])
    print(hist)
    
            
    def func(i,arg_list):
      print(arg_list[i])
      i+=1
      if(i!=len(arg_list)):
        func(i,arg_list)
        
    f = open('trueratios_prompt_67fb_weighted_lumifix_PUoptimized.txt', 'r').readlines()
    true_raddam_0_1_1 = f[1].split()
    true_raddam_0_1_2 = f[2].split()
    true_raddam_0_1_3 = f[3].split()
    true_raddam_0_1_4 = f[4].split()
    true_raddam_0_1_5 = f[5].split()
    true_raddam_0_1_6 = f[6].split()
    true_raddam_0_1_7 = f[7].split()
    true_raddam_0_1_8 = f[8].split()
    true_raddam_0_1_9 = f[9].split()
    true_raddam_0_1_10 = f[10].split()
    true_raddam_0_1_11 = f[11].split()
    true_raddam_0_1_12 = f[12].split()
    true_raddam_0_1_13 = f[13].split()
    true_raddam_0_1_14 = f[14].split()

    true_raddam_0_1_14_value = true_raddam_0_1_14[-1]
    true_raddam_0_1_13_value = true_raddam_0_1_13[-1]
    true_raddam_0_1_12_value = true_raddam_0_1_12[-1]
    true_raddam_0_1_11_value = true_raddam_0_1_11[-1]
    true_raddam_0_1_10_value = true_raddam_0_1_10[-1]
    true_raddam_0_1_9_value = true_raddam_0_1_9[-1]
    true_raddam_0_1_8_value = true_raddam_0_1_8[-1]
    true_raddam_0_1_7_value = true_raddam_0_1_7[-1]
    true_raddam_0_1_6_value = true_raddam_0_1_6[-1]
    true_raddam_0_1_5_value = true_raddam_0_1_5[-1]
    true_raddam_0_1_4_value = true_raddam_0_1_4[-1]
    true_raddam_0_1_3_value = true_raddam_0_1_3[-1]
    true_raddam_0_1_2_value = true_raddam_0_1_2[-1]
    true_raddam_0_1_1_value = true_raddam_0_1_1[-1]


    l14 = float(true_raddam_0_1_14_value.split('}')[0])
    l13 = float(true_raddam_0_1_13_value.split('}')[0])
    l12 = float(true_raddam_0_1_12_value.split('}')[0])
    l11 = float(true_raddam_0_1_11_value.split('}')[0])
    l10 = float(true_raddam_0_1_10_value.split('}')[0])
    l9 = float(true_raddam_0_1_9_value.split('}')[0])
    l8 = float(true_raddam_0_1_8_value.split('}')[0])
    l7 = float(true_raddam_0_1_7_value.split('}')[0])
    l6 = float(true_raddam_0_1_6_value.split('}')[0])
    l5 = float(true_raddam_0_1_5_value.split('}')[0])
    l4 = float(true_raddam_0_1_4_value.split('}')[0])
    l3 = float(true_raddam_0_1_3_value.split('}')[0])
    l2 = float(true_raddam_0_1_2_value.split('}')[0])
    l1 = float(true_raddam_0_1_1_value.split('}')[0])

    liste = l14,l13,l12,l11,l10,l9,l8,l7,l6,l5,l4,l3,l2,l1
    print("liste", liste)

    true_raddam_0_2_1 = f[35].split()
    true_raddam_0_2_2 = f[36].split()
    true_raddam_0_2_3 = f[37].split()
    true_raddam_0_2_4 = f[38].split()
    true_raddam_0_2_5 = f[39].split()
    true_raddam_0_2_6 = f[40].split()
    true_raddam_0_2_7 = f[41].split()
    true_raddam_0_2_8 = f[42].split()
    true_raddam_0_2_9 = f[43].split()
    true_raddam_0_2_10 = f[44].split()
    true_raddam_0_2_11 = f[45].split()
    true_raddam_0_2_12 = f[46].split()
    true_raddam_0_2_13 = f[47].split()
    true_raddam_0_2_14 = f[48].split()

    true_raddam_0_2_14_value = true_raddam_0_2_14[-1]
    true_raddam_0_2_13_value = true_raddam_0_2_13[-1]
    true_raddam_0_2_12_value = true_raddam_0_2_12[-1]
    true_raddam_0_2_11_value = true_raddam_0_2_11[-1]
    true_raddam_0_2_10_value = true_raddam_0_2_10[-1]
    true_raddam_0_2_9_value = true_raddam_0_2_9[-1]
    true_raddam_0_2_8_value = true_raddam_0_2_8[-1]
    true_raddam_0_2_7_value = true_raddam_0_2_7[-1]
    true_raddam_0_2_6_value = true_raddam_0_2_6[-1]
    true_raddam_0_2_5_value = true_raddam_0_2_5[-1]
    true_raddam_0_2_4_value = true_raddam_0_2_4[-1]
    true_raddam_0_2_3_value = true_raddam_0_2_3[-1]
    true_raddam_0_2_2_value = true_raddam_0_2_2[-1]
    true_raddam_0_2_1_value = true_raddam_0_2_1[-1]


    l214 = float(true_raddam_0_2_14_value.split('}')[0])
    l213 = float(true_raddam_0_2_13_value.split('}')[0])
    l212 = float(true_raddam_0_2_12_value.split('}')[0])
    l211 = float(true_raddam_0_2_11_value.split('}')[0])
    l210 = float(true_raddam_0_2_10_value.split('}')[0])
    l29 = float(true_raddam_0_2_9_value.split('}')[0])
    l28 = float(true_raddam_0_2_8_value.split('}')[0])
    l27 = float(true_raddam_0_2_7_value.split('}')[0])
    l26 = float(true_raddam_0_2_6_value.split('}')[0])
    l25 = float(true_raddam_0_2_5_value.split('}')[0])
    l24 = float(true_raddam_0_2_4_value.split('}')[0])
    l23 = float(true_raddam_0_2_3_value.split('}')[0])
    l22 = float(true_raddam_0_2_2_value.split('}')[0])
    l21 = float(true_raddam_0_2_1_value.split('}')[0])

    liste2 = l214,l213,l212,l211,l210,l29,l28,l27,l26,l25,l24,l23,l22,l21

    true_raddam_0_3_1 = f[54].split()
    true_raddam_0_3_2 = f[55].split()
    true_raddam_0_3_3 = f[56].split()
    true_raddam_0_3_4 = f[57].split()
    true_raddam_0_3_5 = f[58].split()
    true_raddam_0_3_6 = f[59].split()
    true_raddam_0_3_7 = f[60].split()
    true_raddam_0_3_8 = f[61].split()
    true_raddam_0_3_9 = f[62].split()
    true_raddam_0_3_10 = f[63].split()
    true_raddam_0_3_11 = f[64].split()
    true_raddam_0_3_12 = f[65].split()
    true_raddam_0_3_13 = f[66].split()
    true_raddam_0_3_14 = f[67].split()

    true_raddam_0_3_14_value = true_raddam_0_3_14[-1]
    true_raddam_0_3_13_value = true_raddam_0_3_13[-1]
    true_raddam_0_3_12_value = true_raddam_0_3_12[-1]
    true_raddam_0_3_11_value = true_raddam_0_3_11[-1]
    true_raddam_0_3_10_value = true_raddam_0_3_10[-1]
    true_raddam_0_3_9_value = true_raddam_0_3_9[-1]
    true_raddam_0_3_8_value = true_raddam_0_3_8[-1]
    true_raddam_0_3_7_value = true_raddam_0_3_7[-1]
    true_raddam_0_3_6_value = true_raddam_0_3_6[-1]
    true_raddam_0_3_5_value = true_raddam_0_3_5[-1]
    true_raddam_0_3_4_value = true_raddam_0_3_4[-1]
    true_raddam_0_3_3_value = true_raddam_0_3_3[-1]
    true_raddam_0_3_2_value = true_raddam_0_3_2[-1]
    true_raddam_0_3_1_value = true_raddam_0_3_1[-1]

    l314 = float(true_raddam_0_3_14_value.split('}')[0])
    l313 = float(true_raddam_0_3_13_value.split('}')[0])
    l312 = float(true_raddam_0_3_12_value.split('}')[0])
    l311 = float(true_raddam_0_3_11_value.split('}')[0])
    l310 = float(true_raddam_0_3_10_value.split('}')[0])
    l39 = float(true_raddam_0_3_9_value.split('}')[0])
    l38 = float(true_raddam_0_3_8_value.split('}')[0])
    l37 = float(true_raddam_0_3_7_value.split('}')[0])
    l36 = float(true_raddam_0_3_6_value.split('}')[0])
    l35 = float(true_raddam_0_3_5_value.split('}')[0])
    l34 = float(true_raddam_0_3_4_value.split('}')[0])
    l33 = float(true_raddam_0_3_3_value.split('}')[0])
    l32 = float(true_raddam_0_3_2_value.split('}')[0])
    l31 = float(true_raddam_0_3_1_value.split('}')[0])

    liste3 = l314,l313,l312,l311,l310,l39,l38,l37,l36,l35,l34,l33,l32,l31

    true_raddam_0_4_1 = f[73].split()
    true_raddam_0_4_2 = f[74].split()
    true_raddam_0_4_3 = f[75].split()
    true_raddam_0_4_4 = f[76].split()
    true_raddam_0_4_5 = f[77].split()
    true_raddam_0_4_6 = f[78].split()
    true_raddam_0_4_7 = f[79].split()
    true_raddam_0_4_8 = f[80].split()
    true_raddam_0_4_9 = f[81].split()
    true_raddam_0_4_10 = f[82].split()
    true_raddam_0_4_11 = f[83].split()
    true_raddam_0_4_12 = f[84].split()
    true_raddam_0_4_13 = f[85].split()
    true_raddam_0_4_14 = f[86].split()



    true_raddam_0_4_14_value = true_raddam_0_4_14[-1]
    true_raddam_0_4_13_value = true_raddam_0_4_13[-1]
    true_raddam_0_4_12_value = true_raddam_0_4_12[-1]
    true_raddam_0_4_11_value = true_raddam_0_4_11[-1]
    true_raddam_0_4_10_value = true_raddam_0_4_10[-1]
    true_raddam_0_4_9_value = true_raddam_0_4_9[-1]
    true_raddam_0_4_8_value = true_raddam_0_4_8[-1]
    true_raddam_0_4_7_value = true_raddam_0_4_7[-1]
    true_raddam_0_4_6_value = true_raddam_0_4_6[-1]
    true_raddam_0_4_5_value = true_raddam_0_4_5[-1]
    true_raddam_0_4_4_value = true_raddam_0_4_4[-1]
    true_raddam_0_4_3_value = true_raddam_0_4_3[-1]
    true_raddam_0_4_2_value = true_raddam_0_4_2[-1]
    true_raddam_0_4_1_value = true_raddam_0_4_1[-1]


    l414 = float(true_raddam_0_4_14_value.split('}')[0])
    l413 = float(true_raddam_0_4_13_value.split('}')[0])
    l412 = float(true_raddam_0_4_12_value.split('}')[0])
    l411 = float(true_raddam_0_4_11_value.split('}')[0])
    l410 = float(true_raddam_0_4_10_value.split('}')[0])
    l49 = float(true_raddam_0_4_9_value.split('}')[0])
    l48 = float(true_raddam_0_4_8_value.split('}')[0])
    l47 = float(true_raddam_0_4_7_value.split('}')[0])
    l46 = float(true_raddam_0_4_6_value.split('}')[0])
    l45 = float(true_raddam_0_4_5_value.split('}')[0])
    l44 = float(true_raddam_0_4_4_value.split('}')[0])
    l43 = float(true_raddam_0_4_3_value.split('}')[0])
    l42 = float(true_raddam_0_4_2_value.split('}')[0])
    l41 = float(true_raddam_0_4_1_value.split('}')[0])

    liste4 = l414,l413,l412,l411,l410,l49,l48,l47,l46,l45,l44,l43,l42,l41

    true_raddam_0_5_1 = f[92].split()
    true_raddam_0_5_2 = f[93].split()
    true_raddam_0_5_3 = f[94].split()
    true_raddam_0_5_4 = f[95].split()
    true_raddam_0_5_5 = f[96].split()
    true_raddam_0_5_6 = f[97].split()
    true_raddam_0_5_7 = f[98].split()
    true_raddam_0_5_8 = f[99].split()
    true_raddam_0_5_9 = f[100].split()
    true_raddam_0_5_10 = f[101].split()
    true_raddam_0_5_11 = f[102].split()
    true_raddam_0_5_12 = f[103].split()
    true_raddam_0_5_13 = f[104].split()
    true_raddam_0_5_14 = f[105].split()

    true_raddam_0_5_14_value = true_raddam_0_5_14[-1]
    true_raddam_0_5_13_value = true_raddam_0_5_13[-1]
    true_raddam_0_5_12_value = true_raddam_0_5_12[-1]
    true_raddam_0_5_11_value = true_raddam_0_5_11[-1]
    true_raddam_0_5_10_value = true_raddam_0_5_10[-1]
    true_raddam_0_5_9_value = true_raddam_0_5_9[-1]
    true_raddam_0_5_8_value = true_raddam_0_5_8[-1]
    true_raddam_0_5_7_value = true_raddam_0_5_7[-1]
    true_raddam_0_5_6_value = true_raddam_0_5_6[-1]
    true_raddam_0_5_5_value = true_raddam_0_5_5[-1]
    true_raddam_0_5_4_value = true_raddam_0_5_4[-1]
    true_raddam_0_5_3_value = true_raddam_0_5_3[-1]
    true_raddam_0_5_2_value = true_raddam_0_5_2[-1]
    true_raddam_0_5_1_value = true_raddam_0_5_1[-1]


    l514 = float(true_raddam_0_5_14_value.split('}')[0])
    l513 = float(true_raddam_0_5_13_value.split('}')[0])
    l512 = float(true_raddam_0_5_12_value.split('}')[0])
    l511 = float(true_raddam_0_5_11_value.split('}')[0])
    l510 = float(true_raddam_0_5_10_value.split('}')[0])
    l59 = float(true_raddam_0_5_9_value.split('}')[0])
    l58 = float(true_raddam_0_5_8_value.split('}')[0])
    l57 = float(true_raddam_0_5_7_value.split('}')[0])
    l56 = float(true_raddam_0_5_6_value.split('}')[0])
    l55 = float(true_raddam_0_5_5_value.split('}')[0])
    l54 = float(true_raddam_0_5_4_value.split('}')[0])
    l53 = float(true_raddam_0_5_3_value.split('}')[0])
    l52 = float(true_raddam_0_5_2_value.split('}')[0])
    l51 = float(true_raddam_0_5_1_value.split('}')[0])

    liste5 = l514,l513,l512,l511,l510,l59,l58,l57,l56,l55,l54,l53,l52,l51

    true_raddam_0_6_1 = f[111].split()
    true_raddam_0_6_2 = f[112].split()
    true_raddam_0_6_3 = f[113].split()
    true_raddam_0_6_4 = f[114].split()
    true_raddam_0_6_5 = f[115].split()
    true_raddam_0_6_6 = f[116].split()
    true_raddam_0_6_7 = f[117].split()
    true_raddam_0_6_8 = f[118].split()
    true_raddam_0_6_9 = f[119].split()
    true_raddam_0_6_10 = f[120].split()
    true_raddam_0_6_11 = f[121].split()
    true_raddam_0_6_12 = f[122].split()
    true_raddam_0_6_13 = f[123].split()
    true_raddam_0_6_14 = f[124].split()

    true_raddam_0_6_14_value = true_raddam_0_6_14[-1]
    true_raddam_0_6_13_value = true_raddam_0_6_13[-1]
    true_raddam_0_6_12_value = true_raddam_0_6_12[-1]
    true_raddam_0_6_11_value = true_raddam_0_6_11[-1]
    true_raddam_0_6_10_value = true_raddam_0_6_10[-1]
    true_raddam_0_6_9_value = true_raddam_0_6_9[-1]
    true_raddam_0_6_8_value = true_raddam_0_6_8[-1]
    true_raddam_0_6_7_value = true_raddam_0_6_7[-1]
    true_raddam_0_6_6_value = true_raddam_0_6_6[-1]
    true_raddam_0_6_5_value = true_raddam_0_6_5[-1]
    true_raddam_0_6_4_value = true_raddam_0_6_4[-1]
    true_raddam_0_6_3_value = true_raddam_0_6_3[-1]
    true_raddam_0_6_2_value = true_raddam_0_6_2[-1]
    true_raddam_0_6_1_value = true_raddam_0_6_1[-1]


    l614 = float(true_raddam_0_6_14_value.split('}')[0])
    l613 = float(true_raddam_0_6_13_value.split('}')[0])
    l612 = float(true_raddam_0_6_12_value.split('}')[0])
    l611 = float(true_raddam_0_6_11_value.split('}')[0])
    l610 = float(true_raddam_0_6_10_value.split('}')[0])
    l69 = float(true_raddam_0_6_9_value.split('}')[0])
    l68 = float(true_raddam_0_6_8_value.split('}')[0])
    l67 = float(true_raddam_0_6_7_value.split('}')[0])
    l66 = float(true_raddam_0_6_6_value.split('}')[0])
    l65 = float(true_raddam_0_6_5_value.split('}')[0])
    l64 = float(true_raddam_0_6_4_value.split('}')[0])
    l63 = float(true_raddam_0_6_3_value.split('}')[0])
    l62 = float(true_raddam_0_6_2_value.split('}')[0])
    l61 = float(true_raddam_0_6_1_value.split('}')[0])

    liste6 = l614,l613,l612,l611,l610,l69,l68,l67,l66,l65,l64,l63,l62,l61

    true_raddam_0_7_1 = f[129].split()
    true_raddam_0_7_2 = f[130].split()
    true_raddam_0_7_3 = f[131].split()
    true_raddam_0_7_4 = f[132].split()
    true_raddam_0_7_5 = f[133].split()
    true_raddam_0_7_6 = f[134].split()
    true_raddam_0_7_7 = f[135].split()
    true_raddam_0_7_8 = f[136].split()
    true_raddam_0_7_9 = f[137].split()
    true_raddam_0_7_10 = f[138].split()
    true_raddam_0_7_11 = f[139].split()
    true_raddam_0_7_12 = f[140].split()
    true_raddam_0_7_13 = f[141].split()
    true_raddam_0_7_14 = f[142].split()

    true_raddam_0_7_14_value = true_raddam_0_7_14[-1]
    true_raddam_0_7_13_value = true_raddam_0_7_13[-1]
    true_raddam_0_7_12_value = true_raddam_0_7_12[-1]
    true_raddam_0_7_11_value = true_raddam_0_7_11[-1]
    true_raddam_0_7_10_value = true_raddam_0_7_10[-1]
    true_raddam_0_7_9_value = true_raddam_0_7_9[-1]
    true_raddam_0_7_8_value = true_raddam_0_7_8[-1]
    true_raddam_0_7_7_value = true_raddam_0_7_7[-1]
    true_raddam_0_7_6_value = true_raddam_0_7_6[-1]
    true_raddam_0_7_5_value = true_raddam_0_7_5[-1]
    true_raddam_0_7_4_value = true_raddam_0_7_4[-1]
    true_raddam_0_7_3_value = true_raddam_0_7_3[-1]
    true_raddam_0_7_2_value = true_raddam_0_7_2[-1]
    true_raddam_0_7_1_value = true_raddam_0_7_1[-1]


    l714 = float(true_raddam_0_7_14_value.split('}')[0])
    l713 = float(true_raddam_0_7_13_value.split('}')[0])
    l712 = float(true_raddam_0_7_12_value.split('}')[0])
    l711 = float(true_raddam_0_7_11_value.split('}')[0])
    l710 = float(true_raddam_0_7_10_value.split('}')[0])
    l79 = float(true_raddam_0_7_9_value.split('}')[0])
    l78 = float(true_raddam_0_7_8_value.split('}')[0])
    l77 = float(true_raddam_0_7_7_value.split('}')[0])
    l76 = float(true_raddam_0_7_6_value.split('}')[0])
    l75 = float(true_raddam_0_7_5_value.split('}')[0])
    l74 = float(true_raddam_0_7_4_value.split('}')[0])
    l73 = float(true_raddam_0_7_3_value.split('}')[0])
    l72 = float(true_raddam_0_7_2_value.split('}')[0])
    l71 = float(true_raddam_0_7_1_value.split('}')[0])

    liste7 = l714,l713,l712,l711,l710,l79,l78,l77,l76,l75,l74,l73,l72,l71

    true_raddam_1_1_1 = f[148].split()
    true_raddam_1_1_2 = f[149].split()
    true_raddam_1_1_3 = f[150].split()
    true_raddam_1_1_4 = f[151].split()
    true_raddam_1_1_5 = f[152].split()
    true_raddam_1_1_6 = f[153].split()
    true_raddam_1_1_7 = f[154].split()
    true_raddam_1_1_8 = f[155].split()
    true_raddam_1_1_9 = f[156].split()
    true_raddam_1_1_10 = f[157].split()
    true_raddam_1_1_11 = f[158].split()
    true_raddam_1_1_12 = f[159].split()
    true_raddam_1_1_13 = f[160].split()
    true_raddam_1_1_14 = f[161].split()

    true_raddam_1_1_14_value = true_raddam_1_1_14[-1]
    true_raddam_1_1_13_value = true_raddam_1_1_13[-1]
    true_raddam_1_1_12_value = true_raddam_1_1_12[-1]
    true_raddam_1_1_11_value = true_raddam_1_1_11[-1]
    true_raddam_1_1_10_value = true_raddam_1_1_10[-1]
    true_raddam_1_1_9_value = true_raddam_1_1_9[-1]
    true_raddam_1_1_8_value = true_raddam_1_1_8[-1]
    true_raddam_1_1_7_value = true_raddam_1_1_7[-1]
    true_raddam_1_1_6_value = true_raddam_1_1_6[-1]
    true_raddam_1_1_5_value = true_raddam_1_1_5[-1]
    true_raddam_1_1_4_value = true_raddam_1_1_4[-1]
    true_raddam_1_1_3_value = true_raddam_1_1_3[-1]
    true_raddam_1_1_2_value = true_raddam_1_1_2[-1]
    true_raddam_1_1_1_value = true_raddam_1_1_1[-1]

    l1114 = float(true_raddam_1_1_14_value.split('}')[0])
    l1113 = float(true_raddam_1_1_13_value.split('}')[0])
    l1112 = float(true_raddam_1_1_12_value.split('}')[0])
    l1111 = float(true_raddam_1_1_11_value.split('}')[0])
    l1110 = float(true_raddam_1_1_10_value.split('}')[0])
    l119 = float(true_raddam_1_1_9_value.split('}')[0])
    l118 = float(true_raddam_1_1_8_value.split('}')[0])
    l117 = float(true_raddam_1_1_7_value.split('}')[0])
    l116 = float(true_raddam_1_1_6_value.split('}')[0])
    l115 = float(true_raddam_1_1_5_value.split('}')[0])
    l114 = float(true_raddam_1_1_4_value.split('}')[0])
    l113 = float(true_raddam_1_1_3_value.split('}')[0])
    l112 = float(true_raddam_1_1_2_value.split('}')[0])
    l111 = float(true_raddam_1_1_1_value.split('}')[0])

    liste11 = l1114,l1113,l1112,l1111,l1110,l119,l118,l117,l116,l115,l114,l113,l112,l111

    true_raddam_1_2_1 = f[167].split()
    true_raddam_1_2_2 = f[168].split()
    true_raddam_1_2_3 = f[169].split()
    true_raddam_1_2_4 = f[170].split()
    true_raddam_1_2_5 = f[171].split()
    true_raddam_1_2_6 = f[172].split()
    true_raddam_1_2_7 = f[173].split()
    true_raddam_1_2_8 = f[174].split()
    true_raddam_1_2_9 = f[175].split()
    true_raddam_1_2_10 = f[176].split()
    true_raddam_1_2_11 = f[177].split()
    true_raddam_1_2_12 = f[178].split()
    true_raddam_1_2_13 = f[179].split()
    true_raddam_1_2_14 = f[180].split()

    true_raddam_1_2_14_value = true_raddam_1_2_14[-1]
    true_raddam_1_2_13_value = true_raddam_1_2_13[-1]
    true_raddam_1_2_12_value = true_raddam_1_2_12[-1]
    true_raddam_1_2_11_value = true_raddam_1_2_11[-1]
    true_raddam_1_2_10_value = true_raddam_1_2_10[-1]
    true_raddam_1_2_9_value = true_raddam_1_2_9[-1]
    true_raddam_1_2_8_value = true_raddam_1_2_8[-1]
    true_raddam_1_2_7_value = true_raddam_1_2_7[-1]
    true_raddam_1_2_6_value = true_raddam_1_2_6[-1]
    true_raddam_1_2_5_value = true_raddam_1_2_5[-1]
    true_raddam_1_2_4_value = true_raddam_1_2_4[-1]
    true_raddam_1_2_3_value = true_raddam_1_2_3[-1]
    true_raddam_1_2_2_value = true_raddam_1_2_2[-1]
    true_raddam_1_2_1_value = true_raddam_1_2_1[-1]

    l1214 = float(true_raddam_1_2_14_value.split('}')[0])
    l1213 = float(true_raddam_1_2_13_value.split('}')[0])
    l1212 = float(true_raddam_1_2_12_value.split('}')[0])
    l1211 = float(true_raddam_1_2_11_value.split('}')[0])
    l1210 = float(true_raddam_1_2_10_value.split('}')[0])
    l129 = float(true_raddam_1_2_9_value.split('}')[0])
    l128 = float(true_raddam_1_2_8_value.split('}')[0])
    l127 = float(true_raddam_1_2_7_value.split('}')[0])
    l126 = float(true_raddam_1_2_6_value.split('}')[0])
    l125 = float(true_raddam_1_2_5_value.split('}')[0])
    l124 = float(true_raddam_1_2_4_value.split('}')[0])
    l123 = float(true_raddam_1_2_3_value.split('}')[0])
    l122 = float(true_raddam_1_2_2_value.split('}')[0])
    l121 = float(true_raddam_1_2_1_value.split('}')[0])

    liste12 = l1214,l1213,l1212,l1211,l1210,l129,l128,l127,l126,l125,l124,l123,l122,l121

    true_raddam_1_3_1 = f[186].split()
    true_raddam_1_3_2 = f[187].split()
    true_raddam_1_3_3 = f[188].split()
    true_raddam_1_3_4 = f[189].split()
    true_raddam_1_3_5 = f[190].split()
    true_raddam_1_3_6 = f[191].split()
    true_raddam_1_3_7 = f[192].split()
    true_raddam_1_3_8 = f[193].split()
    true_raddam_1_3_9 = f[194].split()
    true_raddam_1_3_10 = f[195].split()
    true_raddam_1_3_11 = f[196].split()
    true_raddam_1_3_12 = f[197].split()
    true_raddam_1_3_13 = f[198].split()
    true_raddam_1_3_14 = f[199].split()

    true_raddam_1_3_14_value = true_raddam_1_3_14[-1]
    true_raddam_1_3_13_value = true_raddam_1_3_13[-1]
    true_raddam_1_3_12_value = true_raddam_1_3_12[-1]
    true_raddam_1_3_11_value = true_raddam_1_3_11[-1]
    true_raddam_1_3_10_value = true_raddam_1_3_10[-1]
    true_raddam_1_3_9_value = true_raddam_1_3_9[-1]
    true_raddam_1_3_8_value = true_raddam_1_3_8[-1]
    true_raddam_1_3_7_value = true_raddam_1_3_7[-1]
    true_raddam_1_3_6_value = true_raddam_1_3_6[-1]
    true_raddam_1_3_5_value = true_raddam_1_3_5[-1]
    true_raddam_1_3_4_value = true_raddam_1_3_4[-1]
    true_raddam_1_3_3_value = true_raddam_1_3_3[-1]
    true_raddam_1_3_2_value = true_raddam_1_3_2[-1]
    true_raddam_1_3_1_value = true_raddam_1_3_1[-1]

    l1314 = float(true_raddam_1_3_14_value.split('}')[0])
    l1313 = float(true_raddam_1_3_13_value.split('}')[0])
    l1312 = float(true_raddam_1_3_12_value.split('}')[0])
    l1311 = float(true_raddam_1_3_11_value.split('}')[0])
    l1310 = float(true_raddam_1_3_10_value.split('}')[0])
    l139 = float(true_raddam_1_3_9_value.split('}')[0])
    l138 = float(true_raddam_1_3_8_value.split('}')[0])
    l137 = float(true_raddam_1_3_7_value.split('}')[0])
    l136 = float(true_raddam_1_3_6_value.split('}')[0])
    l135 = float(true_raddam_1_3_5_value.split('}')[0])
    l134 = float(true_raddam_1_3_4_value.split('}')[0])
    l133 = float(true_raddam_1_3_3_value.split('}')[0])
    l132 = float(true_raddam_1_3_2_value.split('}')[0])
    l131 = float(true_raddam_1_3_1_value.split('}')[0])

    liste13 = l1314,l1313,l1312,l1311,l1310,l139,l138,l137,l136,l135,l134,l133,l132,l131

    true_raddam_1_4_1 = f[205].split()
    true_raddam_1_4_2 = f[206].split()
    true_raddam_1_4_3 = f[207].split()
    true_raddam_1_4_4 = f[208].split()
    true_raddam_1_4_5 = f[209].split()
    true_raddam_1_4_6 = f[210].split()
    true_raddam_1_4_7 = f[211].split()
    true_raddam_1_4_8 = f[212].split()
    true_raddam_1_4_9 = f[213].split()
    true_raddam_1_4_10 = f[214].split()
    true_raddam_1_4_11 = f[215].split()
    true_raddam_1_4_12 = f[216].split()
    true_raddam_1_4_13 = f[217].split()
    true_raddam_1_4_14 = f[218].split()

    true_raddam_1_4_14_value = true_raddam_1_4_14[-1]
    true_raddam_1_4_13_value = true_raddam_1_4_13[-1]
    true_raddam_1_4_12_value = true_raddam_1_4_12[-1]
    true_raddam_1_4_11_value = true_raddam_1_4_11[-1]
    true_raddam_1_4_10_value = true_raddam_1_4_10[-1]
    true_raddam_1_4_9_value = true_raddam_1_4_9[-1]
    true_raddam_1_4_8_value = true_raddam_1_4_8[-1]
    true_raddam_1_4_7_value = true_raddam_1_4_7[-1]
    true_raddam_1_4_6_value = true_raddam_1_4_6[-1]
    true_raddam_1_4_5_value = true_raddam_1_4_5[-1]
    true_raddam_1_4_4_value = true_raddam_1_4_4[-1]
    true_raddam_1_4_3_value = true_raddam_1_4_3[-1]
    true_raddam_1_4_2_value = true_raddam_1_4_2[-1]
    true_raddam_1_4_1_value = true_raddam_1_4_1[-1]

    l1414 = float(true_raddam_1_4_14_value.split('}')[0])
    l1413 = float(true_raddam_1_4_13_value.split('}')[0])
    l1412 = float(true_raddam_1_4_12_value.split('}')[0])
    l1411 = float(true_raddam_1_4_11_value.split('}')[0])
    l1410 = float(true_raddam_1_4_10_value.split('}')[0])
    l149 = float(true_raddam_1_4_9_value.split('}')[0])
    l148 = float(true_raddam_1_4_8_value.split('}')[0])
    l147 = float(true_raddam_1_4_7_value.split('}')[0])
    l146 = float(true_raddam_1_4_6_value.split('}')[0])
    l145 = float(true_raddam_1_4_5_value.split('}')[0])
    l144 = float(true_raddam_1_4_4_value.split('}')[0])
    l143 = float(true_raddam_1_4_3_value.split('}')[0])
    l142 = float(true_raddam_1_4_2_value.split('}')[0])
    l141 = float(true_raddam_1_4_1_value.split('}')[0])

    liste14 = l1414,l1413,l1412,l1411,l1410,l149,l148,l147,l146,l145,l144,l143,l142,l141

    true_raddam_1_5_1 = f[224].split()
    true_raddam_1_5_2 = f[225].split()
    true_raddam_1_5_3 = f[226].split()
    true_raddam_1_5_4 = f[227].split()
    true_raddam_1_5_5 = f[228].split()
    true_raddam_1_5_6 = f[229].split()
    true_raddam_1_5_7 = f[230].split()
    true_raddam_1_5_8 = f[231].split()
    true_raddam_1_5_9 = f[232].split()
    true_raddam_1_5_10 = f[233].split()
    true_raddam_1_5_11 = f[234].split()
    true_raddam_1_5_12 = f[235].split()
    true_raddam_1_5_13 = f[236].split()
    true_raddam_1_5_14 = f[237].split()

    true_raddam_1_5_14_value = true_raddam_1_5_14[-1]
    true_raddam_1_5_13_value = true_raddam_1_5_13[-1]
    true_raddam_1_5_12_value = true_raddam_1_5_12[-1]
    true_raddam_1_5_11_value = true_raddam_1_5_11[-1]
    true_raddam_1_5_10_value = true_raddam_1_5_10[-1]
    true_raddam_1_5_9_value = true_raddam_1_5_9[-1]
    true_raddam_1_5_8_value = true_raddam_1_5_8[-1]
    true_raddam_1_5_7_value = true_raddam_1_5_7[-1]
    true_raddam_1_5_6_value = true_raddam_1_5_6[-1]
    true_raddam_1_5_5_value = true_raddam_1_5_5[-1]
    true_raddam_1_5_4_value = true_raddam_1_5_4[-1]
    true_raddam_1_5_3_value = true_raddam_1_5_3[-1]
    true_raddam_1_5_2_value = true_raddam_1_5_2[-1]
    true_raddam_1_5_1_value = true_raddam_1_5_1[-1]

    l1514 = float(true_raddam_1_4_14_value.split('}')[0])
    l1513 = float(true_raddam_1_4_13_value.split('}')[0])
    l1512 = float(true_raddam_1_4_12_value.split('}')[0])
    l1511 = float(true_raddam_1_4_11_value.split('}')[0])
    l1510 = float(true_raddam_1_4_10_value.split('}')[0])
    l159 = float(true_raddam_1_4_9_value.split('}')[0])
    l158 = float(true_raddam_1_4_8_value.split('}')[0])
    l157 = float(true_raddam_1_4_7_value.split('}')[0])
    l156 = float(true_raddam_1_4_6_value.split('}')[0])
    l155 = float(true_raddam_1_4_5_value.split('}')[0])
    l154 = float(true_raddam_1_4_4_value.split('}')[0])
    l153 = float(true_raddam_1_4_3_value.split('}')[0])
    l152 = float(true_raddam_1_4_2_value.split('}')[0])
    l151 = float(true_raddam_1_4_1_value.split('}')[0])

    liste15 = l1514,l1513,l1512,l1511,l1510,l159,l158,l157,l156,l155,l154,l153,l152,l151

    true_raddam_1_6_1 = f[243].split()
    true_raddam_1_6_2 = f[244].split()
    true_raddam_1_6_3 = f[245].split()
    true_raddam_1_6_4 = f[246].split()
    true_raddam_1_6_5 = f[247].split()
    true_raddam_1_6_6 = f[248].split()
    true_raddam_1_6_7 = f[249].split()
    true_raddam_1_6_8 = f[250].split()
    true_raddam_1_6_9 = f[251].split()
    true_raddam_1_6_10 = f[252].split()
    true_raddam_1_6_11 = f[253].split()
    true_raddam_1_6_12 = f[254].split()
    true_raddam_1_6_13 = f[255].split()
    true_raddam_1_6_14 = f[256].split()

    true_raddam_1_6_14_value = true_raddam_1_6_14[-1]
    true_raddam_1_6_13_value = true_raddam_1_6_13[-1]
    true_raddam_1_6_12_value = true_raddam_1_6_12[-1]
    true_raddam_1_6_11_value = true_raddam_1_6_11[-1]
    true_raddam_1_6_10_value = true_raddam_1_6_10[-1]
    true_raddam_1_6_9_value = true_raddam_1_6_9[-1]
    true_raddam_1_6_8_value = true_raddam_1_6_8[-1]
    true_raddam_1_6_7_value = true_raddam_1_6_7[-1]
    true_raddam_1_6_6_value = true_raddam_1_6_6[-1]
    true_raddam_1_6_5_value = true_raddam_1_6_5[-1]
    true_raddam_1_6_4_value = true_raddam_1_6_4[-1]
    true_raddam_1_6_3_value = true_raddam_1_6_3[-1]
    true_raddam_1_6_2_value = true_raddam_1_6_2[-1]
    true_raddam_1_6_1_value = true_raddam_1_6_1[-1]

    l1614 = float(true_raddam_1_6_14_value.split('}')[0])
    l1613 = float(true_raddam_1_6_13_value.split('}')[0])
    l1612 = float(true_raddam_1_6_12_value.split('}')[0])
    l1611 = float(true_raddam_1_6_11_value.split('}')[0])
    l1610 = float(true_raddam_1_6_10_value.split('}')[0])
    l169 = float(true_raddam_1_6_9_value.split('}')[0])
    l168 = float(true_raddam_1_6_8_value.split('}')[0])
    l167 = float(true_raddam_1_6_7_value.split('}')[0])
    l166 = float(true_raddam_1_6_6_value.split('}')[0])
    l165 = float(true_raddam_1_6_5_value.split('}')[0])
    l164 = float(true_raddam_1_6_4_value.split('}')[0])
    l163 = float(true_raddam_1_6_3_value.split('}')[0])
    l162 = float(true_raddam_1_6_2_value.split('}')[0])
    l161 = float(true_raddam_1_6_1_value.split('}')[0])

    liste16 = l1614,l1613,l1612,l1611,l1610,l169,l168,l167,l166,l165,l164,l163,l162,l161

    true_raddam_1_7_1 = f[262].split()
    true_raddam_1_7_2 = f[263].split()
    true_raddam_1_7_3 = f[264].split()
    true_raddam_1_7_4 = f[265].split()
    true_raddam_1_7_5 = f[266].split()
    true_raddam_1_7_6 = f[267].split()
    true_raddam_1_7_7 = f[268].split()
    true_raddam_1_7_8 = f[269].split()
    true_raddam_1_7_9 = f[270].split()
    true_raddam_1_7_10 = f[271].split()
    true_raddam_1_7_11 = f[272].split()
    true_raddam_1_7_12 = f[273].split()
    true_raddam_1_7_13 = f[274].split()
    true_raddam_1_7_14 = f[275].split()

    true_raddam_1_7_14_value = true_raddam_1_7_14[-1]
    true_raddam_1_7_13_value = true_raddam_1_7_13[-1]
    true_raddam_1_7_12_value = true_raddam_1_7_12[-1]
    true_raddam_1_7_11_value = true_raddam_1_7_11[-1]
    true_raddam_1_7_10_value = true_raddam_1_7_10[-1]
    true_raddam_1_7_9_value = true_raddam_1_7_9[-1]
    true_raddam_1_7_8_value = true_raddam_1_7_8[-1]
    true_raddam_1_7_7_value = true_raddam_1_7_7[-1]
    true_raddam_1_7_6_value = true_raddam_1_7_6[-1]
    true_raddam_1_7_5_value = true_raddam_1_7_5[-1]
    true_raddam_1_7_4_value = true_raddam_1_7_4[-1]
    true_raddam_1_7_3_value = true_raddam_1_7_3[-1]
    true_raddam_1_7_2_value = true_raddam_1_7_2[-1]
    true_raddam_1_7_1_value = true_raddam_1_7_1[-1]

    l1714 = float(true_raddam_1_7_14_value.split('}')[0])
    l1713 = float(true_raddam_1_7_13_value.split('}')[0])
    l1712 = float(true_raddam_1_7_12_value.split('}')[0])
    l1711 = float(true_raddam_1_7_11_value.split('}')[0])
    l1710 = float(true_raddam_1_7_10_value.split('}')[0])
    l179 = float(true_raddam_1_7_9_value.split('}')[0])
    l178 = float(true_raddam_1_7_8_value.split('}')[0])
    l177 = float(true_raddam_1_7_7_value.split('}')[0])
    l176 = float(true_raddam_1_7_6_value.split('}')[0])
    l175 = float(true_raddam_1_7_5_value.split('}')[0])
    l174 = float(true_raddam_1_7_4_value.split('}')[0])
    l173 = float(true_raddam_1_7_3_value.split('}')[0])
    l172 = float(true_raddam_1_7_2_value.split('}')[0])
    l171 = float(true_raddam_1_7_1_value.split('}')[0])

    liste17 = l1714,l1713,l1712,l1711,l1710,l179,l178,l177,l176,l175,l174,l173,l172,l171
    #func(0,liste)
    #func(0,liste2)
    
    
 

    for i in range(14):
        #i=i+1      
        hist[0][i] = ROOT.TH2D("hist", "HE+",7, 0, 7, 14, 0, 14)
        hist[1][i] = ROOT.TH2D("hist", "HE-",7, 0, 7, 14, 0, 14)
        
                      
        y[i][0] = func(0,liste)
        y[i][1] = func(0,liste2)
        y[i][2] = func(0,liste3)
        y[i][3] = func(0,liste4)
        y[i][4] = func(0,liste5)
        y[i][5] = func(0,liste6)
        y[i][6] = func(0,liste7)
        
        y1[i][0] = func(0,liste11)
        y1[i][1] = func(0,liste12)
        y1[i][2] = func(0,liste13)
        y1[i][3] = func(0,liste14)
        y1[i][4] = func(0,liste15)
        y1[i][5] = func(0,liste16)
        y1[i][6] = func(0,liste17)
        
        
        for j in range(7):          
            x[i][j] = j  

    for i in range(14):
        for j in range(7):
            hist[0][i].Fill(x[i][j],i, y[i][j])
            hist[1][i].Fill(x[i][j],i, y1[i][j])


    for j in range(1):#### ikiydi
        j = j+0
        c1.cd(j+1)
        c1.SetFrameLineWidth(0)


        for i in range(14):
            if (i==0 & j==0):
                hist[j][i].GetZaxis().SetRangeUser(0.5, 1.2)
                hist[j][i].GetZaxis().SetLabelSize(0.025)
                hist[j][i].Draw("colza text")
                xtitle.DrawLatex(3.35, -1.3, "Depth")
                ytitle.DrawLatex(-0.6, 6, "Channel")

                ReverseYAxis(hist[j][i])

            elif (j==0 & i!=0):
                hist[j][i].Draw("cola text same")
                ReverseYAxis(hist[j][i])

            elif (j==1 & i==0):

                hist[j][i].GetZaxis().SetLabelSize(0.025)
                hist[j][i].GetZaxis().SetRangeUser(0.5, 1.2)
                hist[j][i].Draw("colza text")

                x2title.DrawLatex(3.35, -1.3, "Depth")
                y2title.DrawLatex(-0.6, 6, "Channel")
                ReverseYAxis(hist[j][i])


            else:
                hist[j][i].Draw("cola text same")
                ReverseYAxis(hist[j][i])

            #latex.DrawLatex(-0.4, i+0.3, Form("%i",29-i))
            latex.DrawLatex(-0.4, i+0.3, "")

        for j in range(7):
            j = j+0
            #latex.DrawLatex(j+0.5,-0.6,"Form("%i",j+1)")
            latex.DrawLatex(j+0.5,-0.6,"")


        #lumitex.DrawLatex(5.2, 13,"Form("L = %ifb^{-1}",period)")
        lumitex.DrawLatex(5.2, 13,"")

    #c1.SaveAs(Form("HeatMap_Prompt_%ifb.png",period))
    c1.Print("a.pdf")
    return


def ReverseYAxis(hist):
    hist.GetYaxis().SetLabelOffset(999)
    gPad.Update()
    newaxis = ROOT.TGaxis(gPad.GetUxmin(), gPad.GetUymax(), gPad.GetUxmin()-0.001, gPad.GetUymin(), hist.GetYaxis().GetXmin(), hist.GetYaxis().GetXmax(),0, "B")

    newaxis.SetLabelOffset(-0.05)
    newaxis.SetLabelSize(0.0)
    newaxis.SetTickSize(0.0)
    newaxis.SetLabelFont(42)
    newaxis.Draw()
    return
heatmap(67)    

