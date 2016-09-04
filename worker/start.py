import tensorflow as tf
import os
import logging
import sys
import ast

root = logging.getLogger()
root.setLevel(logging.INFO)
ch = logging.StreamHandler(sys.stdout)
root.addHandler(ch)

WORKER_HOSTS = os.environ.get('WORKER_HOSTS', '')
PS_HOSTS = os.environ.get('PS_HOSTS', '')
MASTER_HOSTS = os.environ.get('MASTER_HOSTS', '')
JOB_NAME = os.environ.get('JOB_NAME', '')
TASK_INDEX = os.environ.get('TASK_INDEX', '0')

def main(job_name, task_id, ps_hosts=[], worker_hosts=[], master_hosts=[]):
    server = tf.train.Server(
        #cluster_def,
        {
            "ps": ps_hosts,
            "worker": worker_hosts,
            "master": master_hosts
        },
        job_name=job_name,
        task_index=task_id
    )
    server.join()

def split_string(env_string):
    # split, strip and ignore the empty string
    return filter(None, [x.strip() for x in env_string.split(',')])


if __name__ == '__main__':
    worker_hosts = split_string(WORKER_HOSTS)
    ps_hosts = split_string(PS_HOSTS)
    master_hosts = split_string(MASTER_HOSTS)
    job_name = JOB_NAME
    task_index = int(TASK_INDEX)
    logging.info("worker_hosts: %s" % worker_hosts)
    logging.info("ps_hosts: %s" % ps_hosts)
    logging.info("master_hosts: %s" % master_hosts)
    logging.info("job_name: %s" % job_name)
    logging.info("task_index: %d" % task_index)
    main(job_name, task_index, ps_hosts=ps_hosts, worker_hosts=worker_hosts, master_hosts=master_hosts)
