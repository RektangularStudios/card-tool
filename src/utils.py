class bcolors:
  FAIL = '\033[91m'
  ENDC = '\033[0m'

def safe_filename(path):
  return path.replace(' ', '_').replace('-', '_').lower()
