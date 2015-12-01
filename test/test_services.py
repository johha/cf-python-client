from config_test import build_client_from_configuration
import unittest
import logging
import json

_logger = logging.getLogger(__name__)


class TestServices(unittest.TestCase):
    def test_list_services(self):
        cpt = 0
        client = build_client_from_configuration()
        for _ in client.service.list_services(client.space_guid):
            cpt += 1
        _logger.debug('test service list - %d found', cpt)

    def test_get_service_by_name(self):
        client = build_client_from_configuration()
        service = client.service.get_service_by_name(client.space_guid, client.service_name)
        self.assertIsNotNone(service)

    def test_list_plans(self):
        cpt = 0
        client = build_client_from_configuration()
        for _ in client.service.list_plans(client.service_guid):
            cpt += 1
        _logger.debug('test plan list - %d found', cpt)

    def test_all(self):
        client = build_client_from_configuration()
        binding_by_app = {}
        for instance in client.service.list_instances(client.space_guid):
            self.assertIsNotNone(client.service.get_instance_by_name(client.space_guid, instance['entity']['name']))
            for binding in client.service.list_bindings_by_instance(instance['metadata']['guid']):
                binding_reloaded = client.service.get_binding(instance['metadata']['guid'],
                                                              binding['entity']['app_guid'])
                self.assertIsNotNone(binding_reloaded)
                binding_by_app[binding['entity']['app_guid']] = binding_by_app.get(binding['entity']['app_guid'], 0) + 1
        for application in client.application.list(client.space_guid):
            cpt = 0
            for _ in client.service.list_bindings_by_application(application['metadata']['guid']):
                cpt += 1
            self.assertEqual(cpt, binding_by_app.get(application['metadata']['guid'], 0))