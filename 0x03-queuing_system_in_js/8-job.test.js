import { createQueue } from 'kue';
import { expect } from 'chai';
import createPushNotificationsJobs from "./8-job";

describe('createPushNotificationsJobs', () => {
  let queue;
  before(() => {
    queue = createQueue({ name: 'push_notification_code_test' });
    queue.testMode.enter();
  });
  after(() => {
    queue.testMode.exit();
    queue.shutdown(1000, err => {
      if (err) {
        console.error('Error shutting down Kue queue:', err);
      } else {
        console.log('Kue queue shut down successfully');
      }
    });
  });
  afterEach(() => {
    queue.testMode.clear();
  });
  it('creates a job for each input object', () => {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account',
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 4562 to verify your account',
      },
      {
        phoneNumber: '4153518743',
        message: 'This is the code 4321 to verify your account',
      },
      {
        phoneNumber: '4153538781',
        message: 'This is the code 4562 to verify your account',
      },
    ];
    createPushNotificationsJobs(jobs, queue);
    queue.on('job complete', (id, result) => {
      queue.testMode.jobs((err, jobs) => {
        if (err) throw err;
        expect(jobs.length).to.be.equal(4);
        jobs.forEach(job => {
          expect(job.type).to.be.equal('push_notification_code_3');
          expect(job.data.phoneNumber).to.be.defined;
          expect(job.data.message).to.be.defined;
        });
      });
    });
  });
  it('throws an error if jobs is not an array', () => {
    expect(() => {
      createPushNotificationsJobs({}, queue);
    }).to.throw('Jobs is not an array');
  });
});