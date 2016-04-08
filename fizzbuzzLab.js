/* Create a function fizzBuzz to return 'Fizz', 'Buzz', 'FizzBuzz',
or the argument it receives, all depending on the argument of the function,
a number that is divisible by, 3, 5, or both 3 and 5, respectively.

When the number is not divisible by 3 or 5, the number itself should be returned.*/

function fizzBuzz(i){

		currentNumberDivisibleBy3 = (i%3 === 0);
		currentNumberDivisibleBy5 = (i%5 === 0);
		if(currentNumberDivisibleBy3 && !currentNumberDivisibleBy5){
			return "Fizz";
		} 
		else if(currentNumberDivisibleBy5 && !currentNumberDivisibleBy3){
			return "Buzz";
		} 
		
		else if(currentNumberDivisibleBy3 && currentNumberDivisibleBy5) {
		return "FizzBuzz";
		}
		else {
	return i;
		}
}