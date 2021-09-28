const express = require('express');
const router = express.Router();

const issueController = require('../controllers/issues.controller');

router.route('/')
      .get(issueController);

router.route('/')
      .post(issueController);

module.exports = router;