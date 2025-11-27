import CRABClient
from CRABClient.UserUtilities import config, ClientException
import yaml
import datetime
from fnmatch import fnmatch
import argparse

import sys
import os
sys.path.append( os.path.join( os.path.dirname(os.path.abspath(__file__)), os.pardir, os.pardir))
import config.conditions as conditions

if __name__ == '__main__':
    from CRABAPI.RawCommand import crabCommand
    from CRABClient.ClientExceptions import ClientException
    from http.client import HTTPException
    from multiprocessing import Process

    parser = argparse.ArgumentParser(description='CRAB configuration for tau3mu production')
    parser.add_argument('--config',
                        type=str, required=True,
                        help='path to the configuration file to submit on CRAB')
    parser.add_argument('--process_name',
                        type=str, default='TTbarLNuLNu_Tau3Mu',
                        help='process to simulate - default is TTbarLNuLNu_Tau3Mu')
    parser.add_argument('--campaign',
                        choices= conditions.campaigns, default='Run3Summer22',
                        help='campaign for the production')
    parser.add_argument('-N', '--Nevents',
                        type=int, default=50000,
                        help='number of events to produce')
    parser.add_argument('-t', '--tag',
                        type=str, default='TTbarLNuLNu',
                        help='tag for the production - use MTauxxxx for the mass of the tau in MeV')
    parser.add_argument('-v', '--version',
                        type=str, default='v0',
                        help='Version of the production')
    parser.add_argument('--dryrun',
                        action='store_true',
                        help='perform a dry run without submitting the task')
    args = parser.parse_args()

    dry_run_ = args.dryrun
    
    config_file     = args.config

    process_name    = args.process_name
    tag             = args.tag
    campaign        = args.campaign
    step            = 'LHEGS' # LHE,GEN,SIM
    production_tag  = datetime.date.today().strftime('%Y%b%d')
    version         = 'v'+str(args.version)

    Nevents        = args.Nevents

    request_name    = '_'.join([process_name, tag, campaign+step, version])
    work_area       = '_'.join([process_name, campaign+step, version, production_tag]) 
    dataset_tag     = '_'.join([process_name, tag, campaign+step, version])
    dataset_name    = '_'.join([process_name, tag, 'TuneCP5_13p6TeV_powheg-pythia8', campaign+step, version])

    config = config()

    config.section_('General')
    config.General.requestName = request_name
    config.General.workArea = work_area 
    config.General.transferOutputs = True
    config.General.transferLogs = True

    config.section_('Data')
    config.Data.publication = True
    config.Data.outputPrimaryDataset = dataset_name 
    config.Data.outLFNDirBase = '/store/group/phys_bphys/crovelli/%s' % (config.General.workArea)
    config.Data.splitting = 'EventBased'
    config.Data.unitsPerJob = 232 
    config.Data.totalUnits = Nevents
    config.Data.outputDatasetTag = dataset_tag
    # chiara: check on DAS the DBS (no need for gridpack)
    #config.Data.inputDBS = 'global'
    #config.Data.inputDBS = 'phys03'

    config.section_('JobType')
    config.JobType.pluginName = 'PrivateMC'
    config.JobType.psetName = config_file
    config.JobType.inputFiles = []
    config.JobType.disableAutomaticOutputCollection = False # automatic recognition of output files
    #config.JobType.outputFiles = ['ppW3MuNu_Run3Summer22EEwmLHEGS.root']
    #config.JobType.allowUndistributedCMSSW = True

    config.section_('User')

    config.section_('Site')
    config.Site.storageSite = 'T2_CH_CERN'
 
    def submit(config):
      try:
          print(config)
          if not dry_run_: crabCommand('submit', config = config)
      except HTTPException as hte:
          print("Failed submitting task:",hte.headers)
      except ClientException as cle:
          print("Failed submitting task:",cle)


    submit(config)
