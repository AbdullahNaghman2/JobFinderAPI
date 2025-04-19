from fastapi import FastAPI, HTTPException
from app.models import JobSearchInput, JobSearchOutput
from app.scraper_indeed import fetch_indeed_jobs
from app.scraper_linkedin import fetch_linkedin_jobs
from app.scraper_glassdoor import fetch_glassdoor_jobs
from app.filter_llm import filter_relevant_jobs

app = FastAPI()

@app.post("/search-jobs", response_model=JobSearchOutput)
def search_jobs(input_data: JobSearchInput):
    try:
        linkedin_jobs = fetch_linkedin_jobs(input_data)
        indeed_jobs = fetch_indeed_jobs(input_data)
        glassdoor_jobs = fetch_glassdoor_jobs(input_data)

        all_jobs = linkedin_jobs + indeed_jobs + glassdoor_jobs
        relevant_jobs = filter_relevant_jobs(all_jobs, input_data)

        return {"relevant_jobs": relevant_jobs}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
