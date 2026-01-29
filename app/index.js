const express = require('express');
const app = express();
const PORT = 3000;

// Debug middleware to log incoming paths
app.use((req, res, next) => {
    console.log(`Request path: ${req.path}`);
    next();
});

// Root route
app.get('/', (req, res) => {
    res.send('Application is running on root (/)');
});

// /testing-load route
app.get('/testing-load', (req, res) => {
    res.send('Testing Load route is working!');
});

// Catch-all for undefined routes
app.get('*', (req, res) => {
    res.status(404).send(`Cannot GET ${req.path}`);
});

app.listen(PORT, () => {
    console.log(`App running on port ${PORT}`);
});
