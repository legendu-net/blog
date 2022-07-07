#!/usr/bin/env python3
import os


print(os.access("/home", os.W_OK, effective_ids=True))

