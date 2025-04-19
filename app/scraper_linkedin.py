from app.models import JobSearchInput, JobResult

def fetch_linkedin_jobs(input_data: JobSearchInput):
    return [
        JobResult(
            job_title="Full Stack Engineer",
            company="XYZ Pvt Ltd",
            experience="2+ years",
            jobNature="onsite",
            location="Islamabad, Pakistan",
            salary="100,000 PKR",
            apply_link="https://linkedin.com/job123"
        )
    ]
