import argparse

import sys
import os
sys.path.append( os.path.join( os.path.dirname(os.path.abspath(__file__)), os.pardir))
import config.conditions as conditions

def cmsDriver_command(genfragment = None, campaign = 'Run3Summer22', number = 1000) :
    """
    Generate the cmsDriver command for the given conditions
    based on the campaign specified in the command line argument.
    = produce the config file for cmsRun 
    """
    
    if genfragment is None:
        raise ValueError("Gen fragment must be specified.")
        return
    #if not os.path.exists(genfragment):
    #    raise FileNotFoundError(f"Gen fragment '{genfragment}' does not exist.")
    #    return
    file_base = os.path.basename(genfragment)
    if file_base.endswith('_fragment.py'):
        file_base = file_base[:-len('_fragment.py')]
    
    out_config = f'{file_base}{campaign}GS_cfg.py'
    out_root = f'{file_base}_{campaign}GS.root'   


    if campaign not in conditions.conditions:
        raise ValueError(f"Campaign '{campaign}' not found in conditions.")
    cond = conditions.conditions[campaign]
    
    command = " ".join(['cmsDriver.py', genfragment,
                        '--eventcontent RAWSIM',
                        '--datatier GEN-SIM',
                        '--conditions', cond['globalTag'],
                        '--beamspot', cond['beamSpot'],
                        '--customise_commands process.source.numberEventsInLuminosityBlock="cms.untracked.uint32(100)"',
                        '--step GEN,SIM',
                        '--geometry DB:Extended',
                        '--era', cond['era'],
                        '--python_filename', out_config,
                        '--fileout', out_root,
                        '--mc',
                        '--no_exec',
                        '--number', str(number),
                        '--number_out', str(number),
    ])
    print(command + '\n')

    return command, out_config


if __name__ == "__main__":

    argparser = argparse.ArgumentParser(description="Generate cmsDriver command for a given campaign.")
    argparser.add_argument("--genfragment", 
                           default=None, 
                           help="Gen fragment to use")
    argparser.add_argument("--campaign", 
                           choices=conditions.campaigns,
                           default="Run3Summer22", 
                           help="Campaign to use")
    argparser.add_argument("-N", "--number",
                           type=int, default=100, 
                           help="Number of events to produce (default: 1000)")
    argparser.add_argument("--dryrun",
                           action="store_true", 
                           help="If set, only print the command without executing it")
    args = argparser.parse_args()
    print('\n')

    genfragment = args.genfragment
    campaign = args.campaign
    N = args.number
    cmd, cfg = cmsDriver_command(genfragment, campaign, N)
    
    if args.dryrun:
        print("[DRY-RUN] command not executed.")
        exit(0)
    print("[EXE] executing command...")
    os.system(cmd)
    if os.path.exists(cfg):
        print(f" DONE - config file {cfg} created.")
        os.system(f' mv {cfg} test/')
    else:
        print(f"[ERROR] config file {cfg} not created.")
        exit(1)
       
    

