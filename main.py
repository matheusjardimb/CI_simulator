MAX_QUEUE_SIZE = 10


class ContinuousIntegrationManager:
    def __init__(self, number_of_workers: int):
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


if __name__ == '__main__':
    manager = ContinuousIntegrationManager(2)

    cmd = -1
    while cmd != 0:
        cmd = input('Choose operation: 1=add job, 2=process jobs, 0=finish')
        if cmd == 1:
            name = input('Project name:')
            duration = int(input('Job duration:'))
            priority = int(input('Has Priority (1=True, 0=False):')) == 1
            manager.add_job(name, duration, priority)
        if cmd == 2:
            manager.process_jobs()
        manager.print_current_status()
    manager.print_final_report()
