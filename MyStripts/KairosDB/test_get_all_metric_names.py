#!/usr/bin/env python


import pyKairosDB

print(pyKairosDB.connect())
# c = pyKairosDB.connect()  # use localhost:8080, the default, no ssl
#
# print(pyKairosDB.metadata.get_all_metric_names(c))
