import subprocess
import argparse
import os
def git(*args):
  return subprocess.check_call(['git'] + list(args))
def switchBranch(name):
  os.system(f"git checkout {name} 2>/dev/null || git checkout -b {name}") # Switch to branch and create it if it does not exist

parser = argparse.ArgumentParser()
parser.add_argument('-b', '--branch', type=str, default='spam', help='Branch to spam on')
parser.add_argument('-c', '--commits', type=int, default=100, help='Number of commits to make')
args = vars(parser.parse_args())

p = subprocess.Popen(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = p.communicate()
startingBranch = stdout.decode("utf-8").splitlines()[0]
returnToB = False
if(startingBranch != args['branch']):
  returnToB = True
  switchBranch(args['branch'])
for i in range(args['commits']):
    git('commit','--allow-empty','-m', 'feat: new spam entry')
git('push', '-u', 'origin', args['branch'])
if returnToB:
  git('checkout', startingBranch)