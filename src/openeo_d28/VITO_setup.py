"""
Script to set up pre-requisites for a validation run (e.g. "precomputed" batch job)
"""

import json
import os
import sys

import openeo


def create_batch_job():
    """
    Create and execute a batch job, to be used for `job_id_precomputed`

    Run with same USERNAME/PASSWORD as validator tool, e.g.:

        USERNAME=validator PASSWORD=v4l164t0r python VITO_setup.py create_batch_job

    """
    url = "http://openeo-dev.vgt.vito.be/openeo/1.0"
    job_file = "body/VITO_job.json"
    con = openeo.connect(url)

    username = os.environ["USERNAME"]
    password = os.environ["PASSWORD"]
    con.authenticate_basic(username=username, password=password)

    with open(job_file) as f:
        pg = json.load(f)["process"]["process_graph"]
    job = con.create_job(pg)
    print("Created job {j}".format(j=job.job_id))
    job.start_and_wait()
    status = job.status()
    if status != "finished":
        raise ValueError(status)
    print("Job {j} finished successfully.".format(j=job.job_id))


if __name__ == '__main__':
    # Very basic CLI here.
    args = sys.argv[1:]
    if args == ["create_batch_job"]:
        create_batch_job()
    else:
        raise ValueError(args)
