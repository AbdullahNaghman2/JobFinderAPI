from app.models import JobSearchInput, JobResult

def fetch_indeed_jobs(input_data: JobSearchInput):
    return [
        JobResult(
            job_title="MERN Stack Developer",
            company="ABC Technologies",
            experience="2 years",
            jobNature="onsite",
            location="Lahore, Pakistan",
            salary="90,000 PKR",
            apply_link="https://indeed.com/job456"
        )
    ]
