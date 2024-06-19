export function formatTime(timeString: string): string {
  const [hours, minutes, secondsWithMicroseconds] = timeString.split(':')
  const [seconds, microseconds] = secondsWithMicroseconds.split('.')

  const date = new Date()
  date.setHours(parseInt(hours))
  date.setMinutes(parseInt(minutes))
  date.setSeconds(parseInt(seconds))
  date.setMilliseconds(parseInt(microseconds) / 1000)

  const options: Intl.DateTimeFormatOptions = { hour: '2-digit', minute: '2-digit', hour12: true }
  return date.toLocaleTimeString('en-US', options)
}
