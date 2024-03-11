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

    def invalid_value(self, value) -> bool:
        return not isinstance(value, (int, str))

    def salary_middleware(self, salary):
        if self.invalid_value(salary):
            raise ValueError("Invalid value")

    def min_max_middleware(self, job, min, max):
        if min not in job or max not in job:
            raise ValueError("Missing min or max keys")

        if self.invalid_value(job[min]) or self.invalid_value(job[max]):
            raise ValueError("Invalid min or max values")

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        self.salary_middleware(salary)

        min = "min_salary"
        max = "max_salary"

        self.min_max_middleware(job, min, max)

        int_min = int(job[min])
        int_max = int(job[max])
        int_salary = int(salary)

        if int_min > int_max:
            raise ValueError("Min value is bigger than max value")

        if int_salary >= int_min and int_salary <= int_max:
            return True

        else:
            return False

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass
