==============
Example server
==============

Sometimes it's easier to just learn by looking at some sample code, so here
is a simple server that demonstrates most of how to use gmtasks.

::

    from multiprocessing   import freeze_support
    from gmtasks.jsonclass import GearmanWorker
    from gmtasks           import GearmanTaskServer, Task

    # Jobs
    def job1(worker, job):
        return job.data['string1']
    def job2(worker, job):
        return job.data['string2']
    def job3(worker, job):
        return job.data['string3']

    # Main loop
    if __name__ == '__main__':
        # Need this to run in Windows
        freeze_support()
        # Import all of the jobs we handle
        tasks = [
            # You can use a Task()
            Task('job1', job1),
            # Or a dict
            {'task': 'job2', 'callback': job2},
            # Or a list/tuple
            ['job3', job3],
            ]
        # Initialize the server
        server = GearmanTaskServer(
            host_list      = ['localhost:4730'],
            tasks          = tasks,
            max_workers    = None, # Defaults to multiprocessing.cpu_count()
            id_prefix      = 'myworker.',
            worker_class   = GearmanWorker,
            use_sighandler = True, # SIGINT and SIGTERM send KeyboardInterrupt
            verbose        = True, # log.info() and log.error() messages
            )
        # Run the loop
        server.serve_forever()
