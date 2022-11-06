let person = {
    name: "Jalen",
    age: 30
};

// Dot notation
person.age = 40;

//Bracket notation
person ['name'] = 'Mary';
console.log (person.name);

// Arrays
let selectedColors = ['red', 'blue'];
selectedColors [2] = 'green';
// Will change array 

console.log (selectedColors [0]);


//Functions
function greet () {
    console.log ("hello world");
};

// Calls funtion
greet ();

function greeting (name, lastName) {
    comsole.log ("Hello" + name + '' + lastName);
};

greet ('Jalen', 'Jones');

// Calculates value 
function square (number) {
    return number * number;
};

console.log (square (2));

