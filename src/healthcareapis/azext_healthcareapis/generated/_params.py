# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines
# pylint: disable=too-many-statements

from knack.arguments import CLIArgumentType
from azure.cli.core.commands.parameters import (
    tags_type,
    get_enum_type,
    resource_group_name_type,
    get_location_type
)
from azure.cli.core.commands.validators import get_default_location_from_resource_group
from azext_healthcareapis.action import AddIdentity


def load_arguments(self, _):

    with self.argument_context('healthcareapis service list') as c:
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('healthcareapis service show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('resource_name', help='The name of the service instance.')

    with self.argument_context('healthcareapis service create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('resource_name', help='The name of the service instance.')
        c.argument('kind', arg_type=get_enum_type(['fhir', 'fhir-Stu3', 'fhir-R4']), help='The kind of the service.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx),
                   validator=get_default_location_from_resource_group)
        c.argument('tags', tags_type)
        c.argument('etag', help='An etag associated with the resource, used for optimistic concurrency when editing it.'
                   '')
        c.argument('identity', action=AddIdentity, nargs='+', help='Setting indicating whether the service has a manage'
                   'd identity associated with it. Expect value: type=xx.')
        c.argument('properties', arg_type=CLIArgumentType(options_list=['--properties'], help='The common properties of'
                   ' a service. Expected value: json-string/@json-file.'))

    with self.argument_context('healthcareapis service update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('resource_name', help='The name of the service instance.')
        c.argument('tags', tags_type)

    with self.argument_context('healthcareapis service delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('resource_name', help='The name of the service instance.')

    with self.argument_context('healthcareapis operation-result show') as c:
        c.argument('location_name', help='The location of the operation.')
        c.argument('operation_result_id', help='The ID of the operation result to get.')
