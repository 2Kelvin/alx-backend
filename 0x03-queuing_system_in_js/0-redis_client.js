import { createClient } from 'redis';

async function connectToRedis() {
  const redisClient = await createClient();

  redisClient.on('error', (err) => (
    console.error(`Redis client not connected to the server: ${err}`)
  ));

  console.log('Redis client connected to the server');
}

connectToRedis();
