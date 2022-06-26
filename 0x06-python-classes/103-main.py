#!/usr/bin/python3
import dis

MagicClass = __import__('103-magic_class').MagicClass

dis.dis(MagicClass.__init__)
dis.dis(MagicClass.area)
dis.dis(MagicClass.circumference)
