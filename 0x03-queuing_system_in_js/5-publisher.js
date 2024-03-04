import { createClient, print } from 'redis';

// creating a redis client db
const redisClient = createClient();

// checking if error creating redis client
redisClient.on('error', (err) => (
  console.log(`Redis client not connected to the server: ${err}`)
));

// successfully created redis client
redisClient.on('connect', () => (
  console.log('Redis client connected to the server')
));

function publishMessage(message, time) {
  setTimeout(() => {
    console.log(`About to send ${message}`);

    // publishing the message in the channel
    redisClient.publish('holberton school channel', message);
  }, time);
}

publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
