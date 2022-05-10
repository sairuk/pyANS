#!/usr/bin/env python3

import zipfile
from pya_logger import Logger

class Zipfile():
    def __init__(self):
        self.pya_zipfile = None
        self.pya_zipdata = None
        self.logger = Logger('LIB_ZIP')

    def read(self, filename):
        self.logger.log_info("Reading %s" % filename)
        try:
            self.pya_zipfile = zipfile.ZipFile(filename, 'r')
            self.logger.log_info("Successfully read %s" % filename)
            return self.pya_zipfile
        except:
            self.logger.log_error("Failed to read %s" % filename)
            return None

    def name_list(self):
        self.pya_zipfile.name_list()
        return self.pya_zipfile.name_list()

    def extract(self, fileset):
        self.logger.log_info("Exracting %s from %s" % (fileset[1], fileset[0]))
        try:
            self.pya_zipdata = self.read(fileset[0]).read(fileset[1])
            self.logger.log_info("Successfully extracted %s into memory" % (fileset[1]))
            return self.pya_zipdata
        except:
            self.logger.log_error("Failed to extract %s from %s" % (fileset[1], fileset[0]))