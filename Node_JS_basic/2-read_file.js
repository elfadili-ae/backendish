const fs = require('fs');

function countStudents(path) {
    fs.readFile(path, 'utf-8', (err, data) => {
        if (err) {
            throw new Error("Cannot load the database");
        }
        const db = data.split('\n').filter((line) => line.trim() !== '');
        console.log(`Number of students: ${db.length - 1}`);

        let byFields = {}
        db.slice(1).forEach((line) => {
            const elements = line.split(',');
            if (!(elements[3] in byFields)) {
                byFields[elements[3]] = [];
            }
            byFields[elements[3]].push(elements[0]);
        })
        for (const key in byFields) {
            console.log(`Number of students in ${key}: ${byFields[key]}. List: ${byFields[key]}`);
        }
    })
}

module.exports = countStudents;