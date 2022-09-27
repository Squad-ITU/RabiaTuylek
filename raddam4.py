#export /home/yildiray/anaconda3/envs/MyRoot/bin/thisroot.sh
import ROOT
import numpy as np
import math
from ROOT import gPad,gStyle,TCanvas,TLatex,TGaxis,TH2D
import ratios

etamx=14
depmx=7
nfile=35
nphi=72
per = (2*nfile)-3

xval=[2.9,4.9,6.4,8.1,10.8,13.1,15.1,16.9,18.9,21.1,22.8,25.0,27.1,29.1,30.7,32.6,34.46,35.61,37.0,39.0,41.,43.,45.,47.0,48.9,50.8, 52.8, 54.5, 56.5, 59.0, 61.1, 63.1, 65.1, 66.9]
xerr=[0]
colcode= [1,2,3,4,6,7,'kGreen+3',11,'kCyan+2,8', 'kBlue-7', 'kMagenta-9', 'kRed-5', 'kYellow-6', 'kGreen-6', 'kRed-7']
            

def heatmap(period):
    index = int((period-5)/2+2)
    c1 = TCanvas("c1", "", 1200, 600)
    c1.Divide(2,1)
    
    latex = TLatex()  	
    latex.SetTextSize(0.025)      
    latex.SetTextFont(42)
    latex.SetTextAlign(1)

    ytitle = TLatex()
    ytitle.SetTextSize(0.035)
    ytitle.SetTextFont(42)
    ytitle.SetTextAngle(90.)
    
    xtitle = TLatex()
    xtitle.SetTextSize(0.035)
    xtitle.SetTextFont(42)
    
    y2title = TLatex()
    y2title.SetTextSize(0.035)
    y2title.SetTextFont(42)
    y2title.SetTextAngle(90.)
    
    x2title = TLatex()
    x2title.SetTextSize(0.035)
    x2title.SetTextFont(42)
    
    lumitex = TLatex()
    lumitex.SetTextSize(0.04);
    lumitex.SetTextFont(42);
    
    gStyle.SetPadLeftMargin(0.15);
    gStyle.SetPadRightMargin(0.2);
    gStyle.SetOptStat(0);
    gStyle.SetPalette(53);
    gStyle.SetPaintTextFormat("1.2f");
    gStyle.SetNumberContours(999);
    
    x = np.zeros(7)
    y = np.zeros((14,7))
    y1 = np.zeros((14,7))

    hist = []

    for z in range(2):
       hist.append([])
       for jj in range(14):
           hist_1 = TH2D("hist HEP {}".format(jj), "HE+",7, 0, 7, 14, 0, 14)
           hist_2 = TH2D("hist HEM {}".format(jj), "HE-",7, 0, 7, 14, 0, 14)
           if (z==0):
               hist[0].append(hist_1)
           else:
               hist[1].append(hist_2)
   

    for i in range(14):
                      
        y[i][0]=ratios.true_raddam_0_1[13-i][index]
        y[i][1]=ratios.true_raddam_0_2[13-i][index]
        y[i][2]=ratios.true_raddam_0_3[13-i][index]
        y[i][3]=ratios.true_raddam_0_4[13-i][index]
        y[i][4]=ratios.true_raddam_0_5[13-i][index]
        y[i][5]=ratios.true_raddam_0_6[13-i][index]
        y[i][6]=ratios.true_raddam_0_7[13-i][index]

        y1[i][0]=ratios.true_raddam_1_1[13-i][index]
        y1[i][1]=ratios.true_raddam_1_2[13-i][index]
        y1[i][2]=ratios.true_raddam_1_3[13-i][index]
        y1[i][3]=ratios.true_raddam_1_4[13-i][index]
        y1[i][4]=ratios.true_raddam_1_5[13-i][index]
        y1[i][5]=ratios.true_raddam_1_6[13-i][index]
        y1[i][6]=ratios.true_raddam_1_7[13-i][index]

    for i in range(14):
        for j in range(7):
            x[j] = j
            hist[0][i].Fill(x[j],i, y[i][j])
            hist[1][i].Fill(x[j],i, y1[i][j])
            #print(y1[i][j])

    for j in range(2):#### ikiydi #### yine iki

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
            
            #elif (j==0 & i>0):
            #    hist[j][i].Draw("cola text same")
            #    ReverseYAxis(hist[j][i])
                            
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

            latex.DrawLatex(-0.4, i+0.3,"{}".format(29-i))
            #latex.DrawLatex(-0.4, i+0.3, "")

        for m in range(7):
            latex.DrawLatex(m+0.5,-0.6,"{}".format(m+1))
            #latex.DrawLatex(j+0.5,-0.6,"")


        #lumitex.DrawLatex(5.2, 13,"Form("L = %ifb^{-1}",period)")
        lumitex.DrawLatex(5.2, 13,"L = {}/fb".format(period))

    #c1.SaveAs(Form("HeatMap_Prompt_%ifb.png",period))
    c1.Print("a.png")
    return
    

def ReverseYAxis(hist):
    hist.GetYaxis().SetLabelOffset(999)
    gPad.Update()
    newaxis = TGaxis(gPad.GetUxmin(), gPad.GetUymax(), gPad.GetUxmin()-0.001, gPad.GetUymin(), hist.GetYaxis().GetXmin(), hist.GetYaxis().GetXmax(),0, "B")

    newaxis.SetLabelOffset(-0.05)
    newaxis.SetLabelSize(0.0)
    newaxis.SetTickSize(0.0)
    newaxis.SetLabelFont(42)
    newaxis.Draw()
    return
heatmap(67)    
