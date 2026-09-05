from fastapi import FastAPI, HTTPException, Query
from queues.worker import process_query
from client.rq_client import queue

app = FastAPI()

@app.get("/")
def root():
    return {"status" : "Server is UP and Running ✅"}


@app.post("/chat")
def chat(query:str = Query(..., description="The chat query of user")):

    job = queue.enqueue(process_query, query)

    return {
        "status": "queued",
        "job_id": job.id
    }


@app.get("/job-status")
def get_result(
    job_id:str=Query(..., description="Job id")
):
    job = queue.fetch_job(job_id=job_id)
    if job is None:
        raise HTTPException(status_code=404, detail=f"Job not found: {job_id}")

    if not job.is_finished:
        return {"status": job.get_status()}

    result = job.return_value()

    return {"status": "finished", "result": result}