#!/usr/bin/env python3

import sys, time
from pya_config import Config
from pya_logger import Logger

class Terminal():
    def __init__(self):
        self.logger = Logger('TERM')
        self.config = Config()
        self.delay_calc()

    def delay_calc(self):
        #### Simulated baud delay (very basic)
        self.baud_delay = ( self.config.cols**2 / ( self.config.baud / self.config.bits ) ) / 6000.0

    def reset(self):
        sys.stdout.write('\033c')  

    def writeout(self,c):
        """ write to stdout then flush stdout """
        sys.stdout.write(c)
        sys.stdout.flush()
        return

    def decode(self, c):
        return c.decode(self.config.cp)
        
    def display(self, data):
        self.reset()
        if data is not None:
            self.logger.log_info("Displaying data")
            for char in data.decode(self.config.cp):
                self.writeout(char)
                time.sleep(self.baud_delay)
            self.writeout('\n')
            time.sleep(self.config.ansi_delay)
        else:
            self.logger.log_error("No data is available to display, skipping")
