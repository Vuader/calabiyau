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

from luxon import register
from luxon import router
from luxon.helpers.api import sql_list, obj

from calabiyau.models.packages import calabiyau_package
from calabiyau.models.package_attrs import calabiyau_package_attr


@register.resources()
class Groups(object):
    def __init__(self):
        router.add('GET', '/v1/package/{id}', self.package,
                   tag='services')
        router.add('GET', '/v1/packages', self.packages,
                   tag='services')
        router.add('POST', '/v1/package', self.create,
                   tag='services')
        router.add(['PUT', 'PATCH'], '/v1/package/{id}', self.update,
                   tag='services')
        router.add('DELETE', '/v1/package/{id}', self.delete,
                   tag='services')
        router.add('GET', '/v1/package/{id}/attrs', self.attrs,
                   tag='services')
        router.add('POST', '/v1/package/{id}/attrs', self.add_attr,
                   tag='services')
        router.add('DELETE', '/v1/package/{id}/attrs', self.rm_attr,
                   tag='services')

    def package(self, req, resp, id):
        return obj(req, calabiyau_package, sql_id=id)

    def packages(self, req, resp):
        return sql_list(req, 'calabiyau_package', ('id', 'name', ))

    def create(self, req, resp):
        package = obj(req, calabiyau_package)
        package.commit()
        return package

    def update(self, req, resp, id):
        package = obj(req, calabiyau_package, sql_id=id)
        package.commit()
        return package

    def delete(self, req, resp, id):
        package = obj(req, calabiyau_package, sql_id=id)
        package.commit()
        return package

    def attrs(self, req, resp, id):
        where = {'package_id': id}
        return sql_list(req, 'calabiyau_package_attr',
                        ('id', 'attribute', 'value', 'ctx', 'nas_type'),
                        where=where)

    def add_attr(self, req, resp, id):
        attr = obj(req, calabiyau_package_attr)
        attr['package_id'] = id
        attr.commit()
        return attr

    def rm_attr(self, req, resp, id):
        attr = obj(req, calabiyau_package_attr, sql_id=id)
        attr.commit()
