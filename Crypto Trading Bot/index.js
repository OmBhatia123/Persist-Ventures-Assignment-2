const express = require('express');
const { spawn } = require('child_process');

const app = express();
const PORT = process.env.PORT || 3000;

app.get('/start_bot', (req, res) => {
    const pythonProcess = spawn('python', ['main.py']);

    pythonProcess.stdout.on('data', (data) => {
        console.log(`stdout: ${data}`);
    });

    pythonProcess.stderr.on('data', (data) => {
        console.error(`stderr: ${data}`);
    });

    pythonProcess.on('close', (code) => {
        console.log(`child process exited with code ${code}`);
        res.send('Bot started!');
    });
});

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
