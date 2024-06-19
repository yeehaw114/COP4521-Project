export function stringArrayToInt(param: string[]): number {
  let result = 0
  for (let i = 0; i < param.length; i++) {
    const digit = parseInt(param[i]) % 10
    result += digit
    result *= 10
  }
  result /= 10

  return result
}
