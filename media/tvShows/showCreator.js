/*jshint esversion: 8 */
/*jshint node: true*/

const fs = require('fs');
argv = require("yargs").argv;

function epC(name) {
  i = 1;
  fs.mkdirSync('./' + name);
  while (i < 11) {
    fs.writeFile('./' + name + '/' + name + ' ' + i + '.jonVid', 'sushi', (err) => {
      if (err) {
        console.log('err: ', err);
      } else {
      }
    });
    i += 1;
  }
  console.log('show printed');
}

epC(argv.show);
