#!/usr/bin/env python

PKG = 'rtshell'
NAME = 'test_rtshell'

import os
import sys
import time
import unittest
import yaml

import rostest

import subprocess
from subprocess import Popen, PIPE, check_output, check_call, call

class TestRtshellOnline(unittest.TestCase):
    PYTHONPATH = ''

    def setUp(self):
        rtshell_path = check_output(['rospack','find','rtshell']).rstrip()
        # if rosbuild environment
        if os.path.exists(os.path.join(rtshell_path, "bin")) :
            rtctree_path = check_output(['rospack','find','rtctree']).rstrip()
            rtsprofile_path = check_output(['rospack','find','rtsprofile']).rstrip()
            self.PYTHONPATH='PYTHONPATH=%s/lib/python2.7/dist-packages:%s/lib/python2.7/dist-packages:%s/lib/python2.7/dist-packages:$PYTHONPATH'%(rtshell_path, rtctree_path, rtsprofile_path)


    def test_rtls(self):
        try:
            check_output('%s rosrun rtshell rtls'%(self.PYTHONPATH), shell=True, stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError, (e):
            self.assertTrue(False, 'subprocess.CalledProcessError: cmd:%s returncode:%s output:%s' % (e.cmd, e.returncode, e.output))

    def test_rtcryo(self):
        try:
            check_output('%s rosrun rtshell rtcryo'%(self.PYTHONPATH), shell=True, stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError, (e):
            self.assertTrue(False, 'subprocess.CalledProcessError: cmd:%s returncode:%s output:%s' % (e.cmd, e.returncode, e.output))

    def test_share(self):
        # check if rtshell runs
        self.assertTrue(os.path.exists(os.path.join(check_output(['rospack','find','rtshell']).rstrip(), "share/rtshell/shell_support")))

    def test_shell_support(self):
        # check if rtshell runs
        fname=os.path.join(check_output(['rospack','find','rtshell']).rstrip(), "share/rtshell/shell_support")
        self.assertTrue(os.path.exists(fname), "%s does not exists"%(fname))
        self.assertEqual(check_call("bash "+fname, shell=True),0)

#unittest.main()
if __name__ == '__main__':
    rostest.run(PKG, NAME, TestRtshellOnline, sys.argv)
