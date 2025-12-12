from typing import List
from dojocommons.model.app_configuration import AppConfiguration
from dojocommons.repository.base_repository import BaseRepository
from enrollmentmgmt.model.enrollment import Enrollment


class EnrollmentRepository(BaseRepository[Enrollment]):
    def __init__(self, cfg: AppConfiguration):
        super().__init__(cfg, Enrollment, "enrollment")
    
    def find_by_athlete_id(self, athlete_id: int) -> List[Enrollment]:
        """Busca todas as matrículas de um atleta"""
        query = f"""
            SELECT * FROM {self._table_name}
            WHERE athlete_id = ?
            ORDER BY enrollment_date DESC
        """
        rows = self._db.execute_query(query, (athlete_id,)).fetchall()
        return [
            Enrollment.model_validate(
                dict(zip(Enrollment.__annotations__.keys(), row))
            )
            for row in rows
        ]
    
    def find_by_class_id(self, class_id: int) -> List[Enrollment]:
        """Busca todas as matrículas de uma aula"""
        query = f"""
            SELECT * FROM {self._table_name}
            WHERE class_id = ?
            ORDER BY enrollment_date DESC
        """
        rows = self._db.execute_query(query, (class_id,)).fetchall()
        return [
            Enrollment.model_validate(
                dict(zip(Enrollment.__annotations__.keys(), row))
            )
            for row in rows
        ]
    
    def find_active_by_athlete_and_class(self, athlete_id: int, class_id: int) -> List[Enrollment]:
        """Verifica se já existe matrícula ativa para o atleta nesta aula"""
        query = f"""
            SELECT * FROM {self._table_name}
            WHERE athlete_id = ?
            AND class_id = ?
            AND is_active = true
        """
        rows = self._db.execute_query(query, (athlete_id, class_id)).fetchall()
        return [
            Enrollment.model_validate(
                dict(zip(Enrollment.__annotations__.keys(), row))
            )
            for row in rows
        ]