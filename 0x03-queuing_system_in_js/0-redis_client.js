import { createClient } from 'redis';

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
