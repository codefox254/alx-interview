#!/usr/bin/node

// Importing the request module
const request = require('request');

// Get the movie ID from command line arguments
const movieId = process.argv[2];

// Validate the movie ID argument
if (!movieId) {
  console.error('Usage: ./script.js <Movie ID>');
  process.exit(1);
}

// Star Wars API URL for the specific movie
const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

// Making a request to get the movie details
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  // Parse the response body to get the movie details
  const movie = JSON.parse(body);

  // Extract the list of character URLs
  const characters = movie.characters;

  // Function to print character names in order
  const printCharacter = (index) => {
    if (index >= characters.length) return;

    // Request each character's details
    request(characters[index], (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }

      // Parse character data and print the name
      const character = JSON.parse(body);
      console.log(character.name);

      // Recursive call to print next character
      printCharacter(index + 1);
    });
  };

  // Start printing characters
  printCharacter(0);
});
