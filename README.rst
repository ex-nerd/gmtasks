===================
Gearman Task Server
===================

``gmtasks`` contains a simple multiprocessing server for Gearman workers,
designed for ease of configuration and maximum availability.  It includes a
task wrapper class that traps any interrupts or exceptions that might be thrown
by your task methods, and attempts to make sure that the affected job is
re-inserted into the queue (which is not the default behavior if the worker
script exits abnormally)

Please see the `full documentation <http://packages.python.org/gmtasks/>`_ for
more detailed information.

Sample usage
~~~~~~~~~~~~

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
            Task('job1', job1),
            {'task': 'job2', 'callback': job2},
            ['job3', job3],
            ]
        # Initialize the server
        server = GearmanTaskServer(
            host_list   = ['localhost:4730'],
            tasks       = tasks,
            max_workers = None, # Defaults to multiprocessing.cpu_count()
            id_prefix   = 'myworker.',
            GMWorker    = GearmanWorker,
            sighandler  = True, # SIGINT and SIGTERM send KeyboardInterrupt
            verbose     = True, # log.info() and log.error() messages
            )
        # Run the loop
        server.serve_forever()

Download
~~~~~~~~

* https://github.com/ex-nerd/gmtasks
* http://pypi.python.org/pypi/gmtasks/
