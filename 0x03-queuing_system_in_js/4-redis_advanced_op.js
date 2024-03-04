import { createClient, print } from 'redis';
import { promisify } from 'util';

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

// adding newSchool key:value pair to redis
function setNewSchool(schoolName, value) {
  redisClient.set(schoolName, value, print);
}

// display schoolName's key value stored in redis
async function displaySchoolValue(schoolName) {
  const theValue = await promisify(redisClient.get).bind(redisClient)(schoolName);
  console.log(theValue);
}

// adding hash data to redis
redisClient.hset('HolbertonSchools', 'Portland', 50, print);
redisClient.hset('HolbertonSchools', 'Seattle', 80, print);
redisClient.hset('HolbertonSchools', 'New York', 20, print);
redisClient.hset('HolbertonSchools', 'Bogota', 20, print);
redisClient.hset('HolbertonSchools', 'Cali', 40, print);
redisClient.hset('HolbertonSchools', 'Paris', 2, print);

// displaying all redis data
redisClient.hgetall('HolbertonSchools', (err, dataObjs) => {
  if (err) console.log(err);
  console.log(dataObjs);
});
