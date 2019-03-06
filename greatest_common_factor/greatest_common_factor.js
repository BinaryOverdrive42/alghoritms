/**
* greatest common factor GCF for a and b
* @param a int
* @param b int
* @return int
*/
function greatestCommonFactor(a, b) {
	while (b != 0) {
		var remainder = a % b;
		a = b;
		b = remainder;
	}
	return a;
}

console.log(greatestCommonFactor(8, 16))