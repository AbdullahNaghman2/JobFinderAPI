# Job Finder API

This document serves as the complete technical documentation for the FastAPI-based Job Finder API built as part of the GoAccelovate assessment. It explains the API's working, input/output schemas, internal logic, and expected behavior.

This FastAPI-based job matching API accepts job preferences and returns relevant job listings from simulated sources (LinkedIn, Glassdoor, Indeed). It includes LLM-based filtering logic to return suitable jobs.

## Tech Stack
- Python 3.12
- FastAPI
- Uvicorn
- OpenAI (for LLM logic)
- BeautifulSoup4
- Requests

## Setup Instructions

1. Clone the Repository

```bash
git clone <your_repo_url>
cd JobFinderAPI


2. Create & Activate Virtual Environment

# For macOS/Linux:
python3 -m venv venv
source venv/bin/activate

# For Windows (Command Prompt):
python -m venv venv
venv\Scripts\activate


3. Install Dependencies

pip install -r requirements.txt


4. Run the API Server

uvicorn app.main:app --reload --port 8000

The server will start at:
http://127.0.0.1:8000

5. Access Swagger Docs (API GUI)

Open your browser and go to:
http://127.0.0.1:8000/docs


##Endpoint

### `POST /search-jobs`
This is the **core endpoint** used to retrieve job listings that match the user's preferences.

##Purpose:
- Accepts user job preferences
- Aggregates jobs from simulated sources (LinkedIn, Indeed, Glassdoor)
- Uses LLM-based filtering to return only relevant jobs



##Input Schema (JSON Request)

{
  "position": "string",
  "experience": "string",
  "salary": "string",
  "jobNature": "string",
  "location": "string",
  "skills": "string"
}


##Example:

{
  "position": "Full Stack Engineer",
  "experience": "2 years",
  "salary": "70,000 PKR to 120,000 PKR",
  "jobNature": "onsite",
  "location": "Lahore, Pakistan",
  "skills": "React, Node.js, Express.js, Firebase"
}



##Output Schema (JSON Response)

{
  "relevant_jobs": [
    {
      "job_title": "string",
      "company": "string",
      "experience": "string",
      "jobNature": "string",
      "location": "string",
      "salary": "string",
      "apply_link": "string"
    }
  ]
}


##Example:

{
  "relevant_jobs": [
    {
      "job_title": "MERN Stack Developer",
      "company": "ABC Technologies",
      "experience": "2 years",
      "jobNature": "onsite",
      "location": "Lahore, Pakistan",
      "salary": "90,000 PKR",
      "apply_link": "https://indeed.com/job456"
    }
  ]
}



##How It Works (Internal Logic)

### 1.Input Collection:

User fills in position, experience, salary, skills, etc.

### 2.Simulated Job Scraping:

- scraper_indeed.py: Returns mock job data from Indeed
- scraper_linkedin.py: Returns mock LinkedIn jobs
- scraper_glassdoor.py: Returns mock Glassdoor jobs

Each returns a list of `dicts` with job details.

### 3.LLM-Based Filtering:

- `filter_llm.py`: Uses a prompt and GPT logic to compare job descriptions against user input
- Filters only jobs matching the position, experience, and skills

### 4.API Returns Filtered Jobs:

Final list is wrapped and returned as:
```python
{"relevant_jobs": filtered_jobs}
```


## Summary
- This API is designed to **simulate job listings** and showcase LLM integration
- Web scraping is mocked for platforms like LinkedIn which have API limitations
- Easily extendable with real APIs in production use

