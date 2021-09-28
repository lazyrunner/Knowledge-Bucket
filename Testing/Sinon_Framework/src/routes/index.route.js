const express = require('express');
const issue = require('./issues.route');

const router = express.Router();

router.use('/issues',issue);

module.exports = router;