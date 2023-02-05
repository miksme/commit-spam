import subprocess
import argparse

def git(*args):
  return subprocess.check_call(['git'] + list(args))


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
  git('switch', '-c', args['branch'])
for i in range(args['commits']):
    open('./spam/file.txt', 'a').write('1')
    git('add','./spam/file.txt')
    git('commit','-m', 'feat: new spam entry')
  
git('push', '-u', 'origin', args['branch'])
if returnToB:
  git('checkout', startingBranch)