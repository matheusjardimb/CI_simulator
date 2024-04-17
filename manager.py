class ContinuousIntegrationManager:
    def __init__(self, number_of_workers: int, max_job_queue_size: int = 10, max_starvation_duration: int = 10):
        pass

    def process_jobs(self):
        pass

    def add_job(self, project_name: str, job_duration: int, is_prioritized: bool):
        pass

    def print_final_report(self):
        print(f'Maximum job queue size reached: {0}')

    def print_current_status(self):
        print(f'Total workers busy/idle: {0}/{0}')
        print(f'Pending jobs: {[]}')
        print(f'Current job per worker: {[]}')
