import os
import fnmatch
import subprocess
import datetime

def merge_ROOT_files():
    output_file = datetime.datetime.utcnow().strftime("./%Y-%m-%dT%H%M%SZ_merged.root")

    root_files = [
        os.path.join(root, filename)
        for root, dirs, files in os.walk('/eos/cms/store/group/phys_bphys/crovelli/ZTauTau3Mu_Run3Summer22GS_v1_2025Aug01/ZTauTau3Mu_testEDM0_TuneCP5_13p6TeV_pythia8_Run3Summer22GS_v1/ZTauTau3Mu_testEDM0_Run3Summer22GS_v1/250801_085354/0000/')
        for filename in files
        if fnmatch.fnmatch(filename, '*.root')
    ]

    # Remove 'echo' when you want to go live.
    subprocess.check_call(['echo', 'python haddnano.py', output_file]+root_files)

if __name__ == "__main__":
    merge_ROOT_files()
