from app.models import JobSearchInput, JobResult

def fetch_glassdoor_jobs(input_data: JobSearchInput):
    return [
        JobResult(
            job_title="React Developer",
            company="Glassdoor Pvt Ltd",
            experience="2 years",
            jobNature="onsite",
            location="Karachi, Pakistan",
            salary="85,000 PKR",
            apply_link="https://glassdoor.com/job789"
        )
    ]
