#!/bin/bash
# dump files in the PU input configuration accessible for local production
#   valid for bot 2022 and 2022EE
# $ dasgoclient -query="site dataset=/Neutrino_E-10_gun/Run3Summer21PrePremix-Summer22_124X_mcRun3_2022_realistic_v11-v2/PREMIX"             
#    T0_CH_CERN_Tape -- > NOT accessible when running locally
#    T1_ES_PIC_Disk
#    T1_US_FNAL_Disk
#    T2_CH_CERN
#    T2_FR_IPHC
#    T2_IT_Rome
#    T3_US_FNALLPC
#    T3_US_Rutgers
dasgoclient -query="file dataset=/Neutrino_E-10_gun/Run3Summer21PrePremix-Summer22_124X_mcRun3_2022_realistic_v11-v2/PREMIX site=T1_ES_PIC_Disk" > Neutrino_E-10_gun_2022.txt
dasgoclient -query="file dataset=/Neutrino_E-10_gun/Run3Summer21PrePremix-Summer22_124X_mcRun3_2022_realistic_v11-v2/PREMIX site=T1_US_FNAL_Disk" >> Neutrino_E-10_gun_2022.txt
dasgoclient -query="file dataset=/Neutrino_E-10_gun/Run3Summer21PrePremix-Summer22_124X_mcRun3_2022_realistic_v11-v2/PREMIX site=T2_CH_CERN" >> Neutrino_E-10_gun_2022.txt
dasgoclient -query="file dataset=/Neutrino_E-10_gun/Run3Summer21PrePremix-Summer22_124X_mcRun3_2022_realistic_v11-v2/PREMIX site=T2_FR_IPHC" >> Neutrino_E-10_gun_2022.txt
dasgoclient -query="file dataset=/Neutrino_E-10_gun/Run3Summer21PrePremix-Summer22_124X_mcRun3_2022_realistic_v11-v2/PREMIX site=T2_IT_Rome" >> Neutrino_E-10_gun_2022.txt
dasgoclient -query="file dataset=/Neutrino_E-10_gun/Run3Summer21PrePremix-Summer22_124X_mcRun3_2022_realistic_v11-v2/PREMIX site=T3_US_FNALLPC" >> Neutrino_E-10_gun_2022.txt
dasgoclient -query="file dataset=/Neutrino_E-10_gun/Run3Summer21PrePremix-Summer22_124X_mcRun3_2022_realistic_v11-v2/PREMIX site=T3_US_FNALLPC" >> Neutrino_E-10_gun_2022.txt