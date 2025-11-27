#!/bin/bash
# dump files in the PU input configuration accessible for local production
#   valid for 2023 pre BPix only!
# $ dasgoclient -query="dasgoclient -query="site dataset=/Neutrino_E-10_gun/Run3Summer21PrePremix-Summer23_130X_mcRun3_2023_realistic_v13-v1/PREMIX"             
#    T0_CH_CERN_Tape --> NOT accessible when running locally
#    T1_ES_PIC_Disk
#    T1_US_FNAL_Disk
#    T2_CH_CERN
#    T2_FR_IPHC
#    T2_IN_TIFR
#    T2_IT_Rome

DATASET="/Neutrino_E-10_gun/Run3Summer21PrePremix-Summer23_130X_mcRun3_2023_realistic_v13-v1/PREMIX"
FILE="Neutrino_E-10_gun_2023.txt"
dasgoclient -query="file dataset=$DATASET site=T1_ES_PIC_Disk" > $FILE
dasgoclient -query="file dataset=$DATASET site=T1_US_FNAL_Disk" >> $FILE
dasgoclient -query="file dataset=$DATASET site=T2_CH_CERN" >> $FILE
dasgoclient -query="file dataset=$DATASET site=T2_FR_IPHC" >> $FILE
dasgoclient -query="file dataset=$DATASET site=T2_IN_TIFR" >> $FILE
dasgoclient -query="file dataset=$DATASET site=T2_IT_Rome" >> $FILE