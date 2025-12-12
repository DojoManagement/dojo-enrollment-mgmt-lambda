from dojocommons.model.base_resource import BaseResource

class Resource(BaseResource):
    """Definição de rotas para Enrollment"""
    ENROLLMENTS = "/enrollments"
    ENROLLMENTS_ID = "/enrollments/{id}"
    ATHLETE_ENROLLMENTS = "/athletes/{athlete_id}/enrollments"
    CLASS_ENROLLMENTS = "/classes/{class_id}/enrollments"