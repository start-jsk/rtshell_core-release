#!/usr/bin/env python

PKG = 'rtshell'
NAME = 'test_rtshell'

import os
import sys
import time
import unittest
import yaml

import rostest

from subprocess import Popen, PIPE, check_output, check_call, call

class TestRtshellOnline(unittest.TestCase):

    def setUp(self):
        pass

    def test_rtls(self):
        # check if rtshell runs
        rtshell_path = check_output(['rospack','find','rtshell']).rstrip()
        # if rosbuild environment
        if os.path.exists(os.path.join(rtshell_path, "bin")) :
            rtctree_path = check_output(['rospack','find','rtctree']).rstrip()
            rtsprofile_path = check_output(['rospack','find','rtsprofile']).rstrip()
            check_call(['PYTHONPATH=%s/lib/python2.7/dist-packages:%s/lib/python2.7/dist-packages:%s/lib/python2.7/dist-packages:$PYTHONPATH rosrun rtshell rtls'%(rtshell_path, rtctree_path, rtsprofile_path)], shell=True)
        # else if catkin environment
        else:
            check_call(['rosrun','rtshell','rtls'])

    def test_rtcryo(self):
        # check if rtcryo runs
        rtshell_path = check_output(['rospack','find','rtshell']).rstrip()
        # if rosbuild environment
        if os.path.exists(os.path.join(check_output(['rospack','find','rtshell']).rstrip(), "bin")) :
            rtctree_path = check_output(['rospack','find','rtctree']).rstrip()
            rtsprofile_path = check_output(['rospack','find','rtsprofile']).rstrip()
            check_call(['PYTHONPATH=%s/lib/python2.7/dist-packages:%s/lib/python2.7/dist-packages:%s/lib/python2.7/dist-packages:$PYTHONPATH rosrun rtshell rtcryo'%(rtshell_path, rtctree_path, rtsprofile_path)], shell=True)
        # else if catkin environment
        else:
            check_call(['rosrun','rtshell','rtcryo'])

    def test_share(self):
        # check if rtshell runs
        self.assertTrue(os.path.exists(os.path.join(check_output(['rospack','find','rtshell']).rstrip(), "share/rtshell/shell_support")))

    def test_shell_support(self):
        # check if rtshell runs
        fname=os.path.join(check_output(['rospack','find','rtshell']).rstrip(), "share/rtshell/shell_support")
        self.assertEqual(check_call("bash "+fname, shell=True),0)

#unittest.main()
if __name__ == '__main__':
    rostest.run(PKG, NAME, TestRtshellOnline, sys.argv)
