const express = require("express");
const productRouter = require("./src/router/productrouter");
const mongoose = require("mongoose");
const bodyParser = require("body-parser");
const app = express();

app.use(bodyParser.json());
app.use(productRouter);

const user = "cosmiosbackend";
const password = "AdUOhGatAv4LoaHk";
const databaseName = "products";
mongoose
  .connect(
    `mongodb+srv://${user}:${password}@cluster0.ijiamuw.mongodb.net/${databaseName}?retryWrites=true&w=majority`
  )
  .then(() => {
    console.log("Connected to database");
  })
  .catch((error) => {
    console.log(error);
  });
app.listen(5000, () => {
  console.log("Server 5000 portunda çalışıyor");
});
