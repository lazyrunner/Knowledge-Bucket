
const issueService = require("../services/issues.service");

const get = function(req,res) {
    const reqBody = req.body;
    res.send(issueService)
}