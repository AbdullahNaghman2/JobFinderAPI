from pydantic import BaseModel
from typing import List

class JobSearchInput(BaseModel):
    position: str
    experience: str
    salary: str
    jobNature: str
    location: str
    skills: str

class JobResult(BaseModel):
    job_title: str
    company: str
    experience: str
    jobNature: str
    location: str
    salary: str
    apply_link: str

class JobSearchOutput(BaseModel):
    relevant_jobs: List[JobResult]
