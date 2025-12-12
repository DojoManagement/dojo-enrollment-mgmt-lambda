from typing import List
from dojocommons.model.app_configuration import AppConfiguration
from dojocommons.service.base_service import BaseService
from dojocommons.exception.business_exception import BusinessException
from enrollmentmgmt.model.enrollment import Enrollment
from enrollmentmgmt.repository.enrollment_repository import EnrollmentRepository


class EnrollmentService(BaseService[Enrollment]):
    def __init__(self, cfg: AppConfiguration):
        super().__init__(cfg, EnrollmentRepository)
    
    def create(self, entity: Enrollment) -> Enrollment:
        """Cria uma nova matrícula com validações de negócio"""
        # Valida se já existe matrícula ativa para este atleta nesta aula
        existing_enrollments = self._repository.find_active_by_athlete_and_class(
            entity.athlete_id, 
            entity.class_id
        )
        
        if existing_enrollments:
            raise BusinessException(
                f"Athlete {entity.athlete_id} is already enrolled in class {entity.class_id}",
                status_code=409
            )
        
        # TODO: Validar se o atleta existe (consultar athlete service)
        # TODO: Validar se a aula existe (consultar class service)
        # TODO: Validar se a aula não está lotada (max_students)
        
        return super().create(entity)
    
    def get_athlete_enrollments(self, athlete_id: int) -> List[Enrollment]:
        """Retorna todas as matrículas de um atleta"""
        return self._repository.find_by_athlete_id(athlete_id)
    
    def get_class_enrollments(self, class_id: int) -> List[Enrollment]:
        """Retorna todas as matrículas de uma aula"""
        return self._repository.find_by_class_id(class_id)
    
    def deactivate_enrollment(self, enrollment_id: int) -> Enrollment:
        """Desativa uma matrícula (cancela)"""
        enrollment = self.get_by_id(enrollment_id)
        if not enrollment:
            raise BusinessException(f"Enrollment {enrollment_id} not found", status_code=404)
        
        enrollment.is_active = False
        return self.update(enrollment)