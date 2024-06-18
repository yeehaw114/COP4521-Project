export type RegisterCreds = {
  email: string
  username: string
  password: string
  role: 'admin' | 'trainer' | 'user'
}

export type LoginCreds = {
  username: string
  password: string
}
