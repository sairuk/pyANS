#!/usr/bin/env python3

import os
from pya_config import Config

class Logger():
    def __init__(self, logger):
        self.level = 'INFO'
        self.logger = logger
        self.config = Config()
        self.log_file = os.path.join(self.config.config_dir,'pyans.log')

    def show(self):
        print(self.entry)

    def write(self):
        with open(self.log_file, 'a') as f:
            f.write(self.entry)

    def log_entry(self, s):
        self.entry = "[%s] %s %s\n" % (self.logger, self.level, s)

    def log_debug(self, s):
        self.level = "DEBUG"
        self.log_entry(s)
        self.write()

    def log_error(self, s):
        self.level = "ERROR"
        self.log_entry(s)
        self.write()

    def log_info(self, s):
        self.level = "INFO"
        self.log_entry(s)
        self.write()