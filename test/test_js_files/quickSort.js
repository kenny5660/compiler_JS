function quickSort (array) {
    if (array.length <= 1) {
      return array;
    } else {
      var pivotIndex = Math.floor(array.length / 2);
      var pivot = array[pivotIndex];
      var less = [];
      var greater = [];
  
      for (var i = 0; i < array.length; i++) {
        if (i === pivotIndex) continue;
        if (array[i] <= pivot) {
          less.push(array[i]);
        } else {
          greater.push(array[i]);
        }
      }
      var result = [];
      return result.concat(quickSort(less), pivot, quickSort(greater));
    }
  }
  console.log(quickSort([5,1,7,4,3]));