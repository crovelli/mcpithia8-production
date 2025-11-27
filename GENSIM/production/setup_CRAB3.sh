# setup CRAB3 dependencies - 
# WARNING: if the crabconfig does not work -> source this file multiple times or directly execute the commands
echo "> Load CRAB3 config"
source /cvmfs/cms.cern.ch/crab3/crab.csh
echo "> activate proxy"
voms-proxy-init --voms cms --valid 168:00
setenv X509_USER_PROXY ~/X509_USER_PROXY
echo $X509_USER_PROXY 
