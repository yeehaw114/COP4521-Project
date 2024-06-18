export type RegisterCreds = {
  email: string
  username: string
  password: string
  role: 'Admin' | 'Trainer' | 'User'
}

export type LoginCreds = {
  username: string
  password: string
}
