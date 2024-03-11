from typing import List, Dict
import csv


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, path) -> List[Dict]:
        with open(path, encoding="utf-8") as file:
            file_reader = csv.DictReader(file, delimiter=',', quotechar='"')
            data = [row for row in file_reader]

            self.jobs_list = data

        return self.jobs_list

    def get_unique_job_types(self) -> List[str]:
        job_type = "job_type"
        unique_job_types = list()

        for job in self.jobs_list:
            if job_type in job:
                unique_job_types.append(job[job_type])

        return set(unique_job_types)

    def filter_by_multiple_criteria(self, jobs, criteria) -> List[dict]:
        i = "industry"
        jt = "job_type"
        found_criteria = False
        filtered_jobs = list()

        for job in jobs:
            if job[i] == criteria[i] and job[jt] == criteria[jt]:
                filtered_jobs.append(job)
                found_criteria = True

        if not found_criteria:
            raise TypeError("Filter provided is not a dictionary")

        return filtered_jobs
