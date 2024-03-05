export default function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) throw new Error('Jobs is not an array');

  jobs.forEach((job) => {
    const kueJob = queue.create('push_notification_code_3', job);

    kueJob
      .on('enqueue', () => console.log(`Notification job created: ${kueJob.id}`))
      .on('complete', () => console.log(`Notification job ${kueJob.id} completed`))
      .on('failed', (err) => console.log(`Notification job ${kueJob.id} failed: ${err}`))
      .on('progress', (progress, data) => {
        console.log(`Notification job ${kueJob.id} ${progress}% complete`)
       });
    kueJob.save((err) => {
      if (err) console.log('Notification job failed');
    });
  });
}
