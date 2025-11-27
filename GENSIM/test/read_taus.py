# !/bin/python3

import ROOT
import sys
from DataFormats.FWLite import Handle, Events
from tqdm import tqdm  # For progress bar
import numpy as np

# Input file
input_file = "file:WTau3Mu_MTau1950-Run3Summer22GS_10.root"  # Change to your input
events = Events(input_file)

# Handle for genParticles
gen_handle = Handle("std::vector<reco::GenParticle>")
gen_label = ("genParticles")

# Output ROOT file and TTree
output_file = ROOT.TFile("taus.root", "RECREATE")
tree = ROOT.TTree("TauTree", "Gen-level taus")

# Define variables
pt = ROOT.std.vector('float')()
eta = ROOT.std.vector('float')()
phi = ROOT.std.vector('float')()
mass = ROOT.std.vector('float')()
charge = ROOT.std.vector('int')()

tree.Branch("pt", pt)
tree.Branch("eta", eta)
tree.Branch("phi", phi)
tree.Branch("mass", mass)
tree.Branch("charge", charge)

# Progress bar setup
n_events = np.min([events.size(), 5000])
print(f"Processing {n_events} events...")

# Event loop with progress bar
for event in tqdm(events, total=n_events, desc="Analyzing"):
    event.getByLabel(gen_label, gen_handle)
    gen_particles = gen_handle.product()

    pt.clear()
    eta.clear()
    phi.clear()
    mass.clear()
    charge.clear()

    for p in gen_particles:
        if abs(p.pdgId()) == 15 and p.status() == 2:  # Status 2: decayed
            pt.push_back(p.pt())
            eta.push_back(p.eta())
            phi.push_back(p.phi())
            mass.push_back(p.mass())
            charge.push_back(p.charge())

    tree.Fill()

# Write and close
output_file.Write()
output_file.Close()

print("Done. Saved output to taus.root")
