import subprocess
import sys
import os
import setup_util

def start(args):
  # setup_util.replace_text("go/src/hello/hello.go", "tcp\(.*:3306\)", "tcp(" + args.database_host + ":3306)")
  subprocess.call("go get github.com/robfig/revel/cmd", shell=True, cwd="go")
  subprocess.call("go build -o bin/revel github.com/robfig/revel/cmd", shell=True, cwd="go")
  subprocess.Popen("bin/revel run benchmark prod".rsplit(" "), cwd="go")
  return 0

def stop():
  p = subprocess.Popen(['ps', 'aux'], stdout=subprocess.PIPE)
  out, err = p.communicate()
  for line in out.splitlines():
    if 'revel' in line:
      pid = int(line.split(None, 2)[1])
      os.kill(pid, 9)
  return 0
