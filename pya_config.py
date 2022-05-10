#!/usr/bin/env python3

import os, shutil
import configparser as ConfigParser

class Config():
    def __init__(self):
        self.config = ConfigParser.RawConfigParser(allow_no_value=False)
        self.config_name = os.path.expanduser('~/.pyANS')
        self.config_dir = self.config_name
        self.config_file = os.path.join(self.config_dir, 'config.ini')
        self.config_example = 'config.ini.example'
        self.config_migrated = self.config_name + "_migrated"

        # migrate users
        if os.path.exists(self.config_name) and os.path.isfile(self.config_name):
            self.migrate()

        self.read()

    def migrate(self):
        os.rename(self.config_name, self.config_migrated)
        self.create(migrate=True)

    def create(self, migrate=False):
        if not os.path.exists(self.config_dir):
            os.mkdir(self.config_dir)

        # are we migrating a user or not
        if not migrate:
            if not os.path.exists(self.config_example):
                shutil.copy(self.config_example, self.config_file)
            else:
                print("Config file %s is missing" % self.config_file)
                exit()
        else:
            shutil.copy(self.config_migrated, self.config_file)


    def read(self):
        self.config.read_file(open(self.config_file,'r'))

        try:
            self.baud = self.config.getint("base", "baud")
            self.bits = self.config.getint("base", "bits")
            self.cols = self.config.getint("base", "cols")
            self.cp = self.config.get("base", "cp")
            self.ansi_delay = self.config.getfloat("base", "ansi_delay")
            self.ansi_store = self.config.get("path", "ansi_store")
            self.arclist = self.comma_to_list(self.config.get("whitelists", "arclist"))
            self.anslist = self.comma_to_list(self.config.get("whitelists", "anslist"))
            self.debug = self.config.getboolean("misc", "debug")
        except ConfigParser.NoOptionError or ConfigParser.NoSectionError:
            print("Config file is damaged or out of date, cannot continue")

    def comma_to_list(self, s):
        """ convert comma seperated whitelists to python lists """
        self.comma_list = []
        for item in s.split(','):
            self.comma_list.append('.%s' % item.lower())
            self.comma_list.append('.%s' % item.upper())
        return self.comma_list