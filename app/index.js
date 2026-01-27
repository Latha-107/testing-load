const express = require('express');
const app = express();


app.get('/', (req, res) => {
res.send('Application is running');
});


app.listen(3000, () => {
console.log('App running on port 3000');
});
