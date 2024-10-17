let numbers = [1,5,3,8,4,7];

// let addnumbers = 0;
// for(let i=0; i < numbers.length; i++){
//     addnumbers = numbers[i] + addnumbers;
// };


// console.log(addnumbers);
let sum = 0;
//numbers.forEach((element) => (console.log(`this is all elements ${element}`)));
     

const sumOfArr = numbers.reduce((acc, item) => (acc + item),0);
// console.log(sumOfArr)

const arrDataGreatertahn3 = numbers.filter( (data) => data>3)
// console.log(arrDataGreatertahn3)

const mappingTest = numbers.map( (data) => data)
// console.log(mappingTest)

for (let i = 1; i <= 10; i++) {
    //console.log(`2 X ${i} = ${i*2}`)
    
}


word = "aladin";

for (let i = 0; i < word.length; i++) {

    //console.log(word[i]) 
    for (let j = 1; j < word.length; j++) {

            if (i==j) {
                console.log("matched");
                
            }
    }
}