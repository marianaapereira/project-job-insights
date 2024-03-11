from src.insights.jobs import ProcessJobs
from typing import List


class ProcessIndustries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_unique_industries(self) -> List[str]:
        i = "industry"
        unique_industries = list()

        for industry in self.jobs_list:
            if i in industry and industry[i]:
                unique_industries.append(industry[i])

        return set(unique_industries)
