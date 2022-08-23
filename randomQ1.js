
function solution(input_array)
{
    let sum = parseInt(input_array[0])
    let arr_size = parseInt(input_array[1])
    let A = []

    for (let i = 2; i < arr_size; i++) {
        A.push(parseInt(input_array[i]))
    }

	let left = 0, right = 0;

	A.sort((num0, num1) => num0 - num1);

	for (i = 0; i < arr_size - 2; i++) {

		left = i + 1;
		
		right = arr_size - 1;

		while (left < right) {
			if (A[i] + A[left] + A[right] == sum)
				return true;
			else if (A[i] + A[left] + A[right] < sum)
				left++;
			else
				right--;
		}
	}

	return false;
}



