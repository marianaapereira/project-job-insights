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
        pass

    def filter_by_multiple_criteria(self) -> List[dict]:
        pass
