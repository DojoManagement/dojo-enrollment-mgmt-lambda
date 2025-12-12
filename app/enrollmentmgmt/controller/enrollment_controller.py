from dojocommons.controller.base_controller import BaseController
from dojocommons.model.app_configuration import AppConfiguration
from enrollmentmgmt.model.enrollment import Enrollment
from enrollmentmgmt.model.resource import Resource
from enrollmentmgmt.service.enrollment_service import EnrollmentService

class EnrollmentController(BaseController[Enrollment]):
    def __init__(self, cfg: AppConfiguration):
        super().__init__(cfg, EnrollmentService, Resource.ENROLLMENTS.value, Enrollment)