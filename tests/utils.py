#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2011 Yesudeep Mangalapilly <yesudeep@gmail.com>
# Copyright (C) 2012 Google, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from __future__ import with_statement

def list_attributes(o, only_public=True):
    if only_public:
        def isattribute(o, attribute):
            return not (attribute.startswith('_') or callable(getattr(o, attribute)))
    else:
        def isattribute(o, attribute):
            return not callable(getattr(o, attribute))
    return [attribute for attribute in dir(o) if isattribute(o, attribute)]
