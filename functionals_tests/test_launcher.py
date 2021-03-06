#! /usr/bin/python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Author:   Fabien Marteau <fabien.marteau@armadeus.com>
# Created:  17/07/2014
# ----------------------------------------------------------------------------
#  Copyright (2014)  Armadeus Systems
# ----------------------------------------------------------------------------
""" class test_launcher
"""

import sys
sys.path.append("./")
import xmlrunner
import unittest
import os

from periphondemand.bin import pod 

class test_launcher(unittest.TestCase):
    """
    """

    def test_apf27_i2cledbuttonextint(self):
        """ testing apf27_uarts_gpios script"""
        PROJECT_NAME = "i2cledbuttonextint"
        os.system("rm -rf  " + PROJECT_NAME)
        with self.assertRaises(SystemExit):
            pod.main(['pod',
                      '-s',
                      'functionals_tests/apf27_i2cledbuttonextint.pod'])
        self.assertTrue(os.path.isfile(PROJECT_NAME + "/objs/top_i2cledbuttonextint.bit"))
        os.system("rm -rf  i2cledbuttonextint")

    def test_apf27_uarts_gpios(self):
        """ testing apf27_uarts_gpios script"""
        PROJECT_NAME = "apf27uartgpio"
        os.system("rm -rf  " + PROJECT_NAME)
        with self.assertRaises(SystemExit):
            pod.main(['pod', '-s', 'functionals_tests/apf27_uarts_gpios.pod'])
        self.assertTrue(os.path.isfile(PROJECT_NAME + "/objs/top_apf27uartgpio.bit"))
        os.system("rm -rf  apf27uartgpio")

    def test_apf6_wbextvalidation(self):
        """ testing apf6_wbextvaldation script"""
        PROJECT_NAME = "apf6_wbextvalidation"
        os.system("rm -rf  " + PROJECT_NAME)
        with self.assertRaises(SystemExit):
            pod.main(['pod', '-s', 'functionals_tests/apf6_wbextvalidation.pod'])
        self.assertTrue(os.path.isfile(PROJECT_NAME + "/binaries/top_apf6_wbextvalidation.core.rbf"))
        self.assertTrue(os.path.isfile(PROJECT_NAME + "/binaries/top_apf6_wbextvalidation.periph.rbf"))
        os.system("rm -rf  apf6_validation")

    def test_redpitaya_blink(self):
        """ testing redpitaya_blink script"""
        PROJECT_NAME = "redpitaya_blink"
        os.system("rm -rf  " + PROJECT_NAME)
        with self.assertRaises(SystemExit):
            pod.main(['pod', '-s', 'functionals_tests/redpitaya_blink.pod'])
        self.assertTrue(os.path.isfile(PROJECT_NAME + "/binaries/top_redpitaya_blink.bit"))
        os.system("rm -rf  redpitaya_blink")

    def test_redpitaya_axi_gpio_ctl(self):
        """ testing redpitaya_axi_gpio_ctl script"""
        PROJECT_NAME = "redpitaya_axi_gpio_ctl"
        os.system("rm -rf  " + PROJECT_NAME)
        with self.assertRaises(SystemExit):
            pod.main(['pod', '-s', 'functionals_tests/redpitaya_axi_gpio_ctl.pod'])
        self.assertTrue(os.path.isfile(PROJECT_NAME + "/binaries/top_redpitaya_axi_gpio_ctl.bit"))
        os.system("rm -rf  redpitaya_axi_gpio_ctl")


if __name__ == "__main__":
    print("Functionnals tests launcher")
    unittest.main(
            testRunner=xmlrunner.XMLTestRunner(
                output='test-reports'))
