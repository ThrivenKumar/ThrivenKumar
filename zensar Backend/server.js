const express = require("express");
const app = express();
const bodyParser = require("body-parser");
app.use(
  bodyParser.urlencoded({
    extended: true,
  })
);
app.use(bodyParser.json());

// const MongoClient = require('mongodb').MongoClient;
// const uri = "mongodb+srv://zensr:<password>@cluster0.hstk1.mongodb.net/myFirstDatabase?retryWrites=true&w=majority";
// const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });
const { MongoClient } = require("mongodb");

// Replace the uri string with your MongoDB deployment's connection string.
const uri =
  "mongodb+srv://zensr:Testcluster@cluster0.hstk1.mongodb.net?retryWrites=true&w=majority";

const client = new MongoClient(uri);

async function getConnection() {
  await client.connect();
  const database = client.db("zensr");
  return database;
}
async function profileLookup(name) {
  try {
    conn = await getConnection();
    profileCollection = conn.collection("profile");
    const query = { name: name };
    const profile = await profileCollection.findOne(query);
    // since this method returns the matched document, not a cursor, print it directly
    console.log(profile);
    return profile;
  } finally {
    await client.close();
  }
}

async function deleteProfile(profileId) {
  try {
    conn = await getConnection();
    profileCollection = conn.collection("profile");
    const query = { id: profileId };
    console.log(query);
    const profile = await profileCollection.deleteOne(query);
    console.log(profile);
    if (profile.deletedCount === 1) {
      console.dir("Successfully deleted one document.");
      return { message: "Successfully deleted one document." };
    } else {
      console.log("No documents matched the query. Deleted 0 documents.");
      return {
        message: "No documents matched the query. Deleted 0 documents.",
      };
    }
  } finally {
    await client.close();
  }
}

async function updateProfile(body, id) {
  conn = await getConnection();
  profileCollection = conn.collection("profile");
  console.log(body);
  const filter = { id: id };
  const options = { upsert: true };
  const updateDoc = {
    $set: body,
  };
  const result = await profileCollection.updateOne(filter, updateDoc, options);
  console.log(
    `${result.matchedCount} document(s) matched the filter, updated ${result.modifiedCount} document(s)`
  );
  return {
    message: `${result.matchedCount} document(s) matched the filter, updated ${result.modifiedCount} document(s)`,
  };
}
async function insertProfile(body) {
  conn = await getConnection();
  profileCollection = conn.collection("profile");
  console.log(body);
  const result = await profileCollection.insertOne(body);
  console.log(
    `${result.insertedCount} documents were inserted with the _id: ${result.insertedId}`
  );
  return {
    message: `${result.insertedCount} documents were inserted with the _id: ${result.insertedId}`,
  };
}

app.use(bodyParser.urlencoded({ extended: true }));

app.listen(3000, function () {
  console.log("listening on 3000");
});

app.get("/profile", function (req, res) {
  if (req.query.name == undefined)
    res.send({
      message: "Please enter valid profileId",
    });
  else {
    console.log(req.query);
    profileLookup(req.query.name)
      .then((lookup) => {
        console.log(lookup);
        res.statusCode = 200;
        res.send(lookup);
      })
      .catch((e) => console.log(e));
  }
});

app.delete("/profile/:profileId", function (req, res) {
  console.log(req.params.profileId);
  if (req.params.profileId == undefined) {
    res.statusCode = 400;
    res.send({
      message: "Please enter valid profileId",
    });
  } else {
    deleteProfile(req.params.profileId).then((del) => {
      console.log(del);
      res.statusCode = 204;
      res.send(del);
    });
  }
});

app.put("/profile/:profileId", function (req, res) {
  console.log(req.params.profileId);
  console.log(req.body);
  if (req.params.profileId == undefined) {
    res.statusCode = 400;
    res.send({
      message: "Please enter valid profileId",
    });
  } else {
    updateProfile(req.body, req.params.profileId).then((update) => {
      res.send(update);
    });
  }
});

app.post("/profile", function (req, res) {
  console.log(req.body);
  if (req.body == undefined) {
    res.send({
      message: "please pass valid json body",
    });
  } else {
    insertProfile(req.body).then((insert) => {
      res.send(insert);
    });
  }
});
