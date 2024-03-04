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

// subscribing to the channel
redisClient.subscribe('holberton school channel');

// subscribing to a channel, listening for channel messages & displaying them
redisClient.on('message', (err, channelMsg) => {
  if (channelMsg === 'KILL_SERVER') {
    redisClient.unsubscribe();
    redisClient.quit();
  }
  console.log(channelMsg);
});
