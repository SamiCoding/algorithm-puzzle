// 10개의 숫자를 모두 표시할 때 끄거나 켜는 횟수가 가장 적은 표시 순서를 구하고, 그 바꾼 횟수를 구해 보세요.

bit = [ 0b1111110, 0b0110000, 0b1101101, 0b1111001, 0b0110011,
        0b1011011, 0b1011111, 0b1110000, 0b1111111, 0b1111011 ]

// 1이 있는 비트의 수를 센다.
function bitcount(x) {
  x = (x & 0x55555555) + (x >> 1 & 0x55555555)
  x = (x & 0x33333333) + (x >> 2 & 0x33333333)
  x = (x & 0x0F0F0F0F) + (x >> 4 & 0x0F0F0F0F)
  x = (x & 0x00FF00FF) + (x >> 8 & 0x00FF00FF)
  x = (x & 0x0000FFFF) + (x >> 16 & 0x0000FFFF)
  return x
}

let flip = new Array(10)
for (i=0; i<10; i++) {
  flip[i] = new Array(10)
  for (j=0; j<10; j++) {
    flip[i][j] = bitcount(bit[i]^bit[j])
  }
}

let min = 63
function search(is_used, sum, prev) {
  if (is_used.indexOf(false) == -1) {
    min = sum
  }
  else {
    for (let i=0; i<10; i++) {
      if (!is_used[i]) {
        is_used[i] = true
        let next_sum = 0
        if (prev >= 0) {
          next_sum = sum + flip[prev][i]
        }
        if (min > next_sum) {
          search(is_used, next_sum, i)
        }
        is_used[i] = false
      }
    }
  }
}
is_used = [ false, false, false, false, false,
            false, false, false, false, false ]
search(is_used, 0, -1)
console.log(min)