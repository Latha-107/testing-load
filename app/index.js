const express = require('express');
const app = express();
const PORT = 3000;

// Root route
app.get('/', (req, res) => {
    res.send('Application is running on root (/)');
});

// /testing-load route
app.get('/testing-load', (req, res) => {
    res.send('Testing Load route is working!');
});

// Optional: Catch-all route for undefined paths
app.get('*', (req, res) => {
    res.status(404).send(`Cannot GET ${req.path}`);
});

// Start the server
app.listen(PORT, () => {
    console.log(`App running on port ${PORT}`);
});
