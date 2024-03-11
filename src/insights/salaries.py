from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_max_salary(self) -> int:
        ms = "max_salary"
        max_value = 0

        for job in self.jobs_list:
            if job[ms] and job[ms].isdigit():
                int_ms = int(job[ms])

                if int_ms > max_value:
                    max_value = int_ms

        return max_value

    def get_min_salary(self) -> int:
        ms = "min_salary"
        min_value = 999999

        for job in self.jobs_list:
            if job[ms] and job[ms].isdigit():
                int_ms = int(job[ms])

                if int_ms < min_value:
                    min_value = int_ms

        return min_value

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        pass

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass
