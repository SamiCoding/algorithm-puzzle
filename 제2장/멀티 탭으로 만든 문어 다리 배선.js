// n = 20일 때 몇 가지의 멀티 탭 배치를 생각할 수 있는지 구해보세요(단, 전원 용량은 생각하지 않기로 합니다).

const N = 20
let memo = []
memo[1] = 1

function set_tap(remain) {
  if (memo[remain]) {
    return memo[remain]    
  }
  let cnt = 0
  // 2구
  for (let i=1; i<=remain/2; i++) {
    if (remain-i == i) {
      cnt += set_tap(i)*(set_tap(i)+1)/2
    }
    else {
      cnt += set_tap(remain-i)*set_tap(i)
    }
  }
  // 3구
  for (let i=1; i<=remain/3; i++) {
    for (let j=i; j<=(remain-i)/2; j++) {
      if ((remain-(i+j) == i) && (i == j)) {
        cnt += set_tap(i)*(set_tap(i)+1)*(set_tap(i)+2)/6
      }
      else if (remain-(i+j) == i) {
        cnt += set_tap(i)*(set_tap(i)+1)*set_tap(j)/2
      }
      else if (i == j) {
        cnt += set_tap(remain-(i+j))*set_tap(i)*(set_tap(i)+1)/2
      }
      else if (remain-(i+j) == j) {
        cnt += set_tap(j)*(set_tap(j)+1)*set_tap(i)/2
      }
      else {
        cnt += set_tap(remain-(i+j))*set_tap(j)*set_tap(i)
      }
    }

  }
  memo[remain] = cnt
  return cnt
}

console.log(set_tap(N))