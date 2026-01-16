# dojo-enrollment-mgmt-lambda/app/enrollmentmgmt/model/enrollment.py
from datetime import date
from typing import Optional
from pydantic import BaseModel, Field

class EnrollmentBase(BaseModel):
    athlete_id: str = Field(..., description="UUID do atleta matriculado")
    athlete_name: Optional[str] = Field(default="", description="Nome do atleta matriculado")
    class_id: str = Field(..., description="UUID da aula")
    enrollment_date: date = Field(..., description="Data de inscrição na aula")
    is_active: bool = Field(default=True, description="Status da matrícula (ativo/inativo)")
    notes: Optional[str] = Field(default="", description="Observações sobre a matrícula")

class EnrollmentCreate(EnrollmentBase):
    """✅ Modelo para criação (sem ID)"""
    pass        

class Enrollment(EnrollmentBase):  
    """Modelo completo com ID"""
    id: str = Field(default="", description="UUID único (gerado automaticamente)")

    class Config:
        from_attributes = True