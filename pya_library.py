#!/usr/bin/env python3

import os, random
from pya_zip import Zipfile
from pya_config import Config
from pya_logger import Logger

class Library():
    def __init__(self):
        self.cache = []
        self.config = Config()
        self.ziplib = Zipfile()
        self.cache_file = os.path.join(self.config.config_dir, 'cachefile')
        self.logger = Logger('LIBRARY')

        self.cache_check()

    def cache_check(self):
        if not os.path.exists(self.cache_file):
            self.logger.log_error("cachefile not found at %s, building" % self.cache_file)
            self.cache_build()
        else:
            self.logger.log_info("cachefile found at %s" % self.cache_file)

    def cache_build(self):
        for root, dirs, files in os.walk(self.config.ansi_store):
            for filename in files:
                file_abs = os.path.join(root, filename)

                # if i can't read it i don't care about it
                self.zip_content = self.ziplib.read(file_abs)
                if self.zip_content is not None:
                    for name in self.zip_content.namelist():
                        ext = os.path.splitext(name)[1].lower()[1:]
                        if ".%s" % ext in self.config.anslist:
                            self.cache.append([file_abs,name])
        self.cache_write()

    def cache_write(self):
        with open(self.cache_file,'w') as f:
            for row in self.cache:
                f.write("%s,%s\n" % ( row[0], row[1]) )

    def cache_read(self):
        f = open(self.cache_file,'r')
        for line in f.readlines():
            fields = line.strip().split(',')
            self.cache.append([fields[0], fields[1]])

    def select(self):
        return self.cache[random.randint(0, len(self.cache)-1)]

    def load(self, fileset):
        self.logger.log_info("Loading %s from %s" % (fileset[1], fileset[0]))
        self.ziplib.extract(fileset)
        if not os.path.exists(fileset[0]):
            return None
        else:
            try:
                return self.ziplib.extract(fileset)
            except:
                return None

