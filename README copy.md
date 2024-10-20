# Dead-Code-Eliminator
<li> Dead Code Eliminator is a Static Javascript Code analyzer which remove the unused javascript code and create a new file </li>
<li> This project is for the Learning purposes </li>
<li> This project is only analyzing JS Files and Removing Unused Functions (Simple Functions and Arrow Function) from single javascript file</li>
<li> This Project can be extended to work on Multiple JS Files and Traverse HTML Code to identify JS functions used in
 HTML Code as well. </li>
<li> This Project is inspired from Lucana https://github.com/Lacuna-JDCE/Lacuna</li>

## How to use
Clone the Repository and execute `npm install` to install the libraries. \
Once you have installed all the dependencies then you just need to place your Javascript File inside the `example` directory with name `script.js` and execute \
`npm run test` \
It will automatically remove the dead code from the provided script.js file. \
You can also run it on your project using `node eliminator -i /source-folder-path/source-file.js -o /destination-folder-path/output-file.js` 

## Development
<li> This is a very basic version of Javascript Dead Code Removal</li>
<li> Feel free to contribute to this project </li>
