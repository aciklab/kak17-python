#/usr/bin/python3
# -*- coding: utf-8 -*-

import os, gi, sys

# config translator
from translate import Translator
translator= Translator(to_lang="tr")

# check notify
gi.require_version('Notify', '0.7')
from gi.repository import Notify

# text to translate
text = os.popen('xsel').read()

# get translated text
result = translator.translate(text)

# notify text
Notify.init("translate")
trlated = Notify.Notification.new(str(text), str(result))
trlated.show ()
