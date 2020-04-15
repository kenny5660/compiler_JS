function quickSort (array_arg) {
    if (array_arg.length <= 1) {
      return array_arg;
    } else {
      var pivotIndex = Math.floor(array_arg.length / 2);
      var pivot = array_arg[pivotIndex];
      var less = [];
      var greater = [];
  
      for (var i = 0; i < array_arg.length; i++) {
        if (i === pivotIndex) continue;
        if (array_arg[i] <= pivot) {
          less.push(array_arg[i]);
        } else {
          greater.push(array_arg[i]);
        }
      }
      var result = [];
      return result.concat(quickSort(less), pivot, quickSort(greater));
    }
  }
  console.log(quickSort([5,1,7,4,3]));