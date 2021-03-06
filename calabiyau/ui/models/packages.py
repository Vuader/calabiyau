# -*- coding: utf-8 -*-
# Copyright (c) 2018-2019 Christiaan Frans Rademan.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# * Neither the name of the copyright holders nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF
# THE POSSIBILITY OF SUCH DAMAGE.
from luxon import Model
from luxon.utils.timezone import now

from calabiyau.ui.helpers.virtual import virtual
from calabiyau.ui.helpers.pool import pool


class package(Model):
    name = Model.String(max_length=64, null=False)
    virtual_id = Model.Uuid(callback=virtual)
    plan = Model.Enum('uncapped', 'data')
    pool_id = Model.Uuid(placeholder='Select IP Pool', callback=pool)
    simultaneous = Model.Boolean(default=True)
    package_metric = Model.Enum('days', 'weeks', 'months')
    package_span = Model.TinyInt(null=True, default=0)
    volume_gb = Model.SmallInt(null=True, default=0)
    volume_metric = Model.Enum('days', 'weeks', 'months')
    volume_span = Model.TinyInt(null=True, default=0)
    volume_repeat = Model.Boolean(default=True)
    creation_time = Model.DateTime(default=now, readonly=True)
