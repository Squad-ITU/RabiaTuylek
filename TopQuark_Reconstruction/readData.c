void readData()

{
    fstream filephotonpt;
    fstream filephotoneta;
    fstream filephotoncleta;
    fstream filephotonphi;
    fstream filephotone;

    fstream filemetmet;
    fstream filemetphi;
    
    fstream filesumet;

    fstream fileise;
    fstream fileismu;
    
    fstream filejetpt;
    fstream filejeteta;
    fstream filejetphi;
    
    fstream filejete;
    fstream filejetbtag;
    fstream filejethasbtag;

    

    filephotonpt.open("lepton_pt.txt", ios::in);
    filephotoneta.open("lepton_eta.txt", ios::in);
    filephotoncleta.open("lepton_cl_eta.txt", ios::in);
    filephotonphi.open("lepton_phi.txt", ios::in);
    filephotone.open("lepton_e.txt", ios::in);

    filemetmet.open("met_met.txt", ios::in);
    filemetphi.open("met_phi.txt", ios::in);

    filesumet.open("sumet.txt", ios::in);

    fileise.open("lepton_is_e.txt", ios::in);
    fileismu.open("lepton_is_mu.txt", ios::in);

    filejetpt.open("jet_pt.txt", ios::in);
    filejeteta.open("jet_eta.txt", ios::in);
    filejetphi.open("jet_phi.txt", ios::in);
    filejete.open("jet_e.txt", ios::in);
    filejetbtag.open("jet_btag_weight.txt", ios::in);
    filejethasbtag.open("jet_has_btag.txt", ios::in);



    double x,   lepton_pt;
    double x1,  lepton_eta;
    double x2, lepton_cl_eta;
    double x3,  lepton_phi;
    double x4,  lepton_e;
    double x5,  met_met;
    double x6,  met_phi;
    double x7, sumet;
    double x8, lepton_is_e;
    double x9, lepton_is_mu;
    double x10,  jet_pt;
    double x11,  jet_eta;
    double x12,  jet_phi;
    double x13, jet_e;
    double x14,  jet_btag_weight;
    double x15, jet_has_btag;
    
    TFile *output = new TFile("data.root", "create");  // TFile can open TBrowser
    
    // create TTree
    TTree *tree = new TTree("tree","tree");
    //tree->Branch("x", &x, "x/D");
    tree->Branch("lepton_pt", &lepton_pt, "lepton_pt/D");
    tree->Branch("lepton_eta", &lepton_eta, "lepton_eta/D");
    tree->Branch("lepton_cl_eta", &lepton_cl_eta, "lepton_cl_eta/D");
    tree->Branch("lepton_phi", &lepton_phi, "lepton_phi/D");
    tree->Branch("lepton_e", &lepton_e, "lepton_e/D");

    tree->Branch("met_met", &met_met, "met_met/D");
    tree->Branch("met_phi", &met_phi, "met_phi/D");

    tree->Branch("sumet", &sumet, "sumet/D");

    tree->Branch("lepton_is_e", &lepton_is_e, "lepton_is_e/D");
    tree->Branch("lepton_is_mu", &lepton_is_mu, "lepton_is_mu/D");

    tree->Branch("jet_pt", &jet_pt, "jet_pt/D");
    tree->Branch("jet_eta", &jet_eta, "jet_eta/D");
    tree->Branch("jet_phi", &jet_phi, "jet_phi/D");
    tree->Branch("jet_e", &jet_e, "jet_e");
    tree->Branch("jet_btag_weight", &jet_btag_weight, "jet_btag_weight/D");
    tree->Branch("jet_has_btag", &jet_has_btag, "jet_has_btag/D");

    
    while(1)
    {
        filephotonpt >>    x >> lepton_pt;
        filephotoneta >>   x1 >> lepton_eta;
        filephotoncleta >> x2 >> lepton_cl_eta;
        filephotonphi >>   x3 >> lepton_phi;
        filephotone >>     x4 >> lepton_e;
        filemetmet >>      x5 >> met_met;
        filemetphi >>      x6 >> met_phi;
        filesumet >>       x7 >> sumet;
        fileise >>         x8 >> lepton_is_e;
        fileismu >>        x9 >> lepton_is_mu;
        filejetpt >>       x10 >> jet_pt;
        filejeteta >>      x11 >> jet_eta;
        filejetphi >>      x12 >> jet_phi;
        filejete >>        x13 >> jet_e;
        filejetbtag >>     x14 >> jet_btag_weight;
        filejethasbtag >>  x15 >> jet_has_btag;

 
        if(filephotonpt.eof()) break;
        if(filephotoneta.eof()) break;   
        if(filephotoncleta.eof()) break;  
        if(filephotonphi.eof()) break;  
        if(filephotone.eof()) break; 
        if(filemetmet.eof()) break; 
        if(filemetphi.eof()) break;
        if(filesumet.eof()) break;   
        if(fileise.eof()) break;  
        if(fileismu.eof()) break;       
        if(filejetpt.eof()) break; 
        if(filejeteta.eof()) break; 
        if(filejetphi.eof()) break; 
        if(filejete.eof()) break;
        if(filejetbtag.eof()) break; 
        if(filejethasbtag.eof()) break;      
        
        //cout << x << " " << muon_eta << endl;
        
        tree->Fill();
         
    }
    output->Write();
    output->Close();

    filephotonpt.close();
    filephotoneta.close();
    filephotoncleta.close();
    filephotonphi.close();
    filephotone.close();
    filemetmet.close();
    filemetphi.close();
    filesumet.close();
    fileise.close();
    fileismu.close();
    filejetpt.close();
    filejeteta.close();
    filejetphi.close();
    filejete.close();
    filejetbtag.close();
    filejethasbtag.close();
    
}
