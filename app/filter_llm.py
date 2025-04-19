from app.models import JobSearchInput, JobResult
from typing import List

def filter_relevant_jobs(jobs: List[JobResult], input_data: JobSearchInput) -> List[JobResult]:
    return [
        job for job in jobs
        if input_data.location.split(',')[0].lower() in job.location.lower()
    ]
