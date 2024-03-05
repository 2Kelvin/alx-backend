import { createClient } from 'redis';
import express from 'express';
import { promisify } from 'util';

const listProducts = [
  { itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
  { itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
  { itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
  { itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5 },
];

function getItemById(id) {
  const item = listProducts.find(obj => obj.itemId === id);
  if (item) {
    return Object.fromEntries(Object.entries(item));
  }
}

// creating an express app listening on port 1245
const app = express();
// redis client
const redisClient = createClient();

function reserveStockById(itemId, stock) {
  return promisify(redisClient.set).bind(redisClient)(`item.${itemId}`, stock);
}

async function getCurrentReservedStockById(itemId) {
  return promisify(redisClient.get).bind(redisClient)(`item.${itemId}`);
}

function resettingStock() {
  return Promise.all(listProducts.map((item) => (
    promisify(redisClient.set).bind(redisClient)(`item.${item.itemId}`, 0)
  )));
}

// routes
app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

app.get('/list_products/:itemId(\\d+)', (req, res) => {
  const itemIdParam = Number.parseInt(req.params.itemId);
  const product = getItemById(Number.parseInt(itemIdParam));

  if (!product) {
    res.json({ status: 'Product not found' });
    return;
  }

  getCurrentReservedStockById(itemIdParam)
    .then((result) => Number.parseInt(result || 0))
    .then((resvdStock) => {
      product.currentQuantity = product.initialAvailableQuantity - resvdStock;
      res.json(product);
    })
});

app.get('/reserve_product/:itemId', (req, res) => {
  const itemIdParam = Number.parseInt(req.params.itemId);
  const product = getItemById(Number.parseInt(itemIdParam));

  if (!product) {
    res.json({ status: 'Product not found' });
    return;
  }

  getCurrentReservedStockById(itemIdParam)
    .then((result) => Number.parseInt(result || 0))
    .then((resvdStock) => {
      if (resvdStock >= product.initialAvailableQuantity) {
        res.json({ status: 'Not enough stock available', itemIdParam });
        return;
      }
      reserveStockById(itemIdParam, (resvdStock + 1))
        .then(() => {
          res.json({ status: 'Reservation confirmed', itemIdParam });
        });
    });
});

app.listen(1245, () => {
  resettingStock()
    .then(() => console.log('API available on localhost port 1245'));
});

export default app;
