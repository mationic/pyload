# -*- coding: utf-8 -*-

import re

from module.plugins.internal.XFSPCrypter import XFSPCrypter


class XFileSharingProFolder(XFSPCrypter):
    __name__ = "XFileSharingProFolder"
    __type__ = "crypter"
    __version__ = "0.02"

    __pattern__ = r'^unmatchable$'

    __description__ = """XFileSharingPro dummy folder decrypter plugin for hook"""
    __license__ = "GPLv3"
    __authors__ = [("Walter Purcaro", "vuolter@gmail.com")]


    def init(self):
        self.__pattern__ = self.core.pluginManager.crypterPlugins[self.__name__]['pattern']
        self.HOSTER_NAME = re.match(self.__pattern__, self.pyfile.url).group(1).lower()

        account_name = "".join([str.capitalize() for str in self.HOSTER_NAME.split('.')])
        self.account = self.core.accountManager.getAccountPlugin(account_name)

        if self.account and self.account.canUse():
            self.user, data = self.account.selectAccount()
            self.req = self.account.getAccountRequest(self.user)
            self.premium = self.account.isPremium(self.user)