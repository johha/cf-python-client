from cloudfoundry_client.v2.entities import EntityManager


class ServicePlanVisibilityManager(EntityManager):
    def __init__(self, target_endpoint, client):
        super(ServicePlanVisibilityManager, self).__init__(target_endpoint, client, '/v2/service_plan_visibilities')

    def create(self, service_plan_guid, organization_guid):
        request = self._request()
        request['service_plan_guid'] = service_plan_guid
        request['organization_guid'] = organization_guid
        return super(ServicePlanVisibilityManager, self)._create(request)

    def update(self, spv_guid, service_plan_guid, organization_guid):
        request = self._request()
        request['service_plan_guid'] = service_plan_guid
        request['organization_guid'] = organization_guid
        return super(ServicePlanVisibilityManager, self)._update(spv_guid, request)

    def remove(self, spv_guid):
        super(ServicePlanVisibilityManager, self)._remove(spv_guid)
