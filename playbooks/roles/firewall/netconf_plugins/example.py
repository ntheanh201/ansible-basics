#
# (c) 2018 Red Hat Inc.
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
#
from __future__ import (absolute_import, division, print_function)
from ansible.errors import AnsibleError
__metaclass__ = type

try:
    from ansible.plugins.terminal import NetconfBase
    """
        Examples:
            https://github.com/ansible/ansible/blob/devel/lib/ansible/plugins/netconf/iosxr.py
            https://github.com/ansible/ansible/blob/devel/lib/ansible/plugins/netconf/junos.py
    """
except ImportError:
    raise AnsibleError("Netconf Plugin [ firewall ]: Dependency not satisfied")


class Netconf(NetconfBase):
    """
        Examples:
            https://github.com/ansible/ansible/blob/devel/lib/ansible/plugins/netconf/iosxr.py
            https://github.com/ansible/ansible/blob/devel/lib/ansible/plugins/netconf/junos.py
    """
    raise AnsibleError("Netconf Plugin [ firewall ]: Not implemented")
