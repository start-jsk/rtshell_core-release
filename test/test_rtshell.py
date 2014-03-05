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
        check_call(['rosrun','rtshell','rtls'])

    def test_rtcryo(self):
        # check if rtcryo runs
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
