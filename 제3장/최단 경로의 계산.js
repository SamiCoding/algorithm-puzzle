// 한 변의 길이가 6cm인 정사각형일 때는 최단 경로가 몇 가지 있는지 구해 보세요.

function route(width, height, back_y) {
  if (width == 1) return (back_y == height) ? back_y : back_y+2
  if (height == 1) return (back_y == 0) ? 2 : 1
  let total = 0
  if (back_y == 0) {
    for (let i=0; i<height; i++) {
      total += 2*route(width-1, height, i+1)
    }
  } else {
    for (let i=back_y; i<=height; i++) {
      total += route(width-1, height, i)
    }
    total += route(width, height-1, back_y-1)
  }
  return total
}
console.log(route(6, 6, 0))