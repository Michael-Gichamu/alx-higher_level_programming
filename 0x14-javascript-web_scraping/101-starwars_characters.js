#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const jsonResponse = JSON.parse(body);
    const characters = jsonResponse.characters;
    const count = 0;
    function printCharacterName(index) {
      if (index >= characters.length) {
        return;
      }

      const nameurl = characters[index];
      request(nameurl, function (error, response, body) {
        if (error) {
          console.error(error);
        } else if (response.statusCode === 200) {
          const charjson = JSON.parse(body);
          console.log(charjson.name);
          printCharacterName(index + 1);
        } else {
          console.log('code: ', response.statusCode);
          printCharacterName(index + 1);
        }
      });
    }

    printCharacterName(count);
  } else {
    console.log('code: ', response.statusCode);
  }
});
