import { createQueue } from 'kue';

const queue = createQueue({name: 'push_notification_code'});

const kueJob = queue.create('push_notification_code', {
  phoneNumber: '4153518780',
  message: 'This is the code to verify your account',
});

kueJob
  .on('enqueue', () => console.log(`Notification job created: ${kueJob.id}`))
  .on('complete', () => console.log('Notification job completed'))
  .on('failed', () => console.log('Notification job failed'));

kueJob.save((err) => {
    if (err) console.log('Notification job failed');
});