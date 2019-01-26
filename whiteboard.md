Questions from [500 data structure and algoriths](https://techiedelight.quora.com/500-Data-Structures-and-Algorithms-interview-questions-and-their-solutions)

General tricks
* check if the order of the input matters. if not, try sort it, put it in a set or a Counter.

## Array
### sub-array
* Have a mental image which plots val as y-axis. Try storing the sum of each element, and check the sum appeared before. The idea is that the extra elements in the sum is just an offset. You may have to modify the input, or check the sums in a special way. Example: [Find max length subarray with equal number of 0 and 1s](https://www.techiedelight.com/find-maximum-length-sub-array-equal-number-0s-1s/)
* Maintain a window that satisfy the problem constraint, i.e. [sliding window technique](https://www.techiedelight.com/sliding-window-problems/) 

### NP-complete
