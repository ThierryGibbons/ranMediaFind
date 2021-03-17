/*jshint esversion: 8 */
/*jshint node: true*/

const fs = require('fs');

function epC(name) {
  i = 1;
  while (i < 11) {
    console.log(i);
    fs.writeFile(name + i + '.jonVid', 'sushi', (err) => {
      if (err) {
        console.log('err: ', err);
      } else {
        console.log('chur');
      }
    });
    i += 1;
  }
}

epC('cool');
